---
name: Deutscher Pfadfinderbund
description: Bootstrap 5, auf eine einzige Markenfarbe eingekürzt — flächenlos, flach, in zwei Farbmodi lesbar.
colors:
  bundesblau: "#0051a8"
  bundesblau-tief: "#00458f"
  bundesblau-nacht: "#6697cb"
  anthrazit: "#333333"
  seitengrund: "#f6f6f6"
  flaeche: "#ffffff"
  seitengrund-nacht: "#1b1d20"
  flaeche-nacht: "#25282c"
  text-nacht: "#dee2e6"
  linie: "#dee2e6"
  linie-nacht: "#495057"
  kontrast-nacht: "#e9ecef"
typography:
  display:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "calc(1.375rem + 1.5vw)"
    fontWeight: 500
    lineHeight: 1.2
  headline:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "calc(1.325rem + 0.9vw)"
    fontWeight: 500
    lineHeight: 1.2
  title:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "calc(1.275rem + 0.3vw)"
    fontWeight: 500
    lineHeight: 1.2
  body:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: "0.25rem"
  md: "0.375rem"
  lg: "0.5rem"
spacing:
  sm: "0.5rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  xxl: "3rem"
components:
  button-primary:
    backgroundColor: "{colors.bundesblau}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "0.375rem 0.75rem"
    typography: "{typography.body}"
  button-primary-hover:
    backgroundColor: "{colors.bundesblau-tief}"
  button-outline-dark:
    backgroundColor: "transparent"
    textColor: "{colors.anthrazit}"
    rounded: "{rounded.md}"
    padding: "0.375rem 0.75rem"
    typography: "{typography.body}"
  button-outline-dark-sm:
    backgroundColor: "transparent"
    textColor: "{colors.anthrazit}"
    rounded: "{rounded.sm}"
    padding: "0.25rem 0.5rem"
    typography: "{typography.label}"
  button-outline-dark-sm-nacht:
    textColor: "{colors.kontrast-nacht}"
  button-dark-lg:
    backgroundColor: "{colors.anthrazit}"
    textColor: "#ffffff"
    rounded: "{rounded.lg}"
    padding: "0.5rem 1rem"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.bundesblau}"
    padding: "0.375rem 0.75rem"
    typography: "{typography.body}"
  card:
    backgroundColor: "{colors.seitengrund}"
    textColor: "{colors.anthrazit}"
    rounded: "{rounded.md}"
    padding: "1rem"
  input:
    backgroundColor: "{colors.seitengrund}"
    textColor: "{colors.anthrazit}"
    rounded: "{rounded.md}"
    padding: "0.375rem 0.75rem"
    typography: "{typography.body}"
  nav-link:
    backgroundColor: "transparent"
    textColor: "rgba(255, 255, 255, 0.65)"
    padding: "0.5rem"
    typography: "{typography.body}"
  img-thumbnail:
    backgroundColor: "{colors.seitengrund}"
    rounded: "{rounded.md}"
    padding: "0.25rem"
  table-cell:
    typography: "{typography.label}"
    padding: "0.5rem 0.5rem"
---

# Design System: Deutscher Pfadfinderbund

## Overview

**Creative North Star: "Bootstrap, auf eine Farbe eingekürzt"**

Die Ansage steht im Quelltext: „One brand colour instead of three: the deep blue that has always been used for links now also drives buttons, focus rings, pagination and form focus, so the whole site reads as one palette." (`styles/style.sass`). Das System ist ein Bootstrap 5, dessen Variablenschicht an sieben Stellen angefasst wurde — Markenfarbe, Dunkelton, Seitengrund und Textfarbe je Farbmodus, dazu die vertikale Zellenausrichtung der Tabellen — und das sich ansonsten bewusst nicht verstellt. Es gibt keine eigene Schrift, keine Schatten und keine Animation außer den Zustandsübergängen und dem Karussell.

Die Oberfläche tritt hinter den Inhalt zurück. Flächen unterscheiden sich durch Linien und minimale Helligkeitsabstufungen, nicht durch Höhe. Wärme kommt aus den Fotos — Großfahrt, Bundeslager, Schwarzzelte im Karussell — nicht aus der Oberfläche. Der einzige dauerhaft farbige Block der Seite ist die dunkle Navigationsleiste am oberen Rand; darunter beginnt Papier.

Beide Farbmodi sind gleichwertig gebaut, nicht einer als nachgereichte Variante. Jede neue Fläche muss in beiden Modi bestehen.

**Key Characteristics:**
- Eine Markenfarbe für alles Anklickbare — Links, Buttons, Fokusring, Pagination, Formularfokus.
- Systemschrift des Betriebssystems, kein Webfont, keine Ladezeit für Typografie.
- Flach: keine Schatten auf Seitenflächen, Trennung über Linien und Tonwert.
- Zwei gleichrangige Farbmodi mit eigenen Tokens.
- Fließtext auf Lesebreite begrenzt.
- Fotos bekommen einen schmalen Rahmen statt einer Effektbehandlung.

## Colors

Eine Markenfarbe, sonst Graustufen.

### Primary
- **Bundesblau** (`#0051a8`): Die einzige Markenfarbe. Links im Fließtext, `btn-primary`, Pagination. Der Fokusring `0 0 0 0.25rem rgba(0, 81, 168, 0.25)` — dieselbe Farbe bei 25 % — gilt für Formularfelder, Navigations-Links und Pagination; Buttons setzen stattdessen ihre eigene `--bs-btn-focus-shadow-rgb` bei 50 % (`38, 107, 181` bei `btn-primary` und `btn-link`, `51, 51, 51` bei `btn-outline-dark`). Im dunklen Modus tritt sie als **Bundesblau Nacht** (`#6697cb`) auf — dieselbe Farbe, um 40 % aufgehellt, damit sie auf `#1b1d20` den Kontrast hält.
- **Bundesblau Tief** (`#00458f`): Hoverzustand von `btn-primary`. Der Aktivzustand geht eine Stufe tiefer auf `#004186`. Beide erscheinen nie als Flächenfarbe.

### Neutral
- **Anthrazit** (`#333333`): Fließtext im hellen Modus und `$dark` — die Farbe der Navigationsleiste und der `btn-outline-dark`-Umrandung. Kein reines Schwarz.
- **Seitengrund** (`#f6f6f6`): Hintergrund der hellen Seite. Leicht abgetöntes Weiß, damit weiße Flächen darauf als eigene Ebene lesbar bleiben.
- **Fläche** (`#ffffff`): Projekteigenes Token `--dpb-surface-bg`. Flächen, die sich vom Seitengrund abheben müssen — derzeit der Footer-Streifen (`.stripe`). Bootstraps eigenes `tertiary-bg` war dafür zu nah am Seitengrund.
- **Seitengrund Nacht** (`#1b1d20`): Hintergrund der dunklen Seite.
- **Fläche Nacht** (`#25282c`): `--dpb-surface-bg` im dunklen Modus.
- **Text Nacht** (`#dee2e6`): Fließtext im dunklen Modus. Kein reines Weiß.
- **Linie** (`#dee2e6` hell / `#495057` dunkel): Rahmen, Trenner, Tabellenlinien, Bildrahmen. Der Wert ist in beiden Modi derselbe Tonwertabstand zum Grund.
- **Kontrast Nacht** (`#e9ecef`): Ersatztoken für die Dark-Variante der `dark`-Buttons.

### Named Rules

**Die Ein-Farben-Regel.** Es gibt genau eine Markenfarbe. Alles, was anklickbar ist, trägt sie; alles, was es nicht ist, trägt sie nicht. Eine zweite Akzentfarbe einzuführen heißt, diese Regel aufzukündigen — dann muss das gesamte System neu entschieden werden, nicht nur eine Komponente. Eine Stelle weicht ab: der Bearbeiten-Link für Staff in der Archiv-Detailseite (`archive/templates/archive/detail.html`) trägt `btn-info` und damit Bootstraps Türkis. Bestand, kein Vorbild.

**Die Bundeszeichen-Regel.** Der Schriftzug mit Lilie (`dpb/static/img/schriftzug-dpb.svg`) ist schwarze Line-Art und wird nie umgefärbt, nie invertiert, nie in eine Markenfarbe gesetzt. Im dunklen Modus bekommt er eine helle Fläche unter sich (`.logo-on-light`, Padding `1rem`, Radius `{rounded.md}`), nicht eine Farbumkehr. Im hellen Modus ist diese Fläche unsichtbar, weil sie dem Seitengrund entspricht.

**Die Zwei-Modi-Regel.** Kein Farbwert wird fest geschrieben, wenn ein Bootstrap-Token existiert. Feste Hex-Werte in Templates kippen im dunklen Modus nicht mit; im aktuellen Bestand gibt es keine. Jede neue Fläche wird in beiden Modi geprüft; beide müssen WCAG 2.1 AA erfüllen.

## Typography

**Display Font:** keine eigene. Bootstraps Systemschrift-Stack, Wortlaut im Frontmatter (`typography.*.fontFamily`).
**Body Font:** dieselbe.
**Label/Mono Font:** dieselbe; `.handwritten` schaltet auf `cursive` und ist die einzige Ausnahme.

**Character:** Die Schrift trägt keine Marke, sie trägt den Text. Die Hierarchie entsteht ausschließlich aus Größe und Gewicht, nicht aus Schnittwechseln, Versalien oder Sperrung.

### Hierarchy
- **Display** (fluid, ab 1200px `2.5rem`): `h1`. Eine pro Seite, gesetzt über den `heading`-Block von `base.html`.
- **Headline** (fluid, ab 1200px `2rem`): `h2`. Abschnitte auf der Startseite und Kapitelüberschriften.
- **Title** (fluid, ab 1200px `1.75rem` für `h3` und `1.5rem` für `h4`): Karten- und Eintragsüberschriften. Auf Listenseiten wird `h2` oft mit der Klasse `h3` gesetzt, damit die Dokumentstruktur stimmt und die Optik trotzdem ruhig bleibt — dieses Muster bleibt.
- **Body**: Fließtext, `text-wrap-style: pretty`.
- **Label**: Tabellenzellen und `btn-sm`. Die Größe markiert sekundäre, dichte Information.

### Named Rules

**Die Zeilenmaß-Regel.** Absätze laufen nie über rund 80 Zeichen; Textkolumnen, die neben dem Raster stehen, bekommen `.text-measure` (`68ch`). Die Breite wird über die Textbreite begrenzt, nicht über die Spaltenbreite — die linke Kante bleibt am Raster stehen.

**Die Struktur-vor-Optik-Regel.** Die Überschriftenebene folgt dem Dokument, die Größe folgt dem Blick. Wenn beides kollidiert, gewinnt die Ebene (`<h2 class="h3">`), nie umgekehrt.

## Layout

Bootstraps 12-Spalten-Raster, Gutter `1.5rem`. Die Seite hängt in `container-xl` (max. `1140px` bis xl, `1320px` ab xxl) — Navigationsleiste, Hauptbereich und Footer teilen sich dieselbe Kante.

Der Körper ist eine Flex-Spalte über die volle Fensterhöhe (`d-flex flex-column min-vh-100`): Navigationsleiste oben, `main` mit `flex-grow-1` und Innenabstand `1.5rem` oben / `3rem` unten, Footer-Streifen unten mit `padding-block: 2rem`. Der Footer wird dadurch nie nach oben gezogen, auch nicht auf kurzen Seiten.

Breakpoints sind Bootstrap-Standard: `sm 576px`, `md 768px`, `lg 992px`, `xl 1200px`, `xxl 1400px`. Die Navigation klappt bei `lg` auf. Inhaltsraster nutzen fast durchgehend `col-md-*` für den Inhalt und `col-md-2`/`col-sm-3`/`col-4` für die Vorschaubilder daneben — das Bild schrumpft also relativ mit, statt unter den Text zu springen.

Rhythmus: `1rem` ist der Grundabstand (`mb-3` zwischen Karten und Blöcken), `3rem` der große Schnitt (`mt-5` vor einem neuen Abschnitt, `pb-5` am Seitenende). Dazwischen wird nicht frei interpoliert.

Das Karussell ist der einzige Bereich, der aus dem Raster ausbricht: es sitzt im `preamble`-Block über dem Hauptinhalt und ändert sein Seitenverhältnis mit der Breite (`2/1` mobil, `3/1` ab `576px`, `1440/280` ab `992px`), weil die Quellbilder sehr breit sind und auf dem Telefon sonst nur ein Streifen bliebe.

## Elevation & Depth

Flach. `$enable-shadows` bleibt aus, Karten tragen `--bs-card-bg: var(--bs-body-bg)` — sie stehen also auf demselben Grund wie die Seite und existieren nur durch ihren `1px`-Rahmen. Die Schatten-Utilities aus dem Bootstrap-Bundle werden in keinem Template verwendet.

Tiefe entsteht über drei Mittel, in dieser Reihenfolge: Linie (`--bs-border-color`), Tonwert (`--dpb-surface-bg` gegen den Seitengrund), Abstand. Der einzige Schatten im laufenden Betrieb ist der Fokusring.

### Named Rules

**Die Flach-von-Haus-aus-Regel.** Flächen liegen auf der Seite, nicht darüber. Wer Tiefe braucht, nimmt eine Linie oder einen Tonwert — `box-shadow` ist Zuständen vorbehalten (Fokus), nicht Ebenen.

## Shapes

Ein Grundradius: `0.375rem` (`--bs-border-radius`). Karten, Formularfelder, Bildrahmen, Standardbuttons und die helle Fläche unter dem Schriftzug teilen ihn. Der Radius hängt an der Buttongröße, nicht am Ort: `btn-sm` zieht auf `0.25rem` (die „Weiterlesen"- und „Details"-Buttons in Listen), `btn-lg` auf `0.5rem` (einmal im Bestand, für die Anmeldung über den externen Anbieter).

Zwei Ausnahmen, beide begründet: die Karussell-Indikatoren sind Kreise (`border-radius: 50%`); das Bundeszeichen ist Line-Art ohne Rahmen.

Rahmen sind immer `1px` und tragen `--bs-border-color`. Es gibt keine doppelten Rahmen, keine gestrichelten Linien und keine Umrandung in Markenfarbe — außer am fokussierten Formularfeld, wo der Rahmen auf eine helle Bundesblau-Tönung wechselt.

Bilder im Inhalt tragen `img-thumbnail`: schmaler Innenabstand, Grundfarbe der Seite, `1px`-Linie, derselbe Radius. Das ist der visuelle Ersatz für einen Schatten — ein Passepartout statt einer Erhebung.

## Components

### Buttons
- **Shape:** Radius nach Buttongröße (siehe Shapes). Immer `1px` Rahmen, nie ein Schatten.
- **Primary:** Bundesblau auf Weiß. Selten und nur für die eine Handlung, die eine Seite anbietet: vier Stellen im Bestand — „Neues Haus / Zeltplatz hinzufügen", „Heimabendprogramm hinzufügen", „Suchen" im Katalog, „Eintrag löschen".
- **Outline-Dark:** die Arbeitsvariante und der häufigste Button im Bestand. Vollgroß ist er der Absende-Button fast aller Formulare (Kontakt, Blogeintrag, Haus anlegen, Heimabend, Anmeldung); als `btn-sm` trägt er „Weiterlesen" und „Details" in Listen. Rahmen und Schrift in Anthrazit, Fläche transparent.
- **Dark in groß:** einmal im Bestand, auf der Anmeldeseite für den externen Anbieter (`btn-lg btn-dark`, Schriftgröße `1.25rem`). Die Größe markiert dort, dass es die einzige Handlung der Seite ist.
- **Link:** unterstrichener Text in Bundesblau ohne Rahmen. Für Weiterführendes innerhalb eines Textblocks.
- **Hover / Focus:** Farbwechsel nach Bundesblau Tief bei `btn-primary`, Übergang `0.15s ease-in-out` auf Farbe, Fläche, Rahmen und Schatten. Der Fokusring trägt die Farbe des Buttons, nicht die Markenfarbe (siehe Colors) — er wird nie entfernt.

**Die Dunkelmodus-Umkehr-Regel.** `btn-dark` und `btn-outline-dark` verschwinden im dunklen Modus, weil Bootstrap seine Farb-Utilities nicht pro Modus dreht. Deshalb tauschen beide dort auf helle Tokens (`#e9ecef` als Schrift- und Rahmenfarbe, `$gray-900` beim Hover). Jede neue Verwendung eines `dark`-Utilities muss denselben Tausch mitbringen oder auf ein modusfestes Token ausweichen.

### Cards / Containers
- **Corner Style:** Grundradius (siehe Shapes).
- **Background:** Seitengrund — Karten heben sich nicht durch Farbe ab.
- **Shadow Strategy:** keine (siehe Elevation & Depth).
- **Border:** `1px` in `--bs-border-color-translucent`. Der Kopfbereich (`card-header`) trägt eine Tönung von 3 % der Textfarbe und die Eintragsüberschrift.
- **Internal Padding:** Grundabstand `1rem`, ebenso zwischen den Karten (`mb-3`).

### Inputs / Fields
- **Style:** Grundfarbe der Seite, `1px`-Linie, Grundradius. Label darüber (`form-label`), nie als Platzhalter im Feld.
- **Focus:** Rahmen wechselt auf eine helle Bundesblau-Tönung (`#80a8d4`), dazu der Fokusring in der Markenfarbe, mit demselben Übergang wie bei Buttons.
- **Error:** als `alert` über dem Formular, fett (`.alert { font-weight: bold }`), nicht als stille rote Umrandung.

### Navigation
- **Style:** durchgehend dunkle Leiste (`bg-dark` mit erzwungenem `data-bs-theme="dark"`) — sie bleibt dunkel, egal welchen Farbmodus die Seite trägt. Links `rgba(255, 255, 255, 0.65)`, Hover `0.8`, aktiv `1`.
- **Marke:** weiße Lilie (Inline-SVG, `50px`) plus Wortmarke „DPB", Abstand `1rem` nach rechts. Dies ist die einzige Stelle, an der die Lilie hell ausgegeben wird; sie ist eine eigene Zeichnung, kein umgefärbtes Bundeszeichen.
- **Struktur:** öffentliche Punkte immer sichtbar, interne Menüs (Infos, Inhalte, Bundesarchiv, Präventionsrat, Kalender) nur für angemeldete Personen. Rechts Farbschema-Umschalter und Login bzw. Verwaltung.
- **Mobil:** Aufklappen unter `lg` über den `navbar-toggler`, Menüs werden zu Listen untereinander. Dropdown-Einträge brechen um statt abzuschneiden (`text-wrap`), weil die Titel lang sind.

### Tables
- **Style:** Zellen vertikal zentriert (`$table-cell-vertical-align: middle`), Linien in `--bs-border-color`, fast immer mit `table-hover`. Die Katalogtreffer des Bundesarchivs sind die Hauptanwendung.
- **State:** besuchte Treffer bleiben unterscheidbar (`--bs-success-text-emphasis`) — in beiden Farbmodi.

### Karussell (Signature Component)
Das Karussell über der Startseite ist die einzige gestaltete Abweichung vom Bootstrap-Standard: die Indikatoren sitzen **unter** dem Bild statt darauf (`position: static`), als `10px`-Kreise in `--bs-secondary-color`. Der `<header>` erzwingt `data-bs-theme="dark"`, deshalb lösen die Punkte immer zum dunklen Wert auf (`rgba(222, 226, 230, 0.75)`) und bleiben hell — auch auf der hellen Seite. Das Bild bleibt unverdeckt. Jedes Bild trägt eine beschreibende `alt`-Angabe; das erste lädt normal, alle weiteren `loading="lazy"`.

### Farbschema-Umschalter
Dreiwertig (Hell / Dunkel / Automatisch), im Dropdown rechts in der Leiste, gespeichert unter `dpb-theme` im `localStorage`. Die Auflösung läuft in einem Inline-Skript im `<head>` vor dem Stylesheet, damit nie das falsche Thema aufblitzt. Diese Reihenfolge ist Teil des Designs, nicht eine Optimierung: ein Wechsel dieser Stelle bringt das Flackern zurück.

## Do's and Don'ts

### Do:
- **Do** Farbwerte über Bootstrap-Tokens beziehen (`var(--bs-body-bg)`, `var(--bs-border-color)`), damit sie mit dem Farbmodus kippen.
- **Do** neue Flächen in beiden Farbmodi prüfen, mit WCAG 2.1 AA als Untergrenze.
- **Do** Fließtext auf das Zeilenmaß begrenzen, Kolumnen im Raster mit `.text-measure`.
- **Do** Bilder mit `img-thumbnail` rahmen und mit beschreibendem `alt` versehen.
- **Do** die Überschriftenebene am Dokument ausrichten und die Optik über `.h3`-artige Klassen nachziehen.
- **Do** bei jeder Verwendung eines `dark`-Utilities den Dunkelmodus-Tausch mitliefern.

### Don't:
- **Don't** eine zweite Akzentfarbe einführen — keine farbigen Badges, keine Statusfarben jenseits der Bootstrap-Alerts, keine Verläufe.
- **Don't** das Bundeszeichen umfärben, invertieren oder auf eine farbige Fläche setzen.
- **Don't** `box-shadow` für Ebenen einsetzen; Schatten sind Zuständen vorbehalten.
- **Don't** einen Webfont nachrüsten — der Bestand lädt keinen; wer einen einführt, ändert das System, nicht eine Seite.
- **Don't** einen vierten Radius einführen; es gibt drei, und sie hängen an der Buttongröße (siehe Shapes). Kreise nur an den Karussell-Indikatoren.
- **Don't** den Fokusring entfernen oder abschwächen.
- **Don't** das Inline-Skript zur Farbmodus-Auflösung aus dem `<head>` verschieben oder es `defer` geben.
