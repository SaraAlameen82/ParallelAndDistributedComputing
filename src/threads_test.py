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
    thread_numbers1 = threading.Thread(target=add_random_numbers, args=(num_numbers))
    thread_numbers2 = threading.Thread(target=add_random_numbers, args=(num_numbers))
    
    thread_letters1 = threading.Thread(target=join_random_letters, args=(num_letters))
    thread_letters2 = threading.Thread(target=join_random_letters, args=(num_letters))

    # Start the processes
    thread_numbers1.start()
    thread_numbers2.start()

    thread_letters1.start()
    thread_letters2.start()

    # Wait for all processes to complete
    thread_numbers1.join()
    thread_numbers2.join()

    thread_letters1.join()
    thread_letters2.join()

    end_time = time.time()
    excution_time = end_time - start_time
    print(f"Total time for threads: {excution_time} seconds.")
    
    return excution_time
