from src.add_random_numbers import add_random_numbers
from src.join_random_letters import join_random_letters

# Testing join_random_letters
def test_letters_threads():
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
    
    print(f"Total time taken: {total_end_time - total_start_time} seconds")


# Testing add_random_numbers
def test_numbers_threads():
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
    
    print(f"Total time taken: {total_end_time - total_start_time} seconds")

