from src.tasks import join_random_letters 
from src.tasks import add_random_numbers
import multiprocessing
import time


def run_processes(num_letters=1000, num_numbers=1000):
    num_letters //= 2
    num_numbers //= 2
    start_time = time.time()

    # Creating two processes for each function
    process_letters1 = multiprocessing.Process(target=join_random_letters, args=(num_letters,))
    process_letters2 = multiprocessing.Process(target=join_random_letters, args=(num_letters,))

    process_numbers1 = multiprocessing.Process(target=add_random_numbers, args=(num_numbers,))
    process_numbers2 = multiprocessing.Process(target=add_random_numbers, args=(num_numbers,))

    # Starting the processes
    process_letters1.start()
    process_letters2.start()

    process_numbers1.start()
    process_numbers2.start()

    # Waiting for all processes to finish
    process_letters1.join()
    process_letters2.join()
  
    process_numbers1.join()
    process_numbers2.join()

    end_time = time.time()
    excution_time = end_time - start_time
    # print(f"Total time for processes: {excution_time} seconds.")
    
    return excution_time
