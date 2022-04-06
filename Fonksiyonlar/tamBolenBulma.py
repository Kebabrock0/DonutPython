def tamBolenler(sayi):
    tamBolenlerList = []
    for i in range(1,sayi):
        if(sayi % i == 0):
            tamBolenlerList.append(i)
    return tamBolenlerList

while True:
    sayi = input("Lütfen bir sayı giriniz: ")


    if(sayi == "q"):
        print("Kullandığınız için teşekkürler..")
        break
    else:
        sayi = int(sayi)

        print("Girdiğiniz sayının tam bölenleri: ")
        print(tamBolenler(sayi))
