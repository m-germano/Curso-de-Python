def custom_len(string):
    count=0
    for char in string:
        if char != ' ':
            count+=1
    return count


nome='Matheus Germano'

numero_de_caracteres=int(len(nome))



# print(custom_len(nome))

count=0
while count < numero_de_caracteres:     
       if count != numero_de_caracteres-1:
            print(f'{nome[count]}*', end='')
            count+=1
       else:
            print(f'{nome[count]}*')
            count+=1
            
            
print('Fim do While')

    