# -*- coding: utf-8 -*-
"""Oguztasdemir_odev2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p1b_dfm50NhBDfRHTdQZzsEUG6L73gqy

1. soru: Kullanıcının girdiği özellikleri dikkate alarak kullanıcıya en uygun eşi bulan izdivaç programı yapınız.
"""

print("Python ile evlen benimle programına hoşgeldiniz!!!!")
print("Lütfen küçük harfler ve Türkçe karakterler kullanın.")
cinsiyet = input("Evlenmek istediğiniz çıtırın cinsiyetini giriniz: ")
sac = input("Beğendiğiniz saç rengini söyleyiniz: ")
goz = input("Göz rengini de söylerseniz tadından yenmez: ")

if cinsiyet == "kadın" and sac == "sarı" and goz == "yeşil":
  print("Senin için en uygun çıtırımız Black Widow lakaplı Scarlett Johansson")

elif cinsiyet == "erkek" and sac == "kahverengi" and goz == "mavi":
  print("Aman tanrımmm sana Kaptanı bulduk Chrisss Evanssss")

elif cinsiyet == "kadın" and sac == "kahverengi" and goz == "yeşil":
  print("Mükemmel, sana Irina Shayk isimli top modelimizi ayarladık")

elif cinsiyet == "erkek" and sac== "siyah" and goz == "ela":
  print("Senin için gelen kişiii CRİSTİANO RONALDOOOOOOO SIUUUUUU")

elif cinsiyet == "kadın" and sac== "kahverengi" and goz == "kahverengi":
  print("Veee Anne Hathawayyy")

elif cinsiyet == "erkek" and sac== "kahverengi" and goz == "mavi":
  print("Supermann ve Witcher senin için buradaa seç beğen al Henryy Cavilll")

elif cinsiyet == "kadın" and sac == "sarı" and goz== "mavi":
  print("Ah sana güzeller güzeli bir kadın bulduk Margot Robbiee")

elif cinsiyet == "erkek" and sac == "siyah" and goz == "kahverengi":
  print("MAMBAAAA seni bekliyor fakat ne yazıkki bu dünyada değil. KOBE BRYANTTT")


else:
  print("Aman tanrım çok arayıcısın aradığın kriterlerde birini bulamadık")

"""Soru 2: Kafede çalışacak bir robot programlayınız. Tematik kafe olursa çok hoş olur (örn: Star Wars kafede R2-D2 çalışsın menüde droidler için motor yağı olsun)."""

print("Witcher Cafeye hoşgeldiniz ben WhiteWolf")

robot = input("Cafemizde oturmak ister misiniz sizin için cadı getirebilirim (y-n)")

if robot == "y" or robot == "Y":
  kisi = int(input("Harikaaaa senin için çok güzel iksirlerim var kaç kişisiniz acaba? "))
  print("Pekala {} kişilik yer hemmmenn hazırlanıyor".format(kisi))
  print("Pekala neler zıkkımlanmak istersiniz bakalım menümüzde çok güzel iksirler ve elf kulakları mevcut, bunları beğenmezseniz de Witcherlarım sizin için hemen gidip canavar veya bazı hayvanları doğrayabilir. Bunları beğenmediyseniz en son sizi kesip yedireceğim karar verin lütfen: ")
  yemek = int(input("Evet bakalımm ne yicekmişsiniz, iksir için (1), elf kulakları için (2), spesyal Witcher avları için (3), kendinizi yedirmek istiyorsanız (4)."))
  if yemek == 1:
    adet = int(input("Çok sıkıcısın cidden sadece en ucuz şeyi mi söylüyorsun??? Neyse kaç adet istiyorsunuz?"))
    fiyat = 20
    print("...A FEW MOMENTS LATER...")
    print("Hop hop hop işte faturanız...{} akçe".format(fiyat*adet))
    para = int(input("Ne kadar akçe yüklemek istiyorsunuz: "))
    if para < (20*adet):
      print("Gerçekten inanılmazsın. O kadar ucuz şey almana rağmen hala eksik para ödüyorsun. Hadi pamuk eller cebe daha {} akçe daha ödemen lazım.".format((20*adet)-para))
    elif para == (20*adet):
      print("Yine beklerizzzz")
    elif para > (20*adet):
      print("Vay canına, yanında o kadar para varken bu kadar ucuz şey alıyorsunuz. Her neyse buyrun para üstünüz tam tamına {} akçe. Yine bekleriz. ".format(para-(20*adet)))



  elif yemek == 2:
    adet = int(input("Ağzının tadını biliyorsunnnnn aferin evet bakalım kaç adet istiyorsunuz"))
    fiyat = 50
    print("...A FEW MOMENTS LATER...")
    print("Seni gidi zevk sahibi gidi {} akçe versen yeterli".format(fiyat*adet))
    para = int(input("Ne kadar akçe yüklemek istiyorsunuz: "))
    if para < (20*adet):
      print("Keşke bonkörlüğün de zevklerin kadar bol olsa, yetersiz para yükledin. {} akçe daha ödemen gerekiyor".format((50*adet)-para))
    elif para == (20*adet):
      print("Yine beklerizzzz")
    elif para > (20*adet):
      print("Vay canına gerçekten çok zengin olmalısın. Buyur işte para üstün {} akçe. Yine bekleriz".format(para-(50*adet)))


  elif yemek == 3:
    av = str(input("Öffff çok uğraştırıcısın her neyse ne avlamamızı istiyorsun?"))
    print("Heh bak şimdi gözüme girdin. Witcherlarım gidin ve {} avlayın. İleriiii".format(av))
    adet = int(input("Kaç adet istiyorsunuz?"))
    fiyat = 250
    print("...A FEW MOMENTS LATER...")
    print("Seni gidi zevk sahibi gidi {} akçe versen yeterli".format(fiyat*adet))
    para = int(input("Ne kadar akçe yüklemek istiyorsunuz: "))
    if para < (250*adet):
      print("Hem uğraştırıcısın hem de para vermiyorsun şaka gibisin. {} akçe daha ödemen gerekiyor".format((50*adet)-para))
    elif para == (250*adet):
      print("Yine beklerizzzz")
    elif para > (250*adet):
      print("Vay canına uğraştıcılığın kadar zenginsin. Al bakalım para üstün. Sadaka kutumuza akçe atmayı unutma Witchlerımız kılıçlarını beleşe bileylemiyor. Ödemezseniz de para üstünüz {} akçedir. Yine bekleriz".format(para-(250*adet)))




  elif yemek == 4:
    print("Seni gidi şakacı seni hadi düzgün bir şey seç ya da kalk masamızdan")


else:
  print("Lanet olası madem oturmayacaksınız beni ne diye uğraştırıyorsunuz umarım canavarlara yem olursunuz!!!!!")