import numpy as np
import pandas as pd
from mpi4py import MPI
from genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, \
    generate_unique_population

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Only the master (rank 0) loads the data
    if rank == 0:
        # Load the distance matrix
        distance_matrix = pd.read_csv('city_distances.csv').to_numpy()
        
        # Parameters
        num_nodes = distance_matrix.shape[0]
        population_size = 10000
        num_tournaments = 4
        mutation_rate = 0.1
        num_generations = 200
        stagnation_limit = 5

        # Generate initial population
        np.random.seed(42)  # For reproducibility
        population = generate_unique_population(population_size, num_nodes)
        
        # Initialize variables for tracking stagnation
        best_fitness = float('inf')
        stagnation_counter = 0
    else:
        # Workers initialize variables as None
        distance_matrix = None
        population = None
        best_fitness = None
        stagnation_counter = None

    # Broadcast the distance matrix to all processes
    distance_matrix = comm.bcast(distance_matrix, root=0)

    # Main GA loop
    for generation in range(num_generations):
        if rank == 0:
            # Master process distributes population chunks to workers
            chunk_size = population_size // size
            chunks = [population[i:i + chunk_size] for i in range(0, population_size, chunk_size)]
            
            # Send chunks to workers
            for i in range(1, size):
                comm.send(chunks[i], dest=i)
            
            # Master processes its own chunk
            local_chunk = chunks[0]
            local_fitness = np.array([calculate_fitness(route, distance_matrix) for route in local_chunk])
            
            # Receive results from workers
            all_fitness = [local_fitness]
            for i in range(1, size):
                worker_fitness = comm.recv(source=i)
                all_fitness.append(worker_fitness)
            
            # Combine fitness values
            fitness_values = np.concatenate(all_fitness)
            
            # Check for stagnation
            current_best_fitness = np.min(fitness_values)
            if current_best_fitness < best_fitness:
                best_fitness = current_best_fitness
                stagnation_counter = 0
            else:
                stagnation_counter += 1

            # Regenerate population if stagnation limit is reached
            if stagnation_counter >= stagnation_limit:
                print(f"Regenerating population at generation {generation} due to stagnation")
                best_individual = population[np.argmin(fitness_values)]
                population = generate_unique_population(population_size - 1, num_nodes)
                population.append(best_individual)
                stagnation_counter = 0
                continue

            # Selection, crossover, and mutation
            selected = select_in_tournament(population, fitness_values)
            offspring = []
            for i in range(0, len(selected), 2):
                parent1, parent2 = selected[i], selected[i + 1]
                route1 = order_crossover(parent1[1:], parent2[1:])
                offspring.append([0] + route1)
            mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

            # Replacement
            for i, idx in enumerate(np.argsort(fitness_values)[::-1][:len(mutated_offspring)]):
                population[idx] = mutated_offspring[i]

            # Ensure population uniqueness
            unique_population = set(tuple(ind) for ind in population)
            while len(unique_population) < population_size:
                individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
                unique_population.add(tuple(individual))
            population = [list(individual) for individual in unique_population]

            # Print progress
            print(f"Generation {generation}: Best fitness = {current_best_fitness}")

        else:
            # Worker processes
            # Receive population chunk
            local_chunk = comm.recv(source=0)
            
            # Calculate fitness for local chunk
            local_fitness = np.array([calculate_fitness(route, distance_matrix) for route in local_chunk])
            
            # Send results back to master
            comm.send(local_fitness, dest=0)

    # Final results
    if rank == 0:
        # Get final fitness values
        final_fitness = np.array([calculate_fitness(route, distance_matrix) for route in population])
        best_idx = np.argmin(final_fitness)
        best_solution = population[best_idx]
        print("Best Solution:", best_solution)
        print("Total Distance:", -final_fitness[best_idx])

if __name__ == "__main__":
    main() 