"""
Filename: visualize.py
Description: Generates performance analytics charts from saved IoT CSV logs.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE_PATH = os.path.join("data", "telemetry_logs.csv")

def generate_analytics():
    if not os.path.exists(LOG_FILE_PATH):
        print(f"[ERROR] '{LOG_FILE_PATH}' not found. Run main.py first to collect data.")
        return

    # Load and parse data
    df = pd.read_csv(LOG_FILE_PATH)
    if df.empty:
        print("[WARNING] Log file is empty. Run main.py longer to generate telemetry points.")
        return

    # Take the last 20 records for clear plotting
    df = df.tail(20)

    # Initialize subplots window
    plt.style.use('default')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Plot 1: Moisture and Water Tank Levels
    ax1.plot(df['Timestamp'], df['SoilMoisture_Percent'], marker='o', color='#2ca02c', label='Soil Moisture (%)', linewidth=2)
    ax1.plot(df['Timestamp'], df['WaterLevel_Percent'], marker='s', color='#1f77b4', label='Water Tank Level (%)', linestyle='--')
    ax1.set_title("Field Hydro-Telemetry & Resource Management Profile", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Percentage (%)")
    ax1.legend(loc="upper left")

    # Plot 2: Temperature Dynamics
    ax2.plot(df['Timestamp'], df['Temperature_C'], marker='^', color='#d62728', label='Air Temperature (°C)', linewidth=2)
    ax2.set_title("Thermal Environmental Dynamics Monitor", fontsize=12, fontweight='bold')
    ax2.set_ylabel("Temperature (°C)")
    ax2.set_xlabel("Telemetry Capture Timestamps")
    ax2.legend(loc="upper left")

    # Highlight when the pump was active (PumpStatus == 1)
    for index, row in df.iterrows():
        if row['PumpStatus'] == 1:
            ax1.axvspan(row['Timestamp'], row['Timestamp'], color='#9467bd', alpha=0.3, label='Pump ACTIVE' if 'Pump ACTIVE' not in ax1.get_legend_handles_labels() else "")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save chart to outputs directory
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    chart_path = os.path.join(output_dir, "analytics_chart.png")
    plt.savefig(chart_path, dpi=300)
    print(f"[SUCCESS] Analytical telemetry charts generated and exported to '{chart_path}'")
    plt.show()

if __name__ == "__main__":
    generate_analytics()
