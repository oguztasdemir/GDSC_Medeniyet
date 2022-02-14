
adet = int(input("Ortalamasını alacağınız sayı adetini giriniz: "))
toplam = 0

for i in range(adet):
    toplam += int(input("Ortalamasını almak istediğiniz sayılardan 1'ini giriniz:"))
    
ortalama = toplam / adet
print("Girilen sayıların aritmetik ortalaması {}'dir.".format(ortalama))