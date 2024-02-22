"""
Pergunte a velocidade de um carro supondo um valor inteiro. Caso ultrapasse 110 km/h exiba uma mensagem
dizendo que o usuario foi multado. Neste caso, exiba o valor da multa cobrando R$5,00 por km acima de 110

"""

velocidade_do_carro=int(input('Qual a velocidade do carro? '))

velocidade_maxima=110

if velocidade_do_carro<=velocidade_maxima:
    print("Tudo OK")
else:
    multa=(velocidade_do_carro-velocidade_maxima)*5
    print(f"O valor da multa eh R$ {multa}")
    
