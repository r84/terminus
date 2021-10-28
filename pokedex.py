import requests
import json

def buscarpokemon():
    pokemon = str(input('informe o pokemon: '))                                                                 #input do usuário onde ele irá inserir o pokémon desejado
    request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")                                      # aqui faremos a requisição da api usando o método requests.get() , levando a para a página do pokémon selecionado
    request = request.json()                                                                                    # convertemos a requisição da api para o formato json utilizando a função json()
    imagem = request['sprites']['other']['official-artwork']['front_default']                                   # aqui percorreremos os dicionários da api até chegarmos na url da imagem, percorremos os demais dicionários    
                                                                                                                # para encontrarmos os parâmetros desejados e colocarmos nos prints a seguir
    print ('Nome: ',request['name'])
    print ('Tipo: ',request['types'][0]['type']['name'])
    print ('peso: ',request['weight'],'Kg')
    print('----- MOVESET: -----')
    print('1- ',request['moves'][0]['move']['name'])
    print('2- ',request['moves'][1]['move']['name'])
    print('3- ',request['moves'][2]['move']['name'])
    print('4- ',request['moves'][3]['move']['name'])
    print(f'link de imagem: {imagem}')

if __name__ == '__main___':
    buscarpokemon()


buscarpokemon()