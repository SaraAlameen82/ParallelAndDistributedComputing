import time
import multiprocessing
from src.functions import calculate_partial_sum


def parallel_processes():
    n = 1000000
    num_processes = 4
    size = n // num_processes
    
    # Store results 
    results = multiprocessing.Array('i', num_processes)
    processes = []
    
    # Measure the execution time
    start_time = time.time()
    
    # Create and start processes
    for i in range(num_processes):
        start = i * size + 1
        end = (i + 1) * size if i != num_processes - 1 else n
        process = multiprocessing.Process(target=calculate_partial_sum, args=(start, end, results, i))
        processes.append(process)
        process.start()
    
    # Waiting for all processes to complete
    for process in processes:
        process.join()
    
    # Total sum
    total_sum = sum(results)
    end_time = time.time()
    
    # Execution time
    execution_time = end_time - start_time
    
    # Printing the sum and execution time
    print(f"Processes Sum: {total_sum}")
    print(f"Processes Execution Time: {execution_time} seconds")
