import os
import requests
from bs4 import BeautifulSoup
import zipfile

pagina = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

#Criando pasta para salvar anexos
pasta_anexos = 'anexos'
if not os.path.exists(pasta_anexos):
    os.makedirs(pasta_anexos)


#localizacao dos anexos
links = dados_pagina.find_all('a', class_='internal-link')

for link in links:
    if 'Anexo I.' in link.text or 'Anexo II.' in link.text:
        if link['href'].endswith('.pdf'):
            url_pdf = link['href']
            
            response = requests.get(url_pdf)
            nome_arquivo = link.text.strip().replace('.', '') + '.pdf'
            caminho_arquivo = os.path.join(pasta_anexos, nome_arquivo)
            
            with open(caminho_arquivo, 'wb') as f:
                f.write(response.content)
            print(f'{nome_arquivo} baixado com sucesso!')


#compactando os anexos
with zipfile.ZipFile('anexos.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(pasta_anexos):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), pasta_anexos))

print("anexos compactado em 'anexos.zip'.")
