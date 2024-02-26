#SIMPLIFICANDO O CODIGO 


RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

RANGE_MIN=99
RANGE_MAX=101

velocidade_do_carro=int(input('Digite a velocidade do carro: '))
local_do_carro=int(input('Digite o local do carro (em numero): '))

carro_ultrapassou_vel_max = velocidade_do_carro > RADAR_1
carro_esta_no_range_de_multa = local_do_carro >= RANGE_MIN and local_do_carro <= RANGE_MAX

carro_multado=carro_ultrapassou_vel_max and carro_esta_no_range_de_multa

if carro_ultrapassou_vel_max and carro_esta_no_range_de_multa:
    print('Voce foi multado por excesso de velocidade')

if carro_esta_no_range_de_multa:
    print('Voce passou pela regiao com limite de velocidade')

if carro_multado:
  print('Voce foi multado no radar 1')

