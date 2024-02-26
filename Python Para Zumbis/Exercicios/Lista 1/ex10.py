DIA_SEGUNDOS=3600
MIN_SEGUNDOS=60


cigarros_fumados=input('Voce fuma quantos cigarros por dia? ')
anos_fumante=input('A quantos anos voce fuma? ')

if cigarros_fumados.isdigit() and anos_fumante.isdigit():
    cigarros_fumados_int=int(cigarros_fumados)
    anos_fumante_int=int(anos_fumante)
    
    minutos_perdidos_por_cigarro=10
    total_cigarros_fumados=cigarros_fumados_int * 365 * anos_fumante_int
    minutos_perdidos=total_cigarros_fumados*minutos_perdidos_por_cigarro
    # (1 dia = 1440 minutos)
    dias_perdidos = minutos_perdidos/1440

    print(f'Voce perdeu {dias_perdidos:.2f} da sua vida.')

else:
    print('Voce nao digitou os valores corretos em um ou mais inputs')



