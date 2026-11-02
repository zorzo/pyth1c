def scitani(a, b):
    return a + b
soucet = scitani(5, 7)
print("Součet je:", soucet)
soucet2 = scitani(b=10, a=15)
print("Součet je:", soucet2)

def delen(a,b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b
print("Dělení je:", delen(b=4, a=8))

