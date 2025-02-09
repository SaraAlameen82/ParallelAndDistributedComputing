import time
import threading

# Function to calculate the sum of a range of numbers
def calculate_partial_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))

# Given large number
n = 1000000
num_threads = 4
chunk_size = n // num_threads

# List to store results from threads
results = [0] * num_threads
threads = []

# Measure the execution time
start_time = time.time()

# Create and start threads
for i in range(num_threads):
    start = i * chunk_size + 1
    end = (i + 1) * chunk_size if i != num_threads - 1 else n
    thread = threading.Thread(target=calculate_partial_sum, args=(start, end, results, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Calculate total sum
total_sum = sum(results)
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Print the sum and execution time
print(f"Sum: {total_sum}")
print(f"Execution Time: {execution_time} seconds")