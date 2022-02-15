#dakikayı saate çeviren program

dakika = int(input("Dakika giriniz: "))
saat = dakika // 60
dakika %= 60

print("{} saat {} dakika".format(saat,dakika))
