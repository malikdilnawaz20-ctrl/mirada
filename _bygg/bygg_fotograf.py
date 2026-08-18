# -*- coding: utf-8 -*-
"""Bygger /fotograf/* — Shujah Maliks ene rom."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mal import side, brodsmule, kapitler, kort, modul, tl, videre, videresend

ROT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def skriv(sti, html):
    d = os.path.join(ROT, sti.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("  ", sti, len(html))

AKTIV = "/fotograf/"
BS = ("Forside", "/")

# ══════════════════ 1. PORTALEN ══════════════════
PERSON_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Person","name":"Shujah Malik",
"jobTitle":"Fotograf, timelapse- og hyperlapse-artist","url":"https://mirada.no/fotograf/",
"image":"https://mirada.no/assets/foto/shujah-portrett-1600.jpg",
"worksFor":{"@type":"Organization","name":"Mirada Nova Kunst- og kulturforening","url":"https://mirada.no"},
"knowsAbout":["Fotografi","Timelapse","Hyperlapse","Dokumentarfotografi","Byrom","Arkitektur","Kulturarv"],
"homeLocation":{"@type":"Place","name":"Drammen, Norge"},
"email":"post@mirada.no","sameAs":["https://mirada.no/fotograf/cv/"]}
</script>
'''

portal = f'''
<section class="hero">
  <div class="hero-media" data-bilde="shujah-portrett"><div class="flate" style="background-position:52% 30%"></div></div>
  <div class="hero-slor"></div>
  <div class="hero-innhold">
    <span class="merkelapp gull" style="display:block;margin-bottom:18px">Fotograf &middot; Kunstner</span>
    <h1 class="display">Shujah<br><em>Malik</em></h1>
    <div class="hero-linjer">
      <span>Fotografi</span><span>Timelapse</span><span>Hyperlapse</span><span>Dokumentar</span>
    </div>
  </div>
  <div class="bla-ned"><i></i><span class="merkelapp">Bla ned</span></div>
</section>

<section class="rom" id="apning">
  <div class="rom-smal">
    {brodsmule(BS, ("Fotograf", None))}
    <div class="oppslag bunn">
      <div class="bred-8">
        <h2 class="stor-sitat rull">Gjennom fotografi, timelapse og hyperlapse dokumenterer han de <em>skjulte historiene</em> i byrommet.</h2>
      </div>
      <div class="smal-3">
        <p class="rull">Arbeidene utforsker arkitektur, kulturarv og menneskers forhold til steder i kontinuerlig endring. Base i Drammen, arbeid over hele Østlandet.</p>
      </div>
    </div>

    <div class="fakta rull" style="margin-top:clamp(40px,6vh,74px)">
      <div><span class="n">Base</span><span class="v">Drammen, Norge</span></div>
      <div><span class="n">Medier</span><span class="v">Fotografi &middot; Timelapse &middot; Hyperlapse &middot; Film</span></div>
      <div><span class="n">Henvendelser</span><span class="v"><a href="mailto:post@mirada.no" style="color:var(--gull)">post@mirada.no</a></span></div>
    </div>
  </div>
</section>

<section class="rom rom-tett" id="arkivet">
  <div class="rom-smal">
    <div class="seksjonsnr rull">
      <span class="merkelapp gull">Arkivet</span><span class="strek"></span>
      <span class="merkelapp">Seks rom</span>
    </div>

    <div class="modul-rad" style="margin-top:clamp(30px,5vh,54px)">
      {modul("/fotograf/cv/","CV","År for år: prosjekter, publiseringer, utstillinger og samarbeid i én tidslinje.","Se tidslinjen")}
      {modul("/fotograf/utstillinger/","Utstillinger","Visninger og presentasjoner av arbeidene — kommende og gjennomførte.")}
      {modul("/fotograf/publikasjoner/","Publikasjoner","Dokumentert bildebruk hos aviser, kommuner, organisasjoner og arkitektkontorer, 2015–2025.")}
      {modul("/fotograf/presse/","Presse","Omtale, presseforespørsler og bilder til redaksjonell bruk.")}
      {modul("/fotograf/film/","Film","Timelapse, hyperlapse og filmarbeid — Final Outlines-dokumentarene og egne produksjoner.")}
      {modul("/fotograf/oppdrag/","Oppdrag","Portrett, seremoni, arrangement, kommersielt og kunstprint. Pris på forespørsel.","Be om tilbud")}
    </div>
  </div>
</section>

<figure class="foto zoom foto-full lav parallakse rull" data-bilde="lysspor">
  <div class="flate"></div>
  <div class="full-tekst"><span class="navn" style="font-family:var(--serif);font-size:1.25rem">Lysspor</span><span class="merkelapp">Nattarbeid, Drammen</span></div>
</figure>

<section class="rom" id="arbeidet">
  <div class="rom-smal">
    <div class="seksjonsnr rull">
      <span class="merkelapp gull">Arbeidet</span><span class="strek"></span>
      <span class="merkelapp">Utvalg</span>
    </div>

    <div class="kort-rad" style="margin-top:clamp(30px,5vh,54px)">
      {kort("/prosjekter/usynlige-rom/","ypsilon-rim","Prosjekt","Usynlige rom",
            "Rom i byen som er tømt for oppmerksomhet — fylt igjen, i noen timer.",
            ["2026","Foto og film"],"Utforsk prosjektet", stor=True)}
      {kort("/fotograf/film/","brua","Film","Gatekunstbølgen",
            "Timelapse og hyperlapse fra Ugang, Port of Drammen og Østensjøbanen.",
            ["2015–2017","Final Outlines"],"Se filmene")}
      {kort("/prosjekter/fjell-skole/","fjell-host","Dokumentasjon","Fjell skole — før og nå",
            "Skolen som var, årene med riving og bygging, og bygget som står der nå.",
            ["2018–2020","Drammen"],"Se prosjektet")}
    </div>

    <div style="margin-top:clamp(40px,6vh,70px);display:flex;gap:40px;flex-wrap:wrap">
      <a class="lenke stor rull" href="/verk/"><span>Alle verk</span><span class="pil">&rarr;</span></a>
      <a class="lenke stor rull" href="/prosjekter/"><span>Alle prosjekter</span><span class="pil">&rarr;</span></a>
    </div>
  </div>
</section>

{videre("Shujah Malik",
  ("01","CV","Tidslinje over arbeidet, år for år.","/fotograf/cv/"),
  ("02","Verk","Fotografiene i husets samling.","/verk/"),
  ("03","Oppdrag","Leie ham til portrett, seremoni eller arrangement.","/fotograf/oppdrag/"),
  ("04","Kontakt","Presse, samarbeid eller spørsmål.","/kontakt/"))}
'''

skriv("/fotograf/", side(
    tittel="Shujah Malik — fotograf og kunstner",
    beskrivelse="Shujah Malik, fotograf og kamerabasert kunstner i Drammen. CV, utstillinger, publikasjoner, presse, film og oppdrag.",
    sti="/fotograf/", og_bilde="shujah-portrett", aktiv_meny=AKTIV,
    og_type="profile", extra_head=PERSON_LD,
    kapitler_html=kapitler(("apning","Åpning"),("arkivet","Arkivet"),("arbeidet","Arbeidet")),
    innhold=portal))
print("portal ferdig")
