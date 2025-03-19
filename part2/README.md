# DSAI 3202 - Parallel and Distributed Computing

## Assignment 1 - Part 2: Navigating the City

### 1. Program Overview

This project implements a genetic algorithm to solve the Traveling Salesman Problem (TSP) for a delivery vehicle in a city. The algorithm finds the optimal route that minimizes the total distance while visiting all delivery locations exactly once.

### 2. Code Structure

The project contains the following files:

- `genetic_algorithms_functions.py`: Contains the core genetic algorithm functions
- `genetic_algorithm_trial.py`: Main script to run the genetic algorithm
- `city_distances.csv`: Distance matrix for 20 nodes
- `city_distances_extended.csv`: Extended distance matrix for 100 nodes

### 3. Implementation Details

#### 3.1 Genetic Algorithm Components

1. **Population Representation**:

   - Each individual represents a route
   - Routes start and end at node 0 (depot)
   - All other nodes are visited exactly once

2. **Fitness Function**:

   - Calculates total distance of a route
   - Returns negative value for minimization
   - Handles infeasible routes with penalties

3. **Selection**:

   - Uses tournament selection
   - Selects best individuals for reproduction
   - Maintains population diversity

4. **Crossover**:

   - Implements order crossover (OX)
   - Preserves route feasibility
   - Maintains starting/ending at depot

5. **Mutation**:
   - Swaps two random nodes
   - Maintains route feasibility
   - Helps escape local optima

### 4. Sequential Implementation Results

- Population Size: 10000
- Number of Generations: 200
- Mutation Rate: 0.1
- Tournament Size: 3
- Number of Tournaments: 4

Execution Time: [Add your execution time here]
Best Route Distance: [Add your best distance here]

### 5. Distributed Implementation

#### 5.1 Distributed Components

The following components were distributed:

1. **Fitness Evaluation**:

   - Most computationally intensive part
   - Each individual's fitness can be calculated independently
   - Natural candidate for parallelization

2. **Population Generation**:
   - Initial population generation
   - Population regeneration after stagnation
   - Can be parallelized across machines

#### 5.2 Parallelization Strategy

- Used MPI4PY for distributed computing
- Master-worker architecture:
  - Master: Handles population management and genetic operations
  - Workers: Perform fitness evaluations in parallel

#### 5.3 Performance Metrics

Before Distribution:

- Execution Time: [Add time]
- Best Solution: [Add solution]

After Distribution:

- Execution Time: [Add time]
- Best Solution: [Add solution]
- Speedup: [Calculate speedup]

### 6. Algorithm Enhancements

1. **Population Diversity**:

   - Implemented population regeneration on stagnation
   - Added elitism to preserve best solutions

2. **Selection Pressure**:

   - Adjusted tournament size dynamically
   - Modified mutation rate based on population diversity

3. **Route Optimization**:
   - Added local search after mutation
   - Implemented 2-opt optimization

### 7. Large Scale Problem

#### 7.1 Extended City Map (100 nodes)

- Successfully executed on distributed system
- Execution Time: [Add time]
- Best Solution: [Add solution]

#### 7.2 Multiple Cars Implementation

To add multiple cars to the problem:

1. **Route Splitting**:

   - Divide nodes among vehicles
   - Ensure balanced workload
   - Maintain depot constraints

2. **Population Structure**:

   - Each individual represents multiple routes
   - Fitness considers total fleet distance
   - Crossover and mutation adapted for multiple routes

3. **Constraints**:
   - Each node visited exactly once
   - All vehicles start/end at depot
   - Balance load among vehicles

### 8. Future Improvements

1. **Algorithm Enhancements**:

   - Implement adaptive mutation rates
   - Add more sophisticated crossover operators
   - Include local search optimization

2. **Distributed Computing**:

   - Scale to more machines
   - Implement dynamic load balancing
   - Add fault tolerance

3. **Multiple Cars**:
   - Implement dynamic fleet sizing
   - Add time window constraints
   - Consider vehicle capacity

### 9. Bonus Features

- [ ] Multiple cars implementation
- [ ] AWS deployment
- [ ] Performance optimization
- [ ] Best solution achievement
