import pdfplumber
import pandas as pd
import zipfile
import os

pdf_path = 'Anexo I.pdf'
csv_path = 'rol.csv'
zip_path = f'Teste_Josias_Henrique.zip'

def extrair_tabelas_para_csv(pdf_path, csv_path):
    with pdfplumber.open(pdf_path) as pdf:

        todas_tabelas = []

        for pagina in pdf.pages:
            tabela = pagina.extract_table()

            if tabela:
                cabecalho = tabela[0]
                # Substituir "OD" por "Seg. Odontológica" e "AMB" por "Seg. Ambulatorial"
                cabecalho_ajustado = [
                    'Seg. Odontológica' if col == 'OD' else
                    'Seg. Ambulatorial' if col == 'AMB' else col
                    for col in cabecalho
                ]
                
                # Adicionar os dados da tabela à lista (ignorando o cabeçalho original)
                for linha in tabela[1:]:
                    todas_tabelas.append(linha)

        # Criar um DataFrame do Pandas com o cabeçalho ajustado
        df = pd.DataFrame(todas_tabelas, columns=cabecalho_ajustado)

        # Salvar o DataFrame como arquivo CSV
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f'Tabela salva em {csv_path}')

def compactar_csv_em_zip(csv_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o arquivo CSV no ZIP
        zipf.write(csv_path, os.path.basename(csv_path))
        print(f'Arquivo compactado como {zip_path}')

extrair_tabelas_para_csv(pdf_path, csv_path)

compactar_csv_em_zip(csv_path, zip_path)
