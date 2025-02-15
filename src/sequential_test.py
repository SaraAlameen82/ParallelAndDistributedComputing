from src.tasks import join_random_letters, add_random_numbers
import time


def run_sequential(num_letters = 1000, num_numbers = 1000):
  # Measure the total time for both operations.
  start_time = time.time()

  join_random_letters(num_letters)
  add_random_numbers(num_numbers)
  
  end_time = time.time()
  excution_time = end_time - start_time
  print(f"Total time for sequential: {excution_time} seconds.")
    
  return excution_time
