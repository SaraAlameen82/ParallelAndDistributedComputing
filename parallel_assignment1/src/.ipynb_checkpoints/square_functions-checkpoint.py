import time
import multiprocessing
from src.square import square
from multiprocessing import Process, Pool, cpu_count
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor


def sequential(numbers):
    start = time.time()
    
    for n in numbers:
        square(n)

    end = time.time()
    
    print("Sequential Execution ended")
    print(f"Execution time: {end - start:.15f}")


def process_chunk(chunk):
    """Function to process a chunk of the numbers list"""
    for n in chunk:
        square(n)


def multiprocessing_for_loop(numbers):
    start = time.time()
    processes = []
    
    chunk_size = len(numbers) // cpu_count()
    chunks = [numbers[i * chunk_size: (i + 1) * chunk_size] for i in range(cpu_count())]
    
    for chunk in chunks:
        process = Process(target=process_chunk, args=(chunk,))
        process.start()
        processes.append(process)
        
    for process in processes:
        process.join()

    end = time.time()
    
    print("Multiprocessing using for loop Execution ended")
    print(f"Parallel time: {end - start:.15f}")


def multiprocessing_pool_apply(numbers):
    """Multiprocessing using apply() (synchronous)."""
    start = time.time()

    chunk_size = len(numbers) // cpu_count()
    chunks = [numbers[i * chunk_size: (i + 1) * chunk_size] for i in range(cpu_count())]

    with Pool(processes=cpu_count()) as pool:
        for chunk in chunks:
            # Calling functions synchronously
            pool.apply(process_chunk, args=(chunk,))  

    end = time.time()
    print("Multiprocessing using 'pool.apply()' Execution ended")
    print(f"Execution time: {end - start:.15f}")


def multiprocessing_pool_apply_async(numbers):
    """Multiprocessing using `apply_async()` (asynchronous)."""
    start = time.time()

    chunk_size = len(numbers) // cpu_count()
    chunks = [numbers[i * chunk_size: (i + 1) * chunk_size] for i in range(cpu_count())]

    with Pool(processes=cpu_count()) as pool:
        results = [pool.apply_async(process_chunk, args=(chunk,)) for chunk in chunks]

        # Wait for all processes to complete
        for result in results:
            result.wait()

    end = time.time()
    print("Multiprocessing using 'pool.apply_async()' Execution ended")
    print(f"Execution time: {end - start:.15f}")


def process_pool_executor(numbers):
    start = time.time()
    chunk_size = len(numbers) // cpu_count()
    chunks = [numbers[i * chunk_size: (i + 1) * chunk_size] for i in range(cpu_count())]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, chunk) for chunk in chunks]
        for future in concurrent.futures.as_completed(futures):
            # Wait for all tasks to finish
            future.result()  

    end = time.time()
    print(f"ProcessPoolExecutor Execution ended")
    print(f"Execution time: {end - start:.15f}")

