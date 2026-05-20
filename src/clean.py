import os
import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # 1. Drop rows with any missing fields
    df = df.dropna()
    
    # 2. Strict Whitelist Filter for event_type (Case-sensitive exact match)
    valid_event_types = {'click', 'login', 'purchase', 'scroll', 'view'}
    df = df[df['event_type'].isin(valid_event_types)]
    
    # 3. Handle duration_seconds safely, enforce positive values, and cast to strict integer
    # This cleans up strings like '46.0' by converting to numeric floats first, then integers
    df['duration_seconds'] = pd.to_numeric(df['duration_seconds'], errors='coerce')
    df = df.dropna(subset=['duration_seconds'])
    df = df[df['duration_seconds'] > 0]
    df['duration_seconds'] = df['duration_seconds'].astype(int)
    
    # 4. Normalize timestamps to ISO 8601 (YYYY-MM-DDTHH:MM:SS)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp']) 
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    
    # Create target directory dynamically if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save output
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data("data/raw/events.csv", "data/clean/events.csv")