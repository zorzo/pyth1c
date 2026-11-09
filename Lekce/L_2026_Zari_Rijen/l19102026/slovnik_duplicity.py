cislo_list = [1,2,2,2,4,5,6,7,7,7,7,7]
unikatni_cisla = set(cislo_list)
prazdna_mnozina = set()
prazdna_mnozina.add(150)
prazdna_mnozina.add(90)
print("Množina po přidání prvků:", prazdna_mnozina)

if 3 in unikatni_cisla:
    print("Číslo 3 je v množině unikátních čísel.")
else:
    print("Číslo 3 ---NENÍ--- v množině unikátních čísel.")
