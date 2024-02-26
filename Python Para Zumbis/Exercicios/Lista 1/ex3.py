DIAS_SEG=86400
HORAS_SEG=3600
MINUTOS_SEG=60

dias=input('Digite o numero de dias: ')
horas=input('Digite o numero de horas: ')
minutos=input('Digite o numero de minutos: ')
segundos=input('Digite o numero de segundos: ')

if dias.isdigit() and horas.isdigit() and minutos.isdigit() and segundos.isdigit():
    dias_int=int(dias)
    horas_int=int(horas)
    minutos_int=int(minutos)
    segundos_int=int(segundos)

    dias_em_segundos=dias_int*DIAS_SEG
    horas_em_segundos=horas_int*HORAS_SEG
    minutos_em_segundos=minutos_int*MINUTOS_SEG
    total_em_segundos=dias_em_segundos+horas_em_segundos+minutos_em_segundos+segundos_int
    print(f'O total de segundos é igual a: {total_em_segundos}')
else:
    print('Algum dos valores digitados esta invalido.')

    





