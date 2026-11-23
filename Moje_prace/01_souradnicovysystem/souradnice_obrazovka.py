# demonstrace souradnicoveho systemu v pygame 
import pygame # Importuje grafickou knihovnu Pygame

pygame.init() # Inicializuje všechny součásti Pygame

SIRKA, VYSKA = 800, 600 # Nastaví rozměry okna na 800x600 pixelů
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Vytvoří okno aplikace

pygame.display.set_caption("Souradnicovy system v Pygame") # Nastaví text v záhlaví okna

# Hlavní smyčka
bezi = True # Proměnná určující, zda program běží
while bezi: # Smyčka běží, dokud je bezi True
    # Zpracování událostí (klávesnice, myš, zavření okna)
    for udalost in pygame.event.get(): # Prochází seznam všech událostí
        if udalost.type == pygame.QUIT: # Pokud uživatel klikl na křížek
            bezi = False # Zastaví hlavní smyčku

    # Vyplnění pozadí barvou (aby nebylo černé)
    okno.fill((255, 255, 255)) # Vyplní okno bílou barvou
    
    # vypisani textu v okně
    font = pygame.font.Font(None, 36) # Vytvoří objekt písma (výchozí font, velikost 36)
    text = font.render("Hello World", True, (0, 0, 0)) # Vytvoří obrázek s textem "Hello World" v černé barvě
    okno.blit(text, (50, 500)) # Vykreslí text na pozici (50, 500)

    # Zde bude vykreslování tvarů

    # Aktualizace obrazovky
    pygame.display.flip() # Překlopí obsah paměti na obrazovku (zobrazí změny)

pygame.quit() # Ukončí Pygame
