import time
import threading
from functions import *

def main():
    """Main function to start the temperature monitoring system."""
    # Initialize display
    initialize_display()

    # Create and start sensor threads
    sensor_threads = [threading.Thread(target=simulate_sensor, args=(i,), daemon=True) for i in range(num_sensors)]
    for thread in sensor_threads:
        thread.start()

    # Create and start processing thread
    process_thread = threading.Thread(target=process_temperatures, daemon=True)
    process_thread.start()

    # Create and start display thread
    display_thread = threading.Thread(target=update_display, daemon=True)
    display_thread.start()

    # Keep the main thread running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user")

if __name__ == "__main__":
    main()
