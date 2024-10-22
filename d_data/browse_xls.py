import os
import pandas as pd

def load_excel_sheets_to_dataframe(directory, keyword):
    # List to hold dataframes
    dataframes = []
    
    # Get list of all files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.xlsx') or f.endswith('.xls')]
    
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            # Read the Excel file
            xls = pd.ExcelFile(file_path)
            
            # Iterate through the sheet names
            for sheet_name in xls.sheet_names:
                if keyword.lower() in sheet_name.lower():
                    df = pd.read_excel(file_path, sheet_name=sheet_name)
                    dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    # Concatenate all dataframes
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df
    else:
        print("No sheets with the specified keyword found.")
        return pd.DataFrame()

# Example usage
directory = r'C:\Users\JavierBenitez\Aperture Investors\Shared - Documents\Fund Finance\NAV Files - From Admin\SSNC-Private Funds\2024\09 Sep'
keyword = 'base'
combined_df = load_excel_sheets_to_dataframe(directory, keyword)
print(combined_df)
