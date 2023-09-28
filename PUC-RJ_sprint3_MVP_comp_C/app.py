from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, redirect, request
import subprocess

from flask_cors import CORS

info = Info(title="Componente C: API para interação com API externa", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
database_tag = Tag(name="Lista de todas as moedas", description="importar API externa pública e criar a base de dados")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/run_db', methods=['POST'], tags=[database_tag])
def run_db():
    """Executa o arquivo run_db através do comando 'python run_db.py'.
    """

    if request.method == 'POST':
        try:
            subprocess.run(["python", "models/importAPI.py"])
            subprocess.run(["python", "models/create_db.py"])
            return "Banco de dados geradocom sucesso.", 200
        except Exception as e:
            return f"Erro ao gerar o banco de dados (run_db.py): {str(e)}", 500
    else:
        return "Solicitação do método POST necessária.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
