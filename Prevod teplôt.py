Kelvin_to_celsium = True
Celsium_to_kelvin = True
Celsium_to_Fahrenheit = True
Fahrenheit_to_Celsium = True
Kelvin_to_Fahrenheit = True
Fahrenheit_to_Kelvin = True


if Kelvin_to_celsium:
    Kelvin = input("Kelvin: ")
    Celsium = float(Kelvin) - 273.15
    print(f'{Kelvin}K = {Celsium}°C.')

if Celsium_to_kelvin:
    Celsium = input("Celsium: ")
    Kelvin = float(Celsium) + 273.15
    print(f'{Celsium}°C = {Kelvin}K.')

if Celsium_to_Fahrenheit:
    Celsium = input("Celsium: ")
    Fahrenheit = float(Celsium) * 1.8 + 32
    print(f'{Celsium}°C = {Fahrenheit}°F')


if Fahrenheit_to_Celsium:
    Fahrenheit = float(input("Fahrenheit: "))
    Fahrenheit_1 = Fahrenheit - 32
    Celsium = float(Fahrenheit_1 / 1.800)
    print(f'{Fahrenheit}°F = {Celsium:.2f}°C')

if Fahrenheit_to_Kelvin:
    Fahrenheit = float(input("Fahrenheit: "))
    Fahrenheit_2 = Fahrenheit + 459
    Kelvin = float(Fahrenheit_2) * (5 / 9)
    print(f'{Fahrenheit}°F = {Kelvin:.2f}K')

if Kelvin_to_Fahrenheit:
    Kelvin = float(input("Kelvin: "))
    Kelvin_1 = Kelvin * 9/5
    Fahrenheit = float(Kelvin_1) - 459.67
    print(f'{Kelvin:.2f}K = {Fahrenheit}°F ')


