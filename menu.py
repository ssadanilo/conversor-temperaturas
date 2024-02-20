# Importe de funções do outro módulo
from funcoes import(celsius_fahrenheit, fahrenheit_celsius, celsius_kelvi, kelvi_celsius)

# Menu com Loop para escolha de conversão desejada
def menu():
    while True:
        print('#' * 50)
        print('Escolha a Conversão desejada')
        print('[1] - Celsius -> Fahrenheit: ')
        print('[2] - Fahrenheit -> Celsius: ')
        print('[3] - Celsius -> Kelvin: ')
        print('[4] - Kelvin -> Celsius: ')
        print('[5] - Sair')
       
        opcoes = int(input('Digite opção desejada: ')) # Escolha de opção do menu

        match opcoes: # Uso do match case para facilicar o uso das opções
            case 1:
                print('#' * 50)
                print(celsius_fahrenheit())
            case 2:
                print('#' * 50)
                print(fahrenheit_celsius())
            case 3:
                print('#' * 50)
                print(celsius_kelvi())
            case 4:
                print('#' * 50)
                print(kelvi_celsius())
            case 5:
                print('#' * 50)
                print('Fim do programa')
                break
                

if __name__ == '__main__':
    menu()
