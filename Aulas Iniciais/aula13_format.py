a='A'
b='B' 
c=1.1856

string= 'a={} b={} c={:.2f}'
formato=string.format(a, b, c)

print('Por padrao temos: ',formato)

# Usando Indices -> Na situacao abaixo temos
# 'a' como indice 0, 'b' como indice 1 e 'c' como indice 2. Logo:

string2='a={0} a={0} a={0} b={1} c={2:.3f}'
formato2=string2.format(a,b,c)

print('Usando indices podemos repetir elementos. Logo: ', formato2)

#Dessa maneira foi possivel printar o elemento 'a' tres vezes

#NOMEANDO O PARAMETRO
string3='a={parametro1} b={parametro2} c={parametro3:.2f}'
formato3=string3.format(
   
    parametro1=a, parametro2=b, parametro3=c   
    )

print('Apos nomear os parametros, temos: ', formato3)