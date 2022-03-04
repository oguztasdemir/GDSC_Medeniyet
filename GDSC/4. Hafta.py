# -*- coding: utf-8 -*-
"""OğuzTaşdemir_ödev4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HpSsBrsZuuPsI1HijtZAN7cIM3JRej8j

1.Soru :

  a) Argümanları "number" ve "len" olan "create_list" isimli fonksiyon işlevi şu şekildedir.
  Bu fonksiyon aldığı "number"ın 0'dan len'e kadar olan kuvvetleriyle (kuvvetler float değil, int olmalı) bir liste oluşturur ve bu listeyi döndürür.

  Örnek çıktı:

      print(create_list(number=2,len=10))
        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

  b) Fonksiyonu çağırdığınızda size bir liste döndürmüş olacak. Bu listeyi parametre olarak alan "my_print" fonksiyonu ise
  her bir elemanı indexler belirterek "yan yana" ekrana basar.

  Aşağıdaki liste için örnek çıktı şu şekildedir.

        [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        0: 1  1: 2  2: 4  3: 8  4: 16  5: 32  6: 64  7: 128  8: 256  9: 512  

  NOT: Bu ödevde math modülünü kullanmanız beklenmekte. Modülde herhangi bir sayının kuvvetini bulabileceğiniz "pow" fonksiyonunu
  kullanabilirsiniz.
"""

import math

def my_print(my_list):
  dictionary = []
  sayac = 0
  print(kare)
  
  for i in kare:
    deger = {sayac : i}
    dictionary.append(deger)
    sayac += 1
  print(dictionary)



def create_list(number,len):
  global kare
  kare = []
  for i in range(0,len):
    sayi = int(math.pow(number,i))
    kare.append(sayi)
  print(kare)


my_list = create_list(number=2,len=10)
my_print(my_list)

"""my_tuple = (23,45,"python",(3,4,5),[111,434,333],45,32,76,98,36,23,868,68,43,23,14)


2.Soru :
  
"my_tuple" isimli tuple'da,

*   a) 45'i
*   b) 23 sayısının kaç tane olduğunu,
*   c) (3,4,5) tuple'ındaki 4'ü,
*   d) "python" string'indeki "o"yu ekrana bastırın.
*   e) [111,434,333] içindeki 434 sayısını 222 ile değiştirin ve tüm tuple'ı indexler belirterek (sadece my_tuple indexleri, içerideki liste veya tuple'ların değil)

ekrana bastırın.

"""

my_tuple = (23,45,"python",(3,4,5),[111,434,333],45,32,76,98,36,23,868,68,43,23,14)

#a
if 45 in my_tuple:
  print(45)

#b
print(my_tuple.count(23))

#c
if 4 in my_tuple[3]:
  print(4)

#d
print(my_tuple[2][-2]) # -2 yerine 4 olabilir

#e
my_tuple[4][1] = 222
print(my_tuple)

"""3.Soru :

  a) Sevdiğiniz şarkılar ve bu şarkıların ait olduğu kişilerle bir dictionary oluşturun. [sanatçı:şarkı] şeklinde olsun.
  Bunu yaparken kendiniz şarkılar ve sanatçılar için tuple oluşturun ve bu tuple'ları kullanarak bir dictionary oluşturun.

  Örnek olarak benim sanatçılar ve şarkılar tuple'ım şu şekilde. İsterseniz bunları kullanabilirsiniz.
  (Not: Bence sevdiğiniz şarkılarla yapmak daha eğlenceli olacak.)

            singer = ("Imagine Dragons","Bruno Mars","Sia")
            songs = ("Believer","Treasure","Titanium") listeleri için,


            {'Imagine Dragons': 'Believer', 'Bruno Mars': 'Treasure', 'Sia': 'Titanium'}

            şeklinde bir dictionary oluşturmalısınız.

  b) Oluşturduğunuz dictionary'nin sadece "value" değerlerini ve sadece "key" değerlerini ekrana bastırın. Bunlar için örnek soru çözümlerindeki metotları da kullanabilirsiniz.
  
"""

singer = ("Model", "Sia", "AC/DC", "Alec Benjamin")
song = ("Pembe Mezarlık", "Cheap Thrillers", "Highway to Hell", "Let Me Down Slowly")

music_dictionary = {singer : song}

print(music_dictionary.keys())
print(music_dictionary.values())