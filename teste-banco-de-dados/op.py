import pymysql
import csv

# Configurações do banco de dados
connection = pymysql.connect(
    host='localhost',
    user='root',   
    password='1234',
    database='intuitive_care',  
    charset='utf8mb4'
)

cursor = connection.cursor()

# Caminho do arquivo CSV
csv_file_path = r''


with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    header = next(reader)  # Ignora o cabeçalho

    for row in reader:
        if len(row) != 20:
            print("Linha com número inesperado de colunas:", row)
            continue

        query = """
            INSERT INTO registro_operadoras 
            (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, 
             Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, 
             Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, row)
        except Exception as e:
            print("Erro ao inserir a linha:", row)
            print(e)

# Confirma as inserções
connection.commit()

cursor.close()
connection.close()

print("Dados importados com sucesso!")
