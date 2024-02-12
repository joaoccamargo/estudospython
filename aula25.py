""" 
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Jose'
preco = 1000.00
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)