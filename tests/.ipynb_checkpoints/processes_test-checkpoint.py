from src.print_numbers import print_numbers

# Testing multiprocessing
def test_processes():
    # Create two processes
    process1 = multiprocessing.Process(target=print_numbers, args=("Process-1", 1))
    process2 = multiprocessing.Process(target=print_numbers, args=("Process-2", 2))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for all processes to complete
    process1.join()
    process2.join()
    print("Exiting the Program")
