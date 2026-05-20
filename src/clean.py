import os
import sys
import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # 1. Drop rows with any missing fields
    df = df.dropna()
    
    # 2. Filter non-positive duration_seconds
    df = df[df['duration_seconds'] > 0]
    
    # 3. Handle invalid event types
    df = df[df['event_type'].astype(str).str.strip() != ""]
    
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