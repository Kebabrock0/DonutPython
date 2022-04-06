import random

tahminiSayi = random.randint(0,1000)

tahminHakki = 7


while(tahminHakki>0):
    tahmin = int(input("Sayıyı tahmin ediniz:"))

    if(tahmin < tahminiSayi):
        print("Yukarı")
    elif(tahmin > tahminiSayi):
        print("Aşağı")
    else:
        print("Doğru sayı")
        break

    tahminHakki -= 1

    if(tahminHakki == 0):
        print("Tahmin hakkınız bitmiştir")
