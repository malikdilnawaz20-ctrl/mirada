# -*- coding: utf-8 -*-
"""Felles mal for Mirada Nova. Alle genererte sider bygges herfra."""

MENY = [("/prosjekter/","Prosjekter"),("/verk/","Verk"),("/fotograf/","Fotograf"),
        ("/om/","Om"),("/delta/","Delta")]

MENY_BESKRIVELSE = {
    "/prosjekter/":"Kunstprosjekter og kulturarv",
    "/verk/":"Store fotografier",
    "/fotograf/":"Shujah Malik",
    "/om/":"Mirada Nova",
    "/delta/":"Samarbeid og modelldeltakelse",
}

MONOGRAM = ('<svg class="monogram" viewBox="0 0 40 40" aria-hidden="true">'
            '<path d="M3 29 V11 L11 24 L19 11 V29"/><path d="M24 29 V11 L36 29 V11"/>'
            '<line x1="3" y1="34.5" x2="36" y2="34.5" stroke-opacity=".45"/></svg>')


def meny(aktiv):
    ut = []
    for sti, navn in MENY:
        cur = ' aria-current="page"' if aktiv and sti == aktiv else ''
        ut.append(f'<a href="{sti}"{cur}>{navn}</a>')
    return "\n    ".join(ut)


def mobilmeny(aktiv):
    ut = []
    for sti, navn in MENY:
        cur = ' aria-current="page"' if aktiv and sti == aktiv else ''
        d = MENY_BESKRIVELSE[sti]
        ut.append(f'<a href="{sti}"{cur}><span class="mm-navn">{navn}</span>'
                  f'<span class="mm-desc">{d}</span></a>')
    return "\n    ".join(ut)


def brodsmule(*ledd):
    """brodsmule(("Forside","/"), ("Fotograf","/fotograf/"), ("CV",None))"""
    b = ['<nav class="brodsmule" aria-label="Du er her">']
    for i, (navn, sti) in enumerate(ledd):
        if i:
            b.append('<span class="skille" aria-hidden="true">/</span>')
        if sti:
            b.append(f'<a href="{sti}">{navn}</a>')
        else:
            b.append(f'<span aria-current="page">{navn}</span>')
    b.append('</nav>')
    return "\n  ".join(b)


def kapitler(*ledd):
    """flytende kapittelnavigasjon: (id, navn)"""
    if not ledd:
        return ""
    a = "".join(f'<a href="#{i}" data-kap="{i}"><span class="navn-k">{n}</span>'
                f'<span class="strek-k"></span></a>' for i, n in ledd)
    return f'<nav class="kapitler" id="kapitler" aria-label="Kapitler">{a}</nav>'


def kort(href, bilde, merkelapp, tittel, tekst, meta=None, mer="Se mer", stor=False):
    m = ''
    if meta:
        m = '<span class="kort-meta">' + "".join(f'<span>{x}</span>' for x in meta) + '</span>'
    return f'''<a class="kort rull{' h' if stor else ''}" href="{href}">
        <span class="kort-foto" data-bilde="{bilde}"><span class="flate"></span></span>
        <span class="kort-innhold">
          <span class="kort-topp"><span class="merkelapp">{merkelapp}</span></span>
          <h3>{tittel}</h3>
          {m}
          <span class="kort-tekst">{tekst}</span>
          <span class="kort-mer">{mer} <span class="pil">&rarr;</span></span>
        </span>
      </a>'''


def modul(href, tittel, tekst, mer="Åpne"):
    return f'''<a class="modul rull" href="{href}">
        <h3>{tittel}</h3>
        <p>{tekst}</p>
        <span class="modul-mer">{mer} <span class="pil">&rarr;</span></span>
      </a>'''


def tl(aar, kategori, tittel, tekst):
    return f'''    <div class="tl rull">
      <span class="aar">{aar}</span>
      <div class="tl-innhold">
        <span class="kat">{kategori}</span>
        <h3>{tittel}</h3>
        <p>{tekst}</p>
      </div>
    </div>
'''


def videre(du_ser, *steg):
    """steg: (nr, tittel, tekst, href)"""
    k = "".join(f'''      <a class="videre-kort" href="{h}">
        <span class="nr">{nr}</span>
        <h4>{t}</h4>
        <p>{be}</p>
        <span class="pil">&rarr;</span>
      </a>
''' for nr, t, be, h in steg)
    return f'''<section class="videre">
  <div class="rom-smal">
    <span class="du-ser">Du ser på</span>
    <p class="na">{du_ser}</p>
    <div class="videre-rad">
{k}    </div>
  </div>
</section>'''


def side(*, tittel, beskrivelse, sti, og_bilde, aktiv_meny, innhold,
         extra_head="", kapitler_html="", og_type="website"):
    return f'''<!DOCTYPE html>
<html lang="nb">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{tittel} — Mirada Nova</title>

<meta name="description" content="{beskrivelse}">
<meta name="author" content="Mirada Nova Kunst- og kulturforening">
<meta name="copyright" content="© 2026 Mirada Nova. Alle fotografier © Shujah Malik.">
<meta name="theme-color" content="#0B0B0D">
<meta name="robots" content="index, follow, max-image-preview:large">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Mirada Nova">
<meta property="og:title" content="{tittel} — Mirada Nova">
<meta property="og:description" content="{beskrivelse}">
<meta property="og:locale" content="nb_NO">
<meta property="og:url" content="https://mirada.no{sti}">
<meta property="og:image" content="https://mirada.no/assets/foto/{og_bilde}-1600.jpg">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" type="image/png" href="/assets/apple-touch-icon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="canonical" href="https://mirada.no{sti}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Inter:wght@200;300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/mirada.css">
{extra_head}</head>

<body>

<a class="hopp" href="#innhold">Hopp til innhold</a>

<header class="nav" id="nav">
  <a class="merke" href="/" aria-label="Mirada Nova — forsiden">
    {MONOGRAM}
    <span class="merke-navn">Mirada Nova</span>
  </a>

  <button class="meny-knapp" id="meny-knapp" aria-expanded="false" aria-controls="mobilmeny" aria-label="Meny">
    <span></span><span></span><span></span>
  </button>

  <nav class="meny" aria-label="Hovedmeny">
    {meny(aktiv_meny)}
  </nav>
</header>

<div class="mobilmeny" id="mobilmeny" inert>
  <nav aria-label="Meny">
    {mobilmeny(aktiv_meny)}
  </nav>
  <div class="meny-bunn">
    <a href="/kontakt/">Kontakt</a>
    <a href="mailto:post@mirada.no">post@mirada.no</a>
  </div>
</div>
{kapitler_html}
<main id="innhold">
{innhold}
</main>

<footer class="lyst">
  <div class="bunn">
    <div>
      <a class="merke" href="/" style="margin-bottom:26px">
        {MONOGRAM}
        <span class="merke-navn">Mirada Nova</span>
      </a>
      <p style="max-width:32ch;font-size:14px">Kunst- og kulturforening i Drammen. Fotografi, film, bevegelse og levende kulturarv.</p>
    </div>

    <div>
      <h5>Shujah Malik</h5>
      <ul>
        <li><a href="/fotograf/">Fotografen</a></li>
        <li><a href="/fotograf/cv/">CV</a></li>
        <li><a href="/fotograf/film/">Film</a></li>
        <li><a href="/fotograf/oppdrag/">Oppdrag</a></li>
      </ul>
    </div>

    <div>
      <h5>Utforsk</h5>
      <ul>
        <li><a href="/prosjekter/">Prosjekter</a></li>
        <li><a href="/verk/">Verk</a></li>
        <li><a href="/delta/">Delta</a></li>
        <li><a href="/om/">Om Mirada Nova</a></li>
      </ul>
    </div>

    <div>
      <h5>Kontakt</h5>
      <ul>
        <li><a href="mailto:post@mirada.no">post@mirada.no</a></li>
        <li><a href="/kontakt/">Kontaktside</a></li>
        <li><a href="/delta/modell/">Modell</a></li>
      </ul>
    </div>
  </div>

  <div class="bunn-strek">
    <small>&copy; <span class="js-aar">2026</span> Mirada Nova Kunst- og kulturforening</small>
    <small>Fotografi &copy; <span class="js-aar">2026</span> Shujah Malik — alle rettigheter forbeholdt</small>
  </div>
</footer>

<script src="/assets/js/mirada.js"></script>
</body>
</html>
'''


def videresend(til, forklaring):
    return f'''<!DOCTYPE html>
<html lang="nb">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={til}">
<title>Flyttet — Mirada Nova</title>
<link rel="canonical" href="https://mirada.no{til}">
<meta name="robots" content="noindex, follow">
<script>location.replace('{til}');</script>
<style>body{{background:#0B0B0D;color:#F4F1EB;font-family:system-ui,sans-serif;display:flex;
align-items:center;justify-content:center;min-height:100vh;margin:0;font-size:15px;
padding:20px;text-align:center;line-height:1.7}}a{{color:#C7A86D}}</style>
</head>
<body><p>{forklaring}<br><a href="{til}">Gå videre &rarr;</a></p></body>
</html>
'''
