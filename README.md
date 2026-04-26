# Smart Energy Analysis for an Automated Container Terminal

## Project Overview

This project analyzes hourly energy consumption for an automated container terminal.  
The goal is to evaluate how solar expansion, efficiency improvements, and load shifting can reduce grid dependency and peak grid demand.

The project is designed as an energy data analysis case study using Python, SQL, and Streamlit.

---

## Main Analytical Questions

This project answers the following questions:

1. When does the terminal consume the most energy?
2. When does solar generation reach its peak?
3. Is there a mismatch between energy demand and solar generation?
4. How dependent is the system on the electrical grid?
5. Which strategy is more effective:
   - increasing solar capacity,
   - improving operational efficiency,
   - or shifting load away from peak hours?
6. Can a combined strategy reduce peak grid demand?

---

## Dataset and Assumptions

The dataset represents a 24-hour operating profile for an automated container terminal.

Main assumptions:

- One row represents one hour.
- Operations per hour represent container-handling activity.
- Energy per operation is assumed to be 4.5 kWh in the baseline case.
- Base load is assumed to be 120 kWh per hour.
- Solar generation follows a daytime production profile.
- No battery storage is modeled in the current version.

Main columns:

| Column | Meaning |
|---|---|
| hour | Hour of the day |
| operations_per_hour | Number of container operations per hour |
| energy_per_operation_kwh | Energy required for one operation |
| base_load_kwh | Constant terminal load |
| solar_generation_kwh | Solar energy generated per hour |
| operational_energy_kwh | Energy used by operations |
| total_demand_kwh | Total energy demand |
| grid_usage_kwh | Energy required from the grid |

---

## Methodology

The analysis follows these steps:

1. Build a baseline hourly energy model.
2. Calculate total demand, solar generation, and grid usage.
3. Calculate key performance indicators.
4. Test different scenarios.
5. Use SQL to validate and analyze the data.
6. Visualize energy profiles and scenario comparisons.
7. Provide recommendations based on the results.

---

## Key Performance Indicators

The following KPIs were used:

- Total Energy Demand
- Solar Contribution %
- Grid Dependency %
- Peak Grid Demand
- Peak Grid Hour

---

## Baseline Results

In the baseline scenario:

| KPI | Value |
|---|---:|
| Total Demand | 6097.5 kWh |
| Total Solar Generation | 1345 kWh |
| Total Grid Usage | 4752.5 kWh |
| Solar Contribution | 22.06% |
| Grid Dependency | 77.94% |
| Peak Grid Demand | 256.0 kWh |
| Peak Grid Hour | 17:00 |

### Baseline Insight

The system is highly dependent on grid electricity.  
Solar generation covers only about 22% of total demand, while grid dependency remains close to 78%.

Peak grid demand occurs at 17:00, when solar generation is already declining while operational demand remains high.

---

## Scenario Analysis

The following scenarios were tested:

| Scenario | Description |
|---|---|
| Baseline | Original system behavior |
| Solar +30% | Increase solar generation by 30% |
| Efficiency +15% | Reduce energy per operation by 15% |
| Operations +20% | Increase operational load by 20% |
| Combined Strategy | Solar +30%, efficiency +15%, and load shifting |

---

## Scenario Results

| Scenario | Total Demand (kWh) | Solar Contribution | Grid Dependency | Peak Grid Demand (kWh) | Peak Hour |
|---|---:|---:|---:|---:|---:|
| Baseline | 6097.5 | 22.06% | 77.94% | 256.0 | 17 |
| Solar +30% | 6097.5 | 28.68% | 71.32% | 251.0 | 18 |
| Efficiency +15% | 5614.88 | 23.95% | 76.05% | 232.4 | 18 |
| Operations +20% | 6741.0 | 19.95% | 80.05% | 290.2 | 17 |
| Combined Strategy | 5614.88 | 31.14% | 68.86% | 227.1 | 19 |

---

## Key Insights

### 1. Solar expansion improves daytime performance

Increasing solar capacity by 30% increased solar contribution from 22.06% to 28.68%.  
Grid dependency decreased from 77.94% to 71.32%.

However, solar expansion alone did not fully solve the late-afternoon peak problem.

### 2. Efficiency improvement reduces total demand

Improving efficiency by 15% reduced total energy demand from 6097.5 kWh to 5614.88 kWh.  
Peak grid demand also decreased from 256.0 kWh to 232.4 kWh.

This shows that efficiency has a direct impact on total energy consumption.

### 3. Increased operations create higher grid dependency

When operations increased by 20%, total demand increased to 6741.0 kWh.  
Grid dependency increased to 80.05%, and peak grid demand reached 290.2 kWh.

This shows that operational growth must be supported by energy optimization.

### 4. The main problem is a timing mismatch

Solar generation peaks around midday, while peak grid demand occurs later in the day.  
This mismatch means that renewable energy is not fully aligned with demand timing.

### 5. Combined strategy gives the best result

The combined strategy reduced grid dependency from 77.94% to 68.86%.  
It also reduced peak grid demand from 256.0 kWh to 227.1 kWh.

This was achieved by combining:

- solar expansion,
- efficiency improvement,
- and load shifting from late afternoon to solar-rich hours.

---

## Final Recommendation

The best strategy is not a single solution, but a combined energy optimization approach.

Recommended actions:

1. Expand solar capacity to reduce daytime grid dependency.
2. Improve operational efficiency to reduce total energy demand.
3. Apply load shifting to move energy-intensive operations toward solar-rich hours.
4. Consider battery storage in future work to store excess solar energy for evening peak periods.

The combined strategy is the most effective because it addresses both total energy demand and the timing mismatch between solar generation and grid demand.

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- Streamlit
- Jupyter Notebook

---

## Dashboard

The project includes a Streamlit dashboard.

To run the dashboard:

```bash
streamlit run app.py
