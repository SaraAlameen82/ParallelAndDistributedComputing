import time
import threading
from src.functions import calculate_partial_sum


def parallel_threads():
    n = 1000000
    num_threads = 4
    size = n // num_threads
    
    # List to store results from threads
    results = [0] * num_threads
    threads = []
    
    # Measure the execution time
    start_time = time.time()
    
    # Create and start threads
    for i in range(num_threads):
        start = i * size + 1
        end = (i + 1) * size if i != num_threads - 1 else n
        thread = threading.Thread(target=calculate_partial_sum, args=(start, end, results, i))
        threads.append(thread)
        thread.start()
    
    # Waiting for all threads to complete
    for thread in threads:
        thread.join()
    
    # Total sum
    total_sum = sum(results)
    end_time = time.time()
    
    # Execution time
    execution_time = end_time - start_time
    
    # Print the sum and execution time
    print(f"Threads Sum: {total_sum}")
    print(f"Threads Execution Time: {execution_time} seconds")
