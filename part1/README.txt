# Part 1 Conclusion and Discussion

## 1. Square Program Conclusion

- **Sequential execution** was faster than all the other methods (~0.25 seconds) with the 10^6 input. However, the execution time grew significantly when the input size increased to 10^7, showing the limitations of sequential processing.  
- **Multiprocessing with for loop** was significantly slower than all other approaches (~2.92 seconds) with the 10^6 input. This is due to the overhead caused by manually creating processes, making it the most inefficient approach.  
- **Multiprocessing using "pool"** was the fastest parallel approach (~0.99 seconds) with the 10^6 input. It reduces overhead by efficiently distributing tasks among processes, making it the best choice for CPU-bound tasks.  
- **ProcessPoolExecutor (concurrent.futures)** took (~1.53 seconds) with the 10^6 input, which is slightly slower than `Pool.map()`. Therefore, it is useful but has a slight overhead.  

### Takeaways
- Sequential processing is more beneficial for smaller inputs.  
- The best parallelism options are **ProcessPoolExecutor** and **multiprocessing Pool**.  
- Managing too many processes causes overhead, increasing execution time instead of decreasing it.  
- **Asynchronous execution (`apply_async`)** can slightly boost performance by improving task scheduling efficiency.  

---

## 2. Process Synchronization with Semaphores  

### **What happens if more processes try to access the pool than there are available connections?**  
All processes that try acquiring a connection when all connections are in use will be blocked (will wait) at the `get_connection()` function until a connection is released. Processes are stored in a **FIFO queue**, where the first arriving processes will acquire the released connections first.  

### **How does the semaphore prevent race conditions and ensure safe access to the connections?**  
By **blocking processes** until a resource is available and only allowing a **limited number of processes** to access the shared resources at any given time.  
