import pandas as pd
import numpy as np

def load_data(path="../Dataset/dataset.csv"):
    return pd.read_csv(path)

def clean_data(df):
    data = df.copy()
    # Parse dates and standardize whitespace in object columns.
    if "Date and Time" in data.columns:
        data["Date and Time"] = pd.to_datetime(data["Date and Time"], errors="coerce")
    for col in data.select_dtypes(include="object").columns:
        data[col] = data[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    # Remove exact duplicate rows.
    data = data.drop_duplicates().reset_index(drop=True)

    # Keep original missing values for categorical fields; add explicit analysis flags.
    if "latitude" in data.columns and "longitude" in data.columns:
        data["has_coordinates"] = data["latitude"].notna() & data["longitude"].notna()

    # Composite accessibility indicators.
    access_cols = [
        "Is there space behind the bus shelter for pedestrians to walk/wheelchair to move freely?",
        "Is there space between the bus shelter and the road for pedestrians to walk/wheelchair to move freely? ",
        "Can pedestrians/wheelchair users move past the bus stop on the footpath, without having to step down on the road? "
    ]
    data["pedestrian_access_score"] = data[access_cols].eq("Yes").sum(axis=1)

    # Kerb/platform boarding quality: lower distance is better.
    kerb_col = "How far away from the kerb/Bus stop platform does the bus stop?"
    data["boarding_access_good"] = data[kerb_col].eq(
        "Perfect / Flush (Less than 30 cm): Passengers can step directly from the footpath onto the bus."
    )

    # Encroachment severity score: 2=clear, 1=partial, 0=heavy.
    enc_col = "Is the bus stop area free of encroachments?"
    enc_map = {
        " Yes – fully accessible, no obstructions": 2,
        "Partially encroached – e.g., vendors, parked two-wheelers, auto-rickshaws, construction material": 1,
        "Heavily encroached – the stop is largely unusable because of obstructions": 0
    }
    data["encroachment_score"] = data[enc_col].map(enc_map)

    # Simple service/information flags.
    route_col = "Is bus route information displayed at the stop?"
    data["route_info_available"] = data[route_col].fillna("").str.startswith("Yes").astype(int)
    name_col = "Is the name of the bus stop clearly displayed?"
    data["stop_name_visible"] = data[name_col].fillna("").str.startswith("Yes").astype(int)

    return data

if __name__ == "__main__":
    df = load_data()
    clean = clean_data(df)
    print("Original shape:", df.shape)
    print("Cleaned shape:", clean.shape)
    print("Created analysis columns: pedestrian_access_score, boarding_access_good, encroachment_score, route_info_available, stop_name_visible")
