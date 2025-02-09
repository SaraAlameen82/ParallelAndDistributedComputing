import threading
import time

from src.tasks import join_random_letters, add_random_letters

# Testing threads
def run_threads():
    total_start_time = time.time()
    # Create threads for both functions
    thread_one = threading.Thread(target=join_random_letters)
    thread_two = threading.Thread(target=join_random_letters)
    
    # Start the threads
    thread_one.start()
    thread_two.start()
    
    # Wait for all threads to complete
    thread_one.join()
    thread_two.join()
    total_end_time = time.time()
    
    print(f"Total time taken for threads: {total_end_time - total_start_time} seconds")