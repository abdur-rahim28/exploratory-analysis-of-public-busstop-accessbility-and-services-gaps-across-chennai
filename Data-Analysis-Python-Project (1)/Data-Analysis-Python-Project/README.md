# Exploratory Analysis of Public Bus Stop Accessibility and Service Gaps Across Chennai

## Project Overview
This project performs exploratory data analysis on a Chennai public bus stop audit dataset. The analysis identifies accessibility constraints, shelter/service conditions, encroachment, safety concerns, and information gaps.

## Dataset
- Records: 210
- Original columns: 85
- Source file used: chennai_bus_stop_audit_2026(2).csv
- Analysis dataset: `Dataset/dataset.csv`

## Problem Definition
To analyze public bus stop accessibility and service conditions across Chennai, identify differences in stop facilities and accessibility, detect areas with inadequate or poor-quality infrastructure, and explore patterns that may indicate public transport service gaps.

## Main Objectives
1. Examine pedestrian and wheelchair accessibility.
2. Analyze bus-to-kerb boarding conditions.
3. Assess shelter condition, roof, shade, seating and capacity.
4. Identify encroachment and drainage problems.
5. Evaluate lighting, safety and passenger information.
6. Explore nearby land-use patterns.
7. Produce visual summaries that support recommendations.

## Project Structure
```text
Data-Analysis-Python-Project/
├── README.md
├── Dataset/
│   └── dataset.csv
├── Notebook/
│   └── Data_Analysis_EDA.ipynb
├── Python/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── data_visualization.py
├── Visualizations/
│   ├── distribution_analysis.png
│   ├── trend_analysis.png
│   ├── category_analysis.png
│   └── correlation_analysis.png
├── Screenshots/
│   ├── dataset_preview.png
│   ├── data_cleaning.png
│   └── analysis_output.png
└── Documentation/
    ├── Project_Report.pdf
    └── Data_Dictionary.xlsx
```

## Key Analysis Indicators
- Pedestrian access score: 0–3 based on three movement/access questions.
- Boarding quality: whether the bus is observed at a flush position (<30 cm).
- Encroachment score: 0–2, where 2 means fully clear.
- Route information flag and stop-name visibility flag.

## How to Run
1. Open the project folder in VS Code or Jupyter.
2. Install: `pandas numpy matplotlib openpyxl reportlab nbformat`.
3. Run `Python/data_loading.py`.
4. Run `Python/data_cleaning.py`.
5. Run `Python/data_visualization.py`.
6. Open `Notebook/Data_Analysis_EDA.ipynb`.

## Important Note
This is an exploratory audit analysis. It identifies observed conditions in the supplied dataset; it should not be interpreted as a complete census of every bus stop in Chennai unless the sampling design supports that claim.
