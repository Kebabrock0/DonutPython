class Yazilimci():
    def __init__(self, isim, soyisim, numara, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller

    def bilgilerigoster(self):
        print("""
        Yazılımcı objesinin özellikleri
        isim: {}
        Soyisim:  {}
        Numara:  {}
        Maaş:  {}
        Bildiği Diller:  {}
        """.format(self.isim, self.soyisim, self.numara, self.maas, self.diller))

    def zam_yap(self, zam_miktari):
        print("Zam yapılıyor")

        self.maas += zam_miktari


yazilimci = Yazilimci("Kemal", "Şerafettin", 5555555555, 5800, "İngilizce Türkçe Almanca")

yazilimci.bilgilerigoster()

yazilimci.zam_yap(500)

print(yazilimci.maas)