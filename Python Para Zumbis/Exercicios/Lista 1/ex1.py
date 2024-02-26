num1_str=input('Digite o primeiro numero: ')
num2_str=input('Digite o segundo numero: ')

if num1_str.isdigit() and num2_str.isdigit():
    num1_int=int(num1_str)
    num2_int=int(num2_str)
    soma=num1_int+num2_int
    print(f'A soma do numeros digitados é igual a: {soma}')
else:
    print('Erro! Voce nao digitou um numero em um ou mais inputs.')

    

  
