# -*- coding: utf-8 -*-
"""bil101_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17y-tUebu7a9JcY_E-t-lZfOqcaQjreQZ

1. soru: Kullanıcıdan input alarak interaktif bir hikaye yazınız.
"""

print("... adında bir basketbolcu varmış. Bu basketbolcu ... karşı oynadığı maçta yedek başlamış. Maçta sadece ... dakika oynamasına rağmen ... sayı ve ... asist yaparak maçın yıldızı seçilmiş.")

a = input("Lütfen 1. boşluğu doldurun.")
b = input("Lütfen 2. boşluğu doldurun.")
c = input("Lütfen 3. boşluğu doldurun.")
d = input("Lütfen 4. boşluğu doldurun.")
e = input("Lütfen 5. boşluğu doldurun.")

print("{} adında bir basketbolcu varmış. Bu basketbolcu {} karşı oynadığı maçta yedek başlamış. Maçta sadece {} dakika oynamasına rağmen {} sayı ve {} asist yaparak maçın yıldızı seçilmiş.".format(a,b,c,d,e))

"""2. Soru: Kullanıcıdan kütle, sürat, yükseklik inputları alan ve bu cismin mekanik enerjisini hesaplayan bir algoritma yazın."""

print("Mekanik enerji hesaplama algoritması")
m = int(input("Lütfen cismin kütlesini giriniz: "))   #Kütle
v = int(input("Lütfen cismin süratini giriniz: "))    #Sürat
h = int(input("Lütfen cismin yüksekliğini giriniz: "))#Yükseklik
g = int(9.8) #Yer çekim ivmesi

mekanik = (m*g*h) + (1/2*m*v**2)

print("Cismin mekanik enerjisi: ", mekanik)

"""3. Soru: Kullanıcıdan alınan Celcius birimindeki sıcaklık değerini Fahrenheit birimine dönüştüren program yazınız."""

print("Celcius --> Fahrenheit dönüştürme algoritması")
c = int(input("Dönüştürmek istediğiniz Celcius derecesini girin: "))
f = (9*c/5) + 32 
print("{} Celcius, {} Fahrenheit'e eşittir.".format(c,f))

"""4. Soru: Kullanıcıdan input alarak dikdörtgen prizma, küre, koni cisimlerinin hacimlerini hesaplayan program yazın."""

print("Hacim hesaplama algoritması")
sec = int(input("Dikdörtgen prizması için (1), Küre için (2), koni için (3)"))

if sec == 1:
  y = int(input("Dikdörtgen prizmanın yüksekliğini giriniz (Cm cinsinden):"))   #Yükseklik
  kt = int(input("Dikdörtgen prizmanın kısa tabanını giriniz (Cm cinsinden):")) #Kısa Taban
  ut = int(input("Dikdörtgen prizmanın uzun tabanını giriniz (Cm cinsinden):")) #Uzun Taban
  hacim = y*kt*ut
  print("Dikdörtgen prizmanın alanı: ", hacim) 

elif sec == 2:
  r = int(input("Kürenin yarıçapını giriniz (cm cinsinden): "))   #Yarıçap
  hacim = (4/3)*3.14*r**2
  print("Kürenin hacmi: ", hacim)

elif sec == 3:
  r = int(input("Koninin yarıçapını giriniz (cm cinsinden): "))   #Yarıçap
  hacim = (1/3)*3.14*r**2
  print("Koninin hacmi: ", hacim)

"""Özel Soru: Kullanıcıdan kütle ve sürat inputları alarak bu cismin kinetik enerjisini hesaplayan, bu enerjiyi enerji korunumundan potansiyel enerjiye çevirerek cismin çıkabileceği maksimum yüksekliği bulan program yazınız."""

print("Kinetik enerji --> Potansiyel Enerji")
m = int(input("Lütfen cismin kütlesini giriniz: "))   #Kütle
v = int(input("Lütfen cismin süratini giriniz: "))    #Sürat
g = int(9.8) #Yer çekim ivmesi

kinetik = (1/2*m*v**2)
h = kinetik / (m*g)

print("Cismin çıkabileceği maksimum yükseklik: ", h)