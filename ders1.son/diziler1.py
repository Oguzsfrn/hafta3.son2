# dizi = array = collection = katar
# list
# tuple	
# dictionary
# set

meyveler = [] # Boş liste
print(meyveler)    


meyveler = ["elma", "armut", "karpuz", "kavun", "muz"]
print(meyveler)    
print(meyveler[1])  
meyveler2 = ["çilek", "kiraz", "erik"]
print(meyveler2)
print(meyveler + meyveler2)
meyveler2 += meyveler
print("birlesirilmış hali:",meyveler2)
meyveler2.append("portakal")
print("b2:",meyveler2)
meyveler2.insert(2, "kivi")
print("B3:",meyveler2)
meyveler2.remove("karpuz")