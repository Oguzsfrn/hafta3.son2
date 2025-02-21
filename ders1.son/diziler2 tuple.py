meyveler = ("elma", "armut", "karpuz", "kavun", "muz")
meyveler2 = ("çilek", "kiraz", "erik")
print(meyveler)

# Tuple'ı listeye dönüştürüp eleman ekleyin
meyveler2_list = list(meyveler2)
meyveler2_list.append("Kivi")
meyveler2 = tuple(meyveler2_list)

print(meyveler2)
print(type(meyveler))
print(type(meyveler2))
print(meyveler[1]) # tuple'lar index var

calima_gunleri = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar")
