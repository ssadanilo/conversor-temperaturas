# Funções para converter temperatuas de sistemas de medição diferentes
def celsius_fahrenheit():
    celsius = float(input('Digite a temperatura em grau celsius: ')) # Float para temperaturas com decimais
    fahrenheit = round(celsius * 1.8 + 32) # Função round para arredondar números com decimais
    return f'A temperatura em Fahrenheit é {fahrenheit}°F' 

def fahrenheit_celsius():
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
    celsius = round((fahrenheit - 32) / 1.8)
    return f'A temperatura em Celsius é {celsius}°C'

def celsius_kelvi():
    celsius = float(input('Digite a temperatura em grau celsius: '))
    kelvin = round(celsius + 273,15)
    return f'A temperatura em Kelvin é {kelvin}°K'

def kelvi_celsius():
    kelvin = float(input('Digite a temperatura em grau Kelvin: ')) 
    celsius = round(kelvin - 273,15)
    return f'A temperatura em Celsius é {celsius}°C'


