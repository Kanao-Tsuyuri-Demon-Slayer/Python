weight= input("Please enter your weight:\n")
unit = input("(L)bs or (K)g:\n")
kilo=int(weight) / 2.20462
pound=int(weight) * 2.20462
if(unit=="L"or unit=="l"):
    print(f"You are %d kilos"%kilo)
elif(unit=="KG"or unit=="kg" or unit=="Kg"):
    print("You are %d pounds"%pound)