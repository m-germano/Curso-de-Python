"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
# maior = 2 > 1
# maior_ou_igual = 2 >= 2
# menor = 1 < 2
# menor_ou_igual = 2 <= 2
# igual = 'a' == 'a'
# diferente = 'a' != 'b'


num1str = input('Digite o primeiro numero: ')
num2str = input('Digite o segundo numero: ')
2

num1=int(num1str)
num2=int(num2str)

if num1 > num2:
    print ('O primeiro numero digitado eh maior que o segundo')
elif num1 == num2:
    print ('Ambos sao iguais')
else:
    print ('O segundo numero eh maior que o primeiro')


