"""
CONSTANTE = "Variáveis que não vão mudar
muitas  condições no mesmo if (ruim)
 <- Contagem de complexidade (ruim)
"""

velocidade = 50
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and  \
    velocidade > RADAR_1:
    print('Carro multado em radar 1')