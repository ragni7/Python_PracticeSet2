def CeltoFar():
    Cel = float(input("Enter celcius:",))
    fahrenheit = (9/5 * Cel) + 32
    return fahrenheit

def fartocel():
    Fah = float(input("Enter fahrenheit:", ))
    celcius = 5/9(Fah-32)
    return celcius

Convert = int(input("Select 1 if want to calculate Celcius to Fahrenheit and seelct 2 if vice versa:", ))
if Convert == 1:
    x = CeltoFar()
    print(x)

elif Convert == 2:
    y = fartocel()
    print(y)

else:
    print("Invalid")

