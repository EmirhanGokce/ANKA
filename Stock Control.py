print(*"***************STOK KONTROL ***************")
#Elimizde Kaç (BİN)TL Lik Ürün Var

c=print("""Ürünler:
10-Klavye
20-Fare
30-Kulaklık
40-Mousepad
50-Koltuk
60-Monitör
70-Hoparlör
80-Ekran Kartı
90-RAM
100-Tüm Her Şey
110-Kasa
120-Anakart
130-PSU
140-HDD
150-SSD""""")
ürünler=10,20,30,40,50,60,70,80,90,100,110,120,130,140,150
hesaplar=1,2,3,4
ürün=int(input("Bir Ürün Kodu Giriniz:"))
stok=ürünler
hoparlor= 38
hoparlorgelis = 135
hoparlorsatis = 215
klavye = 50
klavyegelis = 200
klavyesatis = 300
fare = 100
faregelis = 300
faresatis = 480
kulaklık = 70
kulaklıkgelis = 100
kulaklıksatis = 230
mousepad = 143
mousepadgelis = 85
mousepadsatis = 150
koltuk= 195
koltukgelis = 100
koltuksatis = 250
monitör= 195
monitörgelis = 400
monitörsatis = 740
hoparlor= 38
hoparlorgelis = 135
hoparlorsatis = 215
ekrankartı=140
ekrankartıgelis=385
ekrankartısatis=650
ram=50
ramgelis=280
ramsatis=400
kasa=49
kasagelis=100
kasasatis=255
anakart=214
anakartgelis=385
anakartsatis=550
psu=78
psugelis=110
psusatis=200
hdd=130
hddgelis=95
hddsatis=200
ssd=75
ssdgelis=120
ssdsatis=230
if ürün not in ürünler:
     print("Hatalı Giriş")
     pass

while True:
    if ürün==10:
        print("İŞLEMLER=""1-Satın Alınan Klavyelerin Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
                print(klavye*klavyegelis,"TL'Lik Klavye Var")
        if e == 2:
                print(klavye*klavyesatis,"TL'Lik Klavye Satılacak")
        if e==3:
                print(klavye*klavyesatis-klavye*klavyegelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı!")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")

    if ürün==20:

        print("İŞLEMLER=""1-Satın Alınan Farelerin Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(fare*faregelis,"TL'Lik Fare Var")
        if e==2:
             print(fare*faresatis,"TL'Lik Fare Satılacak")
        if e==3:
            print(fare*faresatis-fare*faregelis,"TL Kar Edilecek")
        if e == 4:
            print("Başarıyla Çıkış Yapıldı!")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")

    if ürün==30:

        print("İŞLEMLER=""1-Satın Alınan Kulaklıkların Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
            print(kulaklık*kulaklıkgelis,"TL'Lik Kulaklık Var")
        if e==2:
            print(kulaklık*kulaklıksatis,"TL'Lik Kulaklık Satılacak")
        if e==3:
             print(kulaklık*kulaklıksatis-kulaklık*kulaklıkgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı!")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")
    if ürün==40:

        print("İŞLEMLER=""1-Satın_Alınan Mousepadların Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
            print(mousepad*mousepadgelis,"TL'Lik Mousepad Var")
        if e==2:
            print(mousepad*mousepadsatis,"TL'Lik Mousepad Satılacak")
        if e==3:
             print(mousepad*mousepadsatis-mousepad*mousepadgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı!")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")
    if ürün==50:

        print("İŞLEMLER=""1-Satın Alınan Koltukların Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(koltuk*koltukgelis,"TL'Lik Koltuk Var")
        if e==2:
             print(koltuk*koltuksatis,"TL'Lik Koltuk Satılacak")
        if e==3:
            print(koltuk*koltuksatis-koltuk*koltukgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı!")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")

    if ürün==60:

        print("İŞLEMLER=""1-Satın Alınan Monitörlerin Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(monitör*monitörgelis,"TL'Lik Monitör Var")
        if e==2:
             print(monitör*monitörsatis,"TL'Lik Monitör Satılacak")
        if e==3:
            print(monitör*monitörsatis-monitör*monitörgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")

    if ürün==70:

        print("İŞLEMLER=""1-Satın Alınan Hoparlörlerin Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(hoparlor*hoparlorgelis,"TL'Lik Hoparlör Var")
        if e==2:
             print(hoparlor*hoparlorsatis,"TL'Lik Hoparlör Satılacak")
        if e==3:
            print(hoparlor*hoparlorsatis-hoparlor*hoparlorgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")
    if ürün==80:

        print("İŞLEMLER=""1-Satın Alınan Ekran Kartlarının Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(ekrankartı*ekrankartıgelis,"TL'Lik Ekran Kartı Var")
        if e==2:
             print(ekrankartı*ekrankartısatis,"TL'Lik Ekran Kartı Satılacak")
        if e==3:
            print(ekrankartı*ekrankartısatis-ekrankartı*ekrankartıgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")
    if ürün==90:

        print("İŞLEMLER=""1-Satın Alınan Ramlerin Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(ram*ramgelis,"TL'Lik RAM Var")
        if e==2:
             print(ram*ramsatis,"TL'Lik RAM Satılacak")
        if e==3:
            print(ram*ramsatis-ram*ramgelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")
    if ürün==110:

        print("İŞLEMLER=""1-Satın Alınan Kasaların Parası","2-Tüm Satışlar","3-Tüm Karlar","4-Çıkış")
        e=(int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(kasa*kasagelis,"TL'Lik Kasa Var")
        if e==2:
             print(kasa*kasasatis,"TL'Lik Kasa Satılacak")
        if e==3:
            print(kasa*kasasatis-kasa*kasagelis,"TL Kar Edilecek")
        if e==4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")

    if ürün == 120:

        print("İŞLEMLER=""1-Satın Alınan Anakartların Parası", "2-Tüm Satışlar", "3-Tüm Karlar", "4-Çıkış")
        e= (int(input("Bir İşlem Giriniz:")))
        if e == 1:
            print(anakart * anakartgelis, "TL'Lik Anakart Var")
        if e == 2:
            print(anakart * anakartsatis, "TL'Lik Anakart Satılacak")
        if e == 3:
            print(anakart * anakartsatis - anakart * anakartgelis, "TL Kar Edilecek")
        if e == 4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!", "Yeniden Deneyiz!")
    if ürün == 130:

        print("İŞLEMLER=""1-Satın Alınan PSU Parası", "2-Tüm Satışlar", "3-Tüm Karlar", "4-Çıkış")
        e = (int(input("Bir İşlem Giriniz:")))
        if e == 1:
            print(psu * psugelis, "TL'Lik PSU Var")
        if e == 2:
            print(psu * psusatis, "TL'Lik PSU Satılacak")
        if e == 3:
            print(psu * psusatis - psu* psugelis, "TL Kar Edilecek")
        if e == 4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!", "Yeniden Deneyiz!")
    if ürün == 140:

        print("İŞLEMLER=""1-Satın Alınan HDD Parası", "2-Tüm Satışlar", "3-Tüm Karlar", "4-Çıkış")
        e = (int(input("Bir İşlem Giriniz:")))
        if e == 1:
            print(hdd* hddgelis, "TL'Lik PSU Var")
        if e == 2:
            print(hdd * hddsatis, "TL'Lik PSU Satılacak")
        if e == 3:
            print(hdd * hddsatis - hdd* hddgelis, "TL Kar Edilecek")
        if e == 4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!", "Yeniden Deneyiz!")
    if ürün == 150:

        print("İŞLEMLER=""1-Satın Alınan SSD Parası", "2-Tüm Satışlar", "3-Tüm Karlar", "4-Çıkış")
        e = (int(input("Bir İşlem Giriniz:")))
        if e == 1:
            print(ssd * ssdgelis, "TL'Lik SSD Var")
        if e == 2:
            print(ssd * ssdsatis, "TL'Lik SSD Satılacak")
        if e == 3:
            print(ssd * ssdsatis - ssd * ssdgelis, "TL Kar Edilecek")
        if e == 4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!", "Yeniden Deneyiz!")

    if ürün==100:
        print("İŞLEMLER=""1-Satın Alınan Her Şeyin Parası", "2-Satılacak Şeylerin Parası", "3-Tüm Karlar", "4-Çıkış")
        e = (int(input("Bir İşlem Giriniz:")))
        if e==1:
             print(ssd * ssdgelis+klavye*klavyegelis+hoparlor*hoparlorgelis+monitör*monitörgelis+fare*faregelis+kulaklık*kulaklıkgelis+koltuk*koltukgelis+mousepadgelis*mousepad+psu*psugelis+ram*ramgelis+kasa*kasagelis+hdd*hddgelis+ekrankartı*ekrankartıgelis+anakart*anakartgelis,"TL'Ye Ürün Alındı")
        if e==2:
             print(ssd * ssdsatis+klavye*klavyesatis+hoparlor*hoparlorsatis+monitör*monitörsatis+fare*faresatis+kulaklık*kulaklıksatis+koltuk*koltuksatis+mousepadsatis*mousepad+psu*psusatis+ram*ramsatis+ekrankartı*ekrankartısatis+hdd*hddsatis+anakart*anakartsatis+kasa*kasasatis,"TL'Ye Ürünler Satılacak")
        if e==3:
            print(klavye*klavyesatis-klavye*klavyegelis+hoparlor*hoparlorsatis-hoparlor*hoparlorgelis+monitör*monitörsatis-monitör*monitörgelis+fare*faresatis-fare*faregelis+kulaklık*kulaklıksatis-kulaklık*kulaklıkgelis+koltuk*koltuksatis-koltuk*koltukgelis+mousepadsatis*mousepad-mousepad*mousepadgelis+ekrankartı*ekrankartısatis-ekrankartı*ekrankartıgelis+kasa*kasasatis-kasa*kasagelis+anakart * anakartsatis - anakart *
                  anakartgelis+psu * psusatis - psu* psugelis+hdd * hddsatis - hdd* hddgelis+ram*ramsatis-ram*ramgelis+ssd * ssdsatis - ssd * ssdgelis,"TL Kar Edilecek")

        if e==4:
            print("Başarıyla Çıkış Yapıldı")
            break
        if e not in hesaplar:
            print("Yanlış İşlem Yaptınız!","Yeniden Deneyiz!")





