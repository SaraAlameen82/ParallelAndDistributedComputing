import time
from threading import Thread
from multiprocessing import Process, Array
from src.lab3_threads import parallel_threads
from src.lab3_sequential import sequential_sum
from src.lab3_processes import parallel_processes

# Calculating speedup and efficiency
def calculate_speedup_and_efficiency(sequential_time, parallel_time, num_partitions):
    # Calculating speedup 
    speedup = sequential_time / parallel_time

    # Calculating efficiency
    efficiency = speedup / num_partitions

    return speedup, efficiency

def amdahls_law_speedup(p, num_partitions):
    # Speedup using Amdahl's Law
    return 1 / ((1 - p) + p / num_partitions)

def gustafsons_law_speedup(p, num_partitions):
    # Speedup using Gustafson's Law
    return num_partitions - (1 - p) * num_partitions

if __name__ == "__main__":
    # Sequential
    print("Running Sequential Execution...")
    start_time = time.time()
    sequential_sum_result = sequential_sum()
    sequential_time = time.time() - start_time
    print(f"Sequential Execution Time: {sequential_time:.6f} seconds\n")

    # Threading Execution
    print("Running Threaded Execution...")
    start_time = time.time()
    parallel_threads()
    threading_time = time.time() - start_time
    print(f"Threaded Execution Time: {threading_time:.6f} seconds\n")

    # Multiprocessing Execution
    print("Running Multiprocessing Execution...")
    start_time = time.time()
    parallel_processes()
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing Execution Time: {multiprocessing_time:.6f} seconds\n")

    # Number of partitions (threads/processes)
    num_partitions = 4

    # Calculate metrics for Threading
    threading_speedup, threading_efficiency = calculate_speedup_and_efficiency(sequential_time, threading_time, num_partitions)
    
    # Calculate metrics for Multiprocessing
    multiprocessing_speedup, multiprocessing_efficiency = calculate_speedup_and_efficiency(sequential_time, multiprocessing_time, num_partitions)

    # Assume a parallelizable portion `p` (e.g., 0.9 for 90% parallelizable workload)
    p = 0.9

    # Amdahl's Law Speedups
    amdahls_threading_speedup = amdahls_law_speedup(p, num_partitions)
    amdahls_multiprocessing_speedup = amdahls_law_speedup(p, num_partitions)

    # Gustafson's Law Speedups
    gustafsons_threading_speedup = gustafsons_law_speedup(p, num_partitions)
    gustafsons_multiprocessing_speedup = gustafsons_law_speedup(p, num_partitions)

    # Print Results
    print(f"Threading Speedup: {threading_speedup:.2f}, Efficiency: {threading_efficiency:.2f}")
    print(f"Multiprocessing Speedup: {multiprocessing_speedup:.2f}, Efficiency: {multiprocessing_efficiency:.2f}\n")

    print(f"Amdahl's Law Speedups - Threading: {amdahls_threading_speedup:.2f}, Multiprocessing: {amdahls_multiprocessing_speedup:.2f}")
    print(f"Gustafson's Law Speedups - Threading: {gustafsons_threading_speedup:.2f}, Multiprocessing: {gustafsons_multiprocessing_speedup:.2f}\n")

# Discussion on Performance Differences and Challenges:
"""
c. Performance Differences:
   - Threading may perform worse than multiprocessing for CPU-bound tasks due to the Global Interpreter Lock (GIL).
   - Multiprocessing achieves true parallelism by utilizing multiple CPU cores.

d. Challenges in Implementing Parallelism:
   - Managing shared data between threads/processes can be complex.
   - Overhead of creating threads/processes may negate performance gains for small tasks.
   - Addressed by using thread-safe data structures or multiprocessing shared memory.

e. When to Choose Threading vs Multiprocessing:
   - Use threading for I/O-bound tasks where the GIL is not a bottleneck.
   - Use multiprocessing for CPU-bound tasks to utilize multiple cores effectively.
"""

    