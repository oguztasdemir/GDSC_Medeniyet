#üçgenin alanını hesaplama

taban = int(input("Taban: "))
yukseklik = int(input("Yükseklik: "))

alan = (taban*yukseklik) / 2
print("Üçgenin tabanı {1}, yüksekliği {2} olan üçgenin alanı {0}'dir.".format(alan,taban,yukseklik))