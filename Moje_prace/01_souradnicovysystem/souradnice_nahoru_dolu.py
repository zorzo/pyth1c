import pygame # Importuje knihovnu Pygame
import sys # Importuje systémový modul

# Inicializace Pygame
pygame.init() # Inicializuje Pygame

# Nastavení okna
SIRKA = 600 # Nastaví šířku okna
VYSKA = 400 # Nastaví výšku okna
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Vytvoří okno
pygame.display.set_caption("Souřadnicový systém - Fáze 2") # Nastaví titulek okna

# Barvy
CERNA = (0, 0, 0) # Definuje černou barvu
BILA = (255, 255, 255) # Definuje bílou barvu
CERVENA = (255, 0, 0) # Definuje červenou barvu

# Nastavení objektu (čtverec)
velikost_ctverce = 50 # Nastaví velikost čtverce
ctverec_x = SIRKA // 2 - velikost_ctverce // 2 # Vycentruje X souřadnici
ctverec_y = VYSKA // 2 - velikost_ctverce // 2 # Vycentruje Y souřadnici
rychlost = 5 # Nastaví rychlost pohybu

# Nastavení písma pro zobrazení souřadnic
pismo = pygame.font.SysFont("Arial", 24) # Nastaví písmo Arial velikost 24

# Hlavní smyčka
bezi = True # Nastaví pro smyčku
hodiny = pygame.time.Clock() # Vytvoří hodiny pro řízení FPS

while bezi: # Hlavní cyklus hry
    # Zpracování událostí
    for event in pygame.event.get(): # Načte všechny události
        if event.type == pygame.QUIT: # Pokud uživatel zavře okno
            bezi = False # Ukončí smyčku

    # Získání stavu kláves
    klavesa = pygame.key.get_pressed() # Zjistí stisknuté klávesy
    
    # Pohyb zleva doprava
    if klavesa[pygame.K_LEFT]: # Pokud je stisknuta šipka vlevo
        ctverec_x -= rychlost # Posune čtverec doleva
    if klavesa[pygame.K_RIGHT]: # Pokud je stisknuta šipka vpravo
        ctverec_x += rychlost # Posune čtverec doprava
        
    # Pohyb nahoru a dolu
    if klavesa[pygame.K_UP]: # Pokud je stisknuta šipka nahoru
        ctverec_y -= rychlost # Posune čtverec nahoru
    if klavesa[pygame.K_DOWN]: # Pokud je stisknuta šipka dolů
        ctverec_y += rychlost # Posune čtverec dolů

    # Vykreslení
    okno.fill(CERNA) # Vyčistí okno černou barvou
    
    # Vykreslení objektu
    pygame.draw.rect(okno, CERVENA, (ctverec_x, ctverec_y, velikost_ctverce, velikost_ctverce)) # Vykreslí čtverec
    
    # Zobrazení souřadnic
    text_souradnice = f"X: {ctverec_x}, Y: {ctverec_y}" # Připraví text se souřadnicemi
    text_plocha = pismo.render(text_souradnice, True, BILA) # Vytvoří obrázek textu
    okno.blit(text_plocha, (10, VYSKA - 30)) # Vykreslí text do okna

    # Aktualizace displeje
    pygame.display.flip() # Zobrazí změny na obrazovce

    # Omezení FPS
    hodiny.tick(60) # Omezí rychlost na 60 FPS

pygame.quit() # Ukončí Pygame
sys.exit() # Ukončí program
