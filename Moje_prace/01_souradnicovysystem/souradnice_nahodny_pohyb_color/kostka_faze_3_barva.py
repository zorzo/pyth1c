# Fáze 3: Přidání změny barvy, pulzování a částic
import pygame
import sys
import random

# Inicializace Pygame
pygame.init()

# Nastavení okna
SIRKA = 600
VYSKA = 400
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Souřadnicový systém - Fáze 3 (Pulzování a částice)")

# Barvy
CERNA = (0, 0, 0)
BILA = (255, 255, 255)

# Nastavení objektu (čtverec)
zakladni_velikost = 50
velikost_ctverce = zakladni_velikost
ctverec_x = SIRKA // 2 - zakladni_velikost // 2
ctverec_y = VYSKA // 2 - zakladni_velikost // 2

# Proměnné pro pulzování velikosti
pulz_smer = 1 # 1 pro zvětšování, -1 pro zmenšování
pulz_rychlost = 0.5
pulz_min = 40
pulz_max = 60

# Proměnné pro plynulou změnu barvy (HUE)
aktualni_hue = random.randint(0, 359)
barva_objekt = pygame.Color(0, 0, 0)
barva_objekt.hsla = (aktualni_hue, 100, 50, 100)
aktualni_barva = (barva_objekt.r, barva_objekt.g, barva_objekt.b)

# Náhodná rychlost a směr
rychlost_x = random.choice([-5, -4, -3, 3, 4, 5])
rychlost_y = random.choice([-5, -4, -3, 3, 4, 5])

# Seznam pro částice (efekt při nárazu)
castice = [] # format: {'x': x, 'y': y, 'vx': vx, 'vy': vy, 'barva': barva, 'cas_vzniku': cas}

# Nastavení písma pro zobrazení souřadnic
pismo = pygame.font.SysFont("Arial", 24)

# Hlavní smyčka
bezi = True
hodiny = pygame.time.Clock()

while bezi:
    aktualni_cas = pygame.time.get_ticks()

    # Zpracování událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bezi = False

    # Automatický pohyb
    ctverec_x += rychlost_x
    ctverec_y += rychlost_y

    # Pulzování velikosti
    velikost_ctverce += pulz_smer * pulz_rychlost
    if velikost_ctverce >= pulz_max or velikost_ctverce <= pulz_min:
        pulz_smer *= -1

    # Pulzování barvy (plynulá změna odstínu)
    aktualni_hue = (aktualni_hue + 1) % 360
    barva_objekt.hsla = (aktualni_hue, 100, 50, 100)
    aktualni_barva = (barva_objekt.r, barva_objekt.g, barva_objekt.b)

    naraz = False

    # Odraz od stěn (používáme základní velikost pro výpočet odrazu)
    # Levá a pravá stěna
    if ctverec_x <= 0 or ctverec_x + zakladni_velikost >= SIRKA:
        rychlost_x = -rychlost_x
        # Zabránění zaseknutí ve stěně
        ctverec_x = max(0, min(ctverec_x, SIRKA - zakladni_velikost))
        naraz = True

    # Horní a dolní stěna
    if ctverec_y <= 0 or ctverec_y + zakladni_velikost >= VYSKA:
        rychlost_y = -rychlost_y
        # Zabránění zaseknutí ve stěně
        ctverec_y = max(0, min(ctverec_y, VYSKA - zakladni_velikost))
        naraz = True

    # Pokud došlo k nárazu, vygeneruj částice
    if naraz:
        # Skoková změna barvy při nárazu
        aktualni_hue = random.randint(0, 359)
        
        # Vystřelení 5 až 7 menších kostiček
        pocet_castic = random.randint(5, 7)
        for _ in range(pocet_castic):
            castice.append({
                'x': ctverec_x + zakladni_velikost / 2, # ze středu hlavní kostky
                'y': ctverec_y + zakladni_velikost / 2,
                'vx': random.uniform(-6, 6) + rychlost_x * 0.5, # rozlet + přidání hybnosti kostky
                'vy': random.uniform(-6, 6) + rychlost_y * 0.5,
                'barva': (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
                'cas_vzniku': aktualni_cas
            })

    # Vykreslení
    okno.fill(CERNA)
    
    # Aktualizace a vykreslení částic
    nove_castice = []
    for c in castice:
        # Zkontrolujeme, zda částice žije méně než 700 ms (0.7 s)
        if aktualni_cas - c['cas_vzniku'] < 700:
            c['x'] += c['vx']
            c['y'] += c['vy']
            velikost_c = 8
            pygame.draw.rect(okno, c['barva'], (c['x'] - velikost_c/2, c['y'] - velikost_c/2, velikost_c, velikost_c))
            nove_castice.append(c) # Ponecháme částici
    castice = nove_castice # Aktualizujeme list tak, že si necháme jen ty, které žijí

    # Výpočet pozice tak, aby se čtverec zvětšoval/zmenšoval ze svého středu
    odsazeni = (zakladni_velikost - velikost_ctverce) / 2
    vykreslit_x = ctverec_x + odsazeni
    vykreslit_y = ctverec_y + odsazeni
    
    # Vykreslení hlavního objektu
    pygame.draw.rect(okno, aktualni_barva, (vykreslit_x, vykreslit_y, velikost_ctverce, velikost_ctverce))
    
    # Zobrazení souřadnic (zakotveno na fyzický roh původního objektu)
    text_souradnice = f"X: {int(ctverec_x)}, Y: {int(ctverec_y)}"
    text_plocha = pismo.render(text_souradnice, True, BILA)
    okno.blit(text_plocha, (10, VYSKA - 30))

    # Aktualizace displeje
    pygame.display.flip()

    # Omezení FPS
    hodiny.tick(60)

pygame.quit()
sys.exit()
