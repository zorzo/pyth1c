# Fáze 1: Zobrazení objektu a jeho souřadnic
import pygame # Importuje knihovnu Pygame
import sys # Importuje systémový modul

# Inicializace Pygame
pygame.init() # Inicializuje Pygame

# Nastavení okna
SIRKA = 600 # Nastaví šířku okna
VYSKA = 400 # Nastaví výšku okna
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Vytvoří okno
pygame.display.set_caption("Souřadnicový systém - Fáze 1 (Základ)") # Nastaví titulek

# Barvy
CERNA = (0, 0, 0) # Definuje černou barvu
BILA = (255, 255, 255) # Definuje bílou barvu
CERVENA = (255, 0, 0) # Definuje červenou barvu

# Nastavení objektu (čtverec)
velikost_ctverce = 50 # Nastaví velikost čtverce
ctverec_x = SIRKA // 2 - velikost_ctverce // 2 # Vycentruje X souřadnici
ctverec_y = VYSKA // 2 - velikost_ctverce // 2 # Vycentruje Y souřadnici

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

    # Vykreslení
    okno.fill(CERNA) # Smaže obrazovku černou barvou
    
    # Vykreslení objektu
    pygame.draw.rect(okno, CERVENA, (ctverec_x, ctverec_y, velikost_ctverce, velikost_ctverce)) # Vykreslí čtverec
    
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
