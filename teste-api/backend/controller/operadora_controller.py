from flask import jsonify, request
from model.operadora_model import carregar_dados_csv

def buscar_operadora():
    termo_busca = request.args.get('termo', '').lower()
    
    if not termo_busca:  # Caso o termo de busca esteja vazio
        return jsonify({"error": "Termo de busca não fornecido."}), 400
    
    try:
        dados = carregar_dados_csv()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    resultados = []

    for operadora in dados:
        if 'Razao_Social' in operadora and 'CNPJ' in operadora:
            # Comparando as colunas 'Razao_Social' e 'CNPJ' com o termo de busca
            if termo_busca in operadora['Razao_Social'].lower() or termo_busca in operadora['CNPJ'].lower():
                resultados.append(operadora)
    
    return jsonify(resultados)
