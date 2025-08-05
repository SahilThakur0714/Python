# Python weight converter

wieght = float(input("Enter yyour wieght: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    wieght = wieght * 2.205
    unit = "Lbs."
    print(f"Your weight is: {wieght} {unit}")

elif unit == "L":
    wieght = wieght / 2.205
    unit = "Kgs."
    print(f"Your weight is: {wieght} {unit}")

else:
    print(f"{unit} is not valid")