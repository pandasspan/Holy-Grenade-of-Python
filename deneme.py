

class kullanici():
    def __init__(self,ad,soyad, ana_para, kullanici_yasi):
        self.ad = ad
        self.ad = soyad
        self.ana_para = ana_para
        self.kullanici_yasi = kullanici_yasi
        self.puan = 0 


    def kullanici_profili_hesapla(self):
            
            if self.kullanici_yasi < 18:
                print("Yaşınız yatırım yapmak için uygun değil")
            elif self.kullanici_yasi < 31:
                print(self.kullanici_yasi)
            elif self.kullanici_yasi < 51:
                print(self.kullanici_yasi)
            elif self.kullanici_yasi < 66:
                print(self.kullanici_yasi)
            elif self.kullanici_yasi >= 66:
                print(self.kullanici_yasi)

               
                
class yatirimlar():
    def __init__(self, yatirim_adi, fiyati, risk_orani, vadesi):
        self.yatirim_adi = yatirim_adi
        self.fiyati = fiyati
        self.risk_orani = risk_orani
        self.vadesi = vadesi




class danisman():
    def __init__(self,tavsiye_edilecek_uygun_yatirim):
        self.tavsiye_edilecek_uygun_yatirim = tavsiye_edilecek_uygun_yatirim
kullanici1 = kullanici("bilal", "işçen", "10000", "15")
kullanici1.kullanici_yasi = int(input("Yaşınızı giriniz: "))
kullanici1.kullanici_profili_hesapla()

 


