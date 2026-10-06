import pandas as pd

def load_dataset(path="../Dataset/dataset.csv"):
    """Load the Chennai bus stop audit dataset."""
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_dataset()
    print("Dataset shape:", df.shape)
    print(df.head())
    print("\nColumns:", len(df.columns))
