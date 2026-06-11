# Comprehensive Engineering Manual: Smart Agriculture Monitoring System

## 1. Underlying Principles of Smart Agriculture
Smart agriculture integrates IoT sensing, automated edge decision-making, and cloud data distribution to maximize crop yields while minimizing resource inputs. By transitioning from scheduled routines to data-driven irrigation, farms reduce freshwater utilization by up to 30%.

## 2. Comprehensive Core Sensor Operations
* **Soil Moisture Monitoring:** Measures changes in soil dielectric permittivity or electrical resistance to calculate volumetric water content (VWC). The system uses this percentage to map crop transpiration needs.
* **DHT22 Microclimate Sensor:** Uses a capacitive humidity sensor element and a thermistor to measure surrounding ambient air conditions. It outputs a synchronized digital signal over a single-wire protocol, monitoring variables that drive plant disease outbreaks (such as high heat combined with stagnant humidity).
* **Light Intensity (LDR):** Operates on photo-conductivity principles where sensor resistance decreases as sunlight exposure increases. This tracks active photosynthesis conditions throughout daylight hours.

## 3. System Workflow & Data Pipeline
```text
[Sensor Inputs Array] 
         │
         ▼ (Data Parsing & Mapping Loop)
[Edge Automation Daemon (main.py)] ──► [Hysteresis Limits Verification] ──► [Relay Pump Power Trigger]
         │
         ▼ (File IO Append Storage)
[Time-Series Local CSV Database]
         │
         ▼ (Dataframe Feature Extraction)
[Matplotlib Chart Plotter (visualize.py)] ──► [PNG Analytics Graphics Export]
```

## 4. Automation Control Logic Matrix
To safeguard electrical components from rapid cycling and damage (actuator fluttering), the system relies on a dual-threshold hysteresis control scheme:
* **Soil Moisture < 35% AND Tank Level > 20%:** Trigger irrigation relay **ON**.
* **Soil Moisture >= 70% OR Tank Level <= 20%:** Trigger irrigation relay **OFF** (Safety Cutoff).
