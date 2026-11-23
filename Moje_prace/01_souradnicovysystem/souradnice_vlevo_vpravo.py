import pygame # Importuje knihovnu Pygame pro tvorbu her
import sys # Importuje systémový modul pro interakci se systémem

# Inicializace Pygame
pygame.init() # Inicializuje všechny moduly knihovny Pygame

# Nastavení okna
SIRKA = 600 # Nastaví šířku okna na 600 pixelů
VYSKA = 400 # Nastaví výšku okna na 400 pixelů
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Vytvoří grafické okno o zadaných rozměrech
pygame.display.set_caption("Souřadnicový systém - Fáze 1") # Nastaví text v titulku okna

# Barvy
CERNA = (0, 0, 0) # Definuje černou barvu pomocí RGB modelu
BILA = (255, 255, 255) # Definuje bílou barvu pomocí RGB modelu
CERVENA = (255, 0, 0) # Definuje červenou barvu pomocí RGB modelu

# Nastavení objektu (čtverec)
velikost_ctverce = 50 # Určuje velikost strany čtverce v pixelech
ctverec_x = SIRKA // 2 - velikost_ctverce // 2 # Vypočítá startovní X souřadnici pro vycentrování čtverce
ctverec_y = VYSKA // 2 - velikost_ctverce // 2 # Vypočítá startovní Y souřadnici pro vycentrování čtverce
rychlost = 5 # Nastaví rychlost pohybu čtverce (o kolik pixelů se posune)

# Nastavení písma pro zobrazení souřadnic
pismo = pygame.font.SysFont("Arial", 24) # Načte systémové písmo Arial o velikosti 24 bodů

# Hlavní smyčka
bezi = True # Nastaví proměnnou pro běh smyčky na True
hodiny = pygame.time.Clock()    # Omezení FPS - 60 # Vytvoří objekt hodin pro řízení snímkové frekvence

while bezi: # Spustí hlavní smyčku, která běží, dokud je bezi True
    # Zpracování událostí
    for event in pygame.event.get(): # Prochází seznam všech událostí, které nastaly
        if event.type == pygame.QUIT: # Kontroluje, zda uživatel klikl na křížek pro zavření
            bezi = False # Pokud ano, ukončí smyčku nastavením bezi na False

    # Získání stavu kláves
    klavesa = pygame.key.get_pressed() # Získá aktuální stav všech kláves na klávesnici
    
    # Pohyb zleva doprava
    if klavesa[pygame.K_LEFT]: # Pokud je stisknuta šipka vlevo
        ctverec_x -= rychlost # Odečte hodnotu rychlosti od X souřadnice (pohyb doleva)
    if klavesa[pygame.K_RIGHT]: # Pokud je stisknuta šipka vpravo
        ctverec_x += rychlost # Přičte hodnotu rychlosti k X souřadnici (pohyb doprava)

    # Vykreslení
    okno.fill(CERNA) # Vyplní celé okno černou barvou, čímž smaže předchozí snímek
    
    # Vykreslení objektu
    pygame.draw.rect(okno, CERVENA, (ctverec_x, ctverec_y, velikost_ctverce, velikost_ctverce)) # Vykreslí červený čtverec na nových souřadnicích
    
    # Zobrazení souřadnic
    text_souradnice = f"X: {ctverec_x}, Y: {ctverec_y}" # Vytvoří textový řetězec s aktuálními souřadnicemi
    text_plocha = pismo.render(text_souradnice, True, BILA) # Převede text na obrázek (surface) s vyhlazováním
    okno.blit(text_plocha, (10, VYSKA - 30)) # Vykreslí obrázek s textem na pozici (10, VYSKA - 30)

    # Aktualizace displeje
    pygame.display.flip() # Překlopí buffer a zobrazí vše, co bylo vykresleno, na monitor

    # Omezení FPS
    hodiny.tick(60)     # Omezení FPS - 60 # Pozastaví program tak, aby běžel maximálně 60 FPS

pygame.quit() # Ukončí Pygame a uvolní zdroje
sys.exit() # Ukončí Python skript
