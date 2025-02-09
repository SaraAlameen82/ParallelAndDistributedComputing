import time
import multiprocessing

# Function to calculate the sum of a range of numbers
def calculate_partial_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))

# Given large number
n = 1000000
num_processes = 4
chunk_size = n // num_processes

# List to store results from processes
results = multiprocessing.Array('i', num_processes)
processes = []

# Measure the execution time
start_time = time.time()

# Create and start processes
for i in range(num_processes):
    start = i * chunk_size + 1
    end = (i + 1) * chunk_size if i != num_processes - 1 else n
    process = multiprocessing.Process(target=calculate_partial_sum, args=(start, end, results, i))
    processes.append(process)
    process.start()

# Wait for all processes to complete
for process in processes:
    process.join()

# Calculate total sum
total_sum = sum(results)
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Print the sum and execution time
print(f"Sum: {total_sum}")
print(f"Execution Time: {execution_time} seconds")