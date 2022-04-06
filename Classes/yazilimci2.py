class Calisan():

    def __init__(self, isim, maas, departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("""
        Çalışan
        
        İsim: {}
        Maaş: {}
        Departman: {}
        
        """.format(self.isim,self.maas,self.departman))

    def departman_degistir(self,yeniDepartman):
        self.departman = yeniDepartman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisiSayisi):

        super().__init__(isim,maas,departman)

        self.kisiSayisi = kisiSayisi

    def zamYap(self, zamArtısı):
        self.maas += zamArtısı

    def bilgilerigoster(self):
        print("""

          İsim: {}
          Maaş: {}
          Departman: {}
          Sorumlu olduğu kişi sayısı: {}

          """.format(self.isim, self.maas, self.departman,self.kisiSayisi))


yonetici = Yonetici("Raşit",5000,"Design",25)

yonetici.zamYap(8000)
yonetici.bilgilerigoster()