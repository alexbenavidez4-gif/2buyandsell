import json,html
B="https://www.2buyandsell.com"
P={
"buy-a-home-san-antonio":dict(lang="en",alt="comprar-casa-san-antonio",go="buy",
 title="Buy a Home in San Antonio | First-Time Buyer Help | Monica Polo",
 desc="Thinking of buying a home in San Antonio? Monica Polo, bilingual REALTOR®, explains every step in English or Spanish. Take the free 2-minute readiness check.",
 eyebrow="Buy a home · San Antonio, TX",h1="Buying a home in San Antonio, explained step by step",
 lede="Whether it's your first home or your fifth, you should know where you stand before you tour a single house. Monica Polo is a bilingual San Antonio REALTOR® who walks you through it in English or Spanish.",
 cta="Take the free 2-minute buyer check",cta2="Call (210) 249-8331",
 secs=[("Find out if you're ready to buy","The free readiness check asks about your savings, income, debts and timing. It takes about 2 minutes and never touches your credit. You get a readiness score, a realistic price range and a clear next step, and Monica replies to you personally."),
 ("What buying in San Antonio usually looks like","Most purchases follow the same path: get your finances in order, talk with a lender about loan options, search for homes in the neighborhoods you like, make an offer, complete the inspection and option period, and close with a title company. Monica explains each step before you get to it, so there are no surprises."),
 ("Loan options to ask about","Depending on your situation, you may want to compare conventional, FHA and VA loans, and ask a lender whether any down payment assistance programs fit you. If you or your spouse serve at Joint Base San Antonio, ask Monica about buying with VA benefits. She holds the Military and Veteran Housing Certification (MVHC)."),
 ("Where Monica helps you buy","San Antonio, Converse, Live Oak, Cibolo, New Braunfels and Seguin.")],
 faq=[("Does the buyer check cost anything?","No. It's free, takes about 2 minutes and doesn't check your credit."),("Can I work with a Spanish-speaking agent?","Yes. Monica is bilingual and can guide you through the whole purchase in English or Spanish."),("Do I need a big down payment?","Not always. Loan programs and down payment amounts vary, so the check helps you see what may fit before you talk to a lender.")],
 other=("sell-your-home-san-antonio","Selling a home instead?","Sell your home in San Antonio")),
"sell-your-home-san-antonio":dict(lang="en",alt="vender-casa-san-antonio",go="sell",
 title="Sell Your Home in San Antonio | Free Home Value Check | Monica Polo",
 desc="Ready to sell your San Antonio home? Monica Polo, bilingual REALTOR®, shows what your home could sell for and what you could walk away with. Free 2-minute check.",
 eyebrow="Sell your home · San Antonio, TX",h1="Selling your San Antonio home: know your number first",
 lede="Before you list, it helps to see what your home could sell for and what you'd actually keep after costs. Monica Polo, a bilingual San Antonio REALTOR®, gives you a personal answer in English or Spanish.",
 cta="Take the free 2-minute seller check",cta2="Call (210) 249-8331",
 secs=[("See what you could walk away with","The free seller check asks a few simple questions about your home and your timing. You see a value range and an estimate of what you could net after costs. It's free, takes about 2 minutes and doesn't check your credit."),
 ("What selling usually looks like","Selling typically means pricing the home with local sales in mind, preparing it for photos and showings, reviewing offers, handling the buyer's inspection and option period, and closing with a title company. Monica walks you through each step and answers your questions as they come up."),
 ("Selling and buying at the same time","Many families need to sell before they can buy. The check lets you answer for both, so you can see how the sale could fund your next home."),
 ("Where Monica helps you sell","San Antonio, Converse, Live Oak, Cibolo, New Braunfels and Seguin.")],
 faq=[("How do I find out what my home is worth?","Take the free seller check, or enter your address in the home value section on the home page. Monica replies within 48 hours and aims for 24."),("Does the seller check cost anything?","No. It's free and doesn't check your credit."),("Can you help me in Spanish?","Yes. Monica is bilingual and can explain every step of selling in English or Spanish.")],
 other=("buy-a-home-san-antonio","Buying a home instead?","Buy a home in San Antonio")),
"comprar-casa-san-antonio":dict(lang="es",alt="buy-a-home-san-antonio",go="buy",
 title="Comprar Casa en San Antonio, TX | Agente en Español | Monica Polo",
 desc="¿Quieres comprar casa en San Antonio? Monica Polo, agente de bienes raíces bilingüe, te explica cada paso en español. Evaluación gratis de 2 minutos.",
 eyebrow="Comprar casa · San Antonio, TX",h1="Comprar casa en San Antonio, paso a paso y en español",
 lede="Ya sea tu primera casa o la quinta, conviene saber dónde estás parado antes de visitar una sola casa. Monica Polo es una agente de bienes raíces bilingüe en San Antonio que te acompaña en español o en inglés.",
 cta="Hacer la evaluación gratis de 2 minutos",cta2="Llama al (210) 249-8331",
 secs=[("Descubre si estás listo para comprar","La evaluación gratis te pregunta por tus ahorros, ingresos, deudas y tiempos. Toma unos 2 minutos y no revisa tu crédito. Recibes una calificación de preparación, un rango de precio realista y un siguiente paso claro, y Monica te responde personalmente."),
 ("Cómo suele ser comprar en San Antonio","La mayoría de las compras siguen el mismo camino: ordenar tus finanzas, hablar con un prestamista sobre tus opciones, buscar casas en las zonas que te gustan, hacer una oferta, completar la inspección y el periodo de opción, y cerrar con una compañía de título. Monica te explica cada paso antes de llegar a él, para que no haya sorpresas."),
 ("Opciones de préstamo para preguntar","Según tu situación, puedes comparar préstamos convencionales, FHA y VA, y preguntarle a un prestamista si algún programa de ayuda para el enganche te sirve. Si tú o tu pareja sirven en Joint Base San Antonio, pregúntale a Monica sobre comprar con beneficios VA. Ella tiene la Certificación de Vivienda para Militares y Veteranos (MVHC)."),
 ("Dónde te ayuda Monica","San Antonio, Converse, Live Oak, Cibolo, New Braunfels y Seguin.")],
 faq=[("¿Cuesta algo la evaluación para compradores?","No. Es gratis, toma unos 2 minutos y no revisa tu crédito."),("¿Puedo trabajar con un agente que hable español?","Sí. Monica es bilingüe y te acompaña en toda la compra en español o en inglés."),("¿Necesito mucho dinero para el enganche?","No siempre. Los programas y los enganches varían, y la evaluación te ayuda a ver qué podría funcionar antes de hablar con un prestamista.")],
 other=("vender-casa-san-antonio","¿Quieres vender tu casa?","Vender tu casa en San Antonio")),
"vender-casa-san-antonio":dict(lang="es",alt="sell-your-home-san-antonio",go="sell",
 title="Vender tu Casa en San Antonio, TX | Agente en Español | Monica Polo",
 desc="¿Listo para vender tu casa en San Antonio? Monica Polo, agente bilingüe, te muestra en qué precio podría venderse y cuánto te quedaría. Evaluación gratis de 2 minutos.",
 eyebrow="Vender casa · San Antonio, TX",h1="Vender tu casa en San Antonio: conoce tu número primero",
 lede="Antes de poner tu casa a la venta, conviene ver en cuánto podría venderse y cuánto te quedaría después de los costos. Monica Polo, agente de bienes raíces bilingüe en San Antonio, te da una respuesta personal en español o en inglés.",
 cta="Hacer la evaluación gratis de 2 minutos",cta2="Llama al (210) 249-8331",
 secs=[("Mira cuánto podrías quedarte","La evaluación gratis para vendedores te hace unas preguntas sencillas sobre tu casa y tus tiempos. Ves un rango de valor y un estimado de lo que te quedaría después de costos. Es gratis, toma unos 2 minutos y no revisa tu crédito."),
 ("Cómo suele ser vender una casa","Vender normalmente significa fijar el precio según las ventas locales, preparar la casa para fotos y visitas, revisar ofertas, atender la inspección y el periodo de opción del comprador, y cerrar con una compañía de título. Monica te acompaña en cada paso y responde tus preguntas conforme surgen."),
 ("Vender y comprar al mismo tiempo","Muchas familias necesitan vender antes de poder comprar. La evaluación te deja responder por las dos cosas, para ver cómo la venta podría ayudarte a pagar tu próxima casa."),
 ("Dónde te ayuda Monica","San Antonio, Converse, Live Oak, Cibolo, New Braunfels y Seguin.")],
 faq=[("¿Cómo sé cuánto vale mi casa?","Haz la evaluación gratis para vendedores, o escribe tu dirección en la sección del valor de tu casa en la página principal. Monica responde en un máximo de 48 horas y busca hacerlo en 24."),("¿Cuesta algo la evaluación para vendedores?","No. Es gratis y no revisa tu crédito."),("¿Me pueden ayudar en español?","Sí. Monica es bilingüe y te explica cada paso de la venta en español o en inglés.")],
 other=("comprar-casa-san-antonio","¿Quieres comprar casa?","Comprar casa en San Antonio")),
}
CSS="""<style>
:root{--navy:#31564F;--navy-2:#264540;--blue:#31564F;--gold:#B8755B;--gold-ink:#fff;--ink:#1F2B27;--muted:#5b655e;--paper:#F5F0E7;--card:#FBF8F2;--line:#E3DCCB}
body{background:#F5F0E7}
.top{background:#31564F;box-shadow:inset 0 -3px 0 #B8755B;border:0}
.top .mark{display:flex;align-items:center;gap:10px;color:#F5F0E7;text-decoration:none;font-weight:700}
.top .mark img{height:44px;width:auto;background:#F5F0E7;border-radius:4px;padding:3px}
.top .btn{background:#F5F0E7;color:#31564F}
.pg{max-width:760px;margin:0 auto;padding:36px 20px 60px}
.pg h1{font-size:clamp(30px,6.5vw,44px);line-height:1.12;margin:8px 0 14px;color:#31564F}
.pg h2{font-size:clamp(22px,4.6vw,28px);margin:34px 0 8px;color:#31564F}
.pg .lede{font-size:20px;color:#3f4a44}
.pg .eyebrow{color:#B8755B}
.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}
.cta-row .btn{background:#31564F;color:#F5F0E7;border-radius:3px;text-transform:uppercase;letter-spacing:.06em;font-size:15px;box-shadow:none;transition:background .25s}
.cta-row .btn:hover{background:#B8755B}
.cta-row .btn.ghost{background:#E9E2D2;color:#31564F}
.cta-row .btn.ghost:hover{background:#DDD3BE}
.rule{height:2px;background:#B8755B;width:64px;margin:6px 0 0;border:0}
.faq dt{font-weight:700;margin-top:16px;color:#1F2B27}.faq dd{margin:4px 0 0;color:#3f4a44}
.foot{border-top:1px solid #E3DCCB;margin-top:44px;padding-top:18px;font-size:15px;color:#5b655e}
.foot a{color:#31564F}
</style>"""
def build(slug,d):
    es=d["lang"]=="es"; url=f"{B}/{slug}.html"; alt=f"{B}/{d['alt']}.html"
    en_url,es_url=(alt,url) if es else (url,alt)
    faq=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in d["faq"]]
    ld=[{"@context":"https://schema.org","@type":"WebPage","name":d["title"],"url":url,"inLanguage":d["lang"],"description":d["desc"],
         "about":{"@type":"Service","name":d["h1"],"areaServed":{"@type":"City","name":"San Antonio, TX"},
          "provider":{"@type":"RealEstateAgent","@id":B+"/#monica","name":"Monica Polo","telephone":"+1-210-249-8331","url":B+"/"}}},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Monica Polo","item":B+"/"},{"@type":"ListItem","position":2,"name":d["eyebrow"].split(" · ")[0],"item":url}]},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq}]
    e=html.escape
    secs="".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h,p in d["secs"])
    faqh="".join(f"<dt>{e(q)}</dt><dd>{e(a)}</dd>" for q,a in d["faq"])
    oslug,oq,olabel=d["other"]
    L=dict(home="Inicio" if es else "Home",faq="Preguntas frecuentes" if es else "Frequently asked questions",
      lang="English version" if es else "Versión en español",
      iabs="Información sobre los servicios de corretaje (TREC)" if es else "Information About Brokerage Services (TREC)",
      cpn="Aviso de protección al consumidor (TREC)" if es else "Consumer Protection Notice (TREC)",
      sub="Monica Polo, REALTOR® · Texas License #769628 · Reliance Residential Realty · San Antonio, TX")
    other_lang_slug=d["alt"]
    return f'''<!DOCTYPE html>
<html lang="{d["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(d["title"])}</title>
<meta name="description" content="{e(d["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Monica Polo Real Estate">
<meta property="og:title" content="{e(d["title"])}">
<meta property="og:description" content="{e(d["desc"])}">
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
<div style="display:flex;align-items:center;gap:14px"><a class="btn" href="/?go={d["go"]}{"&lang=es" if es else ""}">{"Evaluación gratis" if es else "Free check"}</a></div>
</div></header>
<main class="pg">
<span class="eyebrow">{e(d["eyebrow"])}</span>
<h1>{e(d["h1"])}</h1>
<hr class="rule">
<p class="lede">{e(d["lede"])}</p>
<div class="cta-row"><a class="btn" href="/?go={d["go"]}{"&lang=es" if es else ""}">{e(d["cta"])}</a><a class="btn ghost" href="tel:+12102498331">{e(d["cta2"])}</a></div>
{secs}
<div class="cta-row"><a class="btn" href="/?go={d["go"]}{"&lang=es" if es else ""}">{e(d["cta"])}</a></div>
<h2>{L["faq"]}</h2>
<dl class="faq">{faqh}</dl>
<p style="margin-top:28px"><b>{e(oq)}</b> <a href="/{oslug}.html">{e(olabel)}</a></p>
<div class="foot">
<p>{L["sub"]}</p>
<p><a href="/">{L["home"]}</a> · <a href="/{other_lang_slug}.html">{L["lang"]}</a> · <a href="/docs/information-about-brokerage-services.pdf" target="_blank" rel="noopener">{L["iabs"]}</a> · <a href="/docs/consumer-protection-notice.pdf" target="_blank" rel="noopener">{L["cpn"]}</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></p>
</div>
</main>
</body>
</html>
'''
for s,d in P.items(): open(f"/home/claude/2buyandsell/{s}.html","w").write(build(s,d))
print(list(P))
