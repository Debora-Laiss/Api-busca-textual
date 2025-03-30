import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


try:
   
    df = pd.read_csv(
        'cadastros_operadoras.csv', 
        on_bad_lines='skip',  
        encoding='utf-8',     
        delimiter=','        
    )
except Exception as e:
    print(f"Error loading CSV: {e}")
    df = pd.DataFrame()  

# Rota de busca textual
@app.route('/buscar', methods=['GET'])
def buscar():
    # Receber o parâmetro de busca
    termo = request.args.get('termo', '', type=str)
    
    if termo == '':
        return jsonify({"erro": "Parâmetro 'termo' é obrigatório"}), 400
    
    if df.empty:
        return jsonify({"erro": "Não foi possível carregar os dados"}), 500
    
    # Realizar a busca (aqui, o filtro vai considerar uma busca simples por palavras-chave nas colunas do CSV)
    resultados = df[df.apply(lambda row: row.astype(str).str.contains(termo, case=False).any(), axis=1)]
    
    if resultados.empty:
        return jsonify({"mensagem": "Nenhum resultado encontrado"}), 404
    
    # Retornar os resultados encontrados
    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)