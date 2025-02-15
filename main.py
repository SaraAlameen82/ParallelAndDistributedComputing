from src.sequential_test import run_sequential
from src.threads_test import run_threads
from src.processes_test import run_processes
import time


def calculate_speedup(t_seq, t_parallel):
    return t_seq / t_parallel

def calculate_efficiency(speedup, num_units):
    return speedup / num_units

def speedup_amdahls_law(p, n):
    return 1 / ((1 - p) + (p / n))

def speedup_gustafsons_law(p, n):
    return n - (1 - p) * n


# Measuring Execution Times
t_seq = run_sequential()
t_threads = run_threads()
t_processes = run_processes()

# Calculating Speedup
speedup_threads = calculate_speedup(t_seq, t_threads)
speedup_processes = calculate_speedup(t_seq, t_processes)

# Calculating Efficiency
num_threads = 2
num_processes = 2
efficiency_threads = calculate_efficiency(speedup_threads, num_threads)
efficiency_processes = calculate_efficiency(speedup_processes, num_processes)

# Calculate Speedup using Amdahl’s and Gustafson’s Laws
p = 0.9  # Assume 90% of the code is parallelizable

# Amdahl's Law
amdahl_threads = speedup_amdahls_law(p, num_threads)
amdahl_processes = speedup_amdahls_law(p, num_processes)

# Gustafson's Law
gustafson_threads = speedup_gustafsons_law(p, num_threads)
gustafson_processes = speedup_gustafsons_law(p, num_processes)

print("\n Performance Test \n")

print(f"Sequential execution time: {t_seq}")
print(f"Threads execution time: {t_threads}")
print(f"Processes execution time: {t_processes}\n")

# Speedup results
print(f"Threads Speedup: {speedup_threads}")
print(f"Processes Speedup: {speedup_processes}\n")

# Efficiency results
print(f"Threads Efficiency: {efficiency_threads}")
print(f"Processes Efficiency: {efficiency_processes}\n")

# Amdahl's Law results
print(f"Threads speedup using Amdahl's Law: {amdahl_threads}")
print(f"Processes speedup using Amdahl's Law: {amdahl_processes}\n")

# Gustafson's Law results
print(f"Threads speedup using Gustafson's Law: {gustafson_threads}")
print(f"Processes speedup using Gustafson's Law: {gustafson_processes}")

