PRECO_POR_KM=0.15
ALUGUEL_DIA=60

km_percorridos=input('Digite a quilometragem percorrida: ')
dias_alugados=input('Digite a quantidade de dias alugados: ')

if km_percorridos.isdigit and dias_alugados.isdigit():
    km_percorridos_int=int(km_percorridos)
    dias_alugados_int=int(dias_alugados)

    total_a_pagar=(km_percorridos_int*PRECO_POR_KM)+(dias_alugados_int*ALUGUEL_DIA)
    print(f'O preco total a pagar sera {total_a_pagar:.2f}')

else:
    print('Voce nao digitou os valores corretos em um ou mais inputs')
