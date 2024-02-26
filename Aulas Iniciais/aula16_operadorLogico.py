# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0, 0.0, '', False
# Também existe o tipo None que é
# usado para representar um não valor

# Operador E
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
# print(True and False and True)
# print(True and 0 and True)

# Operador OR

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
# print(not True)  # False
# print(not False)  # True

print (15 * '-')
# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  M a t h e u s
# -7-6-5-4-3-2-1
nome = 'Matheus'
print(nome[2])
print(nome[-4])
print('theus' in nome)
print('zero' in nome)
print('theus' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')