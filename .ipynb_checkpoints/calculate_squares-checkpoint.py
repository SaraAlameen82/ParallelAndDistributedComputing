from mpi4py import MPI
import time

def square_chunked(max_n):
    """
    Compute the sum of squares up to max_n using MPI in chunks.
    """
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Divide the range into chunks for each process
    chunk_size = max_n // size
    start = rank * chunk_size + 1
    end = start + chunk_size if rank < size - 1 else max_n + 1

    # Compute the sum of squares for this process's chunk
    local_squares_sum = sum(i**2 for i in range(start, end))

    # Reduce the results to the root process
    total_sum = comm.reduce(local_squares_sum, op=MPI.SUM, root=0)

    if rank == 0:
        return total_sum

    return None

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Start with a small n and dynamically adjust to find the largest n within 300 seconds
    n = int(1e8)  # Start with n = 10^8
    step_size = int(1e7)  # Increment n in steps of 10^7
    max_time_limit = 300  # Maximum allowed runtime in seconds

    while True:
        if rank == 0:
            print(f"Testing with n = {n}...")

        start_time = time.time()
        result = square_chunked(n)
        end_time = time.time()

        elapsed_time = end_time - start_time

        if rank == 0:
            print(f"Time taken for n = {n}: {elapsed_time:.2f} seconds")

            if elapsed_time > max_time_limit:
                print(f"Exceeded time limit of {max_time_limit} seconds.")
                print(f"Largest n computed within limit: {n - step_size}")
                break

            print(f"Sum of squares up to {n}: {result}")
            print(f"Last square: {(n)**2}")

        # Increment n for the next iteration
        n += step_size

        # Synchronize all processes before next iteration
        comm.Barrier()
