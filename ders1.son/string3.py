abc = "OguZ SaFrAn " # string (metin türü) bir değişken tanımladık
print ("OguZ".capitalize()) # İlk harf büyük
print("OguZ".lower()) # küçük harfe çevir
print("OguZ".upper()) # büyük harfe çevir
print(abc.swapcase()) # Büyük küçük harfleri değiştir.
print(abc.title()) # Kelimelerin ilk harflerini büyüt
print(abc.replace("E","a")) # “E” leri “a” yap
print(abc.upper().replace("E","a")) # Önce büyük harfe çevir, sonra “E” leri “a” yap
print(abc.count("D")) # Metindeki bazı karakteler veya karakter gruplarının sayısı
print(abc.find("Dö")) # “Dö” ifadesi kaçıncı indexte 