import requests
import json

def TesteApi():

    InputUsuario = input('insira aqui o cep:')

    if len(InputUsuario) != 8:
        print('CEP INVÁLIDO!')
        exit()

    Requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(InputUsuario))

    DadosRequisicao = Requisicao.json()

    
    if 'erro' not in DadosRequisicao:
        print('Cep:{}'.format(DadosRequisicao['cep']))
        print('Endereço:{}'.format(DadosRequisicao['logradouro']))
        print('Cidade:{}'.format(DadosRequisicao['localidade']))
        print('Estado:{}'.format(DadosRequisicao['uf']))
    else:
        print('CEP INVÁLIDO')

TesteApi()