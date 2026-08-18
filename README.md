# Mirada Nova — nettside

Nettsiden til Mirada Nova Kunst- og kulturforening. Rene HTML-filer, ingen database,
ingen byggesteg, ingen månedlige kostnader. Ligger gratis på GitHub Pages.

## Struktur

Nettstedet er delt i sju sider. Hver side er sin egen `index.html` i sin egen mappe —
det er slik GitHub Pages lager pene adresser uten `.html` i URL-en.

| Adresse | Fil | Innhold |
|---|---|---|
| `/` | `index.html` | Forside: hero, aktuelt prosjekt, tre utvalgte verk, kort intro |
| `/prosjekter` | `prosjekter/index.html` | Oversikt over prosjektene |
| `/prosjekter/usynlige-rom` | `prosjekter/usynlige-rom/index.html` | Egen prosjektside |
| `/verk` | `verk/index.html` | Fotogalleri med lightbox |
| `/om` | `om/index.html` | Manifest, arbeidsfelt, foreningen |
| `/delta` | `delta/index.html` | Deltakelsesformer og påmeldingsskjema |
| `/kontakt` | `kontakt/index.html` | Kontaktside |
| — | `404.html` | Vises når en adresse ikke finnes |

| Fil | Hva det er |
|---|---|
| `assets/css/mirada.css` | All design. Endrer du noe her, endres det på alle sider. |
| `assets/js/mirada.js` | All funksjonalitet: meny, bildelasting, lightbox, skjema. |
| `assets/foto/` | Fotografiene (foto: Shujah Malik) |
| `assets/foto/bilder.json` | Titler, steder og bildestørrelser |
| `CNAME` | Domenet (`mirada.no`) |
| `.nojekyll` | Teknisk fil GitHub trenger. Ikke rør. |
| `sitemap.xml` | Liste over sidene, for søkemotorer |
| `README.md` | Denne veiledningen |

**Vil du endre menyen eller bunnteksten?** Den ligger i hver enkelt HTML-fil.
Endrer du meny eller bunntekst, må du gjøre den samme endringen i alle sju filene
pluss `404.html`.

**Vil du legge til et nytt bilde i galleriet?** Legg de nedskalerte filene i
`assets/foto/`, legg til en oppføring i `bilder.json`, og kopier en av
`<button class="galleri-post">`-blokkene i `verk/index.html`.

---

## 1. Legg siden på GitHub

1. Lag konto på [github.com](https://github.com) hvis du ikke har.
2. Trykk **New repository** øverst til høyre (+ → New repository).
3. Kall den `miradanova` og velg **Public**. Trykk **Create repository**.
4. Trykk **uploading an existing file**, dra inn `index.html`, `README.md`, `CNAME`,
   `.nojekyll` og mappen `assets`. Trykk **Commit changes**.

## 2. Slå på GitHub Pages

1. I repoet: **Settings** → **Pages** (i menyen til venstre).
2. Under *Source*, velg **Deploy from a branch**.
3. Velg branch **main** og mappe **/ (root)**. Trykk **Save**.
4. Etter 1–2 minutter er siden live på
   `https://DITTBRUKERNAVN.github.io/miradanova/`

## 3. Koble på eget domene

Domenet er `mirada.no`, kjøpt hos **Domeneshop**.

**A. Hos Domeneshop** — logg inn → *Mine domener* → `mirada.no` → **DNS-innstillinger**.
Legg inn disse oppføringene (slett eventuelle eksisterende A-records på `@` først):

| Type | Navn (host) | Verdi | TTL |
|---|---|---|---|
| A | @ *(la feltet stå tomt hos Domeneshop)* | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |
| CNAME | www | DITTBRUKERNAVN.github.io. | 3600 |

Legg gjerne også inn AAAA-records hvis Domeneshop tilbyr det (for IPv6):
`2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.

> Hos Domeneshop skriver du **ingenting** i navnefeltet for rot-domenet (det som ellers
> kalles `@`). For `www` skriver du bare `www`. Husk punktum til slutt i CNAME-verdien.

**B. På GitHub** — Settings → Pages → *Custom domain*: skriv inn `mirada.no` og trykk Save.
Kryss av for **Enforce HTTPS** når det blir tilgjengelig (kan ta noen timer).

**C.** Rediger filen `CNAME` i repoet slik at den inneholder domenet ditt, én linje, uten `https://`.

> DNS-endringer kan ta fra 10 minutter til 24 timer før de virker.

## 4. Slå på statist-skjemaet (viktig!)

Skjemaet virker ikke før du kobler det til en mottaker. Gratisløsning:

1. Gå til [formspree.io](https://formspree.io) og lag en gratis konto.
2. Trykk **New Form**, gi den navnet «Statister — Usynlige rom», og oppgi e-postadressen
   påmeldingene skal sendes til.
3. Du får en adresse som ser slik ut: `https://formspree.io/f/xayzbwqd`.
   Den siste delen (`xayzbwqd`) er form-ID-en din.
4. Åpne `index.html`, søk etter `DITT_FORM_ID` og bytt det ut med din ID.
5. Last opp filen på nytt til GitHub. Ferdig — påmeldinger kommer nå rett på e-post.

Gratisplanen tar imot 50 innsendinger i måneden. Blir det flere, får du beskjed fra Formspree —
ingenting belastes automatisk.

## 5. Legge inn bilder

1. Legg bildefilene i mappen `assets/` (bruk `.jpg`, maks ca. 1600 px bredde så siden lastes raskt).
2. Åpne `index.html` og finn seksjonen merket `===== GALLERI =====`.
3. Erstatt en av `<figure class="photo empty">…</figure>`-linjene med denne blokken,
   og bytt ut filnavnet:

```html
<figure class="photo">
  <img src="assets/usynlige-rom-01.jpg" alt="Fra prosjektet Usynlige rom" loading="lazy">
  <div class="shield"></div>
  <figcaption class="credit">
    <span>Usynlige rom</span>
    <span>© <b><span class="js-year">2026</span> Shujah Malik</b></span>
  </figcaption>
</figure>
```

## 6. Endre tekst

All tekst står rett i `index.html` mellom taggene. Du kan trygt redigere teksten
direkte på GitHub: klikk på filen → blyantikonet → endre → **Commit changes**.
Siden oppdaterer seg selv i løpet av et minutt.

Husk å bytte ut disse plassholderne:

- `post@mirada.no` → foreningens virkelige e-postadresse
- Instagram-/Facebook-lenkene i bunnteksten (står som `#` i dag)

---

## Om opphavsrett til bildene

Siden er satt opp slik at:

- Årstallet i alle copyright-merker **oppdateres automatisk** hvert år (`<span class="js-year">`).
- Hvert bilde får et diskret vannmerke «© Shujah Malik» i hjørnet.
- Hvert bilde får en kredittlinje «© [årstall] Shujah Malik» nederst.
- Høyreklikk på bilder er deaktivert, og bildene kan ikke dras ut av siden.
- En egen opphavsrettserklæring står under galleriet, og i bunnteksten.
- `<meta name="copyright">` i toppen av filen forteller søkemotorer hvem som eier bildene.

Merk at ingen nettside kan gjøre bilder teknisk umulige å kopiere — den som virkelig vil,
kan alltid ta et skjermbilde. Tiltakene over stopper tilfeldig kopiering, og den tydelige
merkingen er det som gir juridisk styrke hvis noen bruker bildene uten lov.

For ekstra beskyttelse kan dere:

- legge et synlig vannmerke inn i selve bildefilen før opplasting
- laste opp bilder i moderat oppløsning (f.eks. 1600 px), ikke i full trykk-kvalitet

---

## Hva koster dette?

| | Pris |
|---|---|
| GitHub Pages | Gratis |
| Formspree (50 påmeldinger/mnd) | Gratis |
| Domene (.no) | ca. 100–200 kr per år, betales til domeneleverandøren |

Ingenting her trekker penger fra kortet ditt automatisk.
