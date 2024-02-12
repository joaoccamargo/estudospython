""" 
Repetições
while
executa uma ação quando for verdadeira
"""
condicao = True

while condicao:
    nome = input('Qual seu nome?')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        condicao = False