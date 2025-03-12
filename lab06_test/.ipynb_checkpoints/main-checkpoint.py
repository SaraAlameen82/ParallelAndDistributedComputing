from mpi4py import MPI
import time
from src.calculate_square import square 

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initial parameters
n = int(1e6)  # Start small
max_n = int(1e10)  # Ensures compliance with 3.f
time_limit = 300  # 300 seconds
start_time = time.time()

highest_square = 0  # Tracks max square

while True:
    # Time check BEFORE computing
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        if rank == 0:
            print("[DEBUG] Time limit reached, exiting loop.")
        break  # Exit immediately

    if rank == 0:
        print(f"=== Iteration with n = {n}, Time Elapsed: {elapsed_time:.2f}s ===")

    # Distribute workload using scatter
    local_n = n // size
    start_idx = rank * local_n + 1
    end_idx = (rank + 1) * local_n if rank != size - 1 else n

    # Compute max square in local range
    max_local_square = max(square(i) for i in range(start_idx, end_idx + 1))

    # Time check BEFORE sending/receiving (prevents deadlocks)
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        print(f"[Rank {rank}] Exiting before gather to avoid deadlock.")
        break  # Exit before gathering results

    # Gather the max squares from all processes to rank 0
    all_max_squares = comm.gather(max_local_square, root=0)

    if rank == 0:
        # Rank 0 computes the highest square from the gathered values
        highest_square = max(all_max_squares)
        # Print current highest square
        print(f"Square of {n} : {highest_square}")

    # Time check AFTER sending/receiving (final safeguard)
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        print(f"[Rank {rank}] Exiting after gather.")
        break

    # Dynamically increase `n`, but stay within limit
    n = min(int(n * 1.1), max_n)

# Root process prints final results
if rank == 0:
    final_elapsed_time = time.time() - start_time
    print(f"=== FINAL RESULT ===\nHighest square reached in {final_elapsed_time:.2f}s: {highest_square}")
