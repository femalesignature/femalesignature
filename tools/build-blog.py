#!/usr/bin/env python3
"""Blog: Übersicht und Artikel DE/EN im Stil der Startseite.

    python3 tools/images.py && python3 tools/build-blog.py

Inhalte liegen in tools/blog/<slug>.html: oben ein JSON-Kopf im Kommentar
(Titel, Beschreibung, Kategorie, Datum, Bild, Tags, Abschluss-Text), darunter der Artikeltext.
Englische Fassungen enden auf -en. Die HTML-Dateien in blog/ entstehen hier, nie von Hand ändern.
Kopf, Footer, Schriften, Farben und Knöpfe kommen aus build-home.py, damit beides gleich bleibt.
"""
import datetime
import importlib.util
import json
import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("home", ROOT / "tools" / "build-home.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)
esc, SITE, CAL, WA, MAIL, TEL, TEL_TXT, IG, LI = H.esc, H.SITE, H.CAL, H.WA, H.MAIL, H.TEL, H.TEL_TXT, H.IG, H.LI
ICON_ARROW, ICON_IG, ICON_LI, ICON_WA = H.ICON_ARROW, H.ICON_IG, H.ICON_LI, H.ICON_WA
TODAY = "2026-11-11"
AUTHOR = "Mag. (FH) Mediha Mujcin"


def css_part(start, end=None):
    a = H.CSS.index(start)
    return H.CSS[a:H.CSS.index(end, a) if end else None]


# Grundlage, Kopf, Karten, Abschluss-Bild, Footer und Erscheinen wörtlich von der Startseite
BASE_CSS = (css_part("@font-face", "/* Hero:") + css_part("/* Abschnitte im Vosello", "/* Herausforderungen")
            + css_part("/* Schreibeffekt", "/* Ansatz:") + css_part("/* Abschluss:", "/* Kontakt:")
            + css_part("/* Scroll-Effekte", "/* Schwebende") + css_part("/* Sanftes Einblenden"))

CSS = BASE_CSS + H.CONSENT_CSS + r"""
/* Blog */
.hd:not(.sc){background:var(--ow)}
.nav a[aria-current]{background:var(--ow);font-weight:600}
.crumb{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;font-size:.8125rem;color:var(--mu)}
.crumb a{display:inline-flex;align-items:center;min-height:44px;text-decoration:none;color:var(--ink);font-weight:500}
.crumb a:hover{color:var(--fr)}
.crumb span[aria-hidden]{color:#bdb5aa}
.meta{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;font-size:.8125rem;color:var(--mu)}
.meta .dot{width:3px;height:3px;border-radius:50%;background:#bdb5aa}
.pill.fr{background:var(--fr);color:#fff}

/* Übersicht: Kopf mit großem Wort, Themen-Filter */
.bh{padding:clamp(120px,14vw,168px) 0 clamp(40px,5vw,64px)}
.bh .wrap{display:grid;gap:clamp(28px,4vw,48px)}
.bh h1{font-size:clamp(2.5rem,1.3rem + 5.4vw,6rem);line-height:.98;font-weight:500;letter-spacing:-.05em;max-width:14ch;text-wrap:balance}
.bh h1 em{letter-spacing:-.02em}
.bh .lead{margin-top:0;max-width:46ch}
.bh .side{display:flex;flex-direction:column;gap:22px;justify-content:flex-end}
.count{display:flex;gap:clamp(24px,3vw,40px);border-top:1px solid #d9d2c7;padding-top:18px}
.count b{display:block;font-size:clamp(1.75rem,1.3rem + 1.4vw,2.5rem);font-weight:500;letter-spacing:-.04em;line-height:1}
.count span{display:block;margin-top:8px;font-size:.75rem;color:var(--mu)}
@media (min-width:900px){.bh .wrap{grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);align-items:end}}
.flt{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;margin:0 calc(var(--pad)*-1);padding:4px var(--pad) 8px;scroll-padding-inline:var(--pad)}
.flt::-webkit-scrollbar{display:none}
.flt button{flex:none;display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:10px 18px;border-radius:999px;border:1px solid #d6cfc4;background:transparent;font:inherit;font-size:.875rem;font-weight:500;color:var(--ink);cursor:pointer;transition:background-color .3s var(--ease),color .3s,border-color .3s}
.flt button:hover{border-color:var(--ink)}
.flt button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:#fff}
.flt sup{font-size:.6875rem;font-weight:600;opacity:.6;vertical-align:baseline}
@media (min-width:1000px){.flt{flex-wrap:wrap;overflow:visible;margin:0;padding:4px 0 0}}

/* Hauptartikel: Bild links, Titel groß rechts */
.top{display:grid;gap:clamp(24px,4vw,64px);align-items:center;text-decoration:none;padding:clamp(10px,1.2vw,14px)}
.top .shot{aspect-ratio:4/3}
.top .txt{padding:clamp(4px,1vw,12px) clamp(8px,2vw,32px) clamp(16px,2vw,24px)}
.top h2{hyphens:auto;-webkit-hyphens:auto;hyphenate-limit-chars:12 5 5;font-size:clamp(1.625rem,1rem + 2vw,2.75rem);line-height:1.04;font-weight:500;letter-spacing:-.04em;margin:18px 0 0;text-wrap:balance;transition:color .4s var(--ease)}
.top p.x{color:var(--mu);margin-top:16px;max-width:46ch}
.top .meta{margin-top:16px}
.go{display:inline-flex;align-items:center;gap:10px;margin-top:24px;min-height:44px;font-size:.9375rem;font-weight:600;color:var(--ink)}
.go .ic{transition:transform .4s var(--ease)}
a:hover .go .ic{transform:translateX(5px)}
.top:hover h2{color:var(--fr)}
@media (min-width:900px){.top{grid-template-columns:minmax(0,1.1fr) minmax(0,1fr)}}

/* Alle Artikel als Register: Nummer, Titel, Thema; am Rechner folgt ein Bild dem Mauszeiger */
.idx{border-top:1px solid #d9d2c7}
.idx li{border-bottom:1px solid #d9d2c7}
.idx li[hidden]{display:none}
.row{display:grid;grid-template-columns:auto minmax(0,1fr) 88px;gap:6px 18px;align-items:center;padding:clamp(20px,2.6vw,32px) 0;text-decoration:none;color:var(--ink);position:relative}
.row .n{font-size:.75rem;font-weight:600;letter-spacing:.14em;color:var(--fr);align-self:start;padding-top:.5em}
.row h3{font-size:clamp(1.1875rem,.95rem + 1.1vw,2rem);line-height:1.15;font-weight:500;letter-spacing:-.03em;text-wrap:balance;transition:color .4s var(--ease),transform .5s var(--ease)}
.row .meta{grid-column:2;margin-top:6px}
.row .th{grid-row:1 / span 2;grid-column:3;width:88px;aspect-ratio:1;border-radius:12px;overflow:hidden;background:#e6e0d6}
.row .th img{width:100%;height:100%;object-fit:cover}
.row .ar{display:none}
.row:hover h3{color:var(--fr)}
@media (min-width:900px){
.row{grid-template-columns:72px minmax(0,1fr) 220px 56px;gap:0 24px}
.row .meta{grid-column:3;grid-row:1;margin:0;flex-direction:column;align-items:flex-start;gap:4px}
.row .meta .dot{display:none}
.row .th{display:none}
.row .ar{display:inline-flex;grid-column:4;width:52px;height:52px;border-radius:50%;border:1px solid #d6cfc4;align-items:center;justify-content:center;transition:background-color .4s var(--ease),border-color .4s,color .4s,transform .5s var(--ease)}
.row:hover .ar{background:var(--ink);border-color:var(--ink);color:#fff;transform:rotate(-45deg)}
.row:hover h3{transform:translateX(10px)}
}
.empty{padding:32px 0;color:var(--mu)}
.peek{position:fixed;left:0;top:0;z-index:30;width:300px;aspect-ratio:4/3;border-radius:16px;overflow:hidden;pointer-events:none;opacity:0;scale:.85;transition:opacity .35s var(--ease),scale .45s var(--ease);box-shadow:0 34px 60px -28px rgba(40,22,22,.55)}
.peek.on{opacity:1;scale:1}
.peek img{width:100%;height:100%;object-fit:cover}
@media (hover:none),(max-width:899px),(prefers-reduced-motion:reduce){.peek{display:none}}

/* Artikel: Lesefortschritt oben */
.prog{position:fixed;inset:0 0 auto;z-index:60;height:3px;background:var(--fr);transform-origin:0 50%;transform:scaleX(var(--p,0))}
@supports (animation-timeline:scroll()){.prog{animation:prg linear both;animation-timeline:scroll(root)}@keyframes prg{from{transform:scaleX(0)}to{transform:scaleX(1)}}}
@media (prefers-reduced-motion:reduce){.prog{display:none}}

/* Artikel-Kopf */
.ah{padding:clamp(112px,13vw,152px) 0 clamp(32px,4vw,48px)}
.ah .wrap{max-width:1080px}
.ah .label{margin:18px 0 0}
.ah h1{hyphens:auto;-webkit-hyphens:auto;hyphenate-limit-chars:12 5 5;font-size:clamp(2.125rem,1.2rem + 3.6vw,4.25rem);line-height:1.04;font-weight:500;letter-spacing:-.045em;max-width:20ch;text-wrap:balance}
.ah .lead{max-width:56ch;margin-top:24px}
.simple{min-height:72vh;min-height:72svh;display:flex;align-items:center}.simple h1 em{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--fr)}.simple .acts{display:flex;flex-wrap:wrap;gap:12px;margin-top:36px}
.by{display:flex;flex-wrap:wrap;align-items:center;gap:14px 28px;margin-top:clamp(28px,4vw,40px);padding-top:24px;border-top:1px solid #d9d2c7}
.by .who{display:flex;align-items:center;gap:12px;font-size:.9375rem}
.by .who img{width:48px;height:48px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 2px var(--ow),0 0 0 3px var(--fr)}
.by .who span{display:block;font-size:.8125rem;color:var(--mu)}
.cover{padding:0 clamp(8px,1.4vw,20px)}
.cover .shot{max-width:1400px;margin:0 auto;aspect-ratio:16/9;border-radius:clamp(16px,2vw,28px)}
@media (max-width:699px){.cover .shot{aspect-ratio:4/3}}
@media (prefers-reduced-motion:no-preference){@supports (animation-timeline:view()){
.cover .shot{animation:cvx linear both;animation-timeline:view();animation-range:entry 0% cover 50%}
@keyframes cvx{from{clip-path:inset(0 6% round 40px)}to{clip-path:inset(0 0 round 20px)}}
}}

/* Artikel-Text mit Inhaltsverzeichnis daneben */
.body{padding:clamp(48px,7vw,96px) 0 clamp(56px,8vw,112px)}
.body .wrap{display:grid;grid-template-columns:minmax(0,1fr);gap:32px;max-width:1080px}
@media (min-width:1000px){.body .wrap{grid-template-columns:220px minmax(0,1fr);gap:72px}}
.toc{font-size:.875rem}
.toc ol{list-style:none;padding:0;margin:0;counter-reset:t}
.toc a{display:flex;gap:12px;align-items:baseline;min-height:44px;padding:10px 0;text-decoration:none;color:var(--mu);border-top:1px solid #e2dbd0;line-height:1.4;transition:color .3s}
.toc a::before{counter-increment:t;content:counter(t,decimal-leading-zero);font-size:.6875rem;font-weight:600;letter-spacing:.1em;color:#a69d92;transition:color .3s}
.toc a:hover,.toc a.on{color:var(--ink)}
.toc a.on::before{color:var(--fr)}
.toc details{background:var(--card);border-radius:16px;padding:0 18px;border:1px solid var(--bd)}
.toc summary{display:flex;align-items:center;justify-content:space-between;min-height:56px;cursor:pointer;list-style:none;font-weight:600}
.toc summary::-webkit-details-marker{display:none}
.toc summary::after{content:"+";font-size:1.375rem;font-weight:400;color:var(--fr);transition:transform .4s var(--ease)}
.toc details[open] summary::after{transform:rotate(45deg)}
.toc details ol{padding-bottom:8px}
.toc .tt,.toc .tw{display:none}
@media (min-width:1000px){
.toc>div{position:sticky;top:112px}
.toc details{display:none}
.toc .tw{display:block}
.toc .tt{display:block;font-size:.75rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--fr);margin-bottom:12px}
.toc a{border-top:0;border-left:2px solid #e2dbd0;padding:8px 0 8px 16px;min-height:44px;align-items:center}
.toc a.on{border-color:var(--fr)}
}
.prose{max-width:68ch;font-size:1.0625rem;line-height:1.8;color:#3a3633}
@media (min-width:900px){.prose{font-size:1.125rem}}
.prose>*+*{margin-top:1.15em}
.prose>p:first-child{font-size:clamp(1.1875rem,1.05rem + .5vw,1.4375rem);line-height:1.6;color:var(--ink);letter-spacing:-.01em}
.prose h2{counter-increment:h;font-size:clamp(1.5rem,1.15rem + 1.3vw,2.25rem);line-height:1.15;font-weight:500;letter-spacing:-.035em;color:var(--ink);margin-top:2.2em;scroll-margin-top:104px;text-wrap:balance}
.prose h2::before{content:counter(h,decimal-leading-zero);display:block;margin-bottom:14px;font-size:.75rem;font-weight:600;letter-spacing:.16em;color:var(--fr)}
.prose{counter-reset:h}
.legal .prose h2::before{display:none}
.legal .prose>p:first-child{font-size:inherit;line-height:inherit;color:inherit;letter-spacing:0}
.legal .prose h2{margin-top:1.8em}
.prose h3{font-size:clamp(1.1875rem,1.05rem + .5vw,1.375rem);line-height:1.3;font-weight:600;letter-spacing:-.02em;color:var(--ink);margin-top:1.8em}
.prose strong{color:var(--ink);font-weight:600}
.prose a{color:var(--fr);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}
.prose a:hover{text-decoration-thickness:2px}
.prose ul{display:grid;gap:12px}
.prose ul li{position:relative;padding-left:26px}
.prose ul li::before{content:"";position:absolute;left:2px;top:.72em;width:8px;height:8px;border-radius:50%;background:var(--fr)}
.prose ol{list-style:none;padding:0;display:grid;gap:12px;counter-reset:o}
.prose ol li{counter-increment:o;position:relative;padding:20px 22px 20px 72px;background:var(--card);border:1px solid var(--bd);border-radius:16px}
.prose ol li::before{content:counter(o,decimal-leading-zero);position:absolute;left:22px;top:18px;font-family:var(--serif);font-style:italic;font-size:1.5rem;line-height:1.2;color:var(--fr)}
.prose blockquote{margin:2em 0;padding:clamp(28px,4vw,44px) 0;border-top:1px solid #d9d2c7;border-bottom:1px solid #d9d2c7;font-family:var(--serif);font-style:italic;font-size:clamp(1.5rem,1.15rem + 1.4vw,2.25rem);line-height:1.3;letter-spacing:-.01em;text-wrap:pretty}
.prose blockquote::before{content:"“";display:block;font-size:4rem;line-height:.5;margin-bottom:8px;color:var(--fr)}
.prose blockquote.wr{--wf:#9C948B;--wt:#5C1F2B;color:var(--wt)}
.prose p.src{font-size:.875rem;line-height:1.6;color:var(--mu);padding:16px 20px;background:var(--card);border-radius:12px;border:1px solid var(--bd)}
.prose p.src em{font-family:inherit;font-style:normal;color:inherit}
.keys{display:grid;gap:12px}
.prose .ad{font-size:.8125rem;color:var(--mu)}
.prose .fq{border-bottom:1px solid var(--bd)}
.prose .fq details{border-top:1px solid var(--bd)}
.prose .fq summary{list-style:none;display:flex;justify-content:space-between;align-items:center;gap:16px;min-height:64px;padding:16px 0;cursor:pointer;font-weight:600;color:var(--ink)}
.prose .fq summary::-webkit-details-marker{display:none}
.prose .fq summary::after{content:"+";flex:none;width:36px;height:36px;border-radius:50%;border:1px solid var(--bd);display:grid;place-items:center;font-weight:400;font-size:1.25rem;line-height:1;color:var(--fr);transition:transform .3s}
.prose .fq details[open] summary::after{transform:rotate(45deg)}
.prose .fq details p{margin:0 0 20px}
@media (min-width:640px){.keys{grid-template-columns:repeat(2,minmax(0,1fr))}}
.prose .keys li{padding:22px;background:var(--card);border:1px solid var(--bd);border-radius:16px}
.prose .keys li::before{display:none}
.keys strong{display:block;font-size:1rem;line-height:1.35;margin-bottom:6px}
.keys span{display:block;font-size:.9375rem;line-height:1.6;color:var(--mu)}

/* Nach dem Text: Schlagwörter, Teilen, Autorin */
.after{max-width:68ch;margin-top:clamp(40px,6vw,64px);display:grid;gap:28px}
.tags{display:flex;flex-wrap:wrap;gap:8px}
.tags li{display:inline-flex;align-items:center;min-height:32px;padding:4px 14px;border-radius:999px;border:1px solid #d6cfc4;font-size:.8125rem;color:var(--mu)}
.share{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:20px 0;border-top:1px solid #d9d2c7;border-bottom:1px solid #d9d2c7}
.share>span{font-size:.75rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--fr);margin-right:6px}
.share a,.share button{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-width:44px;min-height:44px;padding:0 14px;border-radius:999px;border:1px solid #d6cfc4;background:transparent;font:inherit;font-size:.8125rem;font-weight:600;color:var(--ink);text-decoration:none;cursor:pointer;transition:border-color .3s,color .3s}
.share a:hover,.share button:hover{border-color:var(--fr);color:var(--fr)}
.share svg{width:18px;height:18px}
.share output{font-size:.8125rem;color:var(--fr)}
.auth{display:grid;grid-template-columns:72px minmax(0,1fr);gap:18px;align-items:start}
.auth img{width:72px;height:72px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 3px var(--ow),0 0 0 4px var(--fr)}
.auth small{display:block;font-size:.75rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--fr)}
.auth strong{display:block;font-size:1.125rem;font-weight:600;margin-top:4px}
.auth p{font-size:.9375rem;color:var(--mu);margin-top:8px}
.auth .link{margin-top:4px;font-size:.9375rem}

/* Abschluss im Artikel: Burgund-Karte */
.acta{background:var(--fr);color:var(--ow);border-radius:clamp(20px,2.4vw,32px);padding:clamp(36px,6vw,80px) clamp(24px,6vw,80px);display:grid;gap:28px;align-items:center;position:relative;overflow:hidden}
.acta::after{content:"“";position:absolute;right:-.06em;bottom:-.42em;font-family:var(--serif);font-style:italic;font-size:clamp(14rem,30vw,26rem);line-height:1;color:rgba(244,241,235,.06);pointer-events:none}
.acta .label{color:#E3C4CA;margin:0}.acta .label::before{background:#E3C4CA}
.acta h2{font-size:clamp(1.75rem,1.2rem + 2.2vw,3rem);line-height:1.08;font-weight:500;letter-spacing:-.035em;max-width:20ch;margin-top:16px;text-wrap:balance}
.acta p{color:rgba(244,241,235,.86);margin-top:16px;max-width:48ch}
.acta .btn{background:var(--ow);border-color:var(--ow);color:var(--ink);min-height:56px;position:relative;z-index:1}
.acta .btn:hover{background:#fff;border-color:#fff}
.acta .sig{display:flex;align-items:center;gap:12px;margin-top:24px;font-size:.875rem;color:rgba(244,241,235,.86)}
.acta .sig img{width:44px;height:44px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 2px var(--fr),0 0 0 3px #E3C4CA}
@media (min-width:900px){.acta{grid-template-columns:minmax(0,1fr) auto}}

/* Weiterlesen */
.more .head{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap}
.cards{display:grid;gap:clamp(28px,3vw,40px)}
@media (min-width:700px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){.cards{grid-template-columns:repeat(3,minmax(0,1fr))}}
.post{display:block;text-decoration:none}
.post .shot{aspect-ratio:4/3}
.post .meta{margin-top:18px}
.post h3{font-size:clamp(1.1875rem,1rem + .5vw,1.4375rem);line-height:1.22;font-weight:500;letter-spacing:-.025em;margin-top:10px;transition:color .4s var(--ease);text-wrap:balance}
.post:hover h3{color:var(--fr)}
"""

JS = r"""
(function(){
var d=document,hd=d.querySelector('.hd'),mb=d.querySelector('.mbtn'),mn=d.getElementById('mnav'),rm=matchMedia('(prefers-reduced-motion: reduce)');
function sc(){hd.classList.toggle('sc',scrollY>8)}addEventListener('scroll',sc,{passive:true});requestAnimationFrame(sc);
function closeNav(){mn.hidden=true;mb.setAttribute('aria-expanded','false');mb.setAttribute('aria-label',mb.dataset.open)}
mb.addEventListener('click',function(){var o=mn.hidden;mn.hidden=!o;mb.setAttribute('aria-expanded',String(o));mb.setAttribute('aria-label',o?mb.dataset.close:mb.dataset.open)});
mn.addEventListener('click',function(e){if(e.target.closest('a'))closeNav()});
d.addEventListener('keydown',function(e){if(e.key==='Escape'&&!mn.hidden){closeNav();mb.focus()}});
/* Einheitliches Erscheinen wie auf der Startseite */
if(d.documentElement.classList.contains('ani')){var AP='.sec .label,.sec .h2,.flt,.idx li,.prose>*,.after>*,.acta>*,.ctab>div>*,.ftg>*,.ftw,.fb',SM='.top,.post,.acta',seen=[];
d.querySelectorAll(AP+','+SM).forEach(function(e){if(e.getBoundingClientRect().top<innerHeight*.9)return;if(seen.indexOf(e)<0)seen.push(e)});
var aio=new IntersectionObserver(function(es){es.forEach(function(x){if(!x.isIntersecting)return;var e=x.target;aio.unobserve(e);e.classList.add('in');setTimeout(function(){e.classList.remove('ap','sm','in');e.style.removeProperty('--d')},1300+parseFloat(e.style.getPropertyValue('--d')||0)*1000)})},{threshold:.08,rootMargin:'0px 0px -4% 0px'});
var grp=new Map();seen.forEach(function(e){var p=e.parentElement,k=grp.get(p)||0;grp.set(p,k+1);e.classList.add('ap');if(e.matches(SM))e.classList.add('sm');e.style.setProperty('--d',Math.min(k*.07,.35).toFixed(2)+'s');aio.observe(e)})}
/* Lesefortschritt, falls der Browser es nicht per CSS kann */
var pg=d.querySelector('.prog');if(pg&&!CSS.supports('animation-timeline','scroll()')){var pt=0,pu=function(){pt=0;var h=d.documentElement.scrollHeight-innerHeight;pg.style.setProperty('--p',h>0?Math.min(1,scrollY/h).toFixed(4):0)};addEventListener('scroll',function(){if(!pt)pt=requestAnimationFrame(pu)},{passive:true});pu()}
/* Inhaltsverzeichnis: aktueller Abschnitt wird markiert */
var tl=[].slice.call(d.querySelectorAll('.toc a'));if(tl.length&&'IntersectionObserver'in window){var hs=tl.map(function(a){return d.getElementById(a.hash.slice(1))}),ton=function(i){tl.forEach(function(a,k){a.classList.toggle('on',k===i);if(k===i)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current')})};
var tio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)ton(hs.indexOf(e.target))})},{rootMargin:'-10% 0px -75% 0px'});hs.forEach(function(h){tio.observe(h)});
d.querySelectorAll('.toc details a').forEach(function(a){a.addEventListener('click',function(){a.closest('details').open=false})})}
/* Link kopieren */
var cp=d.getElementById('copy');if(cp)cp.addEventListener('click',function(){var o=d.getElementById('copied'),done=function(){o.textContent=cp.dataset.ok;setTimeout(function(){o.textContent=''},2500)};if(navigator.clipboard)navigator.clipboard.writeText(location.href.split('#')[0]).then(done,function(){});else done()});
/* Übersicht: nach Thema filtern */
var fb=[].slice.call(d.querySelectorAll('.flt button')),rows=[].slice.call(d.querySelectorAll('.idx li')),cnt=d.getElementById('cnt');
fb.forEach(function(b){b.addEventListener('click',function(){var c=b.dataset.c,n=0;fb.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});rows.forEach(function(r){var on=!c||r.dataset.c===c;r.hidden=!on;if(on){n++;if(!rm.matches){r.animate([{opacity:0,transform:'translateY(12px)'},{opacity:1,transform:'none'}],{duration:500,delay:Math.min(n*50,250),easing:'cubic-bezier(.16,1,.3,1)',fill:'backwards'})}}});if(cnt)cnt.textContent=cnt.dataset[n===1?'one':'many'].replace('#',n)})});
/* Übersicht: Vorschaubild folgt dem Mauszeiger */
var pk=d.querySelector('.peek');if(pk&&matchMedia('(hover:hover) and (min-width:900px)').matches&&!rm.matches){var pi=pk.querySelector('img'),x=0,y=0,tx=0,ty=0,run=0,loop=function(){x+=(tx-x)*.16;y+=(ty-y)*.16;pk.style.transform='translate('+(x+28)+'px,'+(y-110)+'px) rotate('+Math.max(-6,Math.min(6,(tx-x)*.05)).toFixed(2)+'deg)';run=pk.classList.contains('on')||Math.abs(tx-x)>.5?requestAnimationFrame(loop):0};
d.querySelectorAll('.row').forEach(function(r){r.addEventListener('pointerenter',function(e){pi.src=r.dataset.img;if(!pk.classList.contains('on')){x=tx=e.clientX;y=ty=e.clientY}pk.classList.add('on');if(!run)run=requestAnimationFrame(loop)});r.addEventListener('pointermove',function(e){tx=e.clientX;ty=e.clientY});r.addEventListener('pointerleave',function(){pk.classList.remove('on')})})}
})();
"""

UI = {
    "de": {
        "locale": "de_AT", "index": "/blog/", "home": "/", "blog": "Blog", "skip": "Zum Inhalt springen",
        "nav": [("/#systems", "Systeme"), ("/#approach", "Ansatz"), ("/#results", "Ergebnisse"), ("/blog/", "Blog")],
        "menu": "Menü", "close": "Schließen", "cta_short": "Strategie-Call", "cta": "Kostenfreien Strategie-Call buchen",
        "title": "Blog: Wissen, das Ihr Business weiterbringt | Female Signature", "desc": "Insights, Strategien und Inspiration für Unternehmerinnen: Partnerprogramme, Social Media, Branding und Performance Marketing.",
        "h1": ("Wissen, das Ihr Business", "weiterbringt."), "label": "Insights",
        "lead": "Insights, Strategien und Inspiration für Unternehmerinnen.",
        "n_posts": "Artikel", "n_topics": "Themen", "all": "Alle", "filter": "Nach Thema filtern",
        "count_one": "# Artikel", "count_many": "# Artikel", "latest": "Neuester Artikel", "all_h": "Alle Artikel",
        "read": "Weiterlesen", "min": "Min. Lesezeit", "faq_h": "Häufige Fragen", "upd": "aktualisiert am", "by": "von", "toc": "Inhalt", "toc_n": "Abschnitte",
        "share": "Teilen", "copy": "Link kopieren", "copied": "Link kopiert", "mail_sub": "Lesetipp von Female Signature",
        "author_k": "Über die Autorin", "role": "CEO & Founder · Female Signature", "about": "Mehr über Female Signature",
        "next_label": "Weiterlesen", "next_h": ("Mehr aus dem", "Blog."), "to_index": "Alle Artikel",
        "cta_label": "Kostenfreier Strategie-Call", "breadcrumb": "Brotkrumen-Navigation", "tags": "Schlagwörter",
        "lang_name": "Deutsch", "months": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
    },
    "en": {
        "locale": "en_GB", "index": "/blog/index-en", "home": "/en/", "blog": "Blog", "skip": "Skip to content",
        "nav": [("/en/#systems", "Systems"), ("/en/#approach", "Approach"), ("/en/#results", "Results"), ("/blog/index-en", "Blog")],
        "menu": "Menu", "close": "Close", "cta_short": "Strategy Call", "cta": "Book a Free Strategy Call",
        "title": "Blog: Knowledge that moves your business forward | Female Signature", "desc": "Insights, strategies, and inspiration for female entrepreneurs: partner programs, social media, branding, and performance marketing.",
        "h1": ("Knowledge that moves your business", "forward."), "label": "Insights",
        "lead": "Insights, strategies, and inspiration for entrepreneurs.",
        "n_posts": "Articles", "n_topics": "Topics", "all": "All", "filter": "Filter by topic",
        "count_one": "# article", "count_many": "# articles", "latest": "Latest article", "all_h": "All articles",
        "read": "Read more", "min": "min read", "faq_h": "Frequently asked questions", "upd": "updated", "by": "by", "toc": "Contents", "toc_n": "sections",
        "share": "Share", "copy": "Copy link", "copied": "Link copied", "mail_sub": "Reading tip from Female Signature",
        "author_k": "About the author", "role": "CEO & Founder · Female Signature", "about": "More about Female Signature",
        "next_label": "Keep reading", "next_h": ("More from the", "blog."), "to_index": "All articles",
        "cta_label": "Free strategy call", "breadcrumb": "Breadcrumb", "tags": "Tags",
        "lang_name": "English", "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    },
}


def load():
    posts = []
    for f in sorted((ROOT / "tools" / "blog").glob("*.html")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"<!--\s*(\{.*?\})\s*-->\s*(.*)$", raw, re.S)
        meta = json.loads(m[1])
        meta["slug"] = f.stem
        meta["body"] = m[2].strip()
        meta["pair"] = f.stem[:-3] if f.stem.endswith("-en") else f.stem + "-en"
        meta["n"] = int(meta["img"].split("-")[1])
        text = re.sub(r"<[^>]+>", " ", meta["body"])
        meta["mins"] = max(1, math.ceil(len(text.split()) / 200))
        posts.append(meta)
    # neueste zuerst; bei gleichem Datum die Reihenfolge der Startseite (Bildnummer)
    posts.sort(key=lambda p: (p["date"], -p["n"]), reverse=True)
    return posts


def fdate(iso, L):
    y, m, d = map(int, iso.split("-"))
    mon = UI[L]["months"][m - 1]
    return f"{d}. {mon} {y}" if L == "de" else f"{mon} {d}, {y}"


def url(p):
    return f"/blog/{p['slug']}"


def slugify(t):
    t = t.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def prose(body, L="de"):
    """Artikeltext aufbereiten: Anker an Zwischenüberschriften, Zitate mit Schreibeffekt,
    Aufzählungen der Form <p><strong>X</strong>: Text</p> als Kartenraster, Quellen klein."""
    toc = []

    def h2(m):
        inner = m[1]
        hid = slugify(re.sub(r"<[^>]+>", "", inner))
        toc.append((hid, re.sub(r"<[^>]+>", "", inner)))
        return f'<h2 id="{hid}">{inner}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", h2, body)

    def quote(m):
        t = m[1].strip()
        if "<" in t:
            return m[0]
        return f'<blockquote class="wr">{H.words(t, 10, 40)}</blockquote>'
    body = re.sub(r"<blockquote>(.*?)</blockquote>", quote, body, flags=re.S)

    def keys(m):
        items = re.findall(r"<p><strong>(.*?)</strong>:\s*(.*?)</p>", m[0])
        return '<ul class="keys">' + "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in items) + "</ul>"
    body = re.sub(r"(?:<p><strong>[^<]*</strong>:[^\n]*?</p>\s*){2,}", lambda m: keys(m) + "\n\n", body)
    body = re.sub(r"<p><em>((?:Quellen?|Sources?):.*?)</em></p>", r'<p class="src"><em>\1</em></p>', body, flags=re.S)
    # Partnerlink von impact.com ist ein Werbelink
    body = body.replace('href="https://goto.impact.com/', 'rel="sponsored noopener" data-x href="https://goto.impact.com/')
    body = re.sub(r'(rel="sponsored noopener" data-x href="[^"]*" target="_blank") rel="noopener"', r"\1", body).replace(" data-x", "")
    ad = "Werbelink" if L == "de" else "affiliate link"
    body = re.sub(r'(<a rel="sponsored[^>]*>.*?</a>)', r'\1 <span class="ad">(' + ad + ")</span>", body)
    return body, toc


def pic(name, sizes, ratio, ws, alt="", eager=False):
    w = ws[1]
    srcset = ", ".join(f"/images/opt/{name}-{x}.webp {x}w" for x in ws)
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="/images/opt/{name}-{w}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{round(w / ratio)}" '
            f'alt="{esc(alt)}" {load}>')


CARD_W, COVER_W = (480, 720, 960), (800, 1200, 1600)


def shell(L, title, desc, canon, alts, og_img, schema, main, other_url, extra_head="", og_type="website", current="Blog",
          robots="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"):
    U = UI[L]
    other = "en" if L == "de" else "de"
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if t == current else ""}>{esc(t)}</a>' for h, t in U["nav"])
    lang_link = f'<a class="lang" href="{other_url}" hreflang="{other}" lang="{other}" aria-label="{other.upper()}, {UI[other]["lang_name"]}">{other.upper()}</a>'
    alt_links = "".join(f'<link rel="alternate" hreflang="{k}" href="{SITE}{v}">\n' for k, v in alts)
    sys_names = [s[0] for s in (H.DE if L == "de" else H.EN)["systems"]]
    T = H.DE if L == "de" else H.EN
    sys_links = "".join(f'<a href="{U["home"]}#systems">{esc(s)}</a>' for s in sys_names)
    comp = [(U["home"] + "#about", "Über uns" if L == "de" else "About"), (U["home"] + "#results", "Ergebnisse" if L == "de" else "Results"), (U["index"], "Blog")]
    comp_links = "".join(f'<a href="{h}">{esc(t)}</a>' for h, t in comp)
    ld = json.dumps(schema, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!DOCTYPE html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<script>if('IntersectionObserver'in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('ani')</script>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{canon}">
{alt_links}<meta name="robots" content="{robots}">
<meta name="theme-color" content="#F4F1EB">
<meta name="author" content="{AUTHOR if og_type == "article" else "Female Signature"}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Female Signature">
<meta property="og:locale" content="{U["locale"]}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{canon}">
<meta property="og:image" content="{SITE}{og_img[0]}">
<meta property="og:image:width" content="{og_img[1]}">
<meta property="og:image:height" content="{og_img[2]}">
<meta property="og:image:alt" content="{esc(og_img[3] if len(og_img) > 3 else "Female Signature")}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{og_img[0]}">
<meta name="twitter:image:alt" content="{esc(og_img[3] if len(og_img) > 3 else "Female Signature")}">
{extra_head}<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/montserrat-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS.strip()}</style>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">{esc(U["skip"])}</a>
<header class="hd">
<div class="wrap">
<a class="logo" href="{U["home"]}" aria-label="Female Signature"><img src="/images/wordmark-primary-anthracite.svg" width="1475" height="115" alt="Female Signature"></a>
<nav class="nav" aria-label="{"Hauptnavigation" if L == "de" else "Main navigation"}">{nav}{lang_link}<a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(U["cta_short"])}</a></nav>
<button class="mbtn" type="button" aria-controls="mnav" aria-expanded="false" aria-label="{U["menu"]}" data-open="{U["menu"]}" data-close="{U["close"]}"><span></span></button>
</div>
</header>
<nav class="mnav" id="mnav" hidden aria-label="{"Mobile Navigation" if L == "de" else "Mobile navigation"}">{nav}{lang_link.replace('class="lang" ', '')}<a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(U["cta"])}</a></nav>
<main id="main">
{main}
</main>
<footer class="ft">
<div class="wrap">
<div class="ftg">
<div class="brand"><img src="/images/wordmark-primary-anthracite.svg" width="1475" height="115" alt="Female Signature" loading="lazy"><p>{esc(T["ft_text"])}</p><div class="soc"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a><a href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON_LI}</a></div></div>
<nav aria-labelledby="ft-sys"><h2 id="ft-sys">{esc(T["ft_sys"])}</h2>{sys_links}</nav>
<nav aria-labelledby="ft-co"><h2 id="ft-co">{esc(T["ft_company"])}</h2>{comp_links}</nav>
<div><h2>{esc(T["ft_contact"])}</h2><address style="font-style:normal"><nav aria-label="{esc(T["ft_contact"])}"><a href="mailto:{MAIL}">{MAIL}</a><a href="tel:{TEL}">{TEL_TXT}</a></nav><p style="margin-top:8px;color:var(--mu)">Aste 10, 6071 Aldrans, {"Österreich" if L == "de" else "Austria"}</p></address></div>
</div>
<p class="ftw" aria-hidden="true">Female <em>Signature</em></p>
<div class="fb"><p>© 2026 Female Signature</p><nav aria-label="{"Rechtliches" if L == "de" else "Legal"}"><a href="/impressum"{cur if current == "Impressum" else ""}>Impressum</a><a href="/datenschutz"{cur if current == "Datenschutz" else ""}>Datenschutz</a>{H.consent_link(L)}<a href="{other_url}" hreflang="{other}" lang="{other}">{UI[other]["lang_name"]}</a></nav></div>
</div>
</footer>
<script>{JS.strip()}</script>
{H.consent_html(L)}
<script>{H.consent_js(False)}</script>
</body>
</html>
"""


def org():
    return {"@type": "Organization", "@id": SITE + "/#org", "name": "Female Signature", "url": SITE + "/",
            "logo": {"@type": "ImageObject", "url": SITE + "/images/icon-512.png", "width": 512, "height": 512}}


def person():
    return {"@type": "Person", "@id": SITE + "/#mediha", "name": "Mediha Mujcin", "honorificPrefix": "Mag. (FH)",
            "jobTitle": "CEO & Founder", "worksFor": {"@id": SITE + "/#org"}, "url": SITE + "/#about", "sameAs": [LI]}


def meta_line(p, L, cls="meta"):
    U = UI[L]
    return (f'<p class="{cls}"><span>{esc(p["cat"])}</span><span class="dot" aria-hidden="true"></span>'
            f'<time datetime="{p["date"]}">{fdate(p["date"], L)}</time><span class="dot" aria-hidden="true"></span><span>{p["mins"]} {U["min"]}</span></p>')


def index_page(L, posts):
    U = UI[L]
    ps = [p for p in posts if p["lang"] == L]
    cats = []
    for p in ps:
        if p["cat"] not in cats:
            cats.append(p["cat"])
    top = ps[0]
    a, b = U["h1"]
    flt = (f'<button type="button" aria-pressed="true" data-c="">{U["all"]} <sup>{len(ps)}</sup></button>'
           + "".join(f'<button type="button" aria-pressed="false" data-c="{esc(c)}">{esc(c)} <sup>{sum(p["cat"] == c for p in ps)}</sup></button>' for c in cats))
    rows = "".join(
        f'<li data-c="{esc(p["cat"])}"><a class="row" href="{url(p)}" data-img="/images/opt/blog-{p["n"]}-480.webp">'
        f'<span class="n" aria-hidden="true">{i + 1:02d}</span><h3>{esc(p["title"])}</h3>{meta_line(p, L)}'
        f'<span class="th">{pic("blog-" + str(p["n"]), "88px", 4 / 3, CARD_W)}</span>'
        f'<span class="ar" aria-hidden="true">{ICON_ARROW}</span></a></li>'
        for i, p in enumerate(ps))
    T = H.DE if L == "de" else H.EN
    ca, cb = T["cta_h2"]
    main = f"""<section class="bh" aria-labelledby="h1">
<div class="wrap">
<div><p class="label">{U["label"]}</p><h1 id="h1">{esc(a)} <em>{esc(b)}</em></h1></div>
<div class="side"><p class="lead">{esc(U["lead"])}</p><div class="count"><div><b>{len(ps):02d}</b><span>{U["n_posts"]}</span></div><div><b>{len(cats):02d}</b><span>{U["n_topics"]}</span></div></div></div>
</div>
</section>
<section class="sec" style="padding-top:0" aria-label="{esc(U["latest"])}">
<div class="wrap">
<a class="card top" href="{url(top)}"><div class="shot">{pic("blog-" + str(top["n"]), "(min-width:900px) 600px, 92vw", 4 / 3, CARD_W, eager=True)}</div>
<div class="txt"><p class="pill fr">{esc(U["latest"])}</p><h2>{esc(top["title"])}</h2><p class="x">{esc(top["desc"])}</p>{meta_line(top, L)}<span class="go">{esc(U["read"])} {ICON_ARROW}</span></div></a>
</div>
</section>
<section class="sec" style="padding-top:0" aria-labelledby="all-h">
<div class="wrap">
<div class="head" style="display:grid;gap:20px;margin-bottom:28px"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap"><h2 class="h2" id="all-h" style="font-size:clamp(1.75rem,1.2rem + 2vw,2.75rem)">{esc(U["all_h"])}</h2><p id="cnt" aria-live="polite" style="color:var(--mu);font-size:.875rem" data-one="{U["count_one"]}" data-many="{U["count_many"]}">{U["count_many"].replace("#", str(len(ps)))}</p></div>
<div class="flt" role="group" aria-label="{esc(U["filter"])}">{flt}</div></div>
<ul class="idx">{rows}</ul>
</div>
<div class="peek" aria-hidden="true"><img src="/images/opt/blog-{top["n"]}-480.webp" alt="" width="480" height="360"></div>
</section>
<div class="ctawrap">
<section class="ctab" aria-labelledby="cta-h">
{H.pic("cta", "c", "100vw", 21 / 9)}
<div><p class="label">{esc(T["cta_label"])}</p><h2 class="h2" id="cta-h">{esc(ca)} <em>{esc(cb)}</em></h2><p class="lead">{esc(T["cta_sd"])} <strong>{esc(T["cta_strong"])}</strong></p><div class="acts"><a class="btn light" href="{CAL}" target="_blank" rel="noopener">{esc(U["cta"])} {ICON_ARROW}</a></div></div>
</section>
</div>"""
    canon = U["index"]
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": SITE + canon + "#blog", "name": "Female Signature Blog", "url": SITE + canon, "inLanguage": L,
         "description": U["desc"], "publisher": org(),
         "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": SITE + url(p), "datePublished": p["date"],
                       "image": SITE + f"/images/opt/cover-{p['n']}-1200.webp"} for p in ps]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Female Signature", "item": SITE + U["home"]},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + canon}]}]}
    alts = [("de", "/blog/"), ("en", "/blog/index-en"), ("x-default", "/blog/")]
    tn = top["n"]
    pset = ", ".join(f"/images/opt/blog-{tn}-{w}.webp {w}w" for w in CARD_W)
    pre = f'<link rel="preload" as="image" type="image/webp" imagesrcset="{pset}" imagesizes="(min-width:900px) 600px, 92vw" fetchpriority="high">\n'
    other = UI["en" if L == "de" else "de"]["index"]
    return shell(L, page_title(U["title"].replace(" | Female Signature", "")), U["desc"], canon, alts, ("/images/og-image.jpg" if L == "de" else "/images/og-image-en.jpg", 1200, 630), schema, main, other, pre)


def article_page(p, posts):
    L = p["lang"]
    U = UI[L]
    T = H.DE if L == "de" else H.EN
    faq = p.get("faq", [])
    src = p["body"]
    if faq:
        src += f'\n\n<h2>{U["faq_h"]}</h2>\n<div class="fq">' + "".join(
            f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faq) + "</div>"
    body, toc = prose(src, L)
    upd = p.get("updated", p["date"])
    others = [q for q in posts if q["lang"] == L and q["slug"] != p["slug"]]
    others.sort(key=lambda q: (q["cat"] != p["cat"], [-int(x) for x in q["date"].split("-")], q["n"]))
    nxt = others[:3]
    pair = next(q for q in posts if q["slug"] == p["pair"])
    toc_html = ""
    if len(toc) >= 2:
        lis = "".join(f'<li><a href="#{h}">{esc(t)}</a></li>' for h, t in toc)
        toc_html = (f'<aside class="toc" aria-label="{U["toc"]}"><div><p class="tt">{U["toc"]}</p><ol class="tw">{lis}</ol>'
                    f'<details><summary>{U["toc"]} · {len(toc)} {U["toc_n"]}</summary><ol>{lis}</ol></details></div></aside>')
    full = SITE + url(p)
    from urllib.parse import quote
    share = (f'<div class="share"><span>{U["share"]}</span>'
             f'<a href="https://www.linkedin.com/sharing/share-offsite/?url={quote(full, safe="")}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON_LI}</a>'
             f'<a href="https://wa.me/?text={quote(p["title"] + " " + full, safe="")}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON_WA}</a>'
             f'<a href="mailto:?subject={quote(U["mail_sub"])}&amp;body={quote(p["title"] + " " + full)}" aria-label="E-Mail"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></a>'
             f'<button type="button" id="copy" data-ok="{U["copied"]}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>{U["copy"]}</button>'
             f'<output id="copied" aria-live="polite"></output></div>')
    face = ('<img src="/images/opt/mediha-face-96.webp" srcset="/images/opt/mediha-face-96.webp 96w, /images/opt/mediha-face-192.webp 192w" '
            'sizes="{s}px" width="{s}" height="{s}" alt="" loading="lazy" decoding="async">')
    tags = "".join(f"<li>{esc(t)}</li>" for t in p["tags"])
    ch, cp, cb = p["cta"]
    cards = "".join(
        f'<a class="post" href="{url(q)}"><div class="shot">{pic("blog-" + str(q["n"]), "(min-width:1000px) 360px, (min-width:700px) 46vw, 92vw", 4 / 3, CARD_W)}</div>'
        f'{meta_line(q, L)}<h3>{esc(q["title"])}</h3><span class="go">{esc(U["read"])} {ICON_ARROW}</span></a>' for q in nxt)
    na, nb = U["next_h"]
    main = f"""<div class="prog" aria-hidden="true"></div>
<article>
<header class="ah">
<div class="wrap">
<nav class="crumb" aria-label="{U["breadcrumb"]}"><a href="{U["home"]}">Female Signature</a><span aria-hidden="true">/</span><a href="{U["index"]}">Blog</a><span aria-hidden="true">/</span><span>{esc(p["cat"])}</span></nav>
<p class="label">{esc(p["cat"])}</p>
<h1>{esc(p["title"])}</h1>
<p class="lead">{esc(p["desc"])}</p>
<div class="by"><div class="who">{face.format(s=48)}<div><strong>{AUTHOR}</strong><span>{U["role"]}</span></div></div>
<p class="meta"><time datetime="{p["date"]}">{fdate(p["date"], L)}</time>{"" if upd == p["date"] else f'<span class="dot" aria-hidden="true"></span><span>{U["upd"]} <time datetime="{upd}">{fdate(upd, L)}</time></span>'}<span class="dot" aria-hidden="true"></span><span>{p["mins"]} {U["min"]}</span></p></div>
</div>
</header>
<div class="cover"><div class="shot">{pic("cover-" + str(p["n"]), "(min-width:1440px) 1400px, 100vw", 16 / 9, COVER_W, eager=True)}</div></div>
<div class="body">
<div class="wrap">
{toc_html}
<div>
<div class="prose">
{body}
</div>
<div class="after">
<ul class="tags" aria-label="{U["tags"]}">{tags}</ul>
{share}
<div class="auth">{face.format(s=72).replace('alt=""', f'alt="{AUTHOR}"')}<div><small>{U["author_k"]}</small><strong>{AUTHOR}</strong><p>{esc(T["ceo_bio"])}</p><a class="link" href="{U["home"]}#about">{U["about"]} {ICON_ARROW}</a></div></div>
</div>
</div>
</div>
</div>
</article>
<section class="sec" style="padding-top:0" aria-labelledby="cta-a">
<div class="wrap">
<div class="acta"><div><p class="label">{U["cta_label"]}</p><h2 id="cta-a">{esc(ch)}</h2><p>{esc(cp)}</p><p class="sig">{face.format(s=44)}<span>{AUTHOR}</span></p></div><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(cb)} {ICON_ARROW}</a></div>
</div>
</section>
<section class="sec more" style="padding-top:0" aria-labelledby="more-h">
<div class="wrap">
<div class="head"><div><p class="label">{U["next_label"]}</p><h2 class="h2" id="more-h">{esc(na)} <em>{esc(nb)}</em></h2></div><a class="btn ghost" href="{U["index"]}">{U["to_index"]} {ICON_ARROW}</a></div>
<div class="cards">{cards}</div>
</div>
</section>"""
    de_p, en_p = (p, pair) if L == "de" else (pair, p)
    alts = [("de", url(de_p)), ("en", url(en_p)), ("x-default", url(de_p))]
    img = SITE + f"/images/opt/cover-{p['n']}-1200.webp"
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": full + "#article", "headline": p["title"], "description": p.get("meta", p["desc"]), "inLanguage": L,
         "image": {"@type": "ImageObject", "url": img, "width": 1200, "height": 675},
         "datePublished": p["date"], "dateModified": upd, "author": person(), "publisher": org(),
         "mainEntityOfPage": full, "url": full, "articleSection": p["cat"], "keywords": ", ".join(p["tags"]),
         "wordCount": len(re.sub(r"<[^>]+>", " ", p["body"]).split()), "timeRequired": f"PT{p['mins']}M",
         "isPartOf": {"@id": SITE + U["index"] + "#blog"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Female Signature", "item": SITE + U["home"]},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + U["index"]},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": full}]}]}
    if faq:
        schema["@graph"].append({"@type": "FAQPage", "@id": full + "#faq", "inLanguage": L, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faq]})
    pn = p["n"]
    pset = ", ".join(f"/images/opt/cover-{pn}-{w}.webp {w}w" for w in COVER_W)
    pre = (f'<link rel="preload" as="image" type="image/webp" imagesrcset="{pset}" imagesizes="(min-width:1440px) 1400px, 100vw" fetchpriority="high">\n'
           f'<meta property="article:published_time" content="{p["date"]}">\n<meta property="article:modified_time" content="{upd}">\n'
           f'<meta property="article:section" content="{esc(p["cat"])}">\n' + "".join(f'<meta property="article:tag" content="{esc(t)}">\n' for t in p["tags"]))
    return shell(L, page_title(p.get("seo", p["title"])), p.get("meta", p["desc"]), url(p), alts, (f"/images/opt/cover-{p['n']}-1200.webp", 1200, 675, p["title"]), schema, main, url(pair), pre, "article")


def page_title(t):
    """Markenzusatz nur, solange der Titel in Google ungekürzt bleibt (bis 60 Zeichen)."""
    full = f"{t} | Female Signature"
    return full if len(full) <= 60 else t


def simple_page(label, h1a, h1b, lead, buttons, title, desc, canon, L="de"):
    """Kleine Seite im neuen Design (Danke-Seite, 404), noindex."""
    btns = "".join(f'<a class="btn{"" if i == 0 else " ghost"}" href="{h}">{esc(t)}</a>' for i, (h, t) in enumerate(buttons))
    main = f"""<section class="ah simple">
<div class="wrap">
<p class="label">{esc(label)}</p>
<h1>{esc(h1a)} <em>{esc(h1b)}</em></h1>
<p class="lead">{esc(lead)}</p>
<p class="acts">{btns}</p>
</div>
</section>"""
    schema = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": SITE + canon, "inLanguage": L, "publisher": org()}
    og = "/images/og-image.jpg" if L == "de" else "/images/og-image-en.jpg"
    return shell(L, title, desc, canon, [], (og, 1200, 630), schema, main, "/en/" if L == "de" else "/", current="", robots="noindex,follow")


def legal_page(name):
    """Impressum und Datenschutz: nur Deutsch, Inhalt aus tools/legal/<name>.html."""
    raw = (ROOT / "tools" / "legal" / f"{name}.html").read_text(encoding="utf-8")
    m = re.match(r"<!--\s*(\{.*?\})\s*-->\s*(.*)$", raw, re.S)
    meta, body = json.loads(m[1]), m[2].strip()
    toc = []

    def h2(mm):
        t = re.sub(r"<[^>]+>", "", mm[1])
        hid = slugify(re.sub(r"^\d+\.\s*", "", t))
        toc.append((hid, re.sub(r"^\d+\.\s*", "", t)))
        return f'<h2 id="{hid}">{mm[1]}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", h2, body)
    lis = "".join(f'<li><a href="#{h}">{esc(t)}</a></li>' for h, t in toc)
    toc_html = (f'<aside class="toc" aria-label="Inhalt"><div><p class="tt">Inhalt</p><ol class="tw">{lis}</ol>'
                f'<details><summary>Inhalt · {len(toc)} Abschnitte</summary><ol>{lis}</ol></details></div></aside>')
    canon = f"/{name}"
    main = f"""<div class="prog" aria-hidden="true"></div>
<article class="legal">
<header class="ah">
<div class="wrap">
<nav class="crumb" aria-label="Brotkrumen-Navigation"><a href="/">Female Signature</a><span aria-hidden="true">/</span><span>{esc(meta["title"])}</span></nav>
<p class="label">Rechtliches</p>
<h1>{esc(meta["title"])}</h1>
<p class="lead">{esc(meta["sub"])}</p>
</div>
</header>
<div class="body">
<div class="wrap">
{toc_html}
<div class="prose">
{body}
</div>
</div>
</div>
</article>
<section class="sec" style="padding-top:0" aria-labelledby="cta-a">
<div class="wrap">
<div class="acta"><div><p class="label">Fragen?</p><h2 id="cta-a">Schreiben Sie uns direkt.</h2><p><a href="mailto:{MAIL}" style="color:inherit">{MAIL}</a> · <a href="tel:{TEL}" style="color:inherit">{TEL_TXT}</a></p></div><a class="btn" href="/#kontakt">Zum Kontaktformular {ICON_ARROW}</a></div>
</div>
</section>"""
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": meta["title"], "url": SITE + canon, "inLanguage": "de", "publisher": org()},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Female Signature", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": meta["title"], "item": SITE + canon}]}]}
    return shell("de", f'{meta["title"]} | Female Signature', meta["desc"], canon, [], ("/images/og-image.jpg", 1200, 630),
                 schema, main, "/en/", current=name.capitalize(), robots=meta["robots"])


def sitemap(posts):
    f = ROOT / "sitemap.xml"
    s = f.read_text(encoding="utf-8")
    keep = [u for u in re.findall(r"  <url>.*?</url>\n", s, re.S) if "/blog/" not in u]

    def entry(loc, de, en, mod, freq, prio):
        return (f"  <url>\n    <loc>{SITE}{loc}</loc>\n"
                f'    <xhtml:link rel="alternate" hreflang="de" href="{SITE}{de}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{de}"/>\n'
                f"    <lastmod>{mod}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>\n")
    blog = [entry("/blog/", "/blog/", "/blog/index-en", TODAY, "weekly", "0.8"), entry("/blog/index-en", "/blog/", "/blog/index-en", TODAY, "weekly", "0.6")]
    for p in posts:
        de = p["slug"] if p["lang"] == "de" else p["pair"]
        blog.append(entry(url(p), f"/blog/{de}", f"/blog/{de}-en", p.get("updated", p["date"]), "monthly", "0.7" if p["lang"] == "de" else "0.5"))
    # Impressum und Datenschutz sind noindex und gehören daher nicht in die Sitemap
    rest = [u for u in keep if "impressum" not in u and "datenschutz" not in u]
    head = s[:s.index("  <url>")]
    f.write_text(head + "".join(rest + blog) + "</urlset>\n", encoding="utf-8")


def main():
    posts = load()
    out = ROOT / "blog"
    (out / "index.html").write_text(H.versioned(index_page("de", posts)), encoding="utf-8")
    (out / "index-en.html").write_text(H.versioned(index_page("en", posts)), encoding="utf-8")
    for p in posts:
        (out / f"{p['slug']}.html").write_text(H.versioned(article_page(p, posts)), encoding="utf-8")
    for name in ("impressum", "datenschutz"):
        (ROOT / f"{name}.html").write_text(H.versioned(legal_page(name)), encoding="utf-8")
    (ROOT / "success.html").write_text(H.versioned(simple_page(
        "Nachricht gesendet", "Vielen", "Dank.", "Ihre Nachricht ist angekommen. Wir melden uns innerhalb von 24 Stunden bei Ihnen.",
        [("/", "Zurück zur Startseite"), ("/blog/", "Zum Blog")],
        "Nachricht gesendet | Female Signature", "Danke für Ihre Nachricht an Female Signature. Wir melden uns innerhalb von 24 Stunden bei Ihnen.", "/success")), encoding="utf-8")
    (ROOT / "404.html").write_text(H.versioned(simple_page(
        "Fehler 404", "Diese Seite gibt es", "nicht.", "Vielleicht hat sich die Adresse geändert. Auf der Startseite und im Blog finden Sie alle Inhalte.",
        [("/", "Zur Startseite"), ("/blog/", "Zum Blog"), ("/en/", "English version")],
        "Seite nicht gefunden | Female Signature", "Diese Seite gibt es nicht. Zur Startseite und zum Blog von Female Signature.", "/404")), encoding="utf-8")
    (ROOT / "en" / "success.html").write_text(H.versioned(simple_page(
        "Message sent", "Thank", "you.", "Your message has arrived. We will get back to you within 24 hours.",
        [("/en/", "Back to the homepage"), ("/blog/index-en", "Read the blog")],
        "Message sent | Female Signature", "Thank you for your message to Female Signature. We will get back to you within 24 hours.", "/en/success", "en")), encoding="utf-8")
    (ROOT / "en" / "404.html").write_text(H.versioned(simple_page(
        "Error 404", "This page does", "not exist.", "The address may have changed. You will find all our content on the homepage and in the blog.",
        [("/en/", "Go to the homepage"), ("/blog/index-en", "Go to the blog"), ("/", "Deutsche Version")],
        "Page not found | Female Signature", "This page does not exist. Go to the Female Signature homepage or blog.", "/en/404", "en")), encoding="utf-8")
    sitemap(posts)
    print(len(posts), "Artikel,", sum((out / f"{p['slug']}.html").stat().st_size for p in posts) // len(posts), "Bytes im Schnitt")


if __name__ == "__main__":
    main()
