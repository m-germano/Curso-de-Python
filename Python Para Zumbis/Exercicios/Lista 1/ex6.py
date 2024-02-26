distancia_a_percorrer=input("Digite a distancia a ser percorrida (em KM): ")
velocidade_media=input("Digite a velocidade media (em KM/H): ")


if distancia_a_percorrer.isdigit() and velocidade_media.isdigit():
    distancia_a_percorrer_float=float(distancia_a_percorrer)
    velocidade_media_int=int(velocidade_media)

    tempo_da_viagem=distancia_a_percorrer_float/velocidade_media_int

    minutos=tempo_da_viagem%1
    minutos_viagem=minutos*60
    

    print(f'A viagem levara cerca de {tempo_da_viagem:.0f} horas e {minutos_viagem:.0f} minutos ')

else:
    print('Voce nao inseriu corretamente os dados')