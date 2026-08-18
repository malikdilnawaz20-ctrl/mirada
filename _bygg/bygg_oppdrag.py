# -*- coding: utf-8 -*-
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mal import side, brodsmule, kapitler, videre

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def skriv(sti, html):
    d = os.path.join(ROT, sti.strip("/")); os.makedirs(d, exist_ok=True)
    open(os.path.join(d,"index.html"),"w").write(html); print("  ",sti,len(html))

arv = open("/tmp/oppdrag-innhold.html").read()
anerk = open("/tmp/anerkjennelse.html").read()
# id-er og ankere justeres til ny adresse
arv = arv.replace('href="#foresporsel"','href="#foresporsel"')
arv = arv.replace(' class="opp',' class="rull').replace('class="opp"','class="rull"')
anerk = anerk.replace(' class="opp',' class="rull').replace('class="opp"','class="rull"')
# fjern t1/t2/t3-forsinkelser (rull-animasjonen er rullestyrt)
arv = re.sub(r'rull t\d', 'rull', arv); anerk = re.sub(r'rull t\d', 'rull', anerk)

innhold = f'''
<section class="hero" style="min-height:76svh">
  <div class="hero-media" data-bilde="blatimen"><div class="flate"></div></div>
  <div class="hero-slor"></div>
  <div class="hero-innhold">
    <span class="merkelapp gull" style="display:block;margin-bottom:18px">Oppdrag</span>
    <h1 class="display">Leie<br><em>fotografen</em></h1>
    <div class="hero-linjer">
      <span>Portrett</span><span>Seremoni</span><span>Arrangement</span><span>Kommersielt</span><span>Kunstprint</span>
    </div>
  </div>
</section>

<section class="rom rom-tett" id="innledning">
  <div class="rom-smal">
    {brodsmule(("Forside","/"), ("Fotograf","/fotograf/"), ("Oppdrag",None))}
    <div class="oppslag topp">
      <div class="bred-7">
        <h2 class="tittel rull">Rolig tempo, naturlig lys,<br>og bilder som ser ut som deg.</h2>
      </div>
      <div class="smal-4">
        <p class="ingress rull">Samme arbeidsmåte som i kunstprosjektene: han venter heller en time på riktig lys enn å tvinge fram bildet.</p>
        <p class="rull">Få instruksjoner, ingen krav om å posere. De fleste trenger et kvarter på å slappe av — den tiden er regnet inn.</p>
        <div style="margin-top:30px;display:flex;gap:36px;flex-wrap:wrap">
          <a class="lenke rull" href="#foresporsel"><span>Be om et tilbud</span><span class="pil">&rarr;</span></a>
          <a class="lenke rull" href="/delta/modell/portrett/"><span>Modell- og profilbilder</span><span class="pil">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<div id="anerkjennelse">
{anerk}
</div>

<div id="tjenester">
{arv}
</div>

{videre("Oppdrag hos Shujah Malik",
  ("01","Fotografen","Hvem han er, og hva han ellers arbeider med.","/fotograf/"),
  ("02","Verk","Se bildene før du bestemmer deg.","/verk/"),
  ("03","Modellbilder","Profilbilde, portefølje eller headshots.","/delta/modell/portrett/"),
  ("04","Kontakt","Ta kontakt direkte.","/kontakt/"))}
'''

skriv("/fotograf/oppdrag/", side(
    tittel="Oppdrag — Shujah Malik",
    beskrivelse="Fotooppdrag i Drammen og på Østlandet: portrett, bryllup og seremoni, arrangement, kommersielt og kunstprint. Pris på forespørsel.",
    sti="/fotograf/oppdrag/", og_bilde="blatimen", aktiv_meny="/fotograf/",
    kapitler_html=kapitler(("innledning","Innledning"),("anerkjennelse","Anerkjennelse"),
                           ("tjenester","Tjenester"),("foresporsel","Forespørsel")),
    innhold=innhold))
