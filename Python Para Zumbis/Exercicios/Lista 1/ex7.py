temp_celsius=input('Digite a temperatura em Celsius: ')

if temp_celsius.isdigit():
    temp_celsius_float=float(temp_celsius)
    temp_fahrenheit=(temp_celsius_float*(9/5))+32
    print(f'A temperatura {temp_celsius_float}C em Fahrenheit sera: {temp_fahrenheit:.1f}')
else:
    print('Digite um valor em forma de numero!')
   