import os
import pandas as pd

# Get the directory where THIS Python file is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'china_scatter_data.csv')

print(f"Looking for file at: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    # Rename items
    item_mapping = {
        'Cereals, primary': 'Cereals',
        'Roots and Tubers, Total': 'Tubers',
        'Sugar Crops Primary': 'Sugar Crops',
        'Vegetables Primary': 'Vegetables'
    }
    
    df['Item'] = df['Item'].replace(item_mapping)
    
    # Save to same directory
    output_path = os.path.join(script_dir, 'china_scatter_data_renamed.csv')
    df.to_csv(output_path, index=False)
    print(f"Success! Saved to: {output_path}")
else:
    print("File not found. Please check:")
    print("1. The filename is exactly 'china_scatter_data.csv'")
    print("2. The file is in the same folder as your Python script")