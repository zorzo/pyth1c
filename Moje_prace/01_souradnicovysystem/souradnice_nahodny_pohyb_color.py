# nahodny pohyb kostky měnící náhodně barvu
import pygame # Importuje knihovnu Pygame
import sys # Importuje systémový modul
import random # Importuje modul pro náhodná čísla

# Inicializace Pygame
pygame.init() # Inicializuje Pygame

# Nastavení okna
SIRKA = 600 # Nastaví šířku okna
VYSKA = 400 # Nastaví výšku okna
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Vytvoří okno
pygame.display.set_caption("Souřadnicový systém - Fáze 3 (Náhodný pohyb)") # Nastaví titulek

# Barvy
CERNA = (0, 0, 0) # Definuje černou barvu
BILA = (255, 255, 255) # Definuje bílou barvu
CERVENA = (255, 0, 0) # Definuje červenou barvu

# Nastavení objektu (čtverec)
velikost_ctverce = 50 # Nastaví velikost čtverce
ctverec_x = SIRKA // 2 - velikost_ctverce // 2 # Vycentruje X souřadnici
ctverec_y = VYSKA // 2 - velikost_ctverce // 2 # Vycentruje Y souřadnici
aktualni_barva = CERVENA # Počáteční barva =====BARVA=====

# Náhodná rychlost a směr
rychlost_x = random.choice([-5, -4, -3, 3, 4, 5]) # Vybere náhodnou rychlost pro osu X
rychlost_y = random.choice([-5, -4, -3, 3, 4, 5]) # Vybere náhodnou rychlost pro osu Y

# Nastavení písma pro zobrazení souřadnic
pismo = pygame.font.SysFont("Arial", 24) # Nastaví písmo pro text

# Hlavní smyčka
bezi = True # Proměnná pro hlavní smyčku
hodiny = pygame.time.Clock() # Hodiny pro řízení FPS

while bezi: # Hlavní cyklus
    # Zpracování událostí
    for event in pygame.event.get(): # Projde události
        if event.type == pygame.QUIT: # Pokud je požadavek na ukončení
            bezi = False # Zastaví smyčku

    # Automatický pohyb
    ctverec_x += rychlost_x # Změní X souřadnici o rychlost
    ctverec_y += rychlost_y # Změní Y souřadnici o rychlost

    # Odraz od stěn
    # Levá a pravá stěna
    if ctverec_x <= 0 or ctverec_x + velikost_ctverce >= SIRKA: # Pokud narazí do boku
        rychlost_x = -rychlost_x # Otočí směr X
        aktualni_barva = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Změní barvu =====BARVA=====

    # Horní a dolní stěna
    if ctverec_y <= 0 or ctverec_y + velikost_ctverce >= VYSKA: # Pokud narazí nahoru nebo dolů
        rychlost_y = -rychlost_y # Otočí směr Y
        aktualni_barva = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Změní barvu =====BARVA=====

    # Vykreslení
    okno.fill(CERNA) # Smaže obrazovku černou barvou
    
    # Vykreslení objektu
    pygame.draw.rect(okno, aktualni_barva, (ctverec_x, ctverec_y, velikost_ctverce, velikost_ctverce)) # Vykreslí čtverec =====BARVA=====
    
    # Zobrazení souřadnic
    text_souradnice = f"X: {ctverec_x}, Y: {ctverec_y}" # Připraví text souřadnic
    text_plocha = pismo.render(text_souradnice, True, BILA) # Vykreslí text na plochu
    okno.blit(text_plocha, (10, VYSKA - 30)) # Umístí text na obrazovku

    # Aktualizace displeje
    pygame.display.flip() # Zobrazí změny

    # Omezení FPS
    hodiny.tick(60) # Čeká pro dodržení 60 FPS

pygame.quit() # Ukončí Pygame
sys.exit() # Ukončí program
