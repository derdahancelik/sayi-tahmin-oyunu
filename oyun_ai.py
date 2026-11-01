import random


def sayi_al(mesaj):
    """Kullanıcıdan 1-100 arası geçerli bir tam sayı alır."""
    while True:
        giris = input(mesaj).strip()
        try:
            sayi = int(giris)
        except ValueError:
            print("Lütfen geçerli bir tam sayı girin.")
            continue
        if 1 <= sayi <= 100:
            return sayi
        print("Sayı 1 ile 100 arasında olmalı.")


def oyna():
    hedef = random.randint(1, 100)
    tahminler = []

    print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin!")

    while True:
        tahmin = sayi_al("Tahminin: ")

        if tahmin in tahminler:
            print(f"{tahmin} sayısını zaten denedin, başka bir sayı dene.")
            continue

        tahminler.append(tahmin)

        if tahmin < hedef:
            print("Daha büyük bir sayı dene.")
        elif tahmin > hedef:
            print("Daha küçük bir sayı dene.")
        else:
            print(f"\nTebrikler! Sayı {hedef} idi.")
            print(f"{len(tahminler)} tahminde bildin.")
            print("Tahminlerin:", ", ".join(map(str, tahminler)))
            break


def main():
    while True:
        oyna()
        tekrar = input("\nTekrar oynamak ister misin? (e/h): ").strip().lower()
        if tekrar != "e":
            print("Görüşmek üzere!")
            break