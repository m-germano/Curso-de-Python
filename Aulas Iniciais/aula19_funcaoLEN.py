"""
Fatiamento de strings
 012345678
 Matheus Germano
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Matheus Germano'
# print(variavel[4])

# FUNCAO LEN
print(variavel[0])
print(variavel[0:15:1]) # Fatiamento [inicio:final:passos]

# Mesma coisa da funcao acima: Conta de 1 em 1
print(len(variavel))

# Invertendo Strings
print(variavel[::-1])

#Funcao LEN personalizada 
def custom_len(string):
    count=0
    for char in string:
       if char != ' ':
           count += 1
    return count

texto= 'Joao da Silva'

print('Numero de caracteres (incluindo espacos): ', len(texto))
print('Numero de caracteres (excluindo espacos): ', custom_len(texto))