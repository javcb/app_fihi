import snowflake.connector

# Get data from power query: 
#    Source = Odbc.DataSource("dsn=sf", [HierarchicalNavigation=true]),
#    FUND_ACCOUNTING_Database = Source{[Name="FUND_ACCOUNTING",Kind="Database"]}[Data],
#    FA_Schema = FUND_ACCOUNTING_Database{[Name="FA",Kind="Schema"]}[Data],
#    BALANCES_Table = FA_Schema{[Name="BALANCES",Kind="Table"]}[Data]
    
# Define your Snowflake connection parameters
conn_params = {
    'user': 'JAVIERBENITEZ',
    'password': 'Aperture1',
    'account': 'fla16248', #from url: https://app.snowflake.com/east-us-2.azure/fla16248/
    'warehouse': 'FUND_XS', #sql query in snowflake: SHOW WAREHOUSES;
    'database': 'FUND_ACCOUNTING',
    'schema': 'FA'
}

# Establish the connection
conn = snowflake.connector.connect(**conn_params)

try:
    # Create a cursor object
    cursor = conn.cursor()

    # Define the query
    query = "SELECT * FROM FUNDS"

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
