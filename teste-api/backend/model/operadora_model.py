import csv

def carregar_dados_csv():
    dados = []
    with open('Relatorio_cadop.csv', mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file, delimiter=';')  # Definindo o delimitador como ponto e vírgula
       
        print("Cabeçalhos encontrados:", csv_reader.fieldnames)
        
        for row in csv_reader:
            dados.append(row)
    return dados
