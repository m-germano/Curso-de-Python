temp_fahrenheit=input('Digite a temperatura em Fahrenheit: ')

if temp_fahrenheit.isdigit():
    temp_fahrenheit_float=float(temp_fahrenheit)
    temp_celsius=(temp_fahrenheit_float-32)*(5/9)
    print(f'A temperatura {temp_fahrenheit_float}F em Celsius sera: {temp_celsius:.1f}')
else:
    print('Digite um valor em forma de numero!')