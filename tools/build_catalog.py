#!/usr/bin/env python3
"""Reads knowledge/catalog.json and writes faq.html, preguntas-frecuentes.html, llms.txt, knowledge.md."""
import json, html, re, os
R=os.path.join(os.path.dirname(__file__),"..")
C=json.load(open(f"{R}/knowledge/catalog.json"))
B="https://www.2buyandsell.com"
e=html.escape
CSS=open(f"{R}/tools/page-style.html").read()
A=C["agent"]
def page(lang):
    es=lang=="es"; slug="preguntas-frecuentes" if es else "faq"; other="faq" if es else "preguntas-frecuentes"
    url=f"{B}/{slug}.html"; oturl=f"{B}/{other}.html"; en_url,es_url=(oturl,url) if es else (url,oturl)
    title="Preguntas frecuentes | Comprar o vender en San Antonio | Monica Polo" if es else "FAQ | Buying or Selling in San Antonio | Monica Polo"
    desc=("Respuestas claras de Monica Polo, agente bilingüe en San Antonio, sobre comprar o vender casa, la evaluación gratis de 2 minutos y cómo trabaja." if es else
          "Straight answers from Monica Polo, bilingual San Antonio REALTOR®, about buying or selling a home, the free 2-minute check and how she works.")
    h1="Preguntas frecuentes sobre comprar o vender en San Antonio" if es else "Frequently asked questions about buying or selling in San Antonio"
    qa=[(f["q"][lang],f["a"][lang]) for f in C["faq"]]
    ld=[{"@context":"https://schema.org","@type":"FAQPage","inLanguage":lang,"url":url,"mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Monica Polo","item":B+"/"},{"@type":"ListItem","position":2,"name":"FAQ","item":url}]}]
    body="".join(f'<h2 id="{e(f["id"])}">{e(f["q"][lang])}</h2><p>{e(f["a"][lang])}</p>' for f in C["faq"])
    svc="".join(f'<li><a href="{s["urlEs"] if es else s["url"]}"><b>{e(s["name"][lang])}</b></a>. {e(s["desc"][lang])}</li>' for s in C["services"])
    cta="Hacer la evaluación gratis de 2 minutos" if es else "Take the free 2-minute check"
    L=dict(svc="Servicios" if es else "Services",home="Inicio" if es else "Home",lang="English version" if es else "Versión en español",
      iabs="Información sobre los servicios de corretaje (TREC)" if es else "Information About Brokerage Services (TREC)",
      cpn="Aviso de protección al consumidor (TREC)" if es else "Consumer Protection Notice (TREC)",
      upd="Actualizado" if es else "Last updated",sub="Monica Polo, REALTOR® · Reliance Residential Realty · San Antonio, TX")
    go=f"/?go=buy{'&lang=es' if es else ''}"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Monica Polo Real Estate">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{B}/img/og-share3.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#31564F">
<link rel="icon" type="image/png" sizes="192x192" href="/img/favicon.png?v=3">
<link rel="apple-touch-icon" href="/img/app-apple-180.png?v=3">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/site.css">
{CSS}
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="mark" href="/" aria-label="Monica Polo Real Estate"><img src="/img/mp-logo.png" alt="Monica Polo Real Estate" height="44"></a>
<div style="display:flex;align-items:center;gap:14px"><a class="btn" href="{go}">{"Evaluación gratis" if es else "Free check"}</a></div>
</div></header>
<main class="pg">
<span class="eyebrow">FAQ · San Antonio, TX</span>
<h1>{e(h1)}</h1>
<hr class="rule">
<div class="cta-row"><a class="btn" href="{go}">{e(cta)}</a><a class="btn ghost" href="tel:{A["phone"]}">{e(A["phoneDisplay"])}</a></div>
{body}
<h2>{L["svc"]}</h2><ul>{svc}</ul>
<div class="cta-row"><a class="btn" href="{go}">{e(cta)}</a></div>
<div class="foot">
<p>{L["sub"]} · {L["upd"]}: {C["updated"]}</p>
<p><a href="/">{L["home"]}</a> · <a href="/{other}.html">{L["lang"]}</a> · <a href="/docs/information-about-brokerage-services.pdf" target="_blank" rel="noopener">{L["iabs"]}</a> · <a href="/docs/consumer-protection-notice.pdf" target="_blank" rel="noopener">{L["cpn"]}</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></p>
</div>
</main>
</body>
</html>
'''
for lang,fn in (("en","faq.html"),("es","preguntas-frecuentes.html")):
    open(f"{R}/{fn}","w").write(page(lang))
# llms.txt + markdown catalog
md=[f"# {A['name']}, {A['title']['en']}",f"",f"> Bilingual (English/Spanish) real estate agent with {A['brokerage']} serving San Antonio, Texas. Website: {A['website']}. Phone: {A['phoneDisplay']}. Last updated {C['updated']}.","",
 "## Areas served",", ".join(C["areas"]),"","## Services"]
for s in C["services"]: md.append(f"- {s['name']['en']}: {s['desc']['en']}")
md+=["","## Frequently asked questions (English)",""]
for f in C["faq"]: md+=[f"### {f['q']['en']}",f['a']['en'],""]
md+=["## Preguntas frecuentes (español)",""]
for f in C["faq"]: md+=[f"### {f['q']['es']}",f['a']['es'],""]
md+=["## Notices","- Information About Brokerage Services (TREC): "+B+"/docs/information-about-brokerage-services.pdf","- Consumer Protection Notice (TREC): "+B+"/docs/consumer-protection-notice.pdf",""]
open(f"{R}/knowledge.md","w").write("\n".join(md))
ll=[f"# {A['name']} Real Estate (2buyandsell.com)","",f"> Bilingual (English/Spanish) REALTOR® in San Antonio, Texas, with {A['brokerage']}. Free 2-minute buyer/seller readiness check, no credit check.","",
 "## Key pages",
 f"- [Home / free readiness check]({B}/): start the check for buying or selling",
 f"- [Buy a home in San Antonio]({B}/buy-a-home-san-antonio.html)",f"- [Sell your home in San Antonio]({B}/sell-your-home-san-antonio.html)",
 f"- [Comprar casa en San Antonio]({B}/comprar-casa-san-antonio.html)",f"- [Vender tu casa en San Antonio]({B}/vender-casa-san-antonio.html)",
 f"- [FAQ]({B}/faq.html)",f"- [Preguntas frecuentes]({B}/preguntas-frecuentes.html)",
 f"- [Full knowledge catalog in plain text]({B}/knowledge.md)","",
 "## Contact",f"- Phone: {A['phoneDisplay']}",f"- Areas: {', '.join(C['areas'])}"]
open(f"{R}/llms.txt","w").write("\n".join(ll)+"\n")
# sitemap
sm=open(f"{R}/sitemap.xml").read()
for p in ("faq","preguntas-frecuentes"):
    if f"/{p}.html" not in sm:
        sm=sm.replace("</urlset>",f'  <url><loc>{B}/{p}.html</loc><lastmod>{C["updated"]}</lastmod><priority>0.7</priority></url>\n</urlset>')
open(f"{R}/sitemap.xml","w").write(sm)
print("ok",len(C["faq"]),"faqs")
