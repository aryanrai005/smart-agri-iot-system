import os
import sys
import time
import random
import csv
from datetime import datetime
import requests

SOIL_DRY_LIMIT = 35.0
SOIL_WET_LIMIT = 70.0
LOW_TANK_LIMIT = 20.0
THINGSPEAK_URL = "http://thingspeak.com"

# paste your key inside the quotes if you have one, or leave it as is to run locally
THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_WRITE_API_KEY"  

DATA_DIRECTORY = "data"
LOG_FILE_PATH = os.path.join(DATA_DIRECTORY, "telemetry_logs.csv")

def initialize_storage():
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)
        print(f"[SYSTEM INIT] Created missing directory workspace: '{DATA_DIRECTORY}'")
    if not os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, mode='w', newline='', encoding='utf-8') as log_file:
            writer = csv.writer(log_file)
            writer.writerow(["Timestamp", "Temperature_C", "Humidity_Percent", "SoilMoisture_Percent", "Light_Percent", "WaterLevel_Percent", "PumpStatus"])
        print(f"[SYSTEM INIT] Created telemetry log spreadsheet: '{LOG_FILE_PATH}'")

def generate_sensor_readings(current_pump_on):
    temp = round(random.uniform(22.0, 38.0), 1)
    humidity = round(random.uniform(45.0, 85.0), 1)
    light = round(random.uniform(10.0, 95.0), 1)
    water_level = round(random.uniform(60.0, 90.0), 1) if not current_pump_on else round(random.uniform(30.0, 55.0), 1)

    if current_pump_on:
        soil_moisture = round(random.uniform(55.0, 78.0), 1)
    else:
        soil_moisture = round(random.uniform(20.0, 42.0), 1)

    return temp, humidity, soil_moisture, light, water_level

def process_automation_logic(soil_moist, tank_level, current_pump_state):
    new_pump_state = current_pump_state
    if tank_level <= LOW_TANK_LIMIT:
        new_pump_state = 0
        print("[ALARM - CRITICAL] Emergency Low Water Level! Forcing pump shutdown.")
    elif soil_moist < SOIL_DRY_LIMIT:
        if current_pump_state == 0:
            new_pump_state = 1
            print(f"[AUTOMATION Trigger] Soil Moisture dropped to {soil_moist}%. Activating irrigation pump.")
    elif soil_moist >= SOIL_WET_LIMIT:
        if current_pump_state == 1:
            new_pump_state = 0
            print(f"[AUTOMATION Trigger] Soil Moisture reached {soil_moist}%. Deactivating irrigation pump.")
    return new_pump_state

def save_to_csv(timestamp, t, h, sm, l, wl, pump):
    try:
        with open(LOG_FILE_PATH, mode='a', newline='', encoding='utf-8') as log_file:
            writer = csv.writer(log_file)
            writer.writerow([timestamp, t, h, sm, l, wl, pump])
    except IOError as error:
        print(f"[FILE Error] Unable to save data record. Details: {error}")

def transmit_telemetry(t, h, sm, l, wl, pump):
    if THINGSPEAK_API_KEY == "YOUR_THINGSPEAK_WRITE_API_KEY":
        print("[CLOUD NOTICE] Running locally. Add your ThingSpeak API key to push online.")
        return
    payload = {"api_key": THINGSPEAK_API_KEY, "field1": t, "field2": h, "field3": sm, "field4": l, "field5": wl, "field6": pump}
    try:
        response = requests.post(THINGSPEAK_URL, data=payload, timeout=10)
        if response.status_code == 200 and response.text != "0":
            print(f"[CLOUD TELEMETRY] Telemetry update successful. Server Token Code: {response.text}")
    except requests.exceptions.RequestException as network_error:
        print(f"[NETWORK Error] Cloud route timed out. Details: {network_error}")

def run_simulation_engine():
    print("======================================================================")
    print("      LAUNCHING PRODUCTION PYTHON SMART FARMING TELEMETRY ENGINE     ")
    print("======================================================================")
    initialize_storage()
    pump_active = 0
    execution_cycle = 1
    try:
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            temp, hum, moisture, light, water = generate_sensor_readings(pump_active)
            pump_active = process_automation_logic(moisture, water, pump_active)

            print(f"\n[Execution Cycle #{execution_cycle}] - {current_time}")
            print(f" -> Air Context:       {temp}°C | Humidity: {hum}%")
            print(f" -> Soil Status:       Moisture: {moisture}%")
            print(f" -> Resource Context:  Storage Tank Level: {water}% | Light Level: {light}%")
            print(f" -> Actuator Terminal: Active Pump State: {'RUNNING [ON]' if pump_active == 1 else 'IDLE [OFF]'}")

            save_to_csv(current_time, temp, hum, moisture, light, water, pump_active)
            transmit_telemetry(temp, hum, moisture, light, water, pump_active)

            execution_cycle += 1
            time.sleep(5)  # Speeds up local simulation output loop (updates every 5 seconds)
    except KeyboardInterrupt:
        print("\n[SYSTEM MONITOR] Simulation engine safely shut down. Exiting clean.")
        sys.exit(0)

if __name__ == "__main__":
    run_simulation_engine()
