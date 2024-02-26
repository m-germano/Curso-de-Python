"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
def custom_len(string):
    count=0
    for char in string:
       if char != ' ':
           count += 1
    return count







nome=input('Digite seu nome: ')
idade=input('Digite sua idade: ')

if nome and idade:
    print(f'O seu nome é: {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
       print('Seu nome contem espacos')
    else:
       print('Seu nome nao contem espacos')

    print(f'O seu nome tem {nome.count(' ')} espacos')

    print(f'Seu nome tem {custom_len(nome)} letras')
    #Ou usa-se nome2=nome.replace(' ','') e logo apos len(nome2) 

    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')
