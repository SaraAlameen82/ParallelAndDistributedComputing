from src.tasks import *
import threading
import time
import random
import string


def run_threads(num_letters = 1000, num_numbers = 1000):
    num_letters = 1000 // 2
    num_numbers = 1000 // 2
    start_time = time.time()
    
    # Create two processes
    process_numbers1 = threading.thread(target=add_random_numbers, args=(num_numbers))
    process_numbers2 = threading.thread(target=add_random_numbers, args=(num_numbers))
    
    process_letters1 = threading.thread(target=join_random_letters, args=(num_letters))
    process_letters2 = threading.thread(target=join_random_letters, args=(num_letters))

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
    excution_time = end_time - start_time
    print(f"Total time for threads: {excution_time} seconds.")
    
    return excution_time
