import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Set the style for the plot
plt.style.use("seaborn-v0_8-whitegrid")

def create_project_chart(file_path):
    # Step 1: Load the Data
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    # Step 2: Data Preprocessing
    df.columns = df.columns.str.strip()
    df.rename(columns={"Values": "Voltage"}, inplace=True)

    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], format="%d-%m-%Y %H:%M:%S"
    )

    df = df.sort_values("Timestamp").reset_index(drop=True)
    # Step 3: Moving Averages
    df["MA_1000"] = df["Voltage"].rolling(1000).mean()
    df["MA_5000"] = df["Voltage"].rolling(5000).mean()
    # Step 5: Peaks & Lows (Optimized)
    # We do this BEFORE plotting so we have the data ready
    prev_v = df["Voltage"].shift(1)
    next_v = df["Voltage"].shift(-1)

    # Find Peaks: Higher than previous AND higher than next
    peaks_df = df[(df["Voltage"] > prev_v) & (df["Voltage"] > next_v)]

    # Find Lows: Lower than previous AND lower than next
    lows_df = df[(df["Voltage"] < prev_v) & (df["Voltage"] < next_v)]
    
    print(f"Found {len(peaks_df)} peaks and {len(lows_df)} lows.")

    # Step 6: Voltage < 20

    low_voltage_df = df[df["Voltage"] < 20]

    # Step 7: BONUS – Downward Slope Acceleration
    # Slope = difference between current and previous voltage
    df["Slope"] = df["Voltage"].diff()
    # Slope Change (Acceleration) = difference between current slope and previous slope
    df["Slope_Change"] = df["Slope"].diff()

    # If Slope_Change is negative, the drop is accelerating (getting steeper)
    accelerated_drop = df[df["Slope_Change"] < -2]

    # Save outputs to CSV
    accelerated_drop[["Timestamp", "Voltage", "Slope_Change"]].to_csv(
        "downward_slope_acceleration.csv", index=False
    )
    peaks_df.to_csv("peaks.csv", index=False)
    low_voltage_df.to_csv("low_voltage.csv", index=False)
    
    print("Files saved: peaks.csv, low_voltage.csv, downward_slope_acceleration.csv")
    # Step 4: Visualization
    plt.figure(figsize=(14, 7))

    plt.plot(df["Timestamp"], df["Voltage"],
             label="Original Value", color="lightgray", linewidth=1)

    plt.plot(df["Timestamp"], df["MA_1000"],
             label="1000 Value Moving Average", color="orange", linewidth=2)

    plt.plot(df["Timestamp"], df["MA_5000"],
             label="5000 Value Moving Average", color="green", linewidth=2)

    plt.title("Values with 1000 and 5000 Value Moving Averages", fontsize=16)
    plt.xlabel("Timestamp")
    plt.ylabel("Voltage")

    # Format the date on X-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
    plt.xticks(rotation=45)
    
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    
    # Show the plot LAST so it doesn't block the file saving
    plt.show()

    return peaks_df, lows_df, low_voltage_df, accelerated_drop

# Run the project
create_project_chart("Sample_Data.csv")