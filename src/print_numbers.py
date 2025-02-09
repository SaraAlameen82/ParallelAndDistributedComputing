import multiprocessing
import time

# Function to be executed in a process
def print_numbers(process_name, delay):
count = 0
while count < 5: 
    time.sleep(delay) 
    count += 1 
    print(f"{process_name}: {count}")