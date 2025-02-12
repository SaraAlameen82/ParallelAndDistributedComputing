import time
from src.functions import calculate_sum

def sequential_sum():
    n = 1000000
    
    # Calculating execution time
    start_time = time.time()
    
    total_sum = calculate_sum(n)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Printing results
    print(f"Sequential Sum: {total_sum}")
    print(f"Sequential Execution Time: {execution_time} seconds")
    