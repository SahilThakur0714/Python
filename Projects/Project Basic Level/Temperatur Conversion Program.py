unit = input("is this temperature in Celcius or Fahrenheit (C/F): ").upper()
temp = float(input("ENter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "F":
    temp = round((32 * temp) / 5 + 9, 1)
    print(f"The temperature in Celcius is: {temp}°F")

else:
    print(f"{unit} is an invalid unit of measurement")