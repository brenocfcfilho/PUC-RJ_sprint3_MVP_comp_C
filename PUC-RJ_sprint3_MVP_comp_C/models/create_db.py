import os
import sqlite3
import json

# Ir até o diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir o caminho para a pasta 'database' relativa ao script atual
database_folder = os.path.join(current_dir,"..", "database")

# Definir o caminho para o arquivo db.sqlite3 na pasta 'database'
db_path = os.path.join(database_folder, "db.sqlite3")

# Criar e conecatar a SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criar a tabela 'coinbase_currencies' se ela não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS coinbase_currencies (
        id TEXT PRIMARY KEY,
        name TEXT,
        min_size REAL
    )
""")

# Definir o caminho para o arquivo JSON dentro da pasta ‘database’
json_path = os.path.join(database_folder, "currencies.json")

# Verificar se o arquivo JSON existe
if os.path.exists(json_path):
    # Carregar dados do arquivo JSON
    with open(json_path, "r") as json_file:
        currencies_data = json.load(json_file)

    # Insirir as moedas na tabela ‘coinbase_currencies’
    for currency in currencies_data['data']:
        id = currency.get("id")
        name = currency.get("name")
        min_size = currency.get("min_size")

        cursor.execute("INSERT INTO coinbase_currencies (id, name, min_size) VALUES (?, ?, ?)",
                       (id, name, min_size))

    # Confirmar alterações
    conn.commit()

# Fechar a conexão com o database
conn.close()

print(f"Banco de dados 'db.sqlite3' criado na pasta '{database_folder}'.")
print("Tabela 'coinbase_currencies' criada.")
print("Dados importados para a tabela ‘coinbase_currencies’.")
