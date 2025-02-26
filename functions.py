import time
import random
import threading
from queue import Queue
import os


# Synchronization primitives
data_lock = threading.RLock()
data_condition = threading.Condition(data_lock)

# Dictionaries
latest_temperatures = {}
temperature_averages = {}
temperature_queue = Queue()
# flag = threading.Event()

num_sensors = 3
display_update_interval = 5


# Function to initialize the display
def initialize_display():
    print("Current temperatures:")
    print("Latest Temperatures: " + " ".join([f"Sensor {i}: --°C" for i in range(num_sensors)]))
    print("\n".join([f"Sensor {i} Average: --°C" for i in range(num_sensors)]))


# Function to update the display
def update_display():
    global latest_temperatures, temperature_averages
    
    while True:
        # Move cursor up to the beginning of the temperature display
        # print("\033[F" * (num_sensors + 2), end="")
        
        # Update latest temperatures
        latest_temps = " ".join([f"Sensor {i}: {latest_temperatures.get(i, '--')}°C" for i in range(num_sensors)])
        print(f"Latest Temperatures: {latest_temps}")
        
        # Update average temperatures
        for i in range(num_sensors):
            avg = temperature_averages.get(i, "--")
            if avg != "--":
                avg = f"{avg:.2f}"
            print(f"Sensor {i} Average: {avg}°C")
        
        time.sleep(display_update_interval)  # Update every second


# Temperature simulation sensor function
def simulate_sensor(id):
    global latest_temperatures, temperature_queue
    
    while True:
        # Record time 
        # record_time = time.strftime("%H:%M:%S", time.localtime())
    
        # generate temperature
        temp = random.randint(15, 40)
    
        with data_lock:
            latest_temperatures[id] = temp
            temperature_queue.put((id, temp))
            data_condition.notify_all()
           
        # Update the temperatures dictionary
        # latest_temperatures.update({id: temp})
    
        # print result
        #print(f"{temp}C at {record_time}")
    
        time.sleep(1)


# Data Processing
def process_temperatures():
    global latest_temperatures, temperature_averages
    while True:
        with data_condition:
            data_condition.wait()
            
            # Process all temperatures in the queue
            temp_sums = {i: 0 for i in range(num_sensors)}
            temp_counts = {i: 0 for i in range(num_sensors)}
            
            while not temperature_queue.empty():
                id, temp = temperature_queue.get()
                temp_sums[id] += temp
                temp_counts[id] += 1
            
            # Calculate averages
            for id in range(num_sensors):
                if temp_counts[id] > 0:
                    temperature_averages[id] = temp_sums[id] / temp_counts[id]
            
            data_condition.notify_all()
        
        time.sleep(5)
