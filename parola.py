
import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parolanızın uzunluğunu giriniz: "))
randomparola = ""
for i in range(uzunluk):
    randomparola += random.choice(karakter)
print(randomparola)
