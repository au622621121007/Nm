# Import the necessary libraries for sensor and data handling
import time
from air_quality_sensor import AirQualitySensor  # Replace with the actual sensor library

# Initialize the air quality sensor
sensor = AirQualitySensor()

try:
    while True:
        # Read air quality data from the sensor
        air_quality_data = sensor.read_data()
        
        # Extract specific parameters (e.g., PM2.5, CO, NO2)
        pm25 = air_quality_data['PM2.5']
        co = air_quality_data['CO']
        no2 = air_quality_data['NO2']
        
        # Print the data for testing purposes
        print(f"PM2.5: {pm25} µg/m³, CO: {co} ppm, NO2: {no2} ppm")
        
        # You can send this data to your IoT platform for transmission

        # Sleep for a specified interval (e.g., every 5 minutes)
        time.sleep(300)

except KeyboardInterrupt:
    print("Data collection stopped by the user.")
