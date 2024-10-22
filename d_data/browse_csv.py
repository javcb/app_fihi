import os
import pandas as pd

def load_csvs_to_dataframe(directory):
    # List to hold dataframes
    dataframes = []
    
    # Get list of all files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Initialize a reference for column names
    reference_columns = None
    
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # If reference_columns is None, set it to the columns of the first file
            if reference_columns is None:
                reference_columns = df.columns
                dataframes.append(df)
            else:
                # Check if the columns match the reference columns
                if all(df.columns == reference_columns):
                    dataframes.append(df)
                else:
                    print(f"Skipping {file} due to nonconforming columns.")
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    # Concatenate all dataframes
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df
    else:
        print("No conforming CSV files found.")
        return pd.DataFrame()

# Example usage
directory = r'C:\Users\JavierBenitez\Aperture Investors\Shared - Documents\Fund Finance\10 Power Query\00 Source Data\00.11 State Street\Positions'
combined_df = load_csvs_to_dataframe(directory)
print(combined_df)
