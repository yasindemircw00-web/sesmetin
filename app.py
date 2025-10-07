"""Basit toplama işlemi yapan komut satırı programı."""

def main() -> None:
    """Kullanıcıdan iki sayı alıp toplamını yazar."""
    try:
        ilk_sayi = float(input("Birinci sayıyı girin: "))
        ikinci_sayi = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    toplam = ilk_sayi + ikinci_sayi
    print(f"Toplam: {toplam}")


if __name__ == "__main__":
    main()
