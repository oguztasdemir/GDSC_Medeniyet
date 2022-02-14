#Sinema bilet gişesi

bot = input("Merhaba ben Ticketnator, benden bilet almak ister misin?")

bilet_fiyatı = 18.90
bilet_fiyatı_öğrenci = 11.90

if bot == "evet" or bot == "Evet" or bot == "EVET":
    print("Pekala!\n Tam bilet{} TL, öğrenci bileti {} TL'dir.".format(bilet_fiyatı,bilet_fiyatı_öğrenci))
    öğrenci = input("Kaç öğrenci bulunmaktadır?")
    tam = input("Peki tam bilet kaç kişi istemektedir?")
    
    tutar = (öğrenci*bilet_fiyatı_öğrenci) + (tam*bilet_fiyatı)
    print("{} adet tam bilet, {} adet öğrenci bileti istemişsiniz, toplam tutarınız {} TL'dir.".format(tam,öğrenci,tutar))
    
    ödeme = int(input("Lütfen para giriniz: "))
    
    if ödeme < tutar:
        print("Girdiğiniz tutar yetersiz. Lütfen {} TL daha giriniz aksi takdirde biletinizi veremem.".format(tutar-ödeme))
        
    elif ödeme == tutar:
        print("Verdiğiniz para tam, buyrun biletiniz. İyi seyirler dilerim.")
        
    elif ödeme > tutar:
        print("Girdiğiniz para fazla. Para üstünüz veriliyor.")
        print("Verilen para üstü {} TL'dir. İyi seyirler dilerim.".format(ödeme-tutar))
        
else:
    print("Bir dahaki sefere görüşürüz o zaman!!!")
    
