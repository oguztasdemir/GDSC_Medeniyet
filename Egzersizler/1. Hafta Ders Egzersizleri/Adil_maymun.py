#Maymunların adil bir şekilde yiyecek takas etmesini sağlama

kirmizi_maymun = input("Kırmızı maymunun elinde ne var?")
mavi_maymun = input("Mavi maymunun elinde ne var?")

print("Kırmızı maymunun elinde {}, mavi maymunun elinde {} var".format(kirmizi_maymun,mavi_maymun))

adil_maymun = 0

adil_maymun = kirmizi_maymun
kirmizi_maymun = mavi_maymun
mavi_maymun = adil_maymun

print("Adil maymunun sayesinde takas sonrası; kirmizi maymunun elinde {}, mavi maymunun elinde {} var".format(kirmizi_maymun,mavi_maymun))


