Part 1

1. Square program 
Initial conclusion
- Sequential execution was faster than all the other methods (~0.25 seconds)
- Multiprocessing with for loop was significantlyslower that the sequential one (~2.92 secoonds). This is due to the overhead caused by creating processes manually which makes it the most inefficient approach.
- Multiprocessing using pool was the fastest parallel approach (~0.99 seconds). It reduces overhead by efficiently distributing tasks among prrocesses and it would be the best choice for CPU-bound tasks.
- Process pool executor took (~1.53 seconds), which is slightly slower than Pool.map(). Therefore it is useful but seemes to have a slight overhead. 
