# -*- coding: utf-8 -*-
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mal import side, brodsmule, kapitler, kort, modul, tl, videre, videresend

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def skriv(sti, html):
    d = os.path.join(ROT, sti.strip("/")); os.makedirs(d, exist_ok=True)
    open(os.path.join(d,"index.html"),"w").write(html); print("  ",sti,len(html))

def hovedinnhold(fil):
    s = open(os.path.join(ROT, fil)).read()
    i = s.index("<main id=\"innhold\">") + len("<main id=\"innhold\">")
    j = s.index("</main>")
    ut = s[i:j]
    ut = re.sub(r'class="([^"]*?)\bopp\b t\d([^"]*)"', r'class="\1rull\2"', ut)
    ut = re.sub(r'class="([^"]*?)\bopp\b([^"]*)"', r'class="\1rull\2"', ut)
    return ut

def uten_topp(html):
    """fjern sidetopp-seksjonen og den gamle undermenyen"""
    html = re.sub(r'<section class="sidetopp".*?</section>\n', '', html, count=1, flags=re.S)
    html = re.sub(r'<nav aria-label="(Kunstnerarkiv|Modell)".*?</nav>', '', html, count=1, flags=re.S)
    return html

FB = ("Forside","/"); FF = ("Fotograf","/fotograf/")

# ════════════ CV — TIDSLINJE ════════════
cv = f'''
<section class="hero" style="min-height:64svh">
  <div class="hero-media" data-bilde="ypsilon-motlys"><div class="flate"></div></div>
  <div class="hero-slor"></div>
  <div class="hero-innhold">
    <span class="merkelapp gull" style="display:block;margin-bottom:18px">Curriculum vitae</span>
    <h1 class="display">Arbeidet,<br><em>år for år</em></h1>
  </div>
</section>

<section class="rom rom-tett" id="linjen">
  <div class="rom-smal">
    {brodsmule(FB, FF, ("CV", None))}
    <div class="oppslag topp">
      <div class="bred-7">
        <h2 class="tittel rull">Shujah Malik</h2>
        <p class="rull" style="margin-top:14px;color:var(--tekst-2)">Fotograf &middot; Timelapse-artist &middot; Hyperlapse-artist &middot; Dokumentarfotograf &middot; Drammen, Norge</p>
      </div>
      <div class="smal-4">
        <p class="rull">Langsiktig dokumentasjon av Drammen har gitt et visuelt språk som kombinerer dokumentarfotografi med kunstnerisk fortolkning.</p>
      </div>
    </div>

    <div class="tidslinje">
{tl("2026","Utstilling","Usynlige rom","Stedsspesifikt foto- og filmprosjekt med Mirada Nova. Visning i Drammen høsten 2026 — sted og dato annonseres.")}
{tl("2026","Prosjekt","Fjell skole — før og nå","Dokumentasjonen av skolen samles til en egen visning: bygget som var, anleggsårene, og bygget som står der nå.")}
{tl("2015–2025","Dokumentasjon","Gatekunst og urbane transformasjoner","Ti år med systematisk dokumentasjon av gatekunsten og byrommene i endring. Bildene er blant annet brukt i Bærum kommunes gatekunstplan.")}
{tl("2015–2025","Publisering","DRM24","Løpende publiseringer: gatekunst, arkitektur, byrom, timelapse og værfotografi.")}
{tl("2020","Publikasjon","NHO Logistikk og Transport","Fotografier til generalforsamlingen 2020.")}
{tl("2018–2020","Prosjekt","Fjell skole","Fotografering gjennom hele byggeperioden — rehabilitering, utvidelse og ny flerbrukshall som del av områdeløftet på Fjell.")}
{tl("2019","Publikasjon","Norsk kulturforum","Fotografier i årsmeldingen for 2019.")}
{tl("2016","Film","Ugang 2016","Foto og timelapse på dokumentaren fra gressrotfestivalens tredje utgave, sammen med Selina Miles. Final Outlines.")}
{tl("2016","Film","Oslo City Line — Østensjøbanen","Timelapse da fem T-banestasjoner i Oslo ble dekorert, april 2016. Final Outlines, for Sporveien og Oslo kommune.")}
{tl("2015","Film","Ugang 2015","Timelapse og hyperlapse da Drammen avsluttet ti år med nulltoleranse og lot store flater bli malt. Final Outlines.")}
    </div>

    <p class="rull" style="margin-top:clamp(30px,5vh,56px);font-size:13px;color:var(--tekst-3);max-width:60ch">
      Arbeider uten bekreftet årstall — Port of Drammen, The Magic Factory, Munch-muralen i Horten,
      KS, NUNO Arkitektur, Drammen kommune, Strømsgodset og Dagsavisen/Fremtiden — står oppført under
      <a href="/fotograf/publikasjoner/" style="color:var(--gull)">publikasjoner</a> og
      <a href="/fotograf/film/" style="color:var(--gull)">film</a> til datering er bekreftet.
    </p>
  </div>
</section>

<section class="rom lyst" id="praksis">
  <div class="rom-smal">
    <div class="seksjonsnr rull"><span class="merkelapp gull">Praksis</span><span class="strek"></span><span class="merkelapp">Felt og temaer</span></div>
    <div class="fakta rull" style="margin-top:34px">
      <div><span class="n">Medier</span><span class="v">Fotografi · Timelapse · Hyperlapse · Film</span></div>
      <div><span class="n">Temaer</span><span class="v">Urbane landskap · Arkitektur · Kulturarv · Byutvikling · Gatekunst · Tid og bevegelse</span></div>
      <div><span class="n">Geografi</span><span class="v">Drammen · Buskerud · Østlandet</span></div>
    </div>
  </div>
</section>

<section class="rom" id="samarbeid">
  <div class="rom-smal">
    <div class="seksjonsnr rull"><span class="merkelapp gull">Samarbeid</span><span class="strek"></span><span class="merkelapp">Oppdragsgivere</span></div>
    <div class="rader" style="margin-top:34px">
      <div class="rad rull"><div><h3>Final Outlines AS</h3></div><div><p>Timelapse, hyperlapse og foto på gatekunstdokumentarene — sammen med Selina Miles, Eric Ness Christiansen, Dino Trto og Gabrielle Dadgostar. <a href="/fotograf/film/" style="color:var(--gull)">Se filmene &rarr;</a></p></div></div>
      <div class="rad rull"><div><h3>Drammen kommune</h3></div><div><p>Byfotografi og kommunal profilering.</p></div></div>
      <div class="rad rull"><div><h3>Bærum kommune</h3></div><div><p>Gatekunstplan med fotografier fra Drammen.</p></div></div>
      <div class="rad rull"><div><h3>Strømsgodset</h3></div><div><p>Fotografier brukt i klubbens kommunikasjon.</p></div></div>
      <div class="rad rull"><div><h3>Mirada Nova</h3></div><div><p>Fast kunstner i foreningens fotografiske arbeid.</p></div></div>
    </div>
    <!-- TODO: utmerkelser og priser legges inn her nar de er bekreftet av Shujah. -->
  </div>
</section>

{videre("CV — Shujah Malik",
  ("01","Utstillinger","Visninger av arbeidene.","/fotograf/utstillinger/"),
  ("02","Publikasjoner","Hvor bildene har vært trykket.","/fotograf/publikasjoner/"),
  ("03","Film","Timelapse og filmarbeid.","/fotograf/film/"),
  ("04","Presse","Omtale og pressekontakt.","/fotograf/presse/"))}
'''
skriv("/fotograf/cv/", side(
    tittel="CV — Shujah Malik",
    beskrivelse="Curriculum vitae for Shujah Malik: prosjekter, publiseringer, film og samarbeid år for år, fra 2015 til 2026.",
    sti="/fotograf/cv/", og_bilde="shujah-portrett", aktiv_meny="/fotograf/", og_type="profile",
    kapitler_html=kapitler(("linjen","Tidslinje"),("praksis","Praksis"),("samarbeid","Samarbeid")),
    innhold=cv))

# ════════════ UTSTILLINGER ════════════
utst = f'''
<section class="hero" style="min-height:60svh">
  <div class="hero-media" data-bilde="pipedrom"><div class="flate"></div></div>
  <div class="hero-slor"></div>
  <div class="hero-innhold">
    <span class="merkelapp gull" style="display:block;margin-bottom:18px">Utstillinger</span>
    <h1 class="display">Visninger</h1>
  </div>
</section>

<section class="rom rom-tett" id="kommende">
  <div class="rom-smal">
    {brodsmule(FB, FF, ("Utstillinger", None))}
    <div class="seksjonsnr rull"><span class="merkelapp gull">Kommende</span><span class="strek"></span><span class="merkelapp">2026</span></div>
    <div class="tidslinje">
{tl("Høst 2026","Mirada Nova","Usynlige rom","Foto og film fra prosjektet vises i Drammen. Sted og dato annonseres — meld deg på så får du beskjed.")}
    </div>
    <div style="margin-top:clamp(30px,5vh,56px)">
      <a class="lenke stor rull" href="/delta/#skjema"><span>Få beskjed om visningen</span><span class="pil">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="rom lyst" id="tidligere">
  <div class="rom-smal">
    <div class="seksjonsnr rull"><span class="merkelapp gull">Tidligere</span><span class="strek"></span><span class="merkelapp">Under arbeid</span></div>
    <p class="ingress rull" style="margin-top:30px;max-width:56ch">Oversikten over tidligere visninger er under sammenstilling.</p>
    <!-- TODO: legg inn tidligere utstillinger nar Shujah har bekreftet ar, sted og tittel. -->
  </div>
</section>

{videre("Utstillinger",
  ("01","Usynlige rom","Prosjektet som vises.","/prosjekter/usynlige-rom/"),
  ("02","CV","Hele arbeidet, år for år.","/fotograf/cv/"),
  ("03","Verk","Fotografiene i samlingen.","/verk/"),
  ("04","Delta","Vær med når det skjer.","/delta/"))}
'''
skriv("/fotograf/utstillinger/", side(
    tittel="Utstillinger — Shujah Malik",
    beskrivelse="Kommende og tidligere visninger av Shujah Maliks arbeider. Usynlige rom vises i Drammen høsten 2026.",
    sti="/fotograf/utstillinger/", og_bilde="pipedrom", aktiv_meny="/fotograf/",
    kapitler_html=kapitler(("kommende","Kommende"),("tidligere","Tidligere")),
    innhold=utst))

# ════════════ ARVEDE SIDER ════════════
def arv_side(kilde, ny_sti, tittel, beskr, og, bs_navn, kap, vid, erstatt=None):
    inn = uten_topp(hovedinnhold(kilde))
    if erstatt:
        for a,b in erstatt: inn = inn.replace(a,b)
    topp = f'''
<section class="hero" style="min-height:58svh">
  <div class="hero-media" data-bilde="{og}"><div class="flate"></div></div>
  <div class="hero-slor"></div>
  <div class="hero-innhold">
    <span class="merkelapp gull" style="display:block;margin-bottom:18px">{bs_navn}</span>
    <h1 class="display">{tittel.split(" — ")[0]}</h1>
  </div>
</section>

<section class="rom rom-tett">
  <div class="rom-smal">
    {brodsmule(FB, FF, (bs_navn, None))}
  </div>
</section>
'''
    skriv(ny_sti, side(tittel=tittel, beskrivelse=beskr, sti=ny_sti, og_bilde=og,
                       aktiv_meny="/fotograf/", kapitler_html=kap, innhold=topp+inn+"\n"+vid))

arv_side("kunstner/publikasjoner/index.html","/fotograf/publikasjoner/",
  "Publikasjoner — Shujah Malik",
  "Dokumentert bildebruk 2015–2025: KS, NHO Logistikk og Transport, Norsk kulturforum, NUNO Arkitektur, DRM24, Drammens Tidende, Drammen kommune, Strømsgodset og Bærum kommune.",
  "bygarden","Publikasjoner", kapitler(),
  videre("Publikasjoner",
    ("01","CV","Alt året for året.","/fotograf/cv/"),
    ("02","Presse","Omtale og pressekontakt.","/fotograf/presse/"),
    ("03","Film","Filmarbeidene.","/fotograf/film/"),
    ("04","Kontakt","Bildeforespørsler.","/kontakt/")))

arv_side("kunstner/presse/index.html","/fotograf/presse/",
  "Presse — Shujah Malik",
  "Presseomtale og pressekontakt: Dagsavisen/Fremtiden, DRM24 og Drammens Tidende. Pressebilder på forespørsel.",
  "bygarden","Presse", kapitler(),
  videre("Presse",
    ("01","CV","Bakgrunn og arbeider.","/fotograf/cv/"),
    ("02","Publikasjoner","Dokumentert bildebruk.","/fotograf/publikasjoner/"),
    ("03","Verk","Bilder til redaksjonell bruk.","/verk/"),
    ("04","Kontakt","post@mirada.no","/kontakt/")))

arv_side("kunstner/film/index.html","/fotograf/film/",
  "Film og bevegelse — Shujah Malik",
  "Timelapse, hyperlapse og film: Final Outlines-dokumentarene fra Ugang, Port of Drammen, Østensjøbanen, The Magic Factory og Munch-muralen i Horten — og Mirada Novas egne produksjoner.",
  "lysspor","Film", kapitler(("egne","Egne"),("samarbeid","Medvirkende")),
  videre("Film og bevegelse",
    ("01","CV","Årstall og sammenheng.","/fotograf/cv/"),
    ("02","Prosjekter","Kunstprosjektene bak.","/prosjekter/"),
    ("03","Verk","Stillbildene.","/verk/"),
    ("04","Kontakt","Filmoppdrag.","/kontakt/")),
  erstatt=[("/kunstner/film/","/fotograf/film/")])

# ════════════ MODELL UNDER DELTA ════════════
def modellside(kilde, ny_sti, tittel, beskr, og, bsnavn, vid, kap=""):
    inn = uten_topp(hovedinnhold(kilde))
    for a,b in [("/modell/portrett/","/delta/modell/portrett/"),
                ("/modell/base/","/delta/modell/base/"),
                ('href="/modell/"','href="/delta/modell/'+'"')]:
        inn = inn.replace(a,b)
    ledd = [FB, ("Delta","/delta/")]
    if bsnavn != "Modell": ledd.append(("Modell","/delta/modell/"))
    ledd.append((bsnavn, None))
    topp = f'''
<section class="hero" style="min-height:{'86svh' if bsnavn=='Modell' else '58svh'}">
  <div class="hero-media" data-bilde="{og}"><div class="flate"></div></div>
  <div class="hero-slor"></div>
  <div class="hero-innhold">
    <span class="merkelapp gull" style="display:block;margin-bottom:18px">Foran kameraet</span>
    <h1 class="display">{tittel.split(" — ")[0]}</h1>
  </div>
</section>

<section class="rom rom-tett">
  <div class="rom-smal">
    {brodsmule(*ledd)}
  </div>
</section>
'''
    # fjern arvet hero fra kilden (den nye ligger over)
    inn = re.sub(r'<section class="hero">.*?</section>\n', '', inn, count=1, flags=re.S)
    skriv(ny_sti, side(tittel=tittel, beskrivelse=beskr, sti=ny_sti, og_bilde=og,
                       aktiv_meny="/delta/", kapitler_html=kap, innhold=topp+inn+"\n"+vid))

modellside("modell/index.html","/delta/modell/","Modell — Mirada Nova",
  "Modellbilder, profilbilder og portefølje i Drammen — eller registrer deg i modellbasen og bli spurt når vi trenger mennesker foran kameraet.",
  "benken","Modell",
  videre("Modell",
    ("01","Fotografering","Profilbilde, portefølje, headshots.","/delta/modell/portrett/"),
    ("02","Modellbasen","Registrer deg — gratis og uforpliktende.","/delta/modell/base/"),
    ("03","Kunstprosjekter","Vær med i selve prosjektene.","/delta/"),
    ("04","Kontakt","Spør først.","/kontakt/")))

modellside("modell/portrett/index.html","/delta/modell/portrett/","Modell- og profilbilder — Mirada Nova",
  "Profilbilder, modellportefølje, skuespillerbilder og personlige portretter i Drammen. Naturlig lys, rolig tempo, ferdig bearbeidede filer.",
  "blatimen","Fotografering",
  videre("Modell- og profilbilder",
    ("01","Modellbasen","Vil du heller bli spurt om oppdrag?","/delta/modell/base/"),
    ("02","Fotografen","Hvem som står bak kameraet.","/fotograf/"),
    ("03","Verk","Se bildene hans.","/verk/"),
    ("04","Andre oppdrag","Bryllup, arrangement, kommersielt.","/fotograf/oppdrag/")),
  kap=kapitler(("bestill","Bestilling")))

modellside("modell/base/index.html","/delta/modell/base/","Modellbasen — Mirada Nova",
  "Registrer deg i Mirada Novas modellbase i Drammen. Gratis og uforpliktende — vi tar kontakt når et prosjekt eller oppdrag trenger noen som deg.",
  "austad","Modellbasen",
  videre("Modellbasen",
    ("01","Fotografering","Vil du heller bestille bilder?","/delta/modell/portrett/"),
    ("02","Delta","Andre måter å være med på.","/delta/"),
    ("03","Prosjekter","Hva vi faktisk lager.","/prosjekter/"),
    ("04","Kontakt","Spørsmål først.","/kontakt/")),
  kap=kapitler(("registrer","Registrering")))

# ════════════ VIDERESENDINGER ════════════
V = [("/kunstner/","/fotograf/","Kunstnersiden er slått sammen med fotografsiden."),
     ("/kunstner/cv/","/fotograf/cv/","CV-en har flyttet."),
     ("/kunstner/biografi/","/fotograf/","Biografien ligger nå på fotografsiden."),
     ("/kunstner/publikasjoner/","/fotograf/publikasjoner/","Publikasjonene har flyttet."),
     ("/kunstner/presse/","/fotograf/presse/","Pressesiden har flyttet."),
     ("/kunstner/film/","/fotograf/film/","Filmsiden har flyttet."),
     ("/kunstner/prosjekter/","/prosjekter/","Prosjektene ligger nå samlet ett sted."),
     ("/kunstner/galleri/","/verk/","Galleriet er slått sammen med Verk."),
     ("/kunstner/kontakt/","/kontakt/","Kontaktsiden har flyttet."),
     ("/modell/","/delta/modell/","Modellsidene ligger nå under Delta."),
     ("/modell/portrett/","/delta/modell/portrett/","Siden har flyttet."),
     ("/modell/base/","/delta/modell/base/","Modellbasen har flyttet.")]
print("videresendinger:")
for fra, til, tekst in V:
    skriv(fra, videresend(til, tekst))
