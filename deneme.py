
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
                self.puan += 100
            elif self.kullanici_yasi < 51:
                self.puan += 85
            elif self.kullanici_yasi < 66:
                self.puan += 70
            elif self.kullanici_yasi >= 66:
                self.puan += 50
                 
            if self.egitim_durumu.lower() == "ilkokul":
                self.puan += 30
            elif self.egitim_durumu.lower() == "ortaokul":
                self.puan += 50    
            elif self.egitim_durumu.lower() == "lise":
                self.puan += 70
            elif self.egitim_durumu.lower() == "üniversite":
                self.puan += 90
            elif self.egitim_durumu.lower() == "doktora":
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

def tavsiye_et(risk_grubu):
    print(random.choice(risk_grubu))             

kullanici1 = kullanici("ad", "soyad", 10000, 15, "eğitim", 2, 0.6)

try:
    kullanici1.ad = input("Adınız giriniz: ")
    kullanici1.soyad = input("Soyadınızı giriniz: ")
    kullanici1.ana_para = float(input("Lütfen Ana Paranızı giriniz: "))
    kullanici1.kullanici_yasi = int(input("Yaşınızı giriniz: "))
    kullanici1.egitim_durumu = input("ilkokul/ortaokul/lise/üniversite/doktora: ")
    kullanici1.tecrube_yili = float(input("Kaç senelik tecrübeniz vardır: "))
    kullanici1.kaybedebilecegi_oran = float(input("Ana paranızdan kaybedebileceğiniz paranızın oranını yüzde olarak giriniz(Örn: %80 ise 0.80): "))

except ValueError as e:
    print(e)

kullanici1.kullanici_profili_hesapla()

if kullanici1.puan >= 500:
    print(f"Sayın {kullanici1.ad} {kullanici1.soyad} , yatırımcı profiliniz yüksek riskli yatırım yapmaya uygundur.")
    risk_grubu = yüksek_riskli_yatirimlar
elif kullanici1.puan >= 375:
    print(f"Sayın {kullanici1.ad} {kullanici1.soyad} , yatırımcı profiliniz orta riskli yatırım yapmaya uygundur.")
    risk_grubu = orta_riskli_yatirimlar
elif kullanici1.puan >= 300:
    print(f"Sayın {kullanici1.ad} {kullanici1.soyad} , yatırımcı profiliniz düşük riskli yatırım yapmaya uygundur.")
    risk_grubu = düşük_riskli_yatirimlar
elif kullanici1.puan < 200:
    print(f"Sayın {kullanici1.ad} {kullanici1.soyad} , ne yazık ki profiliniz yatırım tavsiyesi vermemiz için uygun değildir.")

tavsiye_et(risk_grubu=risk_grubu)