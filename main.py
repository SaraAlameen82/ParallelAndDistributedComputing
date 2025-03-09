from mpi4py import MPI
import socket
import numpy as np
from src.square import square

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# size -> number of processes
size = comm.Get_size()

print(f"Rank {rank} \nSize {size}")

if rank == 0:
    numbers = np.arange(size, dtype = "i")
    print(numbers)
else:
    numbers = None

# we created a vector of zeros and distributed the jobs
number = np.zeros(1, dtype = "i")
# proadcast -> one process sends to all processes
# Scatter -> one process sends to all machines 
comm.Scatter(numbers, number, root = 0)

print(numbers)
print(number)

result = square(number)
print(result)

request = comm.isend(result, dest = 0, tag = rank)

if rank == 0:
    results = np.zeros(size, dtype = "i")
    for i in range(size):
        results[i] = comm.irecv(source = i, tag = i).wait()
    print(f"The results are: {results}")

request.wait()


