povolene_ovoce = ["jablko", "banán", "pomeranč"]
moje_ovoce = "jablko"

if moje_ovoce in povolene_ovoce:
    print(f"{moje_ovoce.capitalize()} je povolené ovoce.")
else:
    print(f"{moje_ovoce.capitalize()} není na seznamu povoleného ovoce.")