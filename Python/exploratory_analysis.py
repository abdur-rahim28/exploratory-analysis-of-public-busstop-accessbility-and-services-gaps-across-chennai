import pandas as pd
from data_cleaning import load_data, clean_data

def frequency_table(df, column):
    return df[column].value_counts(dropna=False).reset_index(name="count")

def accessibility_summary(df):
    cols = {
        "Behind shelter space":"Is there space behind the bus shelter for pedestrians to walk/wheelchair to move freely?",
        "Road-side space":"Is there space between the bus shelter and the road for pedestrians to walk/wheelchair to move freely? ",
        "Footpath continuity":"Can pedestrians/wheelchair users move past the bus stop on the footpath, without having to step down on the road? ",
        "Good boarding position":"boarding_access_good",
        "No/low encroachment":"encroachment_score"
    }
    rows=[]
    for label,col in cols.items():
        if col in df.columns:
            if col == "encroachment_score":
                rows.append([label, round((df[col] == 2).mean()*100,1)])
            else:
                rows.append([label, round(df[col].eq("Yes").mean()*100,1) if col != "boarding_access_good" else round(df[col].mean()*100,1)])
    return pd.DataFrame(rows, columns=["indicator","percent"])

if __name__ == "__main__":
    raw = load_data()
    df = clean_data(raw)
    print(accessibility_summary(df).to_string(index=False))
