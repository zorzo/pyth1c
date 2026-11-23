# Souřadnicový systém v Pygame

## Popis a cíl projektu

Cílem projektu je vytvořit sadu postupně rozvíjených interaktivních aplikací v jazyce Python s využitím grafické knihovny **Pygame**, které názorně demonstrují fungování 2D souřadnicového systému obrazovky (počátek `[0, 0]` v levém horním rohu, osa `X` roste zleva doprava, osa `Y` roste shora dolů).

Projekt postupuje od jednoduchého vykreslení okna a ručního ovládání čtverce pomocí kurzorových kláves až k automatickému náhodnému pohybu s odrazy od stěn, plynulým změnám barev, pulzování velikosti a částicovým efektům při nárazu. Po celou dobu běhu se v levém dolním rohu okna průběžně zobrazují aktuální souřadnice objektu.

---

## Popis funkcionality a vývojové fáze

Projekt je rozdělen na hlavní vývojovou řadu skriptů a navazující rozšířenou řadu s vizuálními efekty:

### Základní vývojová řada

| Soubor | Fáze | Popis funkcionality |
| --- | --- | --- |
| `souradnice_obrazovka.py` | Příprava | Vytvoří okno `800×600` px s bílým pozadím a vykreslí statický text `"Hello World"` na pozici `(50, 500)`. |
| `souradnice_vlevo_vpravo.py` | Fáze 1 | Okno `600×400` px s černým pozadím a vycentrovaným červeným čtvercem (`50×50` px). Umožňuje vodorovný pohyb šipkami `←` a `→` a vypisuje aktuální souřadnice `X, Y`. |
| `souradnice_nahoru_dolu.py` | Fáze 2 | Rozšiřuje Fázi 1 o svislý pohyb čtverce pomocí šipek `↑` a `↓`. |
| `souradnice_nahodny_pohyb.py` | Fáze 3 | Nahrazuje ovládání klávesnicí automatickým pohybem s náhodnou počáteční rychlostí v obou osách a odrazy od všech čtyř stěn okna. |
| `souradnice_nahodny_pohyb_color.py` | Fáze 3+ | Přidává náhodnou změnu RGB barvy čtverce při každém odrazu od stěny okna. |

### Rozšířená řada (`souradnice_nahodny_pohyb_color/`)

| Soubor | Fáze | Popis funkcionality |
| --- | --- | --- |
| `kostka_faze_1_zaklad.py` | Fáze 1 (základ) | Zobrazení statického vycentrovaného červeného čtverce a jeho souřadnic v okně `600×400` px. |
| `kostka_faze_2_pohyb.py` | Fáze 2 (pohyb) | Přidání automatického náhodného pohybu a odrazů od okrajů okna. |
| `kostka_faze_3_barva.py` | Fáze 3 (efekty) | Pokročilá verze s plynulým pulzováním velikosti objektu ze středu, plynulým přechodem odstínu barvy (HSLA), náhodnou změnou barvy při nárazu, ochranou proti zaseknutí ve stěně a částicovým efektem (5 až 7 odlétávajících kostiček po nárazu). |

---

## Uživatelská příručka (User Guide)

### Požadavky

- Python 3.x
- Knihovna `pygame` nebo `pygame-ce`

### Vytvoření a aktivace virtuálního prostředí

```powershell
# Vytvoření virtuálního prostředí
python -m venv .venv
```

- **Aktivace v PowerShellu:**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Pokud PowerShell zablokuje spuštění skriptu, povolte jej pro aktuální relaci příkazem `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process`.)*

- **Aktivace v příkazovém řádku (CMD / DOS):**
  ```cmd
  .\.venv\Scripts\activate
  ```

- **Deaktivace virtuálního prostředí:**
  ```powershell
  deactivate
  ```

### Instalace závislostí

```powershell
# Instalace knihovny Pygame (doporučeno pygame-ce)
python -m pip install pygame-ce

# Alternativně klasický pygame
# python -m pip install pygame

# Ověření nainstalované verze
python -c "import pygame; print('Pygame version:', pygame.ver)"
```

### Spuštění a ovládání

Ze složky projektu `Moje_prace/01_souradnicovysystem/` spusťte vybraný skript, například:

```powershell
# Ruční pohyb ve všech 4 směrech (Fáze 2)
python souradnice_nahoru_dolu.py

# Automatický pohyb se změnou barvy při odrazu
python souradnice_nahodny_pohyb_color.py

# Finální verze s pulzováním, HSLA barvami a částicemi
python souradnice_nahodny_pohyb_color/kostka_faze_3_barva.py
```

- **Ovládání ve Fázi 1 a 2:** kurzorové klávesy `←`, `→`, `↑`, `↓`.
- **Ovládání ve Fázi 3 a rozšířené řadě:** pohyb a efekty probíhají automaticky.
- **Ukončení aplikace:** kliknutím na křížek (`×`) v záhlaví okna.

---

## Technická část

### Použité knihovny

- **`pygame` / `pygame-ce`** – tvorba grafického okna, zpracování událostí a klávesnice, vykreslování geometrických tvarů (`pygame.draw.rect`), práce s textem (`pygame.font`), barvami (`pygame.Color`) a časováním (`pygame.time.Clock`, `pygame.time.get_ticks`).
- **`random`** – generování náhodných rychlostí pohybu (`random.choice`), náhodných barev a počtu částic (`random.randint`) a náhodného rozletu částic (`random.uniform`).
- **`sys`** – čisté ukončení procesu aplikace pomocí `sys.exit()`.
- Externí API není využíváno.

### Struktura projektu

```text
Moje_prace/01_souradnicovysystem/
├── 01_souradnicovy_system_projekt.md
├── souradnice_obrazovka.py
├── souradnice_vlevo_vpravo.py
├── souradnice_nahoru_dolu.py
├── souradnice_nahodny_pohyb.py
├── souradnice_nahodny_pohyb_color.py
└── souradnice_nahodny_pohyb_color/
    ├── kostka_faze_1_zaklad.py
    ├── kostka_faze_2_pohyb.py
    └── kostka_faze_3_barva.py
```

### Použité algoritmy a principy

- **Herní smyčka (Game Loop) s řízením FPS:** Každý snímek zpracuje frontu událostí (`pygame.event.get()`), aktualizuje polohu a efekty objektů, překreslí pozadí, vykreslí objekty a text se souřadnicemi, překlopí grafický buffer (`pygame.display.flip()`) a omezí snímkovou frekvenci na `60 FPS` (`hodiny.tick(60)`).
- **Vycentrování objektu:** Výchozí pozice levého horního rohu čtverce se počítá jako `SIRKA // 2 - velikost_ctverce // 2` a `VYSKA // 2 - velikost_ctverce // 2`.
- **Detekce kolizí se stěnami a odraz:** Kontroluje se překročení levého/horního okraje (`<= 0`) a pravého/dolního okraje (`pozice + velikost >= rozmer_okna`). Při nárazu se otočí znaménko příslušné složky rychlosti (`rychlost_x = -rychlost_x`, resp. `rychlost_y = -rychlost_y`). V `kostka_faze_3_barva.py` je navíc použito oříznutí souřadnic (`max(0, min(...))`), které zabraňuje zaseknutí objektu ve stěně.
- **Symetrické pulzování velikosti (`kostka_faze_3_barva.py`):** Velikost čtverce osciluje mezi hodnotami `40` a `60` px krokem `0.5` px/snímek. Vykreslovací souřadnice se upravují o `odsazeni = (zakladni_velikost - velikost_ctverce) / 2`, takže se čtverec zvětšuje a zmenšuje ze svého středu, zatímco fyzické kolize používají konstantní `zakladni_velikost`.
- **Barevný model HSLA (`kostka_faze_3_barva.py`):** Plynulá změna barvy probíhá cyklickým posunem odstínu `aktualni_hue = (aktualni_hue + 1) % 360` v prostoru HSLA (`pygame.Color.hsla`), při nárazu se odstín skokově změní na náhodnou hodnotu.
- **Částicový systém (`kostka_faze_3_barva.py`):** Při nárazu vznikne `5` až `7` částic o velikosti `8×8` px, které startují ze středu hlavní kostky s náhodnou rychlostí kombinovanou s polovinou hybnosti hlavní kostky. V každém snímku se zachovávají pouze částice mladší než `700 ms` (měřeno přes `pygame.time.get_ticks()`).

### Datové struktury

- **N-tice (tuple):** Používány pro reprezentaci barev v modelu RGB `(R, G, B)`, rozměrů okna `(SIRKA, VYSKA)` a obdélníků `(x, y, sirka, vyska)`.
- **Seznam slovníků (`list[dict]`):** Struktura `castice` v `kostka_faze_3_barva.py`, kde každý slovník reprezentuje jednu částici s klíči:
  - `x`, `y` – aktuální souřadnice částice,
  - `vx`, `vy` – vektor rychlosti částice,
  - `barva` – náhodná RGB barva částice,
  - `cas_vzniku` – časové razítko vytvoření částice v milisekundách.
