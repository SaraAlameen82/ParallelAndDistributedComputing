from src.tasks import *
import multiprocessing
import time
import random
import string


def run_threads(num_letters = 1000, num_numbers = 1000):
    num_letters = 1000 // 2
    num_numbers = 1000 // 2
    start_time = time.time()
    
    # Create two processes
    process_numbers1 = multiprocessing.Process(target=print_numbers, args=("Process-1", 1))
    process_numbers2 = multiprocessing.Process(target=print_numbers, args=("Process-2", 2))
    
    process_letters1 = multiprocessing.Process(target=print_numbers, args=("Process-1", 1))
    process_letters2 = multiprocessing.Process(target=print_numbers, args=("Process-2", 2))

    # Start the processes
    process_numbers1.start()
    process_numbers2.start()

    process_letters1.start()
    process_letters2.start()

    # Wait for all processes to complete
    process_numbers1.join()
    process_numbers2.join()

    process_letters1.join()
    process_letters2.join()

    end_time = time.time()
    print(f"Total time for processes: {end_time - start_time} seconds.")
