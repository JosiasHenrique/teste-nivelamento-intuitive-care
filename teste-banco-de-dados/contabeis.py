import pymysql
import csv
from datetime import datetime

# Configurações do banco de dados
connection = pymysql.connect(
    host='',          
    user='',       
    password='',      
    database='',  
    charset='utf8mb4'          
)

cursor = connection.cursor()

# Caminho do arquivo CSV
csv_file_path = r''


with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    header = next(reader)  # Ignora o cabeçalho

    for row in reader:
        # Converte a data de dd/mm/yyyy para yyyy-mm-dd
        try:
            row[0] = datetime.strptime(row[0], "%d/%m/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            print("Erro na conversão de data na linha:", row)
            print(e)
            continue

        # Converte as vírgulas para pontos nos valores decimais
        row[4] = row[4].replace(',', '.')
        row[5] = row[5].replace(',', '.')

        query = """
            INSERT INTO demonstracoes_contabeis 
            (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, row)
        except Exception as e:
            print("Erro ao inserir a linha:", row)
            print(e)

connection.commit()
cursor.close()
connection.close()

print("Registros contábeis importados com sucesso!")
