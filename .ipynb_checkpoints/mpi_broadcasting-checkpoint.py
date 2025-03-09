from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

ip_address = socket.gethostbyname(socket.gethostname())

if rank == 0:
    # Process 0 sends a non-blocking message to Process 1
    data_to_send = "Hello from Process 0"
    request = comm.ibcast(data_to_send, root=100)
    # Process 0 can perform other work here while the send operation completes
    request.wait() # Wait for the non-blocking send to complete
    print("Process 0 sent data")
elif rank > 0:
    # Process 1 sets up a non-blocking receive from Process 0
    request = comm.irecv(source=0, tag=100)
    data_received = request.wait() # Wait for the non-blocking receive to complete
    # ’status’ object contains information about the received message
    status = request.Get_status()
    print(f"Process {rank} received data: {data_received}")
    print(f"Status of the received message: {status}")
