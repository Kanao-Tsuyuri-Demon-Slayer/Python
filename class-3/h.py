massKg=input("What's your weight in Kg? ")
mass=float(massKg)
massLb=2.20462*mass
print(type(massLb))
#print("Your mass in pound is "+ massLb)--will give error
print("Your mass in pound is "+ str(massLb))
