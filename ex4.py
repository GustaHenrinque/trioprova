#Gustavo, Julia e Rian

def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
f, k = converter_temperatura(temperatura_celsius)
print(f"A temperatura em Fahrenheit é {f:.2f}°F e em Kelvin é {k:.2f}K.")
