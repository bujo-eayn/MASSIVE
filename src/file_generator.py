import os
import json
import pandas as pd

# Step 1: Specify the folder containing the .jsonl files
dataset_folder = 'data'  # Replace with the actual folder path

# Initialize an empty list to store individual DataFrames
dataframes = []

# Step 2: Iterate through the .jsonl files in the folder
for filename in os.listdir(dataset_folder):
    if filename.endswith(".jsonl"):
        file_path = os.path.join(dataset_folder, filename)
        processed = False  # Flag to track whether the file has been processed

        # Read each JSON line and convert it to a DataFrame
        with open(file_path, 'r', encoding='utf-8') as jsonl_file:
            data = [json.loads(line) for line in jsonl_file]
            df = pd.DataFrame(data)
            dataframes.append(df)
            processed = True  # Set the flag to True after processing

        if processed:
            # You can add further processing or flag-based actions here
            print(f"File '{filename}' has been processed.")

# Step 3: Combine all DataFrames into one
massive_dataset = pd.concat(dataframes, ignore_index=True)

# Step 4: Create a single Excel file for all the data
output_filename = 'massive_dataset.xlsx'
massive_dataset.to_excel(output_filename, sheet_name='Sheet1', index=False)

print("Excel file 'massive_dataset.xlsx' has been generated.")
