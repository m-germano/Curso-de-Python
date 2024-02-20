nome='Matheus Germano'
altura=1.75
peso=90


linha_1='Matheus Germano tem 1.75 de altura'

# Usando F-Strings temos

linha_2= f'{nome} tem {altura:.1f} de altura' #OBS: Note o 'f' antes das aspas simples 

print(linha_1)

print(linha_2) #1.75 foi arredondado para 1.8 visto que na variavel altura foi configurada para .1f
# Logo, sera exibida apenas um casa decimal do numero que foi previamente estabelecido

#Semelhante a usar o %s, %d, etc. dentro de uma sentenca na Linguagem C.
# 