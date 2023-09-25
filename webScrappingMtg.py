# 1.0 Fazendo os imports das bibliotecas Beautiful Soup e requests
import requests
from bs4 import BeautifulSoup

# 2.0 URL da página que queremos acessar
url = 'https://www.mtggoldfish.com/metagame/standard/full#paper'

# 3.0 Fazendo a requisição para a página
requisicao = requests.get(url)

# 4.0 Verificando se a requisição foi bem-sucedida
if requisicao.status_code == 200:
    # 4.1 Se bem sucedida a requisição,dentro do if iremos criar um objeto BeautifulSoup
    # para analisar o HTML da página
    soup = BeautifulSoup(requisicao.content, 'html.parser')

    # 4.2Encontrando todas as divs com a classe que queremos acessar
    divs = soup.find_all('div', class_='archetype-tile-title')

    # 4.3 Iterando sobre as divs encontradas, buscando seu conteúdo e
    # limitando a busca aos 20 primeiros decks da página
    for indice, div in enumerate(divs, start=1):
        limite_de_decks = 20
        if(indice > limite_de_decks):
          break

        # 4.4 Aqui iremos imprimir o nome dos 20 primeiros decks da página
        titulo_deck = div.text.strip().split('\n')[0]
        print(f"Deck {indice}")
        print(f"Nome: {titulo_deck}")

        # 4.5 Aqui iremos imprimir o link dos decks, que irá para a página do mesmo
        # no próprio mtg goldfish
        link = div.a['href']
        print(f"Link: https://www.mtggoldfish.com{link}")
        print("Formato: Standard \n")

# 5.0 Mensagem de erro caso haja falha na requisição
else:
    print('Não foi possível acessar a página, status:', requisicao.status_code)
