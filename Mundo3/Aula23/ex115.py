# Crie um pequeno sistema modularizado para cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from mod115 import *

arquivo = ''
try:
    arquivo = open('cadastro.txt')
except FileNotFoundError:
    arquivo = open('cadastro.txt', 'x')
finally:
    arquivo.close()

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 3:
        titulo('Saindo do sistema... Até logo!')
        break
    elif resposta == 2:
        cadastro()
    elif resposta == 1:
        mostra()
    else:
        print(f'\033[31mERRO: por favor, digite uma opção válida.\033[m')
