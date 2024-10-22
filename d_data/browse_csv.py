<<<<<<< HEAD
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
=======
<!DOCTYPE html>
<html>
<head>
    <title>DataFrame Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            cursor: pointer;
        }
    </style>
    <script>
        function sortTable(n) {
            var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
            table = document.getElementById("dataTable");
            switching = true;
            dir = "asc"; 
            while (switching) {
                switching = false;
                rows = table.rows;
                for (i = 1; i < (rows.length - 1); i++) {
                    shouldSwitch = false;
                    x = rows[i].getElementsByTagName("TD")[n];
                    y = rows[i + 1].getElementsByTagName("TD")[n];
                    if (dir == "asc") {
                        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    } else if (dir == "desc") {
                        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                }
                if (shouldSwitch) {
                    rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                    switching = true;
                    switchcount++; 
                } else {
                    if (switchcount == 0 && dir == "asc") {
                        dir = "desc";
                        switching = true;
                    }
                }
            }
        }

        function filterTable() {
            var input, filter, table, tr, td, i, j, txtValue;
            input = document.getElementById("filterInput");
            filter = input.value.toLowerCase();
            table = document.getElementById("dataTable");
            tr = table.getElementsByTagName("tr");
            for (i = 1; i < tr.length; i++) {
                tr[i].style.display = "none";
                td = tr[i].getElementsByTagName("td");
                for (j = 0; j < td.length; j++) {
                    if (td[j]) {
                        txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toLowerCase().indexOf(filter) > -1) {
                            tr[i].style.display = "";
                            break;
                        }
                    }
                }
            }
        }
    </script>
</head>
<body>

<h2>DataFrame Table</h2>
<input type="text" id="filterInput" onkeyup="filterTable()" placeholder="Filter for names..">
<table id="dataTable">
    <thead>
        <tr>
            <th onclick="sortTable(0)">Column 1</th>
            <th onclick="sortTable(1)">Column 2</th>
            <th onclick="sortTable(2)">Column 3</th>
        </tr>
    </thead>
    <tbody>
        <!-- Rows will be added dynamically by Flask -->
    </tbody>
</table>

</body>
</html>
>>>>>>> 60b12678e798cbd9408d706b34af578692b5542c
