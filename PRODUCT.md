# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Zwei gleichrangige Zielgruppen, die sich dieselbe Website teilen:

- **Außenstehende** — Eltern, Interessierte, Presse. Sie prüfen den Bund, bevor sie Kontakt aufnehmen oder eintreten. Ihr Weg führt über Startseite, Bundesordnung, „Pfadfinderinnen, Pfadfinder und bündische Jugend", Präventionsarbeit, Kontakt und Links.
- **Mitglieder und Führungskräfte** — eingeloggt über den internen Bereich. Sie erledigen laufende Bundesarbeit: Kalender, Häuser und Zeltplätze, Dokumente, Heimabendprogramme, Aktuelles und Themen, Bündisches Segeln, Präventionsrat, Bundesarchiv.

Die Recherche im Bundesarchiv (Online-Katalog, Uploadbereich) ist ein eigener Nutzungsfall, der beide Gruppen berühren kann. Keine der beiden Hauptgruppen darf die andere verdrängen.

## Product Purpose

Offizielle Website des Deutschen Pfadfinderbundes e.V. Sie stellt den Bund nach außen dar und trägt zugleich den internen Betrieb. Erfolg heißt vier Dinge gleichzeitig:

1. **Vertrauen nach außen** — glaubwürdig zeigen, wofür der Bund steht, insbesondere Präventionsarbeit, Präventionsrat und Schutzkonzept.
2. **Mitgliederservice** — Termine, Häuser und Zeltplätze, Dokumente, Heimabendprogramme und Infos verlässlich bereitstellen.
3. **Bundesarchiv zugänglich machen** — Bestand recherchierbar halten und Einsendungen ermöglichen.
4. **Kontakt und Nachwuchs** — Interessierte zu einer Kontaktaufnahme bringen.

## Positioning

Der DPB ist ein unabhängiger, konfessionell nicht gebundener und bündisch geprägter Pfadfinderbund, gemeinnützig und ehrenamtlich getragen, Mitglied im Ring junger Bünde (RjB). Zwei Wurzeln: die aus England stammende weltweite Pfadfinderbewegung und die Deutsche Jugendbewegung. Maßstab sind Gesetz und Versprechen der Pfadfinderinnen und Pfadfinder sowie die Meißnerformel. Erklärtes gesellschaftliches Anliegen: demokratische Gesinnung fördern, totalitären Bestrebungen entgegenwirken, das Gemeinsame betonen statt das Trennende. (Wortlaut: `templates/index.html`.)

## Operating Context

- Inhalte werden im Bund selbst gepflegt (wer genau, ist nicht bestätigt): Seiten als Markdown über die `pages`-App, Dokumente über Django-Filer, Blogeinträge („Aktuelles", „Themen") direkt im Frontend über Formulare.
- Der interne Bereich steht hinter Login (django-allauth, OpenID-Connect-Provider); die Navigation blendet die internen Menüs für anonyme Besucher komplett aus.
- Häuser und Zeltplätze, Heimabendprogramme und Archiveinsendungen werden von Mitgliedern selbst eingetragen.
- Die Übersichtskarte liegt als eigener Dienst unter `karte.deutscher-pfadfinderbund.de`; `/karten/` leitet dauerhaft dorthin.
- Deploy: Image `ghcr.io/deutscher-pfadfinderbund/dpb`, Docker-Compose auf dem Server.

## Capabilities and Constraints

**Vorhandene Funktionen** (Django-Apps): `pages` (Markdown-Seiten), `blog` (Aktuelles/Themen), `archive` (Bundesarchiv: Übersicht, Online-Katalog, Detailseite, Uploadbereich, Feedback), `intern` (Dokumente, Häuser und Zeltplätze, Bündisches Segeln, Kalender), `evening_program` (Heimabendprogramme), `contact` (Kontaktformular), `links`, `permalink` (Kurz-URLs `/s/`, `/x/`, `/l/`), `adressverzeichnis` (kein öffentlicher Routeneintrag — Nutzung derzeit offen).

**Technische Randbedingungen:**
- Stack: Django (Python 3, uv), PostgreSQL, Bootstrap 5 über SASS (`styles/style.sass` → `dpb/static/styles/style.css`), Leaflet für Karten, Font Awesome für Icons. Frontend-Build über npm (`npm run compile-css`).
- Es existiert eine gewachsene, in sich stimmige Oberfläche mit Farbmodus-Umschalter (hell/dunkel/automatisch, `data-bs-theme`, Speicherung in `localStorage`). Eine DESIGN.md gibt es noch nicht — Dokumentationslücke, keine Freifläche.
- Deploy-Falle: `collectstatic` läuft im Image-Build; das Volume `dpbde_web_static` überdeckt neue Assets. Nach jedem Deploy muss das Volume entfernt werden (`README.md`). Statische Dateien werden mit `max-age=86400` ausgeliefert.
- Sprache der Oberfläche ist durchgängig Deutsch (`lang="de"`).

## Brand Commitments

- **Name:** Deutscher Pfadfinderbund e.V., Kurzform DPB.
- **Bundeszeichen:** Der Schriftzug mit Lilie (`dpb/static/img/schriftzug-dpb.svg`) ist schwarze Line-Art. Er wird nie umgefärbt und nie invertiert — auch nicht im dunklen Farbmodus; dort bekommt er eine helle Fläche statt einer Farbumkehr (`.logo-on-light` in `styles/style.sass`). Bestätigt und bindend. Davon unberührt: die separate, weiße Inline-Darstellung der Lilie in der dunklen Navigationsleiste (`templates/base.html`) — bestehender Stand.
- **Tonfall** (aus den vorhandenen Texten abgelesen, nicht bestätigt): sachlich, erklärend, bündische Begriffe ohne Anbiederung (Bundesordnung, Heimabend, Bundesgilde, Meißnerformel).

## Evidence on Hand

Vorhandenes, echtes Material:

- Bundeszeichen als Inline-SVG in `templates/base.html`; Schriftzug `dpb/static/img/schriftzug-dpb.svg` (plus `schriftzug_dpb.png`, `logo_dpb.png`).
- Fotos aus dem Bundesleben: `dpb/static/img/bundeslager2013_200px.jpg`, `schweden2011_200px.jpg`, `irland2012_200px.jpg`, `bundesordnung_200px.png`, `dpb/static/img/carousel/`.
- Präventionsarbeit: Illustration `dpb/static/img/arbeitskreis/arbeitskreis_header.png`; Schutzkonzept als Filer-Dokument (`/filer/filer/1691484458/899/`).
- Redaktionelle Texte in der Datenbank über die `pages`-App (Bundesordnung, DPB, Pfadfinder, Impressum, Datenschutz, Arbeitskreis) sowie Blogeinträge.
- Bundesarchiv-Bestand mit Importpfad `archive/import_books.py`.
- Anschrift: Deutscher Pfadfinderbund e.V., Baueshof 3, 99834 Gerstungen OT Marksuhl. Kontakt: `kanzler@deutscher-pfadfinderbund.de`.

**Was es nicht gibt und was nicht erfunden werden darf:** keine Testimonials, keine Mitglieds- oder Nutzungszahlen, keine Pressestimmen, keine Auszeichnungen, keine Preise oder Fördersummen.

## Product Principles

1. **Zwei Zielgruppen, ein Haus.** Außendarstellung und Mitgliederbereich sind gleichrangig; keine Änderung darf eine der beiden Seiten zugunsten der anderen schwächen.
2. **Präventionsarbeit ist sichtbar, nicht versteckt.** Sie gehört zum öffentlichen Kern des Bundes und bleibt von außen auffindbar.
3. **Inhalte bleiben redigierbar.** Seiten, Dokumente, Blogeinträge, Häuser und Heimabende laufen über Admin, Filer und Frontend-Formulare; neue Arbeit hält diese Wege offen.
4. **Das Bundeszeichen ist gesetzt.** Es wird eingebunden, nicht interpretiert.
5. **Nichts erfinden** (abgeleitet, nicht bestätigt): Es gibt keine Testimonials, Zahlen oder Pressestimmen — fehlende Belege werden weggelassen, nicht ersetzt.

## Accessibility & Inclusion

Verbindlich: **WCAG 2.1 Level AA** — für öffentliche wie interne Seiten. Beide Farbmodi (hell und dunkel) müssen den Kontrastanforderungen genügen.
