import time

# Function to calculate the sum of all numbers from 1 to n
def calculate_sum(n):
    return sum(range(1, n + 1))

# Given large number
n = 1000000

# Measure the execution time
start_time = time.time()
total_sum = calculate_sum(n)
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Print the sum and execution time
print(f"Sum: {total_sum}")
print(f"Execution Time: {execution_time} seconds")