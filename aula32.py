numero_int = int(input('Digite um número inteiro:'))

if numero_int % 2 == 0:
    print('Par')
else:
    print('Impar')



hora_atual = int(input('Digite a hora atual:'))

if hora_atual <= 11:
    print('Bom dia')
elif hora_atual > 12 and hora_atual < 18:
    print('Boa tarde')
else:
    print('Boa noite')

nome_usuario = input('Digite seu nome: ')
tamanho_nome = len(nome_usuario)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome > 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')