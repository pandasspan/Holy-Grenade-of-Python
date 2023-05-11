

import random

yüksek_riskli_yatirimlar = ["NFT" , "Kripto Para" , "Start-Up Şirketleri" , "Gayrimenkul Yatırım Ortakları"]
orta_riskli_yatirimlar = ["Hisse Senetleri", "Yatırım Fonları" , "Emlak" , "Döviz Yatırımları"]
düşük_riskli_yatirimlar = ["Devlet Tahvilleri", "Repo-Ters Repo" , "Vadeli Mevduat" , "Para piyasası"]  


class kullanici():

    def __init__(self,ad,soyad, ana_para, kullanici_yasi, egitim_durumu, tecrube_yili, kaybedebilecegi_oran):
        self.ad = ad
        self.soyad = soyad
        self.ana_para = ana_para
        self.kullanici_yasi = kullanici_yasi
        self.egitim_durumu = egitim_durumu
        self.tecrube_yili = tecrube_yili
        self.kaybedebilecegi_oran = kaybedebilecegi_oran
        self.puan = 0 
        self.kullanici_yasi = 0
   
        

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
            else :
                raise ValueError("Lütfen geçerli sayı giriniz")
            
            if ValueError:
                except ValueError:
            print("Lütfen geçerli bir yaş girin")
            
            
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
            else:
                raise ValueError("Lütfen geçerli bir şey yazınız")
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
            if self.kaybedebilecegi_oran > 0.80:
                self.puan += 200
            elif self.kaybedebilecegi_oran > 0.50:
                self.puan += 150
            elif self.kaybedebilecegi_oran > 0.30:
                self.puan += 100
            elif self.kaybedebilecegi_oran > 0.20:
                self.puan += 75
            elif self.kaybedebilecegi_oran > 0.10:
                self.puan += 50
            elif self.kaybedebilecegi_oran > 0.05:
                self.puan += 15

            if self.puan >= 500:
                print(f"Sayın {self.ad} {self.soyad} , yatırımcı profiliniz yüksek riskli yatırım yapmaya uygundur.")
                a = yüksek_riskli_yatirimlar
            elif self.puan >= 375:
                print(f"Sayın {self.ad} {self.soyad} , yatırımcı profiliniz orta riskli yatırım yapmaya uygundur.")
                risk_grubu = orta_riskli_yatirimlar
            elif self.puan >= 300:
                print(f"Sayın {self.ad} {self.soyad} , yatırımcı profiliniz düşük riskli yatırım yapmaya uygundur.")
                risk_grubu = düşük_riskli_yatirimlar
            elif self.puan < 200:
                print(f"Sayın {self.ad} {self.soyad} , ne yazık ki profiliniz yatırım tavsiyesi vermemiz için uygun değildir.")
    def tavsiye_et(self, risk_grubu):
        yüksek_riskli_yatirimlar = ["NFT" , "Kripto Para" , "Start-Up Şirketleri" , "Gayrimenkul Yatırım Ortakları"]
        orta_riskli_yatirimlar = ["Hisse Senetleri", "Yatırım Fonları" , "Emlak" , "Döviz Yatırımları"]
        düşük_riskli_yatirimlar = ["Devlet Tahvilleri", "Repo-Ters Repo" , "Vadeli Mevduat" , "Para piyasası"]  
        #risk_grubu = kullanici.kullanici_profili_hesapla.
        
        print(random.choice(risk_grubu))             

    def harf_kontrol(self):
        while True:
            try:
                return input(self.egitim_durumu.lower())
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")



class yatirimlar():



    def __init__(self, yatirim_adi, fiyati, risk_orani, vadesi):

        self.yatirim_adi = yatirim_adi
        self.fiyati = fiyati
        self.risk_orani = risk_orani
        self.vadesi = vadesi

kullanici1 = kullanici("bilal", "işçen", 10000, 15, "üniversite", 2, 0.6)

kullanici1.kullanici_yasi = int(input("Yaşınızı giriniz: "))
kullanici1.egitim_durumu = input("ilkokul/ortaokul/lise/üniversite/doktora: ")
kullanici1.tecrube_yili = float(input("Kaç senelik tecrübeniz vardır: "))
kullanici1.kullanici_profili_hesapla()


#kullanici.tavsiye_et(yüksek_riskli_yatirimlar)



