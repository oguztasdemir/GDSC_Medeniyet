#roller coaster botu

bot = input("Merhaba ben co-astreoid, maceraya katılmak istiyor musun? (y-n): ")

if bot == "y" or bot == "Y":
    print("Whoaaa yavaş ol öncelikle koşulları sağlaman lazım!!!")
    
    boy = int(input("Boy: "))    
    kilo = int(input("Kilo: "))
    yas = int(input("Yas: "))
    
    
    if  (110 < boy < 200) and (30 < kilo < 140) and (10 < yas < 65):
        print("Vay canına, bütün koşulları sağlıyorsun. Adeta Roller Coaster için yaratılmışsın. Binmeden önce duvarda yazılı olan şeyleri okuduğunuzdan emin olun, başınıza gelebilecek herhangi bir durumdan şirketimiz sorumlu değildir. İyi eğlenceler.")
        
    elif  (110 > boy or boy > 100) and (30 < kilo < 140) and (10 < yas < 65):
        print("Boy şartını sağlayamıyorsunuz, hız trenine binemezsiniz üzgünüm. SIRADAKİİİİ!")
        
    elif  (110 < boy < 200) and (30 > kilo or kilo > 140) and (10 < yas < 65):
        print("Kilo şartını sağlayamıyorsunuz, hız trenine binemezsiniz üzgünüm. SIRADAKİİİİ!")
        
    elif  (110 < boy < 200) and (30 < kilo < 140) and (10 > yas or yas > 65):
        print("Yaş şartını sağlayamıyorsunuz, hız trenine binemezsiniz üzgünüm. SIRADAKİİİİ!")

    else:
        print("İanılmaz. Koşullardan en az 2'sini karşılamayan birisin, Roller Coaster senlik değil dostum üzgünüm. SIRADAKİİİİ!")
        
else:
    print("KORKAKKK! SIRADAKİİİ!")