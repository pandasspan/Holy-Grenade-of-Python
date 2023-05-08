

class kullanici():
    def __init__(self,ad,soyad, ana_para, kullanici_yasi, egitim_durumu, tecrube_yili):
        self.ad = ad
        self.ad = soyad
        self.ana_para = ana_para
        self.kullanici_yasi = kullanici_yasi
        self.egitim_durumu = egitim_durumu
        self.tecrube_yili = tecrube_yili

        self.puan = 0 


    def kullanici_profili_hesapla(self):
            
            if self.kullanici_yasi < 18:
                print("Yaşınız yatırım yapmak için uygun değil")
            elif self.kullanici_yasi < 31:
                print(self.kullanici_yasi)
                self.puan += 100
            elif self.kullanici_yasi < 51:
                print(self.kullanici_yasi)
                self.puan += 85
            elif self.kullanici_yasi < 66:
                print(self.kullanici_yasi)
                self.puan += 70
            elif self.kullanici_yasi >= 66:
                print(self.kullanici_yasi)
                self.puan += 50
            
            if self.egitim_durumu == "ilkokul":
                self.puan += 30
            elif self.egitim_durumu == "ortaokul":
                self.puan += 50    
            elif self.egitim_durumu == "lise":
                self.puan += 70
            elif self.egitim_durumu == "üniversite":
                self.puan += 90
            elif self.egitim_durumu == "doktora":
                self.puan += 100

            if self.tecrube_yili == 0:
                self.puan += 0
            elif self.tecrube_yili < 5:
                self.puan += 100
            elif self.tecrube_yili < 10:
                self.puan += 140
            elif self.tecrube_yili < 15:
                self.puan += 170
            elif self.tecrube_yili < 20:
                self.puan += 185
            elif self.tecrube_yili >= 20:
                self.puan += 200
            print(self.puan)

            

class yatirimlar():
    def __init__(self, yatirim_adi, fiyati, risk_orani, vadesi):
        self.yatirim_adi = yatirim_adi
        self.fiyati = fiyati
        self.risk_orani = risk_orani
        self.vadesi = vadesi


class danisman():
    def __init__(self,tavsiye_edilecek_uygun_yatirim):
        self.tavsiye_edilecek_uygun_yatirim = tavsiye_edilecek_uygun_yatirim


kullanici1 = kullanici("bilal", "işçen", 10000, 15, "üniversite", 2)
kullanici1.kullanici_yasi = int(input("Yaşınızı giriniz: "))
kullanici1.egitim_durumu = input("ilkokul/ortaokul/lise/üniversite/doktora: ")
kullanici1.tecrube_yili = float(input("Kaç senelik tecrübeniz vardır: "))
kullanici1.kullanici_profili_hesapla()

 


