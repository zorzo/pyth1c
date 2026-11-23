# Požadavky na studentskou práci a strukturu repozitáře

Váš veřejný GitHub repozitář je rozdělen na dvě hlavní složky v kořeni repozitáře:

- **`Lekce/`** – obsahuje veškerou práci realizovanou ve škole během výuky (podrobná pravidla viz sekce *Lekce*).
- **`Moje_prace/`** – obsahuje vaše vlastní domácí projekty, které realizujete doma podle níže uvedených podmínek.

---

## Část A: Domácí projekty – složka `Moje_prace`

Ve složce `Moje_prace/` pracujete samostatně doma na vlastních projektech. Během práce musíte plnit následující požadavky:

### 1. Průběžná práce na GitHubu

- Práce bude průběžně ukládána do veřejného repozitáře na GitHubu do složky `Moje_prace/`.
- Během týdne musí proběhnout vaše aktivita. Aktuální týden se počítá vždy od pondělí do neděle (23:59).
- **Alespoň 3 commity týdně:** Během tohoto období musíte provést minimálně tři smysluplné commity.
- **Pravidlo 12 hodin:** Mezi každým ze tří povinných commitů musí uběhnout časový rozestup alespoň 12 hodin. *(Nesmíte odevzdat vše naráz v neděli večer).*

### 2. Kvalita commitů

- Commit musí být smysluplně popsán.
- Popis ponese stručnou informaci (v trpném nebo minulém čase, např. *Přidána kalkulačka*, *Opravena chyba*) odpovídající změnám, které jste v dané dávce kódu opravdu provedli.

### 3. Komentování kódu

- Kód, který vytvoříte, musí být smysluplně okomentován.
- Zaměřte se zejména na logicky složitější části, smyčky a funkce.

### 4. Technická dokumentace

- Souběžně s programováním budete tvořit reálnou technickou dokumentaci k projektu.
- Nejedná se o sloh "jak jsem klikal v editoru", ale o tzv. *User Guide* a technický popis struktury vašeho programu.

> ⚠️ **Do skriptů a na GitHub nevkládejte žádné osobní údaje (jméno, příjmení, e-mail, telefon, adresa atd.)!**

### Postup práce a organizace ve složce `Moje_prace`

- **Výběr názvu:** Vyberete si název projektu a zaznamenáte ho do hlavní tabulky v souboru `README.md` (v kořeni repozitáře nebo ve složce `Moje_prace/README.md`). Jinými slovy stanovíte si cíl!
- **Organizace souborů:** Každý domácí projekt musí mít ve složce `Moje_prace/` svou vlastní samostatnou podsložku. Veškerý kód, modely a obrázky k danému projektu budou pouze uvnitř této složky (např. `Moje_prace/01_snake`).
- **Dokumentace projektu:** Projekt stručně popíšete a dokumentaci uložíte do souboru ve formátu:
  - Název musí končit slovem `_projekt.md` (např. `01_Snake_hra_projekt.md`).
  - Soubor musí být umístěn přímo uvnitř složky daného projektu.

> **DŮLEŽITÉ:** Než začnete pracovat na samotném kódu projektu, musíte si vybrat jeho název a popsat jej v souborech `README.md` a `[nazev]_projekt.md`. V souboru `README.md` jsou postupně uváděny názvy projektů a jejich stručné popisy. Soubor `[nazev]_projekt.md` je vždy uložen ve složce konkrétního projektu a obsahuje podrobnější popis projektu.

---

## Část B: Školní výuka – složka `Lekce`

Práce realizovaná přímo ve vyučovacích hodinách patří do složky `Lekce/`:

- **Přesun dosavadních souborů:** Veškerý stávající obsah v repozitáři přesuňte do složky `Lekce/L_2026_Zari_Rijen`.
- **Podsložky jednotlivých hodin:** Každá vyučovací hodina má ve složce `Lekce/` podsložku s názvem `L_<YYYYMMDD>_<tema_hodiny>` (např. `L_20261102_smycky`).
- **Měsíční přesuny:** S každým novým měsícem se práce za uplynulý měsíc přesunou do podsložky s názvem měsíce (např. `L_2026_Listopad`, `L_2026_Prosinec`).
- **Přehled lekcí (`Lekce/README.md`):** V kořeni složky `Lekce` je soubor `README.md` stručně a heslovitě popisující lekce (jedna lekce = jeden řádek obsahující datum lekce, umístění a heslovitý popisek).

> 👉 Podrobný rozpis a ukázku struktury najdete na stránce **Lekce**.

---

## Šablony souborů pro domácí projekty (`Moje_prace`)

### Formát souboru `README.md`

Pořadové číslo, název projektu, datum zápisu (pro vaši vlastní evidenci do budoucna).

### Formát souboru `[nazev]_projekt.md`

#### Obsah dokumentace (vytvářena souběžně)

Dokumentace bude obsahovat následující informace:

- Název projektu, na kterém pracujete.
- Popis a cíl projektu.
- Popis funkcionality programu.
- **Technická část:** použité knihovny, algoritmy, vlastní datové struktury, nebo volání externího API atd.

---

*© 2026, J. Heczk*
