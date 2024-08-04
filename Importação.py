import pandas as pd
import sqlite3

# Nome do arquivo CSV local
csv_file = 'money-makers-bb.csv'

# Lendo o arquivo CSV
df = pd.read_csv(csv_file)

# Exibir as primeiras linhas do dataframe para entender a estrutura
print("Primeiras linhas do dataframe:")
print(df.head())

# Criar uma conexão com um banco de dados SQLite
conn = sqlite3.connect('money_makers.db')

# Criar um objeto cursor
cursor = conn.cursor()

# Remover a tabela se ela já existir
cursor.execute("DROP TABLE IF EXISTS money_makers")

# Criar a tabela com a estrutura apropriada com base no arquivo CSV
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

# Confirmar a transação
conn.commit()

# Escrever o dataframe na tabela SQL
df.to_sql('money_makers', conn, if_exists='append', index=False)

# Verificar se os dados foram inseridos corretamente
print("Dados inseridos no banco de dados:")
print(pd.read_sql('SELECT * FROM money_makers LIMIT 5', conn))

# Fechar a conexão
conn.close()
