contador=0

while contador <= 10:
     print(contador)   
     contador += 1
     #  contador = contador +1

    
    

# print('acabou')

"""
Operadores de atribuição
= Simbolo de atribuicao de valor
+=  contador=contador+1
-=  contador=contador-1
*=  contador=contador*1
/= Divisao normal- Retorna resultado com ponto flutuante
//= Retorna resultado inteiro
**= contador=contador**1
%=  contador=contador%1

"""
num=10

num //=5
# num =num/5 

print(num) #Output = 2

#IMPRIMINDO MEU NOME AO CONTRARIO
string='Matheus Germano'

i=0

while i<len(string):
    i+=1
    print(string[-i],end="")