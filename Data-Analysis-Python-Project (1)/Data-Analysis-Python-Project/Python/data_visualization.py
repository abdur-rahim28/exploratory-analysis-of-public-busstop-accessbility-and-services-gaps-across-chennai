import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from data_cleaning import load_data, clean_data

OUT = Path("../Visualizations")
OUT.mkdir(exist_ok=True)

def bar(series, title, filename, xlabel=""):
    ax = series.plot(kind="bar", figsize=(9,5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of bus stops")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUT/filename, dpi=180)
    plt.close()

def create_visualizations(df):
    bar(df["Condition of Bus Shelter"].fillna("Missing").value_counts(),
        "Bus Shelter Condition Distribution", "distribution_analysis.png")
    bar(df["How far away from the kerb/Bus stop platform does the bus stop?"].value_counts(),
        "Bus Boarding Distance / Kerb Relationship", "trend_analysis.png")
    bar(df["Is the bus stop area free of encroachments?"].value_counts(),
        "Encroachment Levels at Bus Stops", "category_analysis.png")
    numeric = df[["pedestrian_access_score","encroachment_score","route_info_available","stop_name_visible"]].corr()
    ax = numeric.plot(kind="bar", figsize=(9,5))
    ax.set_title("Accessibility and Service Indicator Correlations")
    ax.set_ylabel("Correlation value")
    ax.set_xlabel("Indicators")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(OUT/"correlation_analysis.png", dpi=180)
    plt.close()

if __name__ == "__main__":
    create_visualizations(clean_data(load_data()))
