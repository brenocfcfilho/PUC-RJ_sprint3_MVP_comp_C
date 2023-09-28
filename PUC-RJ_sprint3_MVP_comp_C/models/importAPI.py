import os
import requests
import json

# Definir a URL
url = "https://api.coinbase.com/v2/currencies"

# Ir até o diretório onde importAPI.py está localizado
current_dir = os.path.dirname(os.path.abspath(__file__))

try:
    # Solicitação do método GET para a URL
    response = requests.get(url)

    # Verificar se a solicitação obteve sucesso (status code 200)
    if response.status_code == 200:
        # Analisar a respsota JSOn
        data = response.json()

        # Definir o caminho para o arquivo JSON na pasta "database"
        json_path = os.path.join(current_dir, "..", "database", "currencies.json")

        # Exportar os dados das moedas para um arquivo JSON
        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Dados exportados para o arquivo 'currencies.json' na pasta 'database'.")
    else:
        print(f"Falha ao recuperar dados. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
