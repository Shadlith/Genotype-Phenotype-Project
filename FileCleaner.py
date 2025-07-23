import os
import glob
import pandas as pd
import sqlite3

# Path to your CSV files
csv_directory = 'C:\\College\\Masters Semster 5\\Privacy\\opensnp_datadump.current'

print(csv_directory)

# Specify your custom column names (first should be 'Filename')
column_names = ['Filename', 'rsid', 'chromosome', 'position', 'genotype']  # Adjust as needed

csv_files = glob.glob(os.path.join(csv_directory, '*.txt'))

valid_files = []

for file_path in csv_files:
    try:
        # Read only the header line to determine number of columns
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue  # Skip comment or empty lines
                else:
                    header_line = line
                    break
        headers = header_line.split(',')
        num_columns = len(headers)

        # Check if the header has the expected number of columns
        if num_columns == 4:
            valid_files.append(file_path)
        else:
            print(f"Skipping {os.path.basename(file_path)}: {num_columns} columns found.")
    except UnicodeDecodeError:
        print(f"Skipping {os.path.basename(file_path)} due to decoding error.")
        continue

# Process valid files
all_data = []

for file_path in valid_files:
    try:
        # Read CSV, ignoring comment lines starting with '#'
        df = pd.read_csv(file_path, comment='#', header=None, encoding='utf-8')
        # Check if df has the expected number of columns
        if df.shape[1] != len(column_names) - 1:
            print(f"Skipping {os.path.basename(file_path)}: unexpected number of columns after read.")
            continue
        # Assign column names
        df.columns = column_names[1:]  # Set data column names
        # Add filename column
        filename = os.path.basename(file_path)
        df.insert(0, 'Filename', filename)
        all_data.append(df)
    except (UnicodeDecodeError, ValueError) as e:
        print(f"Skipping {os.path.basename(file_path)} during data read: {e}")
        continue

# Combine all dataframes
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv('combined_output.csv', index=False)
    print("Combined data saved to 'combined_output.csv'.")
else:
    print("No valid data files were processed.")
    
    