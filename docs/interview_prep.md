-- 1. Interview Question: Explain your IoT-Enabled Smart Agriculture Monitoring System project.
-- Answer:
-- In this project, I built an IoT-based smart agriculture monitoring system that monitors soil moisture, temperature, humidity, light intensity, and water level. Based on sensor readings, the system generates alerts and can control a water pump or irrigation system automatically. This project helps farmers monitor field conditions and take timely action to improve crop health and reduce water wastage.

-- 2. Interview Question: What problem does this project solve?
-- Answer:
-- This project solves the problem of manual field monitoring and inefficient irrigation. It helps farmers know when soil is dry, when temperature is high, or when water level is low, so they can take action quickly.

-- 3. Interview Question: Which sensors are used in this project?
-- Answer:
-- The project can use a soil moisture sensor, DHT11 or DHT22 temperature and humidity sensor, LDR sensor for light intensity, and a water level sensor.

-- 4. Interview Question: What microcontroller can be used for this project?
-- Answer:
-- Arduino UNO can be used for a basic version, while ESP32 is better for an IoT version because it has built-in Wi-Fi support for sending data to dashboards or cloud platforms.

-- 5. Interview Question: How does the irrigation logic work?
-- Answer:
-- The system reads soil moisture values and compares them with a predefined threshold. If soil moisture is below the threshold, the system turns the pump ON. If soil moisture is sufficient, the pump remains OFF.

-- 6. Interview Question: How does this project use IoT?
-- Answer:
-- The project uses IoT by collecting sensor data from the field and sending it to a dashboard or cloud platform where users can monitor conditions remotely.

-- 7. Interview Question: What output does your project generate?
-- Answer:
-- The project generates sensor readings, alert messages, pump ON/OFF status, dashboard updates, and optional CSV logs for temperature, humidity, soil moisture, light, and water level.

-- 8. Interview Question: Why is data logging useful in this project?
-- Answer:
-- Data logging helps track field conditions over time. Farmers or analysts can use this historical data to understand crop needs, irrigation patterns, and environmental changes.

-- 9. Interview Question: What challenges did you face in this project?
-- Answer:
-- The main challenges were setting correct sensor threshold values, handling fluctuating sensor readings, simulating hardware accurately, and integrating dashboard or alert logic.

-- 10. Interview Question: How can this project be improved further?
-- Answer:
-- This project can be improved by adding weather API integration, automatic drip irrigation, mobile app alerts, solar power support, AI-based crop recommendation, disease detection using camera, and cloud-based analytics.
