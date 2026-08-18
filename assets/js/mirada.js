/* ============================================================
   MIRADA NOVA — felles skript
   Rolige innfaringer, bildelasting, meny, lightbox, skjema.
   Ingen rammeverk, ingen sporing.
   ============================================================ */
(function(){
  'use strict';

  var rolig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- sidefading inn ---------- */
  function vis(){ document.body.classList.add('klar'); }
  if(document.readyState === 'complete' || document.readyState === 'interactive'){
    requestAnimationFrame(vis);
  } else {
    document.addEventListener('DOMContentLoaded', function(){ requestAnimationFrame(vis); });
  }
  window.addEventListener('pageshow', function(){ document.body.classList.remove('forlater'); vis(); });

  /* ---------- webp ---------- */
  var støtterWebp = (function(){
    try{ return document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp')===0; }
    catch(e){ return false; }
  })();

  function sti(slug, ønsket){
    if(!støtterWebp) return '/assets/foto/' + slug + '-1600.jpg';
    return '/assets/foto/' + slug + '-' + ønsket + '.webp';
  }
  /* om en størrelse mangler (f.eks. 2400 av et smalt bilde), faller vi til 1600 */
  function reserve(slug){
    return støtterWebp ? '/assets/foto/' + slug + '-1600.webp' : '/assets/foto/' + slug + '-1600.jpg';
  }
  function størrelse(bredde){
    var b = bredde * (window.devicePixelRatio > 1.5 ? 1.5 : 1);
    return b > 1650 ? 2400 : (b > 1000 ? 1600 : 1000);
  }

  /* ---------- last bilder rolig inn ---------- */
  function last(fig){
    if(fig.dataset.lastet) return;
    fig.dataset.lastet = '1';
    var slug = fig.dataset.bilde;
    var bredde = fig.getBoundingClientRect().width || window.innerWidth;
    if(fig.classList.contains('foto-full') || fig.classList.contains('hero-media')) bredde = window.innerWidth;
    var url = sti(slug, størrelse(bredde));

    var f = fig.querySelector('.flate') || fig;
    var mal = fig.classList.contains('foto') ? fig : (fig.querySelector('.foto') || fig);
    var i = new Image();
    i.onload  = function(){ f.style.backgroundImage = 'url("'+url+'")'; mal.classList.add('lastet'); };
    i.onerror = function(){ f.style.backgroundImage = 'url("'+reserve(slug)+'")'; mal.classList.add('lastet'); };
    i.src = url;
  }

  var foto     = [].slice.call(document.querySelectorAll('[data-bilde]'));
  var animerte = [].slice.call(document.querySelectorAll('.opp'));

  if('IntersectionObserver' in window){
    var obsFoto = new IntersectionObserver(function(rader){
      rader.forEach(function(r){ if(r.isIntersecting){ last(r.target); obsFoto.unobserve(r.target); } });
    }, {rootMargin:'500px 0px'});
    foto.forEach(function(f){ obsFoto.observe(f); });

    var obsOpp = new IntersectionObserver(function(rader){
      rader.forEach(function(r){ if(r.isIntersecting){ r.target.classList.add('inne'); obsOpp.unobserve(r.target); } });
    }, {threshold:.10, rootMargin:'0px 0px -7% 0px'});
    animerte.forEach(function(e){ obsOpp.observe(e); });
  } else {
    foto.forEach(last);
    animerte.forEach(function(e){ e.classList.add('inne'); });
  }

  /* ---------- navigasjon ---------- */
  var nav = document.getElementById('nav');
  var knapp = document.getElementById('meny-knapp');
  var meny = document.getElementById('mobilmeny');

  /* hårtynn lesestrek øverst */
  var strek = document.createElement('div');
  strek.className = 'lesestrek';
  document.body.appendChild(strek);

  /* navigasjonen snur farge når den står over et lyst rom */
  var lyseRom = [].slice.call(document.querySelectorAll('.lyst'));
  function navFarge(){
    if(!nav || !lyseRom.length) return;
    var y = (nav.offsetHeight || 82) * 0.55;
    var over = lyseRom.some(function(s){
      var r = s.getBoundingClientRect();
      return r.top <= y && r.bottom >= y;
    });
    nav.classList.toggle('pa-lyst', over);
  }

  if(nav){
    var sist = 0;
    var venterNav = false;
    var oppdater = function(){
      var y = pageYOffset;
      nav.classList.toggle('festet', y > 60);
      nav.classList.toggle('skjult', y > 560 && y > sist && !(meny && meny.classList.contains('apen')));
      sist = y;
      navFarge();
      var h = document.documentElement.scrollHeight - innerHeight;
      strek.style.transform = 'scaleX(' + (h > 0 ? Math.min(y / h, 1) : 0) + ')';
      strek.classList.toggle('pa', y > 60);
    };
    addEventListener('scroll', function(){
      if(venterNav) return;
      venterNav = true;
      requestAnimationFrame(function(){ oppdater(); venterNav = false; });
    }, {passive:true});
    addEventListener('resize', navFarge, {passive:true});
    oppdater();
  }

  if(knapp && meny){
    var settMeny = function(apen){
      meny.classList.toggle('apen', apen);
      knapp.setAttribute('aria-expanded', apen);
      if(apen){ meny.removeAttribute('inert'); } else { meny.setAttribute('inert',''); }
      if(nav) nav.classList.toggle('meny-apen', apen);
      document.body.style.overflow = apen ? 'hidden' : '';
    };
    knapp.addEventListener('click', function(){ settMeny(!meny.classList.contains('apen')); });
    meny.addEventListener('click', function(e){ if(e.target.tagName === 'A') settMeny(false); });
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape' && meny.classList.contains('apen')) settMeny(false);
    });
  }

  /* ---------- elegante sideoverganger ---------- */
  if(!rolig){
    document.addEventListener('click', function(e){
      var a = e.target.closest && e.target.closest('a');
      if(!a) return;
      if(e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      if(a.target && a.target !== '_self') return;
      if(a.hasAttribute('download')) return;
      var href = a.getAttribute('href') || '';
      if(!href || href.charAt(0) === '#' || /^(mailto:|tel:|https?:\/\/)/i.test(href) && a.host !== location.host) return;
      if(a.host !== location.host) return;
      if(a.pathname === location.pathname && a.hash) return;
      e.preventDefault();
      document.body.classList.add('forlater');
      setTimeout(function(){ location.href = a.href; }, 300);
    });
  }

  /* ---------- årstall ---------- */
  var år = new Date().getFullYear();
  [].forEach.call(document.querySelectorAll('.js-aar'), function(e){ e.textContent = år; });

  /* ---------- vern av fotografiene ---------- */
  document.addEventListener('contextmenu', function(e){
    if(e.target.closest('.foto') || e.target.closest('.lys') || e.target.tagName === 'IMG'){ e.preventDefault(); }
  });
  document.addEventListener('dragstart', function(e){
    if(e.target.closest('.foto') || e.target.closest('.lys') || e.target.tagName === 'IMG'){ e.preventDefault(); }
  });

  /* ---------- hero-video (når den finnes) ---------- */
  var vid = document.getElementById('hero-video');
  if(vid && !rolig){
    fetch('/assets/video/hero.mp4', {method:'HEAD'}).then(function(r){
      if(!r.ok) return;
      vid.src = '/assets/video/hero.mp4';
      vid.load();
      vid.addEventListener('canplay', function(){ vid.classList.add('klar'); vid.play().catch(function(){}); });
    }).catch(function(){});
  }

  /* ---------- behersket parallakse på full-bleed ---------- */
  var para = [].slice.call(document.querySelectorAll('.parallakse'));
  if(para.length && !rolig && window.innerWidth > 900){
    var venter = false;
    addEventListener('scroll', function(){
      if(venter) return;
      venter = true;
      requestAnimationFrame(function(){
        para.forEach(function(p){
          var r = p.getBoundingClientRect();
          if(r.bottom < -200 || r.top > innerHeight + 200) return;
          var midt = (r.top + r.height/2 - innerHeight/2) / innerHeight;
          var f = p.querySelector('.flate');
          if(f) f.style.transform = 'scale(1.08) translate3d(0,' + (midt * -22).toFixed(2) + 'px,0)';
        });
        venter = false;
      });
    }, {passive:true});
  }

  /* ============================================================
     LIGHTBOX
     ============================================================ */
  var galleri = document.getElementById('galleri');
  if(galleri){
    var poster = [].slice.call(galleri.querySelectorAll('.galleri-post'));
    var lys      = document.getElementById('lys');
    var lysFlate = lys.querySelector('.lys-flate');
    var lysNavn  = lys.querySelector('.lys-tekst .navn');
    var lysSted  = lys.querySelector('.lys-tekst .sted');
    var teller   = lys.querySelector('.lys-teller');
    var n = 0, forrigeFokus = null;

    function bildeUrl(el){
      var b = Math.max(window.innerWidth, window.innerHeight);
      return sti(el.dataset.bilde, b > 1400 ? 2400 : 1600);
    }

    function tegn(i){
      n = (i + poster.length) % poster.length;
      var el = poster[n];
      lysFlate.classList.remove('synlig');
      lysNavn.textContent = el.dataset.tittel || '';
      lysSted.textContent = el.dataset.sted || '';
      teller.textContent = String(n+1).padStart(2,'0') + ' / ' + String(poster.length).padStart(2,'0');

      var url = bildeUrl(el);
      var i2 = new Image();
      i2.onload = function(){
        lysFlate.style.backgroundImage = 'url("'+url+'")';
        requestAnimationFrame(function(){ lysFlate.classList.add('synlig'); });
      };
      i2.onerror = function(){
        lysFlate.style.backgroundImage = 'url("'+reserve(el.dataset.bilde)+'")';
        lysFlate.classList.add('synlig');
      };
      i2.src = url;

      /* forhåndslast naboene */
      [poster[(n+1)%poster.length], poster[(n-1+poster.length)%poster.length]].forEach(function(p){
        if(p) (new Image()).src = bildeUrl(p);
      });
    }

    function apne(i){
      forrigeFokus = document.activeElement;
      lys.classList.add('pa');
      document.body.style.overflow = 'hidden';
      requestAnimationFrame(function(){ lys.classList.add('inne'); });
      tegn(i);
      lys.querySelector('.lys-lukk').focus();
    }
    function lukk(){
      lys.classList.remove('inne');
      setTimeout(function(){
        lys.classList.remove('pa');
        lysFlate.classList.remove('synlig');
        document.body.style.overflow = '';
        if(forrigeFokus) forrigeFokus.focus();
      }, 420);
    }

    poster.forEach(function(p, i){ p.addEventListener('click', function(){ apne(i); }); });
    lys.querySelector('.lys-lukk').addEventListener('click', lukk);
    lys.querySelector('.lys-forrige').addEventListener('click', function(){ tegn(n-1); });
    lys.querySelector('.lys-neste').addEventListener('click', function(){ tegn(n+1); });
    lys.addEventListener('click', function(e){
      if(e.target === lys || e.target === lysFlate) lukk();
    });
    document.addEventListener('keydown', function(e){
      if(!lys.classList.contains('pa')) return;
      if(e.key === 'Escape') lukk();
      else if(e.key === 'ArrowRight') tegn(n+1);
      else if(e.key === 'ArrowLeft') tegn(n-1);
    });

    /* sveip på berøring */
    var x0 = null;
    lys.addEventListener('touchstart', function(e){ x0 = e.changedTouches[0].clientX; }, {passive:true});
    lys.addEventListener('touchend', function(e){
      if(x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if(Math.abs(dx) > 55) tegn(dx < 0 ? n+1 : n-1);
      x0 = null;
    }, {passive:true});
  }

  /* ============================================================
     SKJEMA
     ============================================================ */
  [].forEach.call(document.querySelectorAll('.valg label'), function(l){
    var i = l.querySelector('input');
    if(!i) return;
    l.classList.toggle('valgt', i.checked);
    i.addEventListener('change', function(){ l.classList.toggle('valgt', i.checked); });
  });

  /* Generisk skjemamotor. Alle skjema med data-skjema håndteres likt:
     validering ut fra required-attributtene, mailto-reserve så lenge
     Formspree ikke er koblet på, og rolige statusmeldinger. */
  [].forEach.call(document.querySelectorAll('form[data-skjema]'), function(form){
    var send = form.querySelector('[type=submit]');
    var ut   = form.querySelector('.melding');
    var opprinneligTekst = send && send.querySelector('span') ? send.querySelector('span').textContent : 'Send';

    function si(type, html){
      if(!ut) return;
      ut.className = 'melding vis' + (type === 'feil' ? ' feil' : '');
      ut.innerHTML = html;
      ut.scrollIntoView({block:'nearest', behavior: rolig ? 'auto' : 'smooth'});
    }

    function finnFeil(){
      var felt = [].slice.call(form.querySelectorAll('[required]'));
      for(var i = 0; i < felt.length; i++){
        var f = felt[i];
        var melding = f.getAttribute('data-feil') || 'Dette feltet må fylles ut.';
        if(f.type === 'checkbox' || f.type === 'radio'){
          var gruppe = form.querySelectorAll('[name="' + f.name + '"]');
          var kryss = [].some.call(gruppe, function(g){ return g.checked; });
          if(!kryss) return {felt:f, melding:melding};
        } else if(f.type === 'email'){
          if(!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(f.value)) return {felt:f, melding:melding};
        } else if(!String(f.value).trim()){
          return {felt:f, melding:melding};
        }
      }
      return null;
    }

    form.addEventListener('submit', function(e){
      e.preventDefault();

      var feil = finnFeil();
      if(feil){
        try{ feil.felt.focus({preventScroll:true}); }catch(err){}
        return si('feil', feil.melding);
      }

      /* Midlertidig: ingen skjematjeneste koblet på ennå — sendes som e-post.
         Når Formspree er satt opp, byttes DITT_FORM_ID i form-action, og denne grenen kjører aldri. */
      if(form.action.indexOf('DITT_FORM_ID') !== -1){
        var d = new FormData(form), samlet = {};
        d.forEach(function(v,k){
          if(k.charAt(0) === '_' || !String(v).trim()) return;
          (samlet[k] = samlet[k] || []).push(v);
        });
        var linjer = Object.keys(samlet).map(function(k){ return k + ': ' + samlet[k].join(', '); });
        var mottaker = ['malikdilnawaz20','gmail.com'].join('@');
        var emne = form.dataset.skjema || 'Melding fra mirada.no';
        location.href = 'mailto:' + mottaker
          + '?subject=' + encodeURIComponent(emne)
          + '&body='    + encodeURIComponent(emne + '\n(sendt fra mirada.no)\n\n' + linjer.join('\n'));
        return si('ok','<strong>E-postprogrammet ditt åpnes nå</strong> med opplysningene ferdig utfylt — trykk send, så er den levert.<br>Skjer ingenting? Send opplysningene til <a href="mailto:'+mottaker+'">'+mottaker+'</a>.');
      }

      if(send){ send.disabled = true; if(send.querySelector('span')) send.querySelector('span').textContent = 'Sender'; }

      fetch(form.action, {method:'POST', body:new FormData(form), headers:{Accept:'application/json'}})
        .then(function(r){
          if(!r.ok) throw 0;
          form.style.display = 'none';
          si('ok', form.dataset.takk || '<strong>Takk — meldingen er sendt.</strong>');
        })
        .catch(function(){
          if(send){ send.disabled = false; if(send.querySelector('span')) send.querySelector('span').textContent = opprinneligTekst; }
          si('feil','Noe gikk galt. Send gjerne en e-post til <a href="mailto:post@mirada.no">post@mirada.no</a> i stedet.');
        });
    });
  });

})();
