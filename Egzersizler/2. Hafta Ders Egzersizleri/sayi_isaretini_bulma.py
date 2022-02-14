#Negatif - Pozitif bulma

sayı = int(input("Lütfen sayı giriniz: "))

if sayı > 0:
    print("{} sayısı pozitiftir.".format(sayı))
    
elif sayı == 0:
    print("{} sayısı nötrdür".format(sayı))
    
elif sayı < 0:
    print("{} sayısı negatiftir.".format(sayı))