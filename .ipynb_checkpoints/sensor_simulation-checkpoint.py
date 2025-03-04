import random
import time
import threading
from queue import Queue

# Global dictionaries
latest_temperatures = {}
temperature_averages = {}

# Queue for temperature readings
temperature_queue = Queue()

def simulate_sensor(sensor_id):
    """
    Simulates temperature readings from a sensor and updates the global dictionary.
    """
    global latest_temperatures
    while True:
        temperature = random.randint(15, 40)
        latest_temperatures[sensor_id] = temperature
        temperature_queue.put((sensor_id, temperature))
        time.sleep(1)

def process_temperatures():
    """
    Continuously calculates the average temperature from readings in the queue.
    """
    global temperature_averages
    sensor_readings = {}
    
    while True:
        sensor_id, temperature = temperature_queue.get()
        
        if sensor_id not in sensor_readings:
            sensor_readings[sensor_id] = []
        
        sensor_readings[sensor_id].append(temperature)
        
        # Calculate average for each sensor
        for sid, readings in sensor_readings.items():
            average = sum(readings) / len(readings)
            temperature_averages[sid] = average
        
        # Optional: Limit the number of readings to prevent memory growth
        if len(sensor_readings[sensor_id]) > 100:
            sensor_readings[sensor_id] = sensor_readings[sensor_id][-100:]

def main():
    # Create and start sensor simulation threads
    for i in range(3):  # Simulating 3 sensors
        sensor_thread = threading.Thread(target=simulate_sensor, args=(f"Sensor_{i+1}",), daemon=True)
        sensor_thread.start()

    # Create and start data processing thread
    process_thread = threading.Thread(target=process_temperatures, daemon=True)
    process_thread.start()

    # Main program loop
    try:
        while True:
            print("Latest Temperatures:", latest_temperatures)
            print("Temperature Averages:", temperature_averages)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()