import random


sayi = random.randint (1, 100)
tahmin = int(input("1 ile 100 arası bir değer giriniz"))
tahminlerin = [tahmin]

while tahmin != sayi:
     if tahmin < sayi: 
        print("Daha büyük bir sayı deneyiniz")
     else:
        print("Daha küçük bir sayı deneyiniz")
     tahmin = int(input("1 ile 100 arası bir değer giriniz"))
     tahminlerin.append(tahmin)
print("Tebrikler, bildin!")
print("Tahminlerin:", tahminlerin)
print(len(tahminlerin), "tahminde bildin.")