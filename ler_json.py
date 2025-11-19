#!/usr/bin/python3

# para ler um json em forma de string dentro do mesmo script:
import json
texto = '{"nome": "Ana", "idade": 27}'
dados1 = json.loads(texto)	# aqui é loads (s) 
print(f'Lendo JSON de variável:\n{dados1}\n')


# para ler um json que esteja em arquivo na mesma máquina:
import json
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados2 = json.load(arquivo)	# aqui é load (sem 's')
print(f'Lendo JSON de arquivo local:\n{dados2}\n')


# para ler um json em um URL:
import requests
import json
url = "https://raw.githubusercontent.com/HelioGiroto/lendo_json/refs/heads/main/dados.json"
resposta = requests.get(url)
dados3 = resposta.json()  
print(f'Lendo JSON de URL:\n{dados3}')


