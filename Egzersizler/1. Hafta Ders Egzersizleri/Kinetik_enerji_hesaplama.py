#kinetik enerji hesaplayan program

m = int(input("Cismin kütlesiniz giriniz: "))
v = int(input("Cismin süratini giriniz: "))

kinetik = (1/2) * m * v**2

print("Sürati {} m/s, kütlesi {} kg olan cismin kinetik enerjisi {} kJ'dür.".format(m,v,kinetik))