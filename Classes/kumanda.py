import random
import time


class Kumanda():


    def __init__(self,tv_durum = "Kapalı", ses = 0, kanal_listesi = ["TRT"], kanal = "TRT"):
        self.tvDurum = tv_durum
        self.ses = ses
        self.kanalListesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if(self.tvDurum == "Açık"):
            print("TV zaten açık")
        else:
            print("TV açılıyor")
            self.tvDurum = "Açık"

    def tv_kapat(self):

        if(self.tvDurum == "Kapalı"):
            print("TV zaten kapalı")
        else:
            print("TV kapatılıyor")
            self.tvDurum = "Kapalı"



    def sesAyarla(self):

        while True:
            cevap = input("Sesi azalt: <\nSesi arttır: >\nÇıkış: çıkış\n")

            if(cevap == ">"):
                if(self.ses > 0):
                    print("Ses 1 arttırılıyor")
                    self.ses += 1

            elif(cevap == "<"):
                if(self.ses > 0):
                    print("Ses azaltılıyor")
                    self.ses -= 1
                else:
                    print("Ses minimum")
            elif(cevap == "çıkış"):
                print("Ses güncellendi")
                break

            else:
                print("Geçersiz operatör")

    def kanalEkleme(self,kanal_ismi):

        print("Kanal ekleniyor....")
        time.sleep(1)
        self.kanalListesi.append(kanal_ismi)

        print("Kanal eklendi")

    def rastgeleKanal(self):

        rastgele  = random.randint(0,len(self.kanalListesi)-1)

        self.kanal = rastgele

        print("Şu anki kanal: {}".format(self.kanal))

    def __len__(self):

        return len(self.kanalListesi)

    def __str__(self):

        return "TV durumu: {}\n Ses seviyesi: {}\n Kanal listesi: {}\n Şu anki kanal: {}".format(self.tvDurum,self.ses,self.kanalListesi,self.kanal)



kumanda1 = Kumanda("Açık", 20, ["FOX","ATV","Halk TV"], "FOX")





print("""

Kumandayı kullanınız

1. TV aç

2. TV kapat

3. Ses ayarları

4. Kanal ekle

5. Kanal sayısını öğrenme

6. Rastgele kanala geçme

7. Televizyon bilgileri




Çıkış için q yazınız
""")



while True:
    x = input("Operatörü giriniz: ")


    if (x == "q"):
        print("Kullandığınız için teşekkürler")

        break

    elif(int(x) == 1):
        kumanda1.tv_ac()
    elif (int(x) == 2):
        kumanda1.tv_kapat()
    elif (int(x) == 3):
        kumanda1.sesAyarla()
    elif (int(x) == 4):
        kanal_isimleri = str(input("Eklemek istediğiniz kanalın isimlerini , ile ayırarak giriniz: "))

        kanal_listesi = kanal_isimleri.split(",")
        for kanal in kanal_listesi:
            kumanda1.kanalEkleme(kanal)

    elif (int(x) == 5):
        print(kumanda1.__len__())
    elif (int(x) == 6):
        kumanda1.rastgeleKanal()
    elif (int(x) == 7):

        for kanal in kumanda1.kanalListesi:

            print(kanal)
    else:
        print("Geçersiz operatör")