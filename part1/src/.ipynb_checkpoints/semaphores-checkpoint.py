import time
import random
from multiprocessing import Semaphore, Process, current_process


class ConnectionPool:
    """This class simulates a pool of database connections with a semaphore to control access."""
    
    def __init__(self, max_connections):
        # Limit access to max_connections
        self.semaphore = Semaphore(max_connections)  
        self.connections = list(range(1, max_connections + 1))  

    def get_connection(self):
        """Acquires a connection from the pool."""
        self.semaphore.acquire() 
        # Returning the list of connections after removing the acquired 
        # connection so it is not acquired until it gets released.
        return self.connections.pop() 

    def release_connection(self, connection):
        """Releases a connection back to the pool."""
        # Adding the popped connection back to the list so it can be aquired again 
        self.connections.append(connection)
        # Releasing the semaphore
        self.semaphore.release() 


def access_database(pool):
    """This is a function simulates a process performing a database operation"""
    process_name = current_process().name
    
    print(f"{process_name} is waiting for a connection...")
    connection = pool.get_connection()
    
    print(f"{process_name} acquired connection {connection}")
    time.sleep(random.uniform(1, 3)) 
    print(f"{process_name} releasing connection {connection}")

    pool.release_connection(connection)


if __name__ == "__main__":
    MAX_CONNECTIONS = 3  
    NUM_PROCESSES = 10  

    pool = ConnectionPool(MAX_CONNECTIONS)
    processes = [Process(target=access_database, args=(pool,)) for _ in range(NUM_PROCESSES)] 

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("All processes have completed.")




    