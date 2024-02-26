salario_atual=input('Digite seu salario atual: ')
porcentagem=input('Digite a porcentagem do aumento (apenas o numero. Ex 40% = 40): ')

porcentagem_float=float(porcentagem)
salario_atual_float=float(salario_atual)


porcentagem_aumento=porcentagem_float/100
valor_do_aumento=salario_atual_float*porcentagem_aumento

novo_salario=salario_atual_float+valor_do_aumento

print(f'O novo salario sera: {novo_salario:.2f}')
