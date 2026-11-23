rok_narozeni_text = input("Zadejte rok narození: ")
rok_narozeni = int(rok_narozeni_text)  # Převod textu např. "2009" na celé číslo 2009

# V praxi obojí spojujeme do jednoho řádku:
cena_za_kus = float(input("Zadejte cenu za kus v Kč: "))
pocet_kusu = int(input("Zadejte počet kusů: "))

celkem = cena_za_kus * pocet_kusu
celkem_s_dph = celkem * 1.21  # Přidání DPH 21%
print("Celková cena v Kč:", celkem)