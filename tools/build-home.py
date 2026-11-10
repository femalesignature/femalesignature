#!/usr/bin/env python3
"""Baut die Startseite in zwei Sprachen aus einer Vorlage.

    python3 tools/build-home.py

Schreibt index.html (DE) und en/index.html (EN). Texte stehen in DE/EN unten,
Layout und Stil in page(). Nie die erzeugten HTML-Dateien von Hand ändern,
sonst überschreibt der nächste Lauf die Änderung.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://female-signature.com"
CAL = "https://calendly.com/mediha-mujcin/30min"
WA = "https://wa.me/4369912091987?text=Hallo%20Female%20Signature%2C%20ich%20interessiere%20mich%20f%C3%BCr%20ein%20Strategiegespr%C3%A4ch."
MAIL = "contact@female-signature.com"
TEL = "+4369912091987"
TEL_TXT = "+43 699 12091987"
IG = "https://www.instagram.com/femalesignature/"
LI = "https://www.linkedin.com/in/medihamujcin/"
TODAY = "2026-11-10"

PEOPLE = [  # Bild, Name
    ("agnese", "Dr. Agnese Nitto"),
    ("dina", "Dr. Dina Omanovic"),
    ("romana", "Romana Mayr"),
    ("jasmina", "Jasmina Medjic"),
    ("sabina", "Sabina Velic"),
    ("valeriya", "Valeriya Vogl"),
]

DE = {
    "lang": "de", "locale": "de_AT", "path": "/", "other_path": "/en/", "other_label": "EN",
    "other_name": "English",
    "title": "Female Signature | Growth-Agentur für Unternehmerinnen",
    "desc": "Female Signature: Growth-Agentur für Unternehmerinnen im DACH-Raum. Premium Branding, Partner Marketing & Performance. Kostenloser Strategie-Call.",
    "og_title": "Female Signature: Wir bauen Marken, die wachsen.",
    "og_image": "/images/og-image.jpg",
    "skip": "Zum Inhalt springen",
    "nav": [("#systems", "Systeme"), ("#approach", "Ansatz"), ("#results", "Ergebnisse"), ("/blog/", "Blog")],
    "menu": "Menü", "close": "Schließen",
    "cta_short": "Strategie-Call",
    "cta": "Kostenfreien Strategie-Call buchen",
    "cta30": "Kostenfreien 30-Min. Strategie-Call buchen",
    "principles": ["Aufgebaut, nicht ausgedacht.", "Strategie statt Sichtbarkeit.", "Partnerschaft statt Auftragsverhältnis.", "Ihre Marke. Unser System."],
    "hero_label": "Growth Partnership für Unternehmerinnen",
    "h1a": "Schöne Marken kann jeder.", "h1b": "Wir bauen Marken, die wachsen.",
    "hero_sub": "Strategische Markenarbeit, Performance-Systeme und Partnerstrukturen – für Unternehmerinnen mit etabliertem Angebot, denen die Infrastruktur zum Skalieren fehlt.",
    "hero_btn2": "Unsere Systeme",
    "stories_link": "Growth Stories",
    "region": "Aldrans, Tirol · DACH",
    "trust_line": "Unsere Kundinnen wachsen messbar.",
    "call_label": "Kostenfreier Strategie-Call",
    "pain_label": "Kommt Ihnen das bekannt vor?",
    "pain_h2": ("Die Realität vieler", "Female Businesses."),
    "solution": "Unsere Lösung",
    "pains": [
        ("Unsichtbar trotz tollem Angebot", "Ihr Angebot ist erstklassig. Aber zwischen Angebot und Marktwahrnehmung liegt eine Lücke, die das beste Produkt nicht von allein schließt.", "Magnetic Visibility System — Sichtbarkeit, die konvertiert."),
        ("Keine klare Premium-Positionierung", "Ohne klare Positionierung wird der Preis zum einzigen Vergleichskriterium. Das ist der teuerste Fehler, den ein gutes Unternehmen machen kann.", "Signature Brand Experience — Positionierung, die Premium-Kunden anzieht."),
        ("Umsatz stagniert trotz harter Arbeit", "Mehr Stunden bringen irgendwann keinen zusätzlichen Umsatz. Ab dann braucht Wachstum ein System, das unabhängig von Ihrer Zeit funktioniert.", "Revenue Performance System — datengetriebenes Wachstum mit klarem ROI."),
        ("Ihr Kerngeschäft leidet unter Marketing-Chaos", "Sie sind Expertin in dem, was Sie tun. Marketing ist nicht Ihr Handwerk – und sollte es auch nicht werden müssen.", "Wir übernehmen das Marketing — Sie konzentrieren sich auf das, was Sie am besten können."),
        ("Wachstum scheitert am fehlenden Plan", "Investitionsbudget ist nur so gut wie der Plan dahinter. Ohne klare Architektur fließen Mittel in Aktivität statt in Ergebnis.", "Flexible Modelle, die mit Ihrem Business mitwachsen — mit klarem ROI ab Tag eins."),
        ("Fehlende Strategie & Automatisierung", "Aktivität ist nicht Strategie. Posts, Anzeigen und Kampagnen ohne System produzieren Lärm – keinen Return.", "Growth Architecture — ein System, das für Sie arbeitet, auch wenn Sie es nicht tun."),
    ],
    "sys_label": "Was wir aufbauen",
    "sys_h2": ("Vier Systeme. Ein Ziel:", "Ihr Wachstum."),
    "sys_sd": "Keine Einzelmaßnahmen. Wir bauen eine zusammenhängende Infrastruktur, die Sichtbarkeit in Umsatz übersetzt — in der richtigen Reihenfolge.",
    "systems": [
        ("Brand Experience", "Ihr Produkt oder Service ist erstklassig. Ihre Marke erzählt es nur noch nicht.", "Wir entwickeln Markenidentitäten, die den wahren Wert Ihres Angebots sichtbar machen — Positionierung, visuelles System, Markenstimme und eine Erfahrung, die Premium-Kundinnen anzieht und Preisgespräche überflüssig macht.",
         ["Strategische Positionierung & Differenzierung", "Brand Identity & Design", "Texte & Tonalität, die Ihre Kundinnen ansprechen", "Website & Kundenerlebnis, das Besucher zu Kunden macht"]),
        ("Content & Sichtbarkeit", "Sie sind die Expertin. Aber niemand weiß es — weil Ihr Content nicht für Sie arbeitet.", "Wir bauen Content-Systeme, die organisch Reichweite schaffen und Ihre Expertise sichtbar machen — ohne dass Sie jeden Tag posten müssen. Eine Sichtbarkeitsstrategie, die nachhaltig wirkt und Kundinnen anzieht.",
         ["Social Media & Community-Aufbau", "Content-Strategie & Redaktionsplanung", "E-Mail-Marketing & CRM-Systeme", "Organische Reichweite & Markenbekanntheit"]),
        ("Partnership Marketing", "Ihr Wachstum hängt an Ihrer Zeit. Das muss aufhören.", "Andere empfehlen Sie weiter — und Sie verdienen daran. Wir bauen Partnernetzwerke aus Creators, Affiliates und zufriedenen Kundinnen, die Ihr Angebot empfehlen.",
         ["Weiterempfehlungs- & Affiliate-Programme", "Creator- & Influencer-Kooperationen", "Automatisiertes Partner-Management", "Provisionsmodelle & Erfolgsbeteiligung"]),
        ("Performance Marketing", "Sie investieren in Marketing. Aber wissen Sie, was wirklich funktioniert?", "Wir steuern datengetriebene Kampagnen, bei denen jeder investierte Euro nachvollziehbar ist. Von Awareness bis Conversion — immer transparent, immer optimiert, immer mit klarem ROI.",
         ["Paid Social & Search Kampagnen", "Conversion-Optimierung & A/B Testing", "Real-Time Reporting & Dashboards", "ROI-Tracking & Budget-Optimierung"]),
    ],
    "pm_label": "Partnership Marketing",
    "pm_h2": ("Eine Plattform. Alle", "Partnerschaften."),
    "pm_sd": "Influencer, Creator, Affiliates, Loyalty — in den meisten Unternehmen laufen diese Kanäle getrennt. Wir bündeln sie auf einer einzigen Plattform. Jeder Partner, jeder Klick, jede Conversion — messbar, automatisiert, in Ihrer Kontrolle.",
    "pm_list": ["Alle Partnertypen in einem System — keine Insellösungen mehr", "Full-Funnel Tracking von Awareness bis Advocacy", "Zugang zu einem globalen Netzwerk aus Partnern, Influencern und Creators", "Automatisierte Workflows — 10–40 Stunden Zeitersparnis pro Monat", "DSGVO-konform, fraud-geschützt, global skalierbar"],
    "pm_panel": "Partnership Automation Platform",
    "pm_cycle_t": "Der gesamte Partnership-Lifecycle",
    "pm_cycle": [("Awareness", "Influencer & Creator"), ("Consideration", "Content & Blogger"), ("Purchase", "Affiliates"), ("Retention", "Loyalty & CLO"), ("Advocacy", "Customer Referrals")],
    "pm_stats": [("+91%", "Mehr Conversions"), ("40h", "Zeitersparnis / Monat"), ("3,5×", "Partner-Wachstum")],
    "brands": ["Glossier", "Sephora", "Rituals", "Flaconi", "Charlotte Tilbury"],
    "stmt": "Sie haben bereits **etwas Großes geschaffen** – Ihre Vision, Ihr Angebot, Ihr Unternehmen. Doch wahre Größe entsteht nicht allein. Eine Ansprechpartnerin auf höchstem Niveau — **ein ganzes System dahinter.**",
    "stmt_em": "Genau hier kommen wir ins Spiel: Ihr Partner für den nächsten Schritt.",
    "ap_label": "Unser Ansatz",
    "ap_h2": ("Von der Analyse zur gemeinsamen", "Umsetzung."),
    "ap_sd": "Kein Template. Kein Standardpaket. Wir arbeiten mit einer begrenzten Zahl von Unternehmerinnen pro Jahr – damit jede Architektur trägt.",
    "steps": [
        ("Signature Audit", "Wir analysieren Ihre Marke, Zielgruppe und Wettbewerber im Detail — und identifizieren die größten Wachstumshebel für Ihr Business."),
        ("Growth Architecture", "Auf Basis des Audits entwickeln wir einen individuellen Systemplan mit klaren Meilensteinen und messbaren Zielen für Ihr Wachstum."),
        ("System Activation", "Wir setzen Branding, Content, Partner-Netzwerke und Kampagnen operativ um — nicht nur planen, sondern machen."),
        ("Scale & Optimize", "Wir skalieren, was funktioniert, und eliminieren, was nicht performt. Monatliches Reporting, laufende Optimierung, messbare Ergebnisse."),
    ],
    "res_label": "Ergebnisse",
    "res_h2": ("Zahlen, die für sich", "sprechen."),
    "res_sd": "Unsere Kundinnen wachsen messbar.",
    "results": [("3,2×", "Umsatz-Multiplikator", "Ø Umsatzsteigerung in den ersten 12 Monaten."), ("94%", "Retention Rate", "Unsere Kundinnen bleiben, weil die Ergebnisse stimmen."), ("<90", "Tage bis zum ROI", "Schnelle Ergebnisse durch systemisches Vorgehen.")],
    "t_label": "Growth Stories",
    "t_h2": ("Von sichtbar zu", "unverwechselbar."),
    "testis": [
        ("Female Signature hat unsere Praxis komplett transformiert — von der Markenidentität bis zur Premium-Patientengewinnung.", "Plastische Chirurgin", "Premium-Patienten & Umsatzwachstum"),
        ("Innerhalb weniger Wochen hatten wir ein komplettes Branding, klare Positionierung und die ersten neuen Patienten.", "Zahnärztin", "Branding & Patientenaufbau in Wochen"),
        ("Vom Branding über Neukundengewinnung bis zur Skalierung meines Schulungsprogramms — alles auf höchstem Niveau.", "Podologin", "Branding, Neukunden & Schulungs-Skalierung"),
        ("Mein Umsatz hat sich vervielfacht. Das Referral-Programm bringt jeden Monat neue Kunden — automatisch.", "BeautyLounge", "Referral-Programm & Umsatz vervielfacht"),
        ("Die Neupositionierung war ein Gamechanger. Wir ziehen jetzt genau die Premium-Kunden an, die zu uns passen.", "Hair Atelier", "Neupositionierung & Premium-Kunden"),
        ("Von der Studioeröffnung bis zur vollen Auslastung — Female Signature hat Branding, Performance Marketing und ein Referral-Programm aufgebaut, das konstant neue Kundinnen bringt.", "Studioinhaberin", "Studioeröffnung, Branding & Neukundengewinnung"),
    ],
    "ceo_quote": "Sichtbarkeit ohne Strategie ist Lärm. Strategie ohne Persönlichkeit ist Leere. Wer beides verbindet, hinterlässt eine Signatur — keinen flüchtigen Eindruck.",
    "ceo_bio": "Internationale Unternehmensberaterin. Marketingstrategin. Gründerin. Langjährige Expertise in Beauty, FinTech, Education und Health — mit der Mission, Female Businesses nicht nur sichtbar, sondern profitabel und skalierbar zu machen.",
    "ceo_alt": "Mag. (FH) Mediha Mujcin, CEO und Gründerin von Female Signature",
    "about": "Über uns",
    "blog_label": "Insights",
    "blog_h2": ("Wissen, das Ihr Business", "weiterbringt."),
    "new": "NEU", "read": "Weiterlesen", "all_posts": "Alle Artikel lesen", "blog_index": "/blog/",
    "posts": [
        ("/blog/partnerprogramme-wachstum", "Growth Strategy", "Warum Partnerprogramme der wichtigste Wachstumshebel sind", "Ein System, das für dich arbeitet — auch wenn du es nicht tust."),
        ("/blog/social-media-female-businesses", "Content & Sichtbarkeit", "Social Media für Female Businesses: Warum Reichweite allein nicht reicht", "Reichweite ohne Strategie ist Lärm. Wie du Social Media als Wachstumssystem aufbaust."),
        ("/blog/female-empowerment-business", "Female Empowerment", "Female Empowerment ist kein Trend — es ist ein Markt", "Warum Unternehmerinnen mit diesem Wert einen strategischen Wettbewerbsvorteil haben."),
    ],
    "faq_label": "FAQ",
    "faq_h2": ("Häufige", "Fragen."),
    "faq": [
        ("Was ist Female Signature?", "Female Signature ist eine Growth-Agentur für Female Brands im DACH-Raum: Premium Branding, Creator Partnerships, Content-Strategie und Performance Marketing."),
        ("Was ist ein Signature Audit?", "Ein kostenloser Deep-Dive in Marke, Zielgruppe und Positionierung als Grundlage für einen individuellen Growth-Plan."),
        ("Welche Ergebnisse erzielt Female Signature?", "Durchschnittlich 3,2x Umsatzsteigerung in 12 Monaten, 94% Retention Rate, ROI in unter 90 Tagen."),
    ],
    "cta_label": "Bereit für den nächsten Schritt?",
    "cta_h2": ("Wachstum beginnt mit einem", "Gespräch."),
    "cta_sd": "In einem kostenfreien 30-Minuten-Gespräch prüfen wir gemeinsam, wo Ihr Wachstum aktuell hängt und welche Hebel den größten Unterschied machen.",
    "cta_strong": "Ohne Verpflichtung – nur Klarheit.",
    "form_label": "Kontakt",
    "form_h": ("Schreiben Sie", "uns."),
    "form_sd": "Sie möchten lieber schreiben? Wir melden uns innerhalb von 24 Stunden.",
    "f_name": "Name", "f_mail": "E-Mail", "f_company": "Unternehmen (optional)", "f_msg": "Nachricht", "f_send": "Nachricht senden",
    "ph": {"name": "Ihr Name", "email": "ihre@email.com", "company": "Ihr Unternehmen", "message": "Erzählen Sie uns von Ihrem Projekt..."},
    "ft_text": "Growth Partnership für Unternehmerinnen mit Substanz. Strategische Markenarbeit, Performance-Systeme und Partnerstrukturen.",
    "ft_sys": "Systeme", "ft_company": "Company", "ft_contact": "Kontakt",
    "ft_company_links": [("#about", "Über uns"), ("#results", "Ergebnisse"), ("/blog/", "Blog")],
    "quiz_title": "Signature Quiz", "quiz_open": "Signature Quiz öffnen", "wa_label": "WhatsApp",
    "quiz": [
        {"q": "Hallo! 👋 Was beschreibt dich am besten?", "opts": ["Gründerin / Selbstständig", "Bestehendes Unternehmen", "Agentur / Partner"], "key": "role"},
        {"q": "In welcher Branche bist du tätig?", "opts": ["Beauty & Wellness", "Health & Medical", "Fashion & Lifestyle", "Coaching & Consulting", "Andere"], "key": "industry"},
        {"q": "Was ist deine größte Herausforderung?", "opts": ["Branding & Positionierung", "Sichtbarkeit & Content", "Neukundengewinnung", "Umsatz skalieren"], "key": "challenge"},
        {"q": "Wie hoch ist dein monatlicher Umsatz?", "opts": ["Noch kein Umsatz", "< €5.000", "€5.000 – €20.000", "> €20.000"], "key": "revenue"},
        {"q": "Bitte gib deine E-Mail ein:", "input": True, "key": "email"},
    ],
    "quiz_done": "Danke! 🎉 Wir melden uns in Kürze.", "quiz_ph": "Deine Antwort...", "quiz_send": "Senden",
    "org_desc": "Growth-Agentur für Unternehmerinnen im DACH-Raum: Premium Branding, Partner Marketing & Performance Marketing.",
}

EN = {
    "lang": "en", "locale": "en_GB", "path": "/en/", "other_path": "/", "other_label": "DE",
    "other_name": "Deutsch",
    "title": "Female Signature — Growth Infrastructure for Female Brands",
    "desc": "Strategic brand work, performance systems, and partner structures — for entrepreneurs with an established offer who lack the infrastructure to scale.",
    "og_title": "Female Signature — Growth Infrastructure for Female Brands",
    "og_image": "/images/og-image-en.jpg",
    "skip": "Skip to content",
    "nav": [("#systems", "Systems"), ("#approach", "Approach"), ("#results", "Results"), ("/blog/index-en", "Blog")],
    "menu": "Menu", "close": "Close",
    "cta_short": "Strategy Call",
    "cta": "Book Free Strategy Call",
    "cta30": "Book Free 30-Min. Strategy Call",
    "principles": ["Built, not imagined.", "Strategy over visibility.", "Partnership over service contract.", "Your brand. Our system."],
    "hero_label": "Growth Partnership for Entrepreneurs",
    "h1a": "We don't just build beautiful brands.", "h1b": "We build brands that grow.",
    "hero_sub": "Strategic brand work, performance systems, and partner structures — for entrepreneurs with an established offer who lack the infrastructure to scale.",
    "hero_btn2": "Explore our Systems",
    "stories_link": "Growth Stories",
    "region": "Aldrans, Tyrol · DACH",
    "trust_line": "Our clients grow measurably.",
    "call_label": "Free Strategy Call",
    "pain_label": "Does this sound familiar?",
    "pain_h2": ("The reality of many", "female businesses."),
    "solution": "Our Solution",
    "pains": [
        ("Invisible despite a great offer", "Your offer is first-class. But between your product and market perception lies a gap that even the best product cannot close on its own.", "Magnetic Visibility System — visibility that converts."),
        ("No clear premium positioning", "Without clear positioning, price becomes the only comparison. That is the most expensive mistake a good business can make.", "Signature Brand Experience — positioning that attracts premium clients."),
        ("Revenue stagnates despite hard work", "More hours eventually stop generating more revenue. Beyond that point, growth needs a system that works independently of your time.", "Revenue Performance System — data-driven growth with clear ROI."),
        ("Your core business suffers from marketing chaos", "You are the expert at what you do. Marketing is not your craft — and it shouldn't have to be.", "We handle the marketing — you focus on what you do best."),
        ("Growth fails without a plan", "Investment budget is only as good as the plan behind it. Without clear architecture, resources flow into activity instead of results.", "Flexible models that scale with your business — with clear ROI from day one."),
        ("Lack of strategy & automation", "Activity is not strategy. Posts, ads, and campaigns without a system produce noise — not return.", "Growth Architecture — a system that works for you, even when you don't."),
    ],
    "sys_label": "What We Build",
    "sys_h2": ("Four systems. One goal:", "Your growth."),
    "sys_sd": "No isolated tactics. We build connected infrastructure that turns visibility into revenue — in the right order.",
    "systems": [
        ("Brand Experience", "Your product or service is world-class. Your brand just doesn't tell that story yet.", "We develop brand identities that make the true value of your offer visible — positioning, visual system, brand voice, and an experience that attracts premium clients and makes price discussions obsolete.",
         ["Strategic positioning & differentiation", "Brand Identity & Design", "Copy & tone of voice that resonates with your clients", "Website & customer experience that turns visitors into clients"]),
        ("Content & Visibility", "You're the expert. But nobody knows it — because your content isn't working for you.", "We build content systems that organically create reach and make your expertise visible — without you having to post every day. A visibility strategy with lasting impact that attracts clients.",
         ["Social media & community building", "Content strategy & editorial planning", "Email marketing & CRM systems", "Organic reach & brand awareness"]),
        ("Partnership Marketing", "Your growth depends on your time. That needs to stop.", "Others recommend you — and you earn from it. We build partner networks of creators, affiliates, and happy customers who refer your offer.",
         ["Referral & affiliate programs", "Creator & influencer collaborations", "Automated partner management", "Commission models & revenue sharing"]),
        ("Performance Marketing", "You invest in marketing. But do you know what's actually working?", "We run data-driven campaigns where every euro invested is traceable. From awareness to conversion — always transparent, always optimized, always with clear ROI.",
         ["Paid social & search campaigns", "Conversion optimization & A/B testing", "Real-time reporting & dashboards", "ROI tracking & budget optimization"]),
    ],
    "pm_label": "Partnership Marketing",
    "pm_h2": ("One platform. All", "partnerships."),
    "pm_sd": "Influencers, creators, affiliates, loyalty — in most companies, these channels run separately. We unify them on a single platform. Every partner, every click, every conversion — measurable, automated, under your control.",
    "pm_list": ["All partner types in one system — no more silos", "Full-funnel tracking from awareness to advocacy", "Access to a global network of partners, influencers, and creators", "Automated workflows — 10–40 hours saved per month", "GDPR-compliant, fraud-protected, globally scalable"],
    "pm_panel": "Partnership Automation Platform",
    "pm_cycle_t": "The Complete Partnership Lifecycle",
    "pm_cycle": [("Awareness", "Influencer & Creator"), ("Consideration", "Content & Blogger"), ("Purchase", "Affiliates"), ("Retention", "Loyalty & CLO"), ("Advocacy", "Customer Referrals")],
    "pm_stats": [("+91%", "More Conversions"), ("40h", "Time Saved / Month"), ("3.5×", "Partnership Growth")],
    "brands": ["Glossier", "Sephora", "Rituals", "Flaconi", "Charlotte Tilbury"],
    "stmt": "You've already **built something great** – your vision, your offer, your company. But true greatness doesn't happen alone. One point of contact at the highest level — **an entire system behind it.**",
    "stmt_em": "That's where we come in: your partner for the next step.",
    "ap_label": "Our Approach",
    "ap_h2": ("From analysis to shared", "execution."),
    "ap_sd": "No templates. No standard packages. We work with a limited number of entrepreneurs per year — so every architecture holds.",
    "steps": [
        ("Signature Audit", "We analyze your brand, audience, and competitors in detail — identifying the biggest growth levers for your business."),
        ("Growth Architecture", "Based on the audit, we develop a custom system plan with clear milestones and measurable goals for your growth."),
        ("System Activation", "We implement branding, content, partner networks, and campaigns operationally — not just planning, but doing."),
        ("Scale & Optimize", "We scale what works and eliminate what doesn't. Monthly reporting, ongoing optimization, measurable results."),
    ],
    "res_label": "Results",
    "res_h2": ("Numbers that speak for", "themselves."),
    "res_sd": "Our clients grow measurably.",
    "results": [("3.2×", "Revenue Multiplier", "Avg. revenue increase within the first 12 months."), ("94%", "Retention Rate", "Our clients stay because results speak for themselves."), ("<90", "Days to ROI", "Fast results through systematic execution.")],
    "t_label": "Growth Stories",
    "t_h2": ("From visible to", "unmistakable."),
    "testis": [
        ("Female Signature completely transformed our practice — from brand identity to premium patient acquisition.", "Plastic Surgeon", "Premium patients & revenue growth"),
        ("Within weeks we had complete branding, clear positioning, and our first new patients.", "Dentist", "Branding & patient acquisition in weeks"),
        ("From branding to client acquisition to scaling my training program — everything at the highest level.", "Podiatrist", "Branding, new clients & training scale"),
        ("My revenue multiplied. The referral program brings new clients every month — automatically.", "BeautyLounge", "Referral program & revenue multiplied"),
        ("The repositioning was a gamechanger. We now attract exactly the premium clients that fit our brand.", "Hair Atelier", "Repositioning & premium clients"),
        ("From studio launch to full capacity — Female Signature built branding, performance marketing, and a referral program that consistently brings new clients.", "Studio Owner", "Studio launch, branding & client acquisition"),
    ],
    "ceo_quote": "Visibility without strategy is noise. Strategy without personality is emptiness. Those who combine both leave a signature — not a fleeting impression.",
    "ceo_bio": "International business consultant. Marketing strategist. Founder. Deep expertise across beauty, fintech, education, and health — on a mission to make female businesses not just visible, but profitable and scalable.",
    "ceo_alt": "Mag. (FH) Mediha Mujcin, CEO & Founder of Female Signature",
    "about": "About",
    "blog_label": "Insights",
    "blog_h2": ("Knowledge that moves your", "business forward."),
    "new": "NEW", "read": "Read more", "all_posts": "Read all articles", "blog_index": "/blog/index-en",
    "posts": [
        ("/blog/partnerprogramme-wachstum-en", "Growth Strategy", "Why Partner Programs Are the Most Important Growth Lever for Female Businesses", "A system that works for you — even when you're not."),
        ("/blog/social-media-female-businesses-en", "Content & Visibility", "Social Media for Female Businesses: Why Reach Alone Is Not Enough", "Reach without strategy is noise. How to build social media as a growth system."),
        ("/blog/female-empowerment-business-en", "Female Empowerment", "Female Empowerment Is Not a Trend — It's a Market", "Why entrepreneurs who live this value have a strategic competitive advantage."),
    ],
    "faq": [],  # Englische FAQ gibt es noch nicht; nicht übersetzen, erst von Marlene liefern lassen.
    "cta_label": "Ready for the next step?",
    "cta_h2": ("Growth begins with a", "conversation."),
    "cta_sd": "In a free 30-minute call, we assess together where your growth is stalling and which levers make the biggest difference.",
    "cta_strong": "No obligation — just clarity.",
    "form_label": "Contact",
    "form_h": ("Get in", "touch."),
    "form_sd": "Prefer to write? We'll get back to you within 24 hours.",
    "f_name": "Name", "f_mail": "E-Mail", "f_company": "Company (optional)", "f_msg": "Message", "f_send": "Send Message",
    "ph": {},
    "ft_text": "Growth partnership for founders with substance. Strategic brand work, performance systems, and partner structures.",
    "ft_sys": "Systems", "ft_company": "Company", "ft_contact": "Contact",
    "ft_company_links": [("#about", "About"), ("#results", "Results"), ("/blog/index-en", "Blog")],
    "quiz_title": "Signature Quiz", "quiz_open": "Signature Quiz", "wa_label": "WhatsApp",
    "quiz": [
        {"q": "Hello! 👋 What describes you best?", "opts": ["Founder / Self-employed", "Existing Business", "Agency / Partner"], "key": "role"},
        {"q": "What industry are you in?", "opts": ["Beauty & Wellness", "Health & Medical", "Fashion & Lifestyle", "Coaching & Consulting", "Other"], "key": "industry"},
        {"q": "What is your biggest challenge?", "opts": ["Branding & Positioning", "Visibility & Content", "Client Acquisition", "Scaling Revenue"], "key": "challenge"},
        {"q": "What is your monthly revenue?", "opts": ["No revenue yet", "< €5,000", "€5,000 – €20,000", "> €20,000"], "key": "revenue"},
        {"q": "Please enter your email:", "input": True, "key": "email"},
    ],
    "quiz_done": "Thank you! 🎉 We'll get back to you shortly.", "quiz_ph": "Your answer...", "quiz_send": "Send",
    "org_desc": "Growth agency for female entrepreneurs in the DACH region: premium branding, partner marketing & performance marketing.",
}


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


ICON_CHECK = '<svg class="ic" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_ARROW = '<svg class="ic" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h12m-5-5 5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor"/></svg>'
ICON_LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4v11H3zm7 0h3.8v1.6h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1v6.35h-4v-5.63c0-1.34-.02-3.07-1.87-3.07-1.87 0-2.16 1.46-2.16 2.97v5.73h-4z"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.2A9.8 9.8 0 0 0 3.6 17l-1.4 4.8 4.9-1.3A9.8 9.8 0 1 0 12 2.2zm0 17.8a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20zm4.4-6c-.2-.1-1.4-.7-1.7-.8-.2-.1-.4-.1-.5.1l-.8 1c-.1.2-.3.2-.5.1a6.6 6.6 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.5-.4h-.5a.9.9 0 0 0-.7.3 2.8 2.8 0 0 0-.9 2.1 4.9 4.9 0 0 0 1 2.6 11.2 11.2 0 0 0 4.3 3.8c1.6.7 2.2.7 3 .6.5-.1 1.4-.6 1.6-1.1.2-.6.2-1 .1-1.1l-.5-.3z"/></svg>'
ICON_CHAT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H10l-4.5 4v-4h0A1.5 1.5 0 0 1 4 14.5z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M8.5 8.5h7M8.5 11.5h4.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'


IMG_W = {"s": (600, 900, 1200), "p": (480, 720, 960), "b": (480, 720, 960), "c": (800, 1400, 2000)}


def pic(name, kind, sizes, ratio, alt=""):
    ws = IMG_W[kind]
    w = ws[1]
    h = round(w / ratio)
    srcset = ", ".join(f"/images/opt/{name}-{x}.webp {x}w" for x in ws)
    return (f'<img src="/images/opt/{name}-{w}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{esc(alt)}" loading="lazy" decoding="async">')


def bold(t):
    parts = esc(t).split("**")
    return "".join(f"<strong>{x}</strong>" if i % 2 else x for i, x in enumerate(parts))


def h2(parts, cls="h2"):
    a, b = parts
    return f'<h2 class="{cls}">{esc(a)} <em>{esc(b)}</em></h2>'


def schema(T):
    lang = T["lang"]
    url = SITE + T["path"]
    org = {
        "@type": ["Organization", "ProfessionalService"],
        "@id": SITE + "/#org",
        "name": "Female Signature",
        "url": SITE + "/",
        "logo": SITE + "/images/monogram-square-burgundy.svg",
        "image": SITE + "/images/og-image.jpg",
        "description": T["org_desc"],
        "email": MAIL,
        "telephone": TEL,
        "priceRange": "€€€",
        "address": {"@type": "PostalAddress", "streetAddress": "Aste 10", "addressLocality": "Aldrans", "postalCode": "6071", "addressRegion": "Tirol", "addressCountry": "AT"},
        "areaServed": [{"@type": "Country", "name": n} for n in ("Austria", "Germany", "Switzerland")],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"},
        "founder": {"@id": SITE + "/#mediha"},
        "knowsAbout": [s[0] for s in DE["systems"]] + ["Affiliate Marketing", "Creator Partnerships", "Branding"],
        "sameAs": [IG, LI],
    }
    person = {
        "@type": "Person", "@id": SITE + "/#mediha", "name": "Mediha Mujcin", "honorificPrefix": "Mag. (FH)",
        "jobTitle": "CEO & Founder", "worksFor": {"@id": SITE + "/#org"},
        "image": SITE + "/images/opt/mediha-600.webp", "sameAs": [LI],
    }
    website = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Female Signature", "publisher": {"@id": SITE + "/#org"}, "inLanguage": ["de", "en"]}
    page = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": T["title"], "description": T["desc"], "inLanguage": lang,
            "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#org"}, "dateModified": TODAY,
            "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + T["og_image"], "width": 1200, "height": 630}}
    graph = [org, person, website, page]
    if T["faq"]:
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in T["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


CSS = r"""
@font-face{font-family:Montserrat;font-style:normal;font-weight:400 700;font-display:swap;src:url(/fonts/montserrat-normal-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Playfair Display";font-style:italic;font-weight:400 600;font-display:swap;src:url(/fonts/playfair-display-italic-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Playfair Display";font-style:normal;font-weight:400 600;font-display:swap;src:url(/fonts/playfair-display-normal-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
:root{--bg:#fff;--ow:#F4F1EB;--card:#FBFAF7;--ink:#1C1C1C;--fr:#5C1F2B;--fd:#4A1822;--bd:#E8E5DE;--mu:#5F5A55;--r:24px;--pad:clamp(20px,5vw,48px);--max:1200px;--sans:Montserrat,"Helvetica Neue",Arial,sans-serif;--serif:"Playfair Display",Georgia,"Times New Roman",serif;--ease:cubic-bezier(.16,1,.3,1)}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:88px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
body{margin:0;background:var(--bg);color:var(--ink);font:400 1rem/1.65 var(--sans);-webkit-font-smoothing:antialiased;overflow-x:clip}
@media (min-width:900px){body{font-size:1.0625rem}}
img,svg{display:block;max-width:100%}
img{height:auto}
a{color:inherit}
h1,h2,h3,p,ul,ol,blockquote,figure,dl,dd{margin:0}
ul{padding:0;list-style:none}
em{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--fr);letter-spacing:0}
:focus-visible{outline:2px solid var(--fr);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:12px;top:-60px;z-index:100;background:var(--ink);color:#fff;padding:10px 16px;border-radius:999px;text-decoration:none;font-weight:600}
.skip:focus{top:12px}
.wrap{width:100%;max-width:var(--max);margin:0 auto;padding:0 var(--pad)}
.sec{padding:clamp(72px,10vw,128px) 0}
.ow{background:var(--ow)}
.ic{width:1.1em;height:1.1em;flex:none}
.label{display:inline-flex;align-items:center;gap:10px;font-size:.75rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--fr);margin-bottom:20px}
.label::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--fr)}
.h2{font-size:clamp(2rem,1.2rem + 3.4vw,3.5rem);line-height:1.08;font-weight:600;letter-spacing:-.025em;max-width:18ch;text-wrap:balance}
.lead{font-size:clamp(1.0625rem,1rem + .3vw,1.1875rem);color:var(--mu);max-width:60ch;margin-top:20px;text-wrap:pretty}
.head{margin-bottom:clamp(40px,6vw,64px)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;background:var(--ink);color:#fff;font-weight:600;font-size:.9375rem;text-decoration:none;border:1px solid var(--ink);transition:background .3s var(--ease),border-color .3s var(--ease),transform .3s var(--ease);cursor:pointer;font-family:inherit;text-align:center}
.btn:hover{background:var(--fr);border-color:var(--fr)}
.btn:active{transform:scale(.98)}
@media (max-width:479px){.btn{font-size:.875rem;padding:14px 20px}.acts .btn,.ap .btn{width:100%}}
.btn.ghost{background:transparent;color:var(--ink);border-color:#cfcac2}
.btn.ghost:hover{border-color:var(--ink);background:transparent}
.btn .ic{transition:transform .3s var(--ease)}
.btn:hover .ic{transform:translateX(3px)}
.acts{display:flex;flex-wrap:wrap;gap:12px;margin-top:36px}
.link{display:inline-flex;align-items:center;gap:8px;font-weight:600;text-decoration:none;color:var(--fr);min-height:44px}
.link:hover{text-decoration:underline;text-underline-offset:4px}

/* Header */
.hd{position:fixed;inset:0 0 auto;z-index:50;background:rgba(255,255,255,.86);-webkit-backdrop-filter:saturate(1.4) blur(14px);backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid transparent;transition:border-color .3s}
.hd.sc{border-color:var(--bd)}
.hd:not(.sc){background:transparent;-webkit-backdrop-filter:none;backdrop-filter:none}
.hd .wrap{max-width:none;display:flex;align-items:center;justify-content:space-between;gap:24px;height:72px}
.logo{display:flex;align-items:center;min-height:44px}
.logo img{width:clamp(168px,22vw,220px);height:auto}
.nav{display:none;align-items:center;gap:6px}
.nav a{display:inline-flex;align-items:center;min-height:44px;padding:10px 14px;border-radius:999px;text-decoration:none;font-size:.875rem;font-weight:500;color:var(--ink)}
.nav a:hover{background:var(--ow)}
.nav .lang{font-weight:600;letter-spacing:.06em}
.nav .btn{min-height:44px;padding:10px 20px;margin-left:8px;color:#fff;font-size:.875rem}
.nav .btn:hover{background:var(--fr)}
.mbtn{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:999px;border:1px solid var(--bd);background:#fff;cursor:pointer;padding:0}
.mbtn span{position:relative;width:18px;height:1.5px;background:var(--ink)}
.mbtn span::before,.mbtn span::after{content:"";position:absolute;left:0;width:18px;height:1.5px;background:var(--ink);transition:transform .3s var(--ease)}
.mbtn span::before{top:-6px}.mbtn span::after{top:6px}
.mbtn[aria-expanded=true] span{background:transparent}
.mbtn[aria-expanded=true] span::before{transform:translateY(6px) rotate(45deg)}
.mbtn[aria-expanded=true] span::after{transform:translateY(-6px) rotate(-45deg)}
.mnav{position:fixed;inset:72px 0 auto;z-index:49;background:#fff;border-bottom:1px solid var(--bd);padding:12px var(--pad) 28px;display:grid;gap:4px;box-shadow:0 24px 48px -24px rgba(28,28,28,.25)}
.mnav[hidden]{display:none}
.mnav a{display:flex;align-items:center;min-height:52px;font-size:1.125rem;font-weight:500;text-decoration:none;border-bottom:1px solid var(--bd)}
.mnav .btn{margin-top:16px;border-bottom:0;color:#fff;font-size:1rem}
@media (min-width:1000px){.nav{display:flex}.mbtn,.mnav{display:none!important}}

/* Hero: Foto links randlos mit Markenname, Aussage rechts */
.hero{--mf:clamp(3.25rem,16vw,6.5rem);position:relative;background:var(--ow);overflow:hidden;padding:72px 0 64px}
@media (max-width:999px){.hd:not(.sc){background:var(--ow)}}
.hero-img{position:relative;margin:0;height:min(124vw,660px);border-radius:0 0 28px 28px;overflow:hidden;background:#e6e0d6}
.hero-img .par{position:absolute;inset:0 0 -10%}
.hero-img img{width:100%;height:100%;object-fit:cover;object-position:50% 0}
.hero-img::before{content:"";display:none;position:absolute;inset:0 0 auto;height:18%;background:linear-gradient(to bottom,rgba(244,241,235,.7),rgba(244,241,235,0));pointer-events:none;z-index:1}
.hero-img::after{content:"";position:absolute;inset:auto 0 0;height:55%;background:linear-gradient(to top,rgba(20,18,18,.7) 0%,rgba(20,18,18,.35) 45%,rgba(20,18,18,0));pointer-events:none;z-index:1}
.mega{position:absolute;left:var(--pad);bottom:calc(var(--mf) * .16 + 16px);z-index:2;margin:0;font-size:var(--mf);font-weight:500;letter-spacing:-.045em;line-height:.92;color:var(--ow);white-space:nowrap}
.mega em{display:block;color:var(--ow);letter-spacing:-.015em}
.loc{position:absolute;left:var(--pad);bottom:calc(var(--mf) * 2 + 36px);z-index:2;margin:0;display:flex;align-items:center;gap:12px;font-size:.6875rem;font-weight:600;letter-spacing:.18em;line-height:1.6;text-transform:uppercase;color:var(--ow)}
.loc::before{content:"";width:28px;height:1px;background:currentColor;opacity:.7}
.hero-txt{padding:48px var(--pad) 0}
.eyebrow{display:flex;align-items:center;gap:14px;margin:0 0 28px;font-size:.6875rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--fr)}
.eyebrow::before{content:"";width:36px;height:1px;background:var(--fr)}
.hero .h1{font-size:clamp(2.125rem,1.5rem + 1.9vw,3.375rem);font-weight:500;line-height:1.08;letter-spacing:-.035em;max-width:15ch;text-wrap:balance}
.hero .h1 em{display:block;margin-top:.08em;font-size:1.04em;letter-spacing:-.02em}
.hero .lead{margin-top:24px;max-width:44ch;font-size:clamp(1rem,.95rem + .2vw,1.125rem);line-height:1.75}
.hero .acts{align-items:center;gap:8px 28px;margin-top:36px}
.hero .acts .btn{min-height:56px;padding:16px 28px}
@media (max-width:479px){.hero .acts{justify-content:center}}
.textlink{display:inline-flex;align-items:center;gap:10px;min-height:44px;font-weight:600;font-size:.9375rem;text-decoration:none;color:var(--ink);border-bottom:1px solid transparent}
.textlink:hover{border-color:var(--ink)}
.trust{display:flex;align-items:center;flex-wrap:wrap;gap:14px;margin-top:32px}
.faces{display:flex}
.faces img{width:40px;height:40px;border-radius:50%;border:2px solid var(--ow);object-fit:cover;background:var(--ow)}
.faces img+img{margin-left:-10px}
.trust p{flex:1;min-width:170px;margin:0;font-size:.875rem;line-height:1.45;color:var(--mu)}
.trust a{color:var(--ink);font-weight:600;text-decoration:none;border-bottom:1px solid #cfc8bd}
.trust a:hover{border-color:var(--ink)}
.kpis{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:48px 0 0;border-top:1px solid #d9d2c7}
.kpis div{padding:22px 16px 0 0}
.kpis div+div{padding-left:clamp(14px,2vw,28px);border-left:1px solid #d9d2c7}
.kpis dt{font-size:clamp(1.75rem,1.3rem + 1.4vw,2.625rem);font-weight:500;letter-spacing:-.04em;line-height:1;color:var(--ink)}
.kpis dd{margin:10px 0 0;font-size:.75rem;line-height:1.45;color:var(--mu)}
@media (min-width:1000px){
.hero{--mf:clamp(4.5rem,8.2vw,10.5rem);min-height:clamp(700px,100svh,1040px);padding:0}
.hero-img{position:absolute;top:0;left:0;bottom:0;width:50%;height:auto;border-radius:0 0 48px 0}
.hero-img::before{display:block}
.mega{bottom:calc(var(--mf) * .2 + 24px)}
.loc{bottom:calc(var(--mf) * 2.04 + 48px)}
.hero-txt{margin-left:50%;min-height:inherit;display:flex;flex-direction:column;justify-content:center;padding:clamp(96px,12vh,128px) clamp(40px,5vw,96px) clamp(32px,5vh,56px) clamp(40px,6vw,112px)}
.hero .lead{margin-top:clamp(16px,2.4vh,24px)}
.hero .acts{margin-top:clamp(24px,3.6vh,36px)}
.kpis{margin-top:clamp(32px,5vh,72px)}
}
@media (prefers-reduced-motion:no-preference){
.hero-img img{animation:hz 1.8s var(--ease) both}
.mega{animation:mu 1.1s var(--ease) .2s both}
.hero-txt>*,.loc{animation:fu .9s var(--ease) both}
.hero-txt>:nth-child(2){animation-delay:.08s}.hero-txt>:nth-child(3){animation-delay:.16s}.hero-txt>:nth-child(4){animation-delay:.24s}.hero-txt>:nth-child(5){animation-delay:.32s}.hero-txt>:nth-child(6){animation-delay:.4s}.loc{animation-delay:.35s}
@keyframes hz{from{transform:scale(1.06)}}
@keyframes mu{from{opacity:0;transform:translateY(24%)}}
@keyframes fu{from{opacity:0;transform:translateY(16px)}}
@supports (animation-timeline:scroll()){.hero-img .par{animation:px linear both;animation-timeline:scroll(root);animation-range:0 100vh}@keyframes px{to{transform:translateY(-8%)}}}
}

/* Marquee */
.mq{border-block:1px solid var(--bd);background:var(--ow);overflow:hidden;padding:22px 0}
.mq ul{display:flex;width:max-content;gap:48px;animation:mq 42s linear infinite}
.mq li{display:flex;align-items:center;gap:48px;font-family:var(--serif);font-style:italic;font-size:clamp(1.25rem,1rem + 1vw,1.75rem);white-space:nowrap;color:var(--ink)}
.mq li::after{content:"✦";font-style:normal;font-size:.8rem;color:var(--fr)}
@keyframes mq{to{transform:translateX(-50%)}}
.mq:hover ul{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.mq ul{flex-wrap:wrap;width:auto;justify-content:center;gap:16px 40px;padding:0 var(--pad)}.mq li[aria-hidden]{display:none}}

/* Abschnitte im Vosello-Stil: warme Fläche, weiche Karten, Fotos mit tiefem Schatten */
main{background:var(--ow)}
.sec{padding:clamp(72px,10vw,136px) 0}
.ow{background:var(--ow)}
.card{background:var(--card);border-radius:22px;padding:clamp(22px,2.6vw,32px)}
.h2{font-weight:500;letter-spacing:-.035em}
.center{text-align:center}.center .h2,.center .lead{margin-left:auto;margin-right:auto}
.shot{position:relative;min-width:0;overflow:hidden;border-radius:16px;background:#e6e0d6;box-shadow:0 34px 60px -28px rgba(40,22,22,.55),0 14px 26px -14px rgba(40,22,22,.35)}
.shot img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s var(--ease)}
a:hover>.shot img,.zoomhover:hover .shot img{transform:scale(1.035)}
.pill{display:inline-flex;align-items:center;min-height:28px;padding:4px 12px;border-radius:999px;background:var(--ow);font-size:.75rem;font-weight:500;color:var(--mu)}
.btn.soft{background:#E7E1D7;border-color:#E7E1D7;color:var(--ink)}
.btn.soft:hover{background:#dcd4c8;border-color:#dcd4c8}
.btn.light{background:var(--ow);border-color:var(--ow);color:var(--ink)}
.btn.light:hover{background:#fff;border-color:#fff}
.btn{box-shadow:0 10px 22px -12px rgba(28,28,28,.55)}
.btn.ghost,.btn.soft{box-shadow:none}
.grid{display:grid;gap:16px}
@media (min-width:700px){.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){.g3{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:699px){.snap{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 calc(var(--pad)*-1);padding:0 var(--pad) 12px;scrollbar-width:none}.snap::-webkit-scrollbar{display:none}.snap>*{flex:0 0 86%;scroll-snap-align:center}}
.ic{width:1.1em;height:1.1em;flex:none}
.num{font-size:.75rem;font-weight:600;letter-spacing:.14em;color:var(--fr)}

/* Herausforderungen */
/* Realität: links feste Spalte, rechts ziehen Problem und Lösung vorbei (nach Neiden "What we build"); Handy: Slider nach rechts */
.pl{display:grid;gap:clamp(32px,5vw,64px)}
.pl .head{margin:0}
.pctr{display:flex;align-items:center;gap:16px;margin-top:28px;font-size:.8125rem;font-weight:600;letter-spacing:.14em;color:var(--mu)}
.pctr b{font-weight:600;color:var(--fr);min-width:2ch}
.pctr i{flex:0 0 120px;height:2px;background:var(--bd);position:relative;overflow:hidden}
.pctr i::after{content:"";position:absolute;inset:0;background:var(--fr);transform-origin:0 50%;transform:scaleX(var(--pp,.1667));transition:transform .6s var(--ease)}
.pl .head .btn{margin-top:36px}
.pi{display:flex;flex-direction:column;background:var(--card);border-radius:22px;padding:24px}
.pi{cursor:pointer;-webkit-tap-highlight-color:transparent}.pi:focus-visible{outline:2px solid var(--fr);outline-offset:4px}
.pi .n{font-size:.75rem;font-weight:600;letter-spacing:.14em;color:var(--fr)}
.pi .n span{color:var(--mu)}
.pi h3{margin-top:14px;font-size:clamp(1.25rem,1rem + 1.2vw,2.25rem);line-height:1.12;font-weight:500;letter-spacing:-.035em}
.pi .pb{display:grid;gap:20px;margin-top:18px;flex:1}
.pi .pb>p{margin:0;color:var(--mu)}
.pi .sol{align-self:end;border-top:2px solid var(--fr);padding-top:14px}
.pi .sol small{display:block;font-size:.6875rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--fr);margin-bottom:6px}
.pi .sol p{margin:0;font-weight:500;font-size:.9375rem;line-height:1.55}
@media (max-width:999px){.pil{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 calc(var(--pad)*-1);padding:0 var(--pad) 12px;scrollbar-width:none;scroll-padding-inline:var(--pad)}.pil::-webkit-scrollbar{display:none}.pi{flex:0 0 min(86%,440px);scroll-snap-align:start}.pl .head .btn{display:none}}
@media (min-width:1000px){
.pl{grid-template-columns:minmax(0,.8fr) minmax(0,1.45fr);gap:0 clamp(48px,6vw,96px);align-items:start}
.pl .head{position:sticky;top:120px}
.pil{border-left:1px solid var(--bd)}
.pi{background:none;border-radius:0;padding:clamp(40px,5vh,64px) 0 clamp(40px,5vh,64px) clamp(32px,4vw,56px);border-bottom:1px solid var(--bd);min-height:min(62vh,560px);justify-content:center}
.pi:first-child{padding-top:0;min-height:0}
.pi .pb{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,3vw,48px);margin-top:28px;flex:0}
.pi .sol{align-self:start;background:var(--card);border-top:0;border-left:2px solid var(--fr);border-radius:0 14px 14px 0;padding:18px 20px}
.pi:last-child{border-bottom:0}
}
@media (min-width:1000px) and (prefers-reduced-motion:no-preference){
.js .pi>*,.js .pi h3,.js .pi .n,.js .pi .sol,.js .pi .sol small{transition:color .6s var(--ease),border-color .6s var(--ease),background-color .6s var(--ease),transform .7s var(--ease)}
.js .pi:not(.act)>*{transform:translateX(18px)}
.js .pi:not(.act) h3{color:#857E77}
.js .pi:not(.act) .n,.js .pi:not(.act) .pb>p,.js .pi:not(.act) .sol small,.js .pi:not(.act) .sol p{color:#6F6963}
.js .pi:not(.act) .sol{transform:translateX(36px);border-left-color:#D9D2C7;background-color:transparent}
}

/* Systeme: wechselnde Bild-Text-Karten */
.sysl{display:grid;gap:20px}
.sysc{display:grid;gap:clamp(20px,3vw,40px);align-items:stretch}
.sysc>*{min-width:0}
.sysc .shot{aspect-ratio:4/3;align-self:center}
.sysc .txt{display:flex;flex-direction:column;padding:clamp(4px,1vw,12px) clamp(0px,1vw,12px)}
.sysc .top{display:flex;align-items:center;gap:12px;margin-bottom:18px}
.sysc h3{font-size:clamp(1.375rem,1.1rem + 1vw,2rem);line-height:1.15;font-weight:500;letter-spacing:-.03em}
.sysc .txt>p{color:var(--mu);margin-top:14px}
.ticks{display:grid;gap:10px;margin-top:24px}
.ticks li{display:flex;gap:12px;align-items:flex-start;font-size:.9375rem;font-weight:500}
.ticks .ic{color:var(--fr);margin-top:.25em}
.sysc .foot{margin-top:auto;padding-top:24px;display:flex;gap:8px;flex-wrap:wrap}
@media (min-width:900px){.sysc{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}.sysc:nth-child(even) .shot{order:2}}
/* Gestapelte Karten wie Vosello "Recent talks": jede Karte bleibt oben stehen, die nächste schiebt sich darüber, die untere wird kleiner */
@media (min-width:900px) and (min-height:700px){.sysl{gap:40px;padding-bottom:8px}.sysc{position:sticky;top:calc(104px + var(--i) * 18px);transform-origin:50% 0;box-shadow:0 -24px 48px -36px rgba(40,22,22,.45),0 0 0 1px rgba(40,22,22,.04);will-change:scale}.sysc.rv{animation:none}}

/* Partnership */
.pmc{display:grid;gap:clamp(28px,4vw,56px);align-items:center}
.pmc .ticks{margin-top:28px}
.panel{background:var(--fr);color:var(--ow);border-radius:20px;padding:clamp(24px,3.4vw,40px);box-shadow:0 34px 60px -28px rgba(60,16,26,.6)}
.panel .pt{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;padding-bottom:20px;border-bottom:1px solid rgba(244,241,235,.2)}
.panel .pt strong{font-size:1.0625rem;font-weight:600}
.panel .pt span{font-size:.8125rem;opacity:.85}
.panel h3{font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin:24px 0 8px;opacity:.85}
.cycle li{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid rgba(244,241,235,.14);font-size:.9375rem}
.cycle li span:first-child{font-family:var(--serif);font-style:italic;font-size:1.0625rem}
.cycle li span:last-child{opacity:.9;text-align:right}
.stats3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:24px}
.stats3 div{background:rgba(244,241,235,.08);border-radius:14px;padding:16px 12px}
.stats3 b{display:block;font-size:clamp(1.5rem,1.2rem + 1vw,2rem);font-weight:600;letter-spacing:-.02em}
.stats3 span{font-size:.75rem;line-height:1.35;display:block;margin-top:4px;opacity:.9}
.brands{display:flex;flex-wrap:wrap;justify-content:center;gap:12px 44px;margin-top:clamp(36px,5vw,56px)}
.brands li{font-family:var(--serif);font-size:clamp(1.125rem,1rem + .5vw,1.5rem);color:#6f6a64}
@media (min-width:1000px){.pmc{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}

/* Manifest: großes zentriertes Zitat mit hervorgehobenen Wörtern */
.quote{max-width:30ch;margin:0 auto;text-align:center;font-size:clamp(1.5rem,1.05rem + 1.9vw,2.5rem);line-height:1.3;letter-spacing:-.025em;font-weight:400;text-wrap:balance}
.quote strong{font-weight:600}
.quote em{display:block;margin-top:.5em}
.by{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:32px;font-size:.875rem}
.by img{width:44px;height:44px;border-radius:50%;box-shadow:0 8px 18px -8px rgba(40,22,22,.6)}
.by span{display:block;color:var(--mu);font-size:.75rem}

/* Ansatz */
.ap{display:grid;gap:clamp(36px,5vw,72px)}
.ap .btn{margin-top:28px}
.ap .shot{aspect-ratio:4/5;margin-top:40px;max-width:420px}
.steps{display:grid;gap:12px;list-style:none;margin:0;padding:0}
.step{display:grid;grid-template-columns:auto 1fr;gap:12px 20px}
.step .n{font-family:var(--serif);font-style:italic;font-size:2rem;line-height:1;color:var(--fr);width:2.2ch}
.step h3{font-size:1.1875rem;font-weight:600}
.step p{color:var(--mu);margin-top:8px}
@media (min-width:1000px){.ap{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}.ap .sticky{position:sticky;top:110px;align-self:start}}

/* Ergebnisse */
.res .card{text-align:center;padding:clamp(28px,3vw,44px) 20px}
.res b{display:block;font-size:clamp(2.75rem,2rem + 3vw,4.25rem);line-height:1;font-weight:500;letter-spacing:-.045em;color:var(--fr);font-variant-numeric:tabular-nums}
.res strong{display:block;margin-top:18px;font-weight:600}
.res p{color:var(--mu);margin-top:6px;font-size:.9375rem;max-width:30ch;margin-left:auto;margin-right:auto}

/* Growth Stories */
.feat{max-width:860px;margin:0 auto clamp(48px,6vw,72px);text-align:center}
.feat blockquote{font-size:clamp(1.375rem,1rem + 1.6vw,2.25rem);line-height:1.32;letter-spacing:-.025em;text-wrap:balance}
.feat figcaption{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:28px;text-align:left;font-size:.9375rem}
.feat figcaption img{width:52px;height:52px;border-radius:50%;object-fit:cover;box-shadow:0 8px 18px -8px rgba(40,22,22,.6)}
.feat figcaption span{display:block;font-size:.8125rem;color:var(--mu)}
.tcards{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px var(--pad) 24px;margin:0 calc(var(--pad)*-1);scrollbar-width:none}
.tcards::-webkit-scrollbar{display:none}
.tcards figure{flex:0 0 min(86%,380px);scroll-snap-align:start;margin:0;display:flex;flex-direction:column}
.tq{font-size:1.0625rem;line-height:1.6}
.tq::before{content:"“";display:block;font-family:var(--serif);font-size:3rem;line-height:.6;color:var(--fr);margin-bottom:12px}
.out{margin-top:16px;align-self:flex-start;font-size:.8125rem;font-weight:500;color:var(--fr)}
.who{display:flex;align-items:center;gap:14px;margin-top:auto;padding-top:24px}
.who img{width:48px;height:48px;border-radius:50%;object-fit:cover}
.who strong{display:block;font-size:.9375rem}
.who span{font-size:.8125rem;color:var(--mu)}
.tnav{display:flex;justify-content:flex-end;gap:8px;margin-top:8px}
.tnav button{width:48px;height:48px;border-radius:50%;border:1px solid #d6cfc4;background:transparent;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;color:var(--ink)}
.tnav button:hover{background:var(--card)}
.tnav button:first-child .ic{transform:rotate(180deg)}
@media (min-width:1000px){.tcards{margin:0;padding:4px 0 24px}}

/* Über Mediha */
.aboutc{display:grid;gap:clamp(28px,4vw,56px);padding:clamp(22px,3vw,40px)}
.aboutc>*{min-width:0}
.aboutc .shot{aspect-ratio:4/5;align-self:start}
.aboutc .txt{display:flex;flex-direction:column}
.aboutc h2{font-size:clamp(2.25rem,1.4rem + 3.4vw,4rem);line-height:1;font-weight:500;letter-spacing:-.045em}
.aboutc blockquote{font-family:var(--serif);font-style:italic;color:var(--fr);font-size:clamp(1.25rem,1rem + 1vw,1.75rem);line-height:1.35;margin-top:24px}
.aboutc .role{display:block;margin-top:24px;font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--mu)}
.aboutc .bio{color:var(--mu);margin-top:12px;max-width:52ch}
.aboutc .acts{margin-top:28px}
@media (min-width:900px){.aboutc{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr)}.aboutc .txt{padding:clamp(8px,2vw,24px)}}

/* Blog */
.row{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}
.post{display:block;text-decoration:none}
.post .shot{aspect-ratio:4/3}
.post h3{font-size:clamp(1.1875rem,1rem + .6vw,1.5rem);line-height:1.2;font-weight:500;letter-spacing:-.025em;margin-top:22px}
.post p{color:var(--mu);margin-top:8px;font-size:.9375rem}
.post .meta{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.post .meta .new{background:var(--fr);color:#fff}
.post:hover h3{text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}

/* FAQ */
.faq{display:grid;gap:clamp(28px,4vw,64px)}
.faq .list{display:grid;gap:10px}
.faq details{background:var(--card);border-radius:14px;padding:0 20px}
.faq summary{list-style:none;display:flex;justify-content:space-between;align-items:center;gap:20px;min-height:60px;padding:14px 0;cursor:pointer;font-weight:600;font-size:1.0625rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";flex:none;width:12px;height:12px;border-right:1.6px solid var(--ink);border-bottom:1.6px solid var(--ink);transform:translateY(-3px) rotate(45deg);transition:transform .3s var(--ease)}
.faq details[open] summary::after{transform:translateY(2px) rotate(-135deg)}
.faq details p{color:var(--mu);padding:0 0 20px;max-width:62ch}
@media (min-width:1000px){.faq{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}}

/* Abschluss: Vollbild-Foto mit Aufruf */
.ctab{position:relative;overflow:hidden;border-radius:clamp(20px,2.4vw,32px);min-height:clamp(460px,62vw,640px);display:grid;place-items:center;text-align:center;color:var(--ow);padding:clamp(48px,7vw,96px) var(--pad);box-shadow:0 40px 80px -40px rgba(40,22,22,.7)}
.ctab>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ctab::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(20,14,14,.62),rgba(20,14,14,.42) 60%,rgba(20,14,14,.55))}
.ctab>div{position:relative;z-index:1;max-width:640px}
.ctab .h2{color:var(--ow);margin:0 auto;font-size:clamp(2.25rem,1.4rem + 3.6vw,4.25rem)}
.ctab .h2 em{color:var(--ow)}
.ctab .lead{color:rgba(244,241,235,.86);margin:20px auto 0}
.ctab .lead strong{color:var(--ow)}
.ctab .acts{justify-content:center}
.ctab .label{color:var(--ow)}.ctab .label::before{background:var(--ow)}
.ctawrap{padding:0 clamp(8px,1.4vw,20px) clamp(72px,10vw,136px)}

/* Kontakt */
.contact{display:grid;gap:clamp(28px,4vw,56px)}
.direct{display:grid;gap:4px;margin-top:28px}
.direct a{display:inline-flex;align-items:center;gap:12px;min-height:44px;text-decoration:none;font-weight:500}
.direct a:hover{color:var(--fr)}
.direct svg{width:20px;height:20px;color:var(--fr)}
.form>p{color:var(--mu);margin:8px 0 24px}
.form h3{font-size:1.375rem;font-weight:600;letter-spacing:-.01em}
.f2{display:grid;gap:16px}
@media (min-width:600px){.f2{grid-template-columns:1fr 1fr}}
.fld{display:grid;gap:6px;margin-bottom:16px}
.f2 .fld{margin:0}
.fld label{font-size:.8125rem;font-weight:600}
.fld input,.fld textarea{width:100%;font:inherit;font-size:1rem;color:var(--ink);background:#fff;border:1px solid #ddd6cb;border-radius:12px;padding:14px 16px;min-height:52px;transition:border-color .2s}
.fld textarea{min-height:140px;resize:vertical;line-height:1.55}
.fld input:focus,.fld textarea:focus{outline:none;border-color:var(--fr);box-shadow:0 0 0 3px rgba(92,31,43,.12)}
.hp{position:absolute!important;left:-9999px;width:1px;height:1px;overflow:hidden}
.form .btn{width:100%;margin-top:8px}
@media (min-width:1000px){.contact{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);align-items:start}}

/* Scroll-Effekte nur per CSS: Fotos zoomen beim Hereinscrollen sanft auf */
@media (prefers-reduced-motion:no-preference){@supports (animation-timeline:view()){
.shot img{animation:zin linear both;animation-timeline:view();animation-range:entry 0% cover 45%}
@keyframes zin{from{transform:scale(1.14)}}
.ctab>img{animation:zin2 linear both;animation-timeline:view();animation-range:entry 0% exit 100%}
@keyframes zin2{from{transform:scale(1.18)}to{transform:scale(1)}}
}}

/* Footer */
.ft{background:var(--ow);border-top:1px solid #e2dbd0;padding:clamp(64px,8vw,96px) 0 32px;font-size:.9375rem}
.ftg{display:grid;gap:40px}
.ft .brand img{width:150px;height:auto}
.ft .brand p{color:var(--mu);margin-top:20px;max-width:36ch}
.soc{display:flex;gap:8px;margin-top:20px}
.soc a{display:inline-flex;width:44px;height:44px;border-radius:50%;align-items:center;justify-content:center;border:1px solid #d6d1c8}
.soc a:hover{border-color:var(--fr);color:var(--fr)}
.soc svg{width:18px;height:18px}
.ft h2{font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--fr);margin-bottom:12px}
.ft nav a{display:flex;align-items:center;min-height:44px;text-decoration:none}
.ft nav a:hover{color:var(--fr)}
.fb{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px 24px;margin-top:56px;padding-top:24px;border-top:1px solid #dcd6cc;font-size:.8125rem;color:var(--mu)}
.fb nav{display:flex;gap:20px}
.fb a{min-height:44px;display:inline-flex;align-items:center;text-decoration:none}
.fb a:hover{color:var(--ink)}
@media (min-width:700px){.ftg{grid-template-columns:1.6fr 1fr 1fr 1.2fr}}

/* Schwebende Knöpfe + Quiz */
.fab{position:fixed;right:16px;bottom:16px;z-index:40;display:grid;gap:10px;transition:opacity .3s,transform .3s var(--ease)}
.fab.off{opacity:0;transform:translateY(16px);pointer-events:none;visibility:hidden}
@media (max-width:699px){.fab a,.fab button{width:50px;height:50px}.fab svg{width:23px;height:23px}}
.fab a,.fab button{width:56px;height:56px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;border:0;cursor:pointer;box-shadow:0 10px 28px -10px rgba(28,28,28,.45);transition:transform .3s var(--ease)}
.fab a:hover,.fab button:hover{transform:translateY(-2px)}
.fab svg{width:26px;height:26px}
.fab .wa{background:#fff;color:#128C4A}
.fab .qz{background:var(--fr);color:#fff}
.quiz{position:fixed;right:16px;bottom:16px;z-index:60;width:min(380px,calc(100vw - 32px));max-height:min(620px,calc(100dvh - 32px));display:flex;flex-direction:column;background:#fff;border-radius:var(--r);box-shadow:0 30px 80px -20px rgba(28,28,28,.45);overflow:hidden}
.quiz[hidden]{display:none}
.quiz .qh{display:flex;justify-content:space-between;align-items:center;padding:16px 16px 16px 22px;background:var(--fr);color:#fff}
.quiz .qh h2{font-size:1rem;font-weight:600}
.quiz .qh button{width:44px;height:44px;border-radius:50%;border:0;background:rgba(255,255,255,.12);color:#fff;font-size:1.125rem;cursor:pointer}
.qb{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:10px;min-height:200px}
.msg{max-width:85%;padding:10px 14px;border-radius:16px;font-size:.9375rem;line-height:1.45}
.msg.bot{background:var(--ow);align-self:flex-start;border-bottom-left-radius:4px}
.msg.user{background:var(--ink);color:#fff;align-self:flex-end;border-bottom-right-radius:4px}
.qo{display:flex;flex-wrap:wrap;gap:8px;padding:0 20px 20px}
.qo button{font:inherit;font-size:.875rem;font-weight:500;min-height:44px;padding:8px 14px;border-radius:999px;border:1px solid var(--bd);background:#fff;cursor:pointer}
.qo button:hover{border-color:var(--fr);color:var(--fr)}
.qi{display:flex;gap:8px;padding:0 20px 20px}
.qi[hidden]{display:none}
.qi input{flex:1;min-width:0;font:inherit;font-size:1rem;border:1px solid #d6d1c8;border-radius:999px;padding:0 16px;min-height:48px}
.qi button{min-height:48px;padding:0 18px}

/* Sanftes Einblenden, nur wo der Browser es nativ kann (kein JS, kein Layout-Shift) */
@media (prefers-reduced-motion:no-preference){@supports (animation-timeline:view()){.rv{animation:rv linear both;animation-timeline:view();animation-range:entry 0% entry 45%}@keyframes rv{from{opacity:0;transform:translateY(28px)}}}}
"""

JS = r"""
(function(){
var d=document,hd=d.querySelector('.hd'),mb=d.querySelector('.mbtn'),mn=d.getElementById('mnav');
var pis=[].slice.call(d.querySelectorAll('.pi')),pc=d.querySelector('.pctr'),pl=d.querySelector('.pil');if(pis.length>1&&pc&&pl){var pa=-1,wide=matchMedia('(min-width:1000px)'),pset=function(i){if(i===pa)return;pa=i;pis.forEach(function(x,k){x.classList.toggle('act',k===i)});pc.firstChild.textContent=(i<9?'0':'')+(i+1);pc.style.setProperty('--pp',((i+1)/pis.length).toFixed(4))};pset(0);
if('IntersectionObserver'in window){var pio=new IntersectionObserver(function(es){if(!wide.matches)return;d.documentElement.classList.add('js');es.forEach(function(e){if(e.isIntersecting)pset(pis.indexOf(e.target))})},{rootMargin:'-45% 0px -45% 0px'});pis.forEach(function(x){pio.observe(x)})}
pl.addEventListener('scroll',function(){if(wide.matches)return;var w=pis[1].offsetLeft-pis[0].offsetLeft;pset(pl.scrollLeft>=pl.scrollWidth-pl.clientWidth-4?pis.length-1:Math.round(pl.scrollLeft/w))},{passive:true})
var prm=matchMedia('(prefers-reduced-motion: reduce)'),phold=0,pvis=false,pgo=function(i){i=(i+pis.length)%pis.length;pl.scrollTo({left:pis[i].offsetLeft-pis[0].offsetLeft,behavior:prm.matches?'auto':'smooth'})},pstop=function(){phold=Date.now()+12000};
if('IntersectionObserver'in window)new IntersectionObserver(function(e){pvis=e[0].isIntersecting},{threshold:.5}).observe(pl);
setInterval(function(){if(wide.matches||prm.matches||!pvis||d.hidden||Date.now()<phold)return;pgo(pa+1)},4500);
['touchstart','pointerdown','wheel'].forEach(function(t){pl.addEventListener(t,pstop,{passive:true})});
pis.forEach(function(x,k){var f=function(){pstop();if(wide.matches)x.scrollIntoView({block:'center',behavior:prm.matches?'auto':'smooth'});else pgo(k===pa?k+1:k)};x.addEventListener('click',f);x.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();f()}})})}
var sk=[].slice.call(d.querySelectorAll('.sysc')),smq=matchMedia('(min-width:900px) and (min-height:700px) and (prefers-reduced-motion:no-preference)'),stt=0;function stk(){stt=0;var on=smq.matches;sk.forEach(function(c,i){var n=sk[i+1];if(!on||!n){c.style.scale='';return}var r=c.getBoundingClientRect(),p=Math.min(1,Math.max(0,(r.bottom-n.getBoundingClientRect().top)/r.height));c.style.scale=(1-p*.07).toFixed(4)})}addEventListener('scroll',function(){if(!stt)stt=requestAnimationFrame(stk)},{passive:true});addEventListener('resize',stk);stk();
function sc(){hd.classList.toggle('sc',scrollY>8)}addEventListener('scroll',sc,{passive:true});requestAnimationFrame(sc);
function closeNav(){mn.hidden=true;mb.setAttribute('aria-expanded','false');mb.setAttribute('aria-label',mb.dataset.open)}
mb.addEventListener('click',function(){var o=mn.hidden;mn.hidden=!o;mb.setAttribute('aria-expanded',String(o));mb.setAttribute('aria-label',o?mb.dataset.close:mb.dataset.open)});
mn.addEventListener('click',function(e){if(e.target.closest('a'))closeNav()});
d.addEventListener('keydown',function(e){if(e.key==='Escape'){if(!mn.hidden){closeNav();mb.focus()}if(!qz.hidden)toggleQuiz(false)}});
/* Schwebende Knöpfe erst nach dem Startbereich, damit sie den Hauptknopf nicht verdecken */
var fab=d.querySelector('.fab'),hero=d.querySelector('.hero');if('IntersectionObserver'in window){new IntersectionObserver(function(e){fab.classList.toggle('off',e[0].isIntersecting)},{rootMargin:'-35% 0px 0px 0px'}).observe(hero)}else fab.classList.remove('off');
/* Kundenstimmen blättern */
var tc=d.getElementById('tcards');d.querySelectorAll('.tnav button').forEach(function(b){b.addEventListener('click',function(){var c=tc.querySelector('figure');tc.scrollBy({left:(+b.dataset.dir)*(c.offsetWidth+16),behavior:'smooth'})})});
/* Ergebnisse zählen beim Hereinscrollen hoch (Endwert steht im HTML) */
if('IntersectionObserver'in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;io.unobserve(e.target);var el=e.target,t=el.textContent,m=t.match(/[\d.,]+/);if(!m)return;var end=parseFloat(m[0].replace(',','.')),dec=(m[0].split(/[.,]/)[1]||'').length,sep=m[0].indexOf(',')>-1?',':'.',t0=performance.now();(function f(n){var k=Math.min(1,(n-t0)/1400),v=(end*(1-Math.pow(1-k,3))).toFixed(dec).replace('.',sep);el.textContent=t.replace(m[0],v);if(k<1)requestAnimationFrame(f);else el.textContent=t})(t0)})},{threshold:.6});d.querySelectorAll('[data-count]').forEach(function(el){io.observe(el)})}
/* Quiz */
var Q=JSON.parse(d.getElementById('quiz-data').textContent),qz=d.getElementById('quiz'),qb=d.getElementById('qb'),qo=d.getElementById('qo'),qi=d.getElementById('qi'),inp=qi.querySelector('input'),opener=d.getElementById('qopen'),step=0,data={};
function msg(t,x){var m=d.createElement('div');m.className='msg '+t;m.textContent=x;qb.appendChild(m);qb.scrollTop=qb.scrollHeight}
function show(){qo.innerHTML='';qi.hidden=true;if(step>=Q.steps.length){send();msg('bot',Q.done);var a=d.createElement('a');a.className='btn ghost';a.href=Q.wa;a.target='_blank';a.rel='noopener';a.textContent='WhatsApp';qo.appendChild(a);return}var s=Q.steps[step];msg('bot',s.q);if(s.opts){s.opts.forEach(function(o){var b=d.createElement('button');b.type='button';b.textContent=o;b.onclick=function(){data[s.key]=o;msg('user',o);step++;setTimeout(show,250)};qo.appendChild(b)});qo.firstChild&&qo.firstChild.focus()}else{qi.hidden=false;inp.focus()}}
qi.addEventListener('submit',function(e){e.preventDefault();var v=inp.value.trim();if(!v||!inp.checkValidity())return;data[Q.steps[step].key]=v;msg('user',v);inp.value='';step++;setTimeout(show,250)});
function send(){var p=new URLSearchParams({'form-name':'signature-quiz'});for(var k in data)p.append(k,data[k]);fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:p.toString()}).catch(function(){})}
function toggleQuiz(open){qz.hidden=!open;opener.setAttribute('aria-expanded',String(open));if(open){if(!qb.children.length){step=0;data={};show()}else{qz.querySelector('.qh button').focus()}}else opener.focus()}
opener.addEventListener('click',function(){toggleQuiz(qz.hidden)});
qz.querySelector('.qh button').addEventListener('click',function(){toggleQuiz(false)});
})();
"""


def page(T):
    L = T["lang"]
    url = SITE + T["path"]
    alt_de, alt_en = SITE + "/", SITE + "/en/"
    pre = "" if L == "de" else "../"  # nicht genutzt, alle Pfade absolut
    face_imgs = "".join(
        f'<img src="/images/opt/{img}-96.webp" width="44" height="44" alt="" loading="lazy" decoding="async">' for img, _ in PEOPLE[:5])

    kpis = "".join(f"<div><dt>{esc(n)}</dt><dd>{esc(u)}</dd></div>" for n, u, _ in T["results"])
    nav = "".join(f'<a href="{h}">{esc(t)}</a>' for h, t in T["nav"])
    lang_link = f'<a class="lang" href="{T["other_path"]}" hreflang="{"en" if L == "de" else "de"}" lang="{"en" if L == "de" else "de"}" aria-label="{T["other_label"]}, {esc(T["other_name"])}">{T["other_label"]}</a>'

    np = len(T["pains"])
    pains = "".join(
        f'<article class="pi" tabindex="0"><p class="n">{i + 1:02d} <span>/ {np:02d}</span></p><h3>{esc(h)}</h3><div class="pb"><p>{esc(p)}</p>'
        f'<div class="sol"><small>{esc(T["solution"])}</small><p>{esc(s)}</p></div></div></article>'
        for i, (h, p, s) in enumerate(T["pains"]))

    sys_imgs = ["s1-brand", "s2-content", "s3-partnership", "s4-performance"]
    systems = "".join(
        f'<article class="card sysc rv zoomhover" style="--i:{i}"><div class="shot">{pic(sys_imgs[i], "s", "(min-width:900px) 560px, 92vw", 4 / 3)}</div>'
        f'<div class="txt"><div class="top"><span class="num">0{i + 1}</span><span class="pill">{esc(n)}</span></div>'
        f'<h3>{esc(h)}</h3><p>{esc(p)}</p><ul class="ticks">'
        + "".join(f"<li>{ICON_CHECK}<span>{esc(x)}</span></li>" for x in items) + "</ul></div></article>"
        for i, (n, h, p, items) in enumerate(T["systems"]))

    pm_list = "".join(f"<li>{ICON_CHECK}<span>{esc(x)}</span></li>" for x in T["pm_list"])
    cycle = "".join(f"<li><span>{esc(a)}</span><span>{esc(b)}</span></li>" for a, b in T["pm_cycle"])
    stats3 = "".join(f"<div><b>{esc(a)}</b><span>{esc(b)}</span></div>" for a, b in T["pm_stats"])
    brands = "".join(f"<li>{esc(b)}</li>" for b in T["brands"])

    steps = "".join(
        f'<li class="card step rv"><span class="n" aria-hidden="true">0{i + 1}</span><div><h3>{esc(h)}</h3><p>{esc(p)}</p></div></li>'
        for i, (h, p) in enumerate(T["steps"]))

    results = "".join(
        f'<div class="card rv"><b data-count>{esc(n)}</b><strong>{esc(u)}</strong><p>{esc(d)}</p></div>'
        for n, u, d in T["results"])

    def tcard(img, name, q, role, o):
        return (f'<figure class="card"><blockquote class="tq"><p>{esc(q)}</p></blockquote><span class="out">→ {esc(o)}</span>'
                f'<figcaption class="who"><img src="/images/opt/{img}-96.webp" srcset="/images/opt/{img}-96.webp 96w, /images/opt/{img}-192.webp 192w" sizes="48px" width="48" height="48" alt="{esc(name)}" loading="lazy" decoding="async">'
                f'<span><strong>{esc(name)}</strong><span>{esc(role)}</span></span></figcaption></figure>')
    pairs = list(zip(PEOPLE, T["testis"]))
    (fimg, fname), (fq, frole, _) = pairs[5]
    featured = (f'<figure class="feat rv"><blockquote>„{esc(fq)}“</blockquote><figcaption><img src="/images/opt/{fimg}-96.webp" srcset="/images/opt/{fimg}-96.webp 96w, /images/opt/{fimg}-192.webp 192w" sizes="52px" width="52" height="52" alt="{esc(fname)}" loading="lazy" decoding="async">'
                f'<span><strong>{esc(fname)}</strong><span>{esc(frole)}</span></span></figcaption></figure>')
    testis = "".join(tcard(img, name, q, role, o) for (img, name), (q, role, o) in pairs[:5])

    post_imgs = ["blog-1", "blog-2", "blog-3"]
    posts = "".join(
        f'<a class="post rv" href="{u}"><div class="shot">{pic(post_imgs[i], "b", "(min-width:1000px) 380px, (min-width:700px) 46vw, 86vw", 4 / 3)}</div>'
        f'<h3>{esc(t)}</h3><p>{esc(x)}</p><div class="meta"><span class="pill new">{T["new"]}</span><span class="pill">{esc(c)}</span></div></a>'
        for i, (u, c, t, x) in enumerate(T["posts"]))

    faq_html = ""
    if T["faq"]:
        items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in T["faq"])
        faq_html = (f'<section class="sec" id="faq" aria-labelledby="faq-h"><div class="wrap faq"><div><p class="label">{T["faq_label"]}</p>'
                    + h2(T["faq_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="faq-h">') + f'</div><div class="list rv">{items}</div></div></section>')

    ph = T["ph"]
    def p_(k):
        return f' placeholder="{esc(ph[k])}"' if k in ph else ""

    sys_links = "".join(f'<a href="#systems">{esc(s[0])}</a>' for s in T["systems"])
    comp_links = "".join(f'<a href="{h}">{esc(t)}</a>' for h, t in T["ft_company_links"])
    quiz_json = json.dumps({"steps": T["quiz"], "done": T["quiz_done"], "wa": WA}, ensure_ascii=False).replace("</", "<\\/")
    principles = "".join(f"<li>{esc(p)}</li>" for p in T["principles"]) + "".join(f'<li aria-hidden="true">{esc(p)}</li>' for p in T["principles"])

    stmt_bg = "ow"
    return f"""<!DOCTYPE html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(T["title"])}</title>
<meta name="description" content="{esc(T["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="de" href="{alt_de}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="x-default" href="{alt_de}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#ffffff">
<meta name="author" content="Female Signature">
<meta name="impact-site-verification" value="11bb3694-0e20-43ed-9167-6fac7198a3c9">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Female Signature">
<meta property="og:locale" content="{T["locale"]}">
<meta property="og:locale:alternate" content="{"en_GB" if L == "de" else "de_AT"}">
<meta property="og:title" content="{esc(T["og_title"])}">
<meta property="og:description" content="{esc(T["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{T["og_image"]}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(T["h1a"] + " " + T["h1b"])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(T["og_title"])}">
<meta name="twitter:description" content="{esc(T["desc"])}">
<meta name="twitter:image" content="{SITE}{T["og_image"]}">
<link rel="icon" href="/images/monogram-square-burgundy.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/montserrat-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" as="image" type="image/webp" imagesrcset="/images/opt/hero-mediha-480.webp 480w, /images/opt/hero-mediha-720.webp 720w, /images/opt/hero-mediha-960.webp 960w, /images/opt/hero-mediha-1024.webp 1024w" imagesizes="(min-width:1000px) 50vw, 100vw" fetchpriority="high">
<style>{CSS.strip()}</style>
<script type="application/ld+json">{schema(T)}</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VXL6C4DDES"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-VXL6C4DDES");</script>
</head>
<body>
<a class="skip" href="#main">{esc(T["skip"])}</a>

<form name="signature-quiz" netlify netlify-honeypot="bot-field" hidden><input name="bot-field"><input name="role"><input name="industry"><input name="challenge"><input name="revenue"><input name="email"></form>

<header class="hd">
<div class="wrap">
<a class="logo" href="{T["path"]}" aria-label="Female Signature"><img src="/images/wordmark-primary-anthracite.svg" width="1475" height="115" alt="Female Signature"></a>
<nav class="nav" aria-label="{"Hauptnavigation" if L == "de" else "Main navigation"}">{nav}{lang_link}<a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta_short"])}</a></nav>
<button class="mbtn" type="button" aria-controls="mnav" aria-expanded="false" aria-label="{T["menu"]}" data-open="{T["menu"]}" data-close="{T["close"]}"><span></span></button>
</div>
</header>
<nav class="mnav" id="mnav" hidden aria-label="{"Mobile Navigation" if L == "de" else "Mobile navigation"}">{nav}{lang_link.replace('class="lang" ', '')}<a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])}</a></nav>

<main id="main">
<section class="hero" aria-labelledby="h1">
<figure class="hero-img">
<div class="par"><img src="/images/opt/hero-mediha-960.webp" srcset="/images/opt/hero-mediha-480.webp 480w, /images/opt/hero-mediha-720.webp 720w, /images/opt/hero-mediha-960.webp 960w, /images/opt/hero-mediha-1024.webp 1024w" sizes="(min-width:1000px) 50vw, 100vw" width="1024" height="1536" alt="{esc(T["ceo_alt"])}" fetchpriority="high" decoding="async"></div>
<p class="loc">{esc(T["region"])}</p>
<p class="mega" aria-hidden="true">Female <em>Signature</em></p>
</figure>
<div class="hero-txt">
<p class="eyebrow">{esc(T["hero_label"])}</p>
<h1 class="h1" id="h1">{esc(T["h1a"])} <em>{esc(T["h1b"])}</em></h1>
<p class="lead">{esc(T["hero_sub"])}</p>
<div class="acts"><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a><a class="textlink" href="#systems">{esc(T["hero_btn2"])}</a></div>
<div class="trust"><div class="faces">{face_imgs}</div><p><a href="#stories">{esc(T["stories_link"])}</a><br>{esc(T["trust_line"])}</p></div>
<dl class="kpis">{kpis}</dl>
</div>
</section>

<div class="mq"><ul>{principles}</ul></div>

<section class="sec" aria-labelledby="pain-h">
<div class="wrap">
<div class="pl">
<div class="head"><p class="label">{esc(T["pain_label"])}</p>{h2(T["pain_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="pain-h">')}<p class="pctr" aria-hidden="true"><b>01</b><i></i><span>{np:02d}</span></p><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a></div>
<div class="pil">{pains}</div>
</div>
</div>
</section>

<section class="sec" id="systems" aria-labelledby="sys-h" style="padding-top:0">
<div class="wrap">
<div class="head"><p class="label">{esc(T["sys_label"])}</p>{h2(T["sys_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="sys-h">')}<p class="lead">{esc(T["sys_sd"])}</p></div>
<div class="sysl">{systems}</div>
<div class="acts" style="justify-content:center;margin-top:40px"><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a></div>
</div>
</section>

<section class="sec" aria-labelledby="pm-h" style="padding-top:0">
<div class="wrap">
<div class="card pmc">
<div><p class="label">{esc(T["pm_label"])}</p>{h2(T["pm_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="pm-h">')}<p class="lead">{esc(T["pm_sd"])}</p><ul class="ticks">{pm_list}</ul></div>
<div class="panel rv"><div class="pt"><strong>{esc(T["pm_panel"])}</strong><span>powered by <b>impact.com</b></span></div><h3>{esc(T["pm_cycle_t"])}</h3><ul class="cycle">{cycle}</ul><div class="stats3">{stats3}</div></div>
</div>
<ul class="brands">{brands}</ul>
</div>
</section>

<section class="sec" style="padding-top:0"><div class="wrap">
<p class="quote rv">{bold(T["stmt"])} <em>{esc(T["stmt_em"])}</em></p>
<p class="by"><img src="/images/monogram-square-burgundy.svg" width="44" height="44" alt=""><span><strong>Female Signature</strong><span>Mag. (FH) Mediha Mujcin</span></span></p>
</div></section>

<section class="sec" id="approach" aria-labelledby="ap-h" style="padding-top:0">
<div class="wrap ap">
<div class="sticky"><p class="label">{esc(T["ap_label"])}</p>{h2(T["ap_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="ap-h">')}<p class="lead">{esc(T["ap_sd"])}</p><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a>
<div class="shot">{pic("approach", "p", "(min-width:1000px) 420px, 92vw", 4 / 5)}</div></div>
<ol class="steps">{steps}</ol>
</div>
</section>

<section class="sec res" id="results" aria-labelledby="res-h" style="padding-top:0">
<div class="wrap">
<div class="head center"><p class="label">{esc(T["res_label"])}</p>{h2(T["res_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="res-h">')}<p class="lead">{esc(T["res_sd"])}</p></div>
<div class="grid g3">{results}</div>
</div>
</section>

<section class="sec" id="stories" aria-labelledby="t-h" style="padding-top:0">
<div class="wrap">
<div class="head center"><p class="label">{esc(T["t_label"])}</p>{h2(T["t_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="t-h">')}</div>
{featured}
<div class="tcards" id="tcards" tabindex="0" aria-label="{esc(T["t_label"])}">{testis}</div>
<div class="tnav"><button type="button" data-dir="-1" aria-label="{"Zurück" if L == "de" else "Previous"}">{ICON_ARROW}</button><button type="button" data-dir="1" aria-label="{"Weiter" if L == "de" else "Next"}">{ICON_ARROW}</button></div>
</div>
</section>

<section class="sec" id="about" aria-labelledby="about-h" style="padding-top:0">
<div class="wrap">
<div class="card aboutc">
<div class="txt rv"><p class="label">{esc(T["about"])}</p><h2 id="about-h">Mediha Mujcin</h2><blockquote>{esc(T["ceo_quote"])}</blockquote><span class="role">Mag. (FH) · CEO &amp; Founder</span><p class="bio">{esc(T["ceo_bio"])}</p>
<div class="acts"><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a><a class="btn soft" href="{LI}" target="_blank" rel="noopener">LinkedIn {ICON_ARROW}</a></div></div>
<div class="shot">{pic("about", "p", "(min-width:900px) 480px, 92vw", 4 / 5, T["ceo_alt"])}</div>
</div>
</div>
</section>

<section class="sec" aria-labelledby="blog-h" style="padding-top:0">
<div class="wrap">
<div class="head row"><div><p class="label">{esc(T["blog_label"])}</p>{h2(T["blog_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="blog-h">')}</div><a class="textlink" href="{T["blog_index"]}">{esc(T["all_posts"])} {ICON_ARROW}</a></div>
<div class="grid g3">{posts}</div>
</div>
</section>

{faq_html}

<div class="ctawrap">
<section class="ctab" aria-labelledby="cta-h">
{pic("cta", "c", "100vw", 21 / 9)}
<div class="rv"><p class="label">{esc(T["cta_label"])}</p>{h2(T["cta_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="cta-h">')}<p class="lead">{esc(T["cta_sd"])} <strong>{esc(T["cta_strong"])}</strong></p>
<div class="acts"><a class="btn light" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta30"])} {ICON_ARROW}</a></div></div>
</section>
</div>

<section class="sec" id="kontakt" aria-labelledby="form-h" style="padding-top:0">
<div class="wrap">
<div class="card contact">
<div><p class="label">{esc(T["form_label"])}</p><h2 class="h2" id="form-h">{esc(T["form_h"][0])} <em>{esc(T["form_h"][1])}</em></h2><p class="lead">{esc(T["form_sd"])}</p>
<div class="direct"><a href="mailto:{MAIL}"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>{MAIL}</a><a href="tel:{TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 3.5h3l1.5 4-2 1.3a11 11 0 0 0 6.2 6.2l1.3-2 4 1.5v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>{TEL_TXT}</a><a href="{WA}" target="_blank" rel="noopener">{ICON_WA}WhatsApp</a></div>
</div>
<form class="form" name="contact" method="POST" action="/success" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="contact">
<p class="hp"><label>Bot <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="f2"><div class="fld"><label for="f-name">{esc(T["f_name"])}</label><input id="f-name" type="text" name="name" autocomplete="name" required{p_("name")}></div><div class="fld"><label for="f-mail">{esc(T["f_mail"])}</label><input id="f-mail" type="email" name="email" autocomplete="email" inputmode="email" required{p_("email")}></div></div>
<div class="fld" style="margin-top:16px"><label for="f-co">{esc(T["f_company"])}</label><input id="f-co" type="text" name="company" autocomplete="organization"{p_("company")}></div>
<div class="fld"><label for="f-msg">{esc(T["f_msg"])}</label><textarea id="f-msg" name="message" required{p_("message")}></textarea></div>
<button class="btn" type="submit">{esc(T["f_send"])} {ICON_ARROW}</button>
</form>
</div>
</div>
</section>
</main>

<footer class="ft">
<div class="wrap">
<div class="ftg">
<div class="brand"><img src="/images/wordmark-stacked-anthracite.svg" width="150" height="80" alt="Female Signature" loading="lazy"><p>{esc(T["ft_text"])}</p><div class="soc"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a><a href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON_LI}</a></div></div>
<nav aria-labelledby="ft-sys"><h2 id="ft-sys">{esc(T["ft_sys"])}</h2>{sys_links}</nav>
<nav aria-labelledby="ft-co"><h2 id="ft-co">{esc(T["ft_company"])}</h2>{comp_links}</nav>
<div><h2>{esc(T["ft_contact"])}</h2><address style="font-style:normal"><nav aria-label="{esc(T["ft_contact"])}"><a href="mailto:{MAIL}">{MAIL}</a><a href="tel:{TEL}">{TEL_TXT}</a></nav><p style="margin-top:8px;color:var(--mu)">Aste 10, 6071 Aldrans, {"Österreich" if L == "de" else "Austria"}</p></address></div>
</div>
<div class="fb"><p>© 2026 Female Signature</p><nav aria-label="Rechtliches"><a href="/impressum">Impressum</a><a href="/datenschutz">Datenschutz</a><a href="{T["other_path"]}" hreflang="{"en" if L == "de" else "de"}" lang="{"en" if L == "de" else "de"}">{esc(T["other_name"])}</a></nav></div>
</div>
</footer>

<div class="fab off"><a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICON_WA}</a><button class="qz" id="qopen" type="button" aria-controls="quiz" aria-expanded="false" aria-label="{esc(T["quiz_open"])}">{ICON_CHAT}</button></div>
<section class="quiz" id="quiz" role="dialog" aria-labelledby="quiz-h" hidden>
<div class="qh"><h2 id="quiz-h">{esc(T["quiz_title"])}</h2><button type="button" aria-label="{T["close"]}">✕</button></div>
<div class="qb" id="qb" aria-live="polite"></div>
<div class="qo" id="qo"></div>
<form class="qi" id="qi" hidden><input type="email" autocomplete="email" inputmode="email" required aria-label="{"E-Mail"}" placeholder="{esc(T["quiz_ph"])}"><button class="btn" type="submit">{esc(T["quiz_send"])}</button></form>
</section>
<script type="application/json" id="quiz-data">{quiz_json}</script>
<script>{JS.strip()}</script>
</body>
</html>
"""


def versioned(html):
    """Hängt an jede lokale Bild- und Schriftadresse einen Inhalts-Fingerabdruck (?v=...).
    Bilder werden 30 Tage im Browser gehalten; ohne Fingerabdruck sähe man nach einem
    Bildtausch weiter das alte Bild."""
    import hashlib
    import re
    cache = {}

    def rep(m):
        path = m.group(0)
        if path not in cache:
            f = ROOT / path.lstrip("/")
            cache[path] = path + "?v=" + hashlib.sha1(f.read_bytes()).hexdigest()[:8] if f.exists() else path
        return cache[path]
    return re.sub(r"/(?:images|fonts)/[\w./-]+\.(?:webp|jpg|png|svg|woff2)(?![\w?])", rep, html)


def main():
    (ROOT / "index.html").write_text(versioned(page(DE)), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(versioned(page(EN)), encoding="utf-8")
    for p in ("index.html", "en/index.html"):
        print(p, (ROOT / p).stat().st_size, "Bytes")


if __name__ == "__main__":
    main()
