import pandas as pd
import sqlite3

# URL of the CSV file
csv_file = 'money-makers-bb.csv'

# Reading the CSV file
df = pd.read_csv(csv_file)

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Create a connection to a SQLite database
conn = sqlite3.connect('money_makers.db')

# Create a cursor object
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS money_makers")

# Create table with appropriate schema based on the CSV file
create_table_query = """
CREATE TABLE money_makers (
    Nome TEXT,
    Cargo TEXT,
    Empresa TEXT,
    Ano INTEGER,
    Salario FLOAT
)
"""
cursor.execute(create_table_query)

# Commit the transaction
conn.commit()

# Write the dataframe to the SQL table
df.to_sql('money_makers', conn, if_exists='append', index=False)

# Verify that the data has been inserted correctly
print(pd.read_sql('SELECT * FROM money_makers LIMIT 5', conn))

# Close the connection
conn.close()
