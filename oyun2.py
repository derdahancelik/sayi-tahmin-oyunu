
import random
 
def sayitut():
    return random.randint(1, 100)
 
def tahmin_al():
    while True:
        try:
            return int(input("1 ile 100 arasında bir sayı giriniz: "))
        except ValueError:
            print("Lütfen 1 ile 100 arası bir sayı girin!")

def ipucu_ver(gizlisayi, tahmin):
    if tahmin < gizlisayi:
        print("Daha büyük bir sayı dene")
    elif tahmin > gizlisayi:
        print("Daha küçük bir sayı dene")
 
sonuc = sayitut()
tahmin_edilen = tahmin_al()
tahminler = [tahmin_edilen]
 
while tahmin_edilen != sonuc:
    ipucu_ver(sonuc, tahmin_edilen)
    tahmin_edilen = tahmin_al()
    tahminler.append(tahmin_edilen)
 
print("Tebrikler, bildin!")
print("Tahminlerin:", tahminler)
print(len(tahminler), "tahminde bildin.")