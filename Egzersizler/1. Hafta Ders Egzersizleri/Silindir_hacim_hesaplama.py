#silindir hacmi hesaplama

r = int(input("Yarıçapı giriniz: "))
h = int(input("Yüksekliği giriniz: "))
p = 3.14

hacim = p * r ** 2 * h

print("Yarıçapı {} metre, yüksekliği {} metre olan silindirin hacmi {} metreküptür.".format(r,h,hacim))