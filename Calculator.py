#Addition1
def Add(a,b):
        return a + b

    #Multiplication:
def Sub(a,b):
        return a - b

    #Multiplication:
def Mul(a,b):
        return a * b

     #Division:
def Division(a,b):
        return a / b

Number1 = int(input())
Number2 = int(input())
Calculate = int(input())
 
if Calculate == 1:
    Cal = Add(Number1,Number2)
    print(Cal)

elif Calculate == 2:
      Cal = Sub(Number1,Number2)
      print(Cal)


elif Calculate == 3:
      Cal = Mul(Number1,Number2)
      print(Cal)
    
elif Calculate == 4:
      Cal = Division(Number1,Number2)
      print(Cal)
    
else:
    print("bye")
