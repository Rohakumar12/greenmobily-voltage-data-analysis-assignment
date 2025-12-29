# Voltage Data Analysis Project

## Objective
Analyze time-series voltage data to demonstrate data manipulation, analysis, and visualization skills using Python. This project was completed as part of an internship assessment.

---

## Dataset Description
The dataset contains:
- **Timestamp** – Date and time of measurement
- **Values** – Voltage readings over time

---

## Tools Used
- Python 3
- Pandas
- Matplotlib
- VS Code

---

## Analysis Performed

### 1. Data Preprocessing
- Loaded CSV data
- Cleaned column names
- Renamed `Values` to `Voltage`
- Converted timestamps to datetime format
- Sorted data chronologically

---

### 2. Data Visualization
- Plotted Voltage vs Timestamp
- Visualized raw signal to observe fluctuations

---

### 3. Moving Average Analysis
- 1000-point moving average for medium-term smoothing
- 5000-point moving average for long-term trend analysis

> Note: If the dataset contains fewer than 5000 points, the 5000-point moving average may be partially visible.

---

### 4. Peak and Low Detection
- Identified local peaks and local lows using neighboring comparisons
- Exported peak data for further analysis

---

### 5. Voltage Threshold Analysis
- Checked for all instances where Voltage < 20
- Exported results to CSV

---

### 6. Bonus: Downward Slope Acceleration
- Calculated slope and slope change
- Identified timestamps where voltage drop accelerates rapidly
- Exported results to `downward_slope_acceleration.csv`

---

## How to Run

```bash
pip install pandas matplotlib
python analysis.py
