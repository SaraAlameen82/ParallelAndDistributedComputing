import random
import multiprocessing
from src.square_functions import *


# numbers = [random.randint(1, 5) for i in range(1, 10**6 + 1)]
numbers = [i for i in range(1, 10**6 + 1)]

if __name__ == '__main__':
    print("\nRunning with 10^7 numbers\n")
    multiprocessing.set_start_method("spawn")
    sequential(numbers)
    print("---------------------------------------")
    multiprocessing_for_loop(numbers)
    print("---------------------------------------")
    multiprocessing_pool_apply(numbers)
    print("---------------------------------------")
    multiprocessing_pool_apply_async(numbers)
    print("---------------------------------------")
    process_pool_executor(numbers) 
    print("\n")
