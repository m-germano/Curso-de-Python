preco_mercadoria=input('Digite o preco da mercadoria: ')
desconto=input('Digite o percentual de desconto: ')


preco_mercadoria_float=float(preco_mercadoria)
desconto_float=float(desconto)

desconto_na_compra=preco_mercadoria_float*(desconto_float/100)

novo_preco_mercadoria=preco_mercadoria_float-desconto_na_compra

print(f"""Com o desconto de {desconto_float}%, foram economizados R${desconto_na_compra:.2f}.
Portanto, o preco a ser pago sera: {novo_preco_mercadoria:.2f}""")