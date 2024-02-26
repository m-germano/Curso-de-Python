def custom_len(string):
    count=0
    for char in string:
       if char != ' ':
           count += 1
    return count



"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num=input('Digite um numero inteiro: ')


# if num.isdigit():
#     num_inteiro=int(num)
#     if num_inteiro%2==0:
#         print('O numero digitado eh par')
#     else:
#         print('O numero digitado eh impar')

# else:
#     print('O numero digitado nao eh inteiro')

num=input('Digite um numero inteiro: ')

try:
    num2 = int(num)
    if num2 % 2 == 0:
        print(f'{num2} é um número par')
    else:
        print(f'{num2} é um número ímpar')
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horas=input('Que horas sao?')
# horas_int=int(horas)

# msg_bomdia=[0,1,2,3,4,5,6,7,8,9,10,11]
# msg_boatarde=[12,13,14,15,16,17]
# msg_boanoite=[18,19,20,21,22,23,24]

# if horas_int in msg_bomdia:
#     print('Bom dia')
# elif horas_int in msg_boatarde:
#     print('Boa tarde')
# else:
#     print('Boa noite')

hora=input('Que horas sao?')



try:
    horas_sem_minutos=int(hora[:2])
    dia= horas_sem_minutos>=0 and horas_sem_minutos <=11
    tarde=horas_sem_minutos>=12 and horas_sem_minutos <=17
    noite= horas_sem_minutos>=18 and horas_sem_minutos <=23

    if dia:
        print('bom dia')
    elif tarde:
        print('boa tarde')
    elif noite:
        print('boa noite')
except:
    print('Voce nao digitou a hora corretamente')
    



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
normal_name=[5,6]

nome=input('Digite seu nome: ')

letras=custom_len(nome)

if letras <= 4:
    print('Seu nome é curto')
elif letras in normal_name:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')