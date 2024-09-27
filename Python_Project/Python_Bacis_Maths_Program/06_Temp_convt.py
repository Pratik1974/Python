# Temperature Converter in Python

def celsius_to_kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

print("---WELCOME TO TEMPERATURE CONVERTER---")
print("1. Celsius to Kelvin")
print("2. Kelvin to Celsius")

option = int(input("Choose an option: "))

if option == 1:
    temp = float(input("Enter temperature in Celsius: "))
    print(f"The temperature in Kelvin is: {celsius_to_kelvin(temp)} K")
elif option == 2:
    temp = float(input("Enter temperature in Kelvin: "))
    print(f"The temperature in Celsius is: {kelvin_to_celsius(temp)} °C")
else:
    print("ERROR! Please choose a valid option.")
