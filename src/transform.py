import os
import pandas as pd

def transform_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    df['date'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
    
    # Create target directory dynamically if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    transform_data("data/clean/events.csv", "data/transformed/events.csv")