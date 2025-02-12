# Function to calculate the sum of numbers from start to end
def calculate_partial_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))


# Sequential function to calculate the sum of all numbers from 1 to n
def calculate_sum(n):
    return sum(range(1, n + 1))
