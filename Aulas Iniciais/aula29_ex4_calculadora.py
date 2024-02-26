#CALCULADORA USANDO WHILE

while True:    

    num1=input('Digite o primeiro numero: ')
    num2=input('Digite o segundo numero: ')
    operador=input('Digite o operador (+-/*): ')

    operadores_validos='+-*/'
    numeros_validos=None
    num1_float=0
    num2_float=0

    try:
        
        num1_float=float(num1)
        num2_float=float(num2)
        numeros_validos=True
    except:
          print('error')
          numeros_validos=None
          
    if numeros_validos is None:
           print('Um ou ambos numeros digitados sao invalidos.')
           continue
    
    if operador not in operadores_validos:
           print('Operador Invalido')
           continue
    
    if len(operador)>1:
          print('Digite apenas um operador. ')
          continue
    
    print(f'{num1_float} {operador} {num2_float} = ', end='') 
    if operador == '+':
          print(num1_float+num2_float)
    elif operador == '-':
          print(num1_float-num2_float)  
    elif operador == '*':
          print(num1_float*num2_float)
    elif operador == '/':
          print(num1_float/num2_float)  

    sair=input('Deseja sair? [S]im: ').lower().startswith('s')

    if sair is True:
          break
      

