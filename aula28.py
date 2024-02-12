""" 
Exercicio
Pedir para o usuário digitar seu nome
Pedir para o usuário digitar sua idade
Se nome e idade forem digitados:  
Exibir :
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exibir "Desculpe, você deixou campos vazios"

"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if nome in ' ':
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço.')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')