import os
import pandas as pd

def extract_features(input_path, output_path):
    df = pd.read_csv(input_path)
    
    df['duration_minutes'] = df['duration_seconds'] / 60.0
    df['weekday'] = pd.to_datetime(df['date']).dt.day_name()
    
    # Create target directory dynamically if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    extract_features("data/transformed/events.csv", "data/features/events.csv")