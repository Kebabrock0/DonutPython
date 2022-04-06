def notHesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ortalama = not1 * 0.3 + not2 * 0.3 + not3 * 0.4

    if ortalama > 90:
        harfNotu = "AA"
    elif ortalama > 80:
        harfNotu = "BA"
    elif ortalama > 70:
        harfNotu = "BB"
    elif ortalama > 60:
        harfNotu = "CB"
    elif ortalama > 50:
        harfNotu = "CC"
    elif ortalama > 40:
        harfNotu = "DC"
    elif ortalama > 35:
        harfNotu = "DD"
    else:
        harfNotu = "FF"

    return "{},{}".format(isim, harfNotu)


def kalanOgrenciler(x):
    x = x[:-1]
    harfler = x.split(",")

    isim = harfler[0]
    harf = harfler[1]

    if harf == "FF":
        return "{} kaldı".format(isim)
    else:
        return ""


with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler = []
    for i in file:
        eklenecekler.append(notHesapla(i))


with open("ders_notları.txt", "w", encoding="utf-8") as file2:
    for i in eklenecekler:
        file2.write(i + "\n")

with open("ders_notları.txt", "r", encoding="utf-8") as file3:
    kalanlar = []
    for i in file3:
        kalanlar.append(kalanOgrenciler(i))

with open("kalanlar.txt", "w", encoding="utf-8") as file4:
    for k in kalanlar:
        if k == "":
            continue
        else:file4.write(k + "\n")
