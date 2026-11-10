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
    "stmt": "Sie haben bereits etwas Großes geschaffen – Ihre Vision, Ihr Angebot, Ihr Unternehmen. Doch wahre Größe entsteht nicht allein. Eine Ansprechpartnerin auf höchstem Niveau — ein ganzes System dahinter.",
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
    "stmt": "You've already built something great – your vision, your offer, your company. But true greatness doesn't happen alone. One point of contact at the highest level — an entire system behind it.",
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
:root{--bg:#fff;--ow:#F4F1EB;--ink:#1C1C1C;--fr:#5C1F2B;--fd:#4A1822;--bd:#E8E5DE;--mu:#5F5A55;--r:24px;--pad:clamp(20px,5vw,48px);--max:1200px;--sans:Montserrat,"Helvetica Neue",Arial,sans-serif;--serif:"Playfair Display",Georgia,"Times New Roman",serif;--ease:cubic-bezier(.16,1,.3,1)}
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
.link{display:inline-flex;align-items:center;gap:8px;font-weight:600;text-decoration:none;color:var(--fr);min-height:44px}
.link:hover{text-decoration:underline;text-underline-offset:4px}

/* Header */
.hd{position:fixed;inset:0 0 auto;z-index:50;background:rgba(255,255,255,.86);-webkit-backdrop-filter:saturate(1.4) blur(14px);backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid transparent;transition:border-color .3s}
.hd.sc{border-color:var(--bd)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;height:72px}
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

/* Hero */
.hero{padding:clamp(120px,16vw,176px) 0 clamp(56px,8vw,96px)}
.hero .wrap,.pm,.ap,.about,.faq,.contact{grid-template-columns:minmax(0,1fr)}
.hero .wrap{display:grid;gap:clamp(40px,6vw,72px);align-items:end}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px}
.chip{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;border:1px solid var(--bd);background:#fff;font-size:.8125rem;font-weight:500;color:var(--ink)}
.chip.dark{background:var(--ow);border-color:var(--ow)}
.chip .dot{width:7px;height:7px;border-radius:50%;background:var(--fr)}
.h1{font-size:clamp(2.375rem,1.1rem + 4.6vw,4.75rem);line-height:1.02;font-weight:600;letter-spacing:-.035em;text-wrap:balance}
.h1 em{display:block;margin-top:.08em;letter-spacing:-.01em}
.hero .lead{margin-top:28px;max-width:56ch}
.acts{display:flex;flex-wrap:wrap;gap:12px;margin-top:36px}
.trust{display:flex;align-items:center;gap:14px;margin-top:40px;flex-wrap:wrap}
.faces{display:flex}
.faces img{width:44px;height:44px;border-radius:50%;border:2px solid #fff;object-fit:cover;background:var(--ow)}
.faces img+img{margin-left:-12px}
.portrait{position:relative;margin:0;max-width:420px;width:100%;justify-self:start}
.portrait img{width:100%;aspect-ratio:4/5;object-fit:cover;object-position:50% 12%;border-radius:var(--r);background:var(--ow)}
.portrait figcaption{position:absolute;left:14px;right:14px;bottom:14px;background:rgba(255,255,255,.92);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-radius:16px;padding:14px 16px;display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:.8125rem;line-height:1.35}
.portrait figcaption .link{width:44px;height:44px;justify-content:center;border-radius:50%;background:var(--ow)}
.portrait figcaption strong{display:block;font-size:.9375rem}
.portrait figcaption span{color:var(--mu)}
@media (min-width:900px){.hero .wrap{grid-template-columns:minmax(0,1.7fr) minmax(0,.7fr)}.portrait{justify-self:end}}

/* Marquee */
.mq{border-block:1px solid var(--bd);background:var(--ow);overflow:hidden;padding:22px 0}
.mq ul{display:flex;width:max-content;gap:48px;animation:mq 42s linear infinite}
.mq li{display:flex;align-items:center;gap:48px;font-family:var(--serif);font-style:italic;font-size:clamp(1.25rem,1rem + 1vw,1.75rem);white-space:nowrap;color:var(--ink)}
.mq li::after{content:"✦";font-style:normal;font-size:.8rem;color:var(--fr)}
@keyframes mq{to{transform:translateX(-50%)}}
.mq:hover ul{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.mq ul{flex-wrap:wrap;width:auto;justify-content:center;gap:16px 40px;padding:0 var(--pad)}.mq li[aria-hidden]{display:none}}

/* Cards */
.grid{display:grid;gap:16px}
.card{background:#fff;border:1px solid var(--bd);border-radius:var(--r);padding:clamp(24px,3vw,36px);display:flex;flex-direction:column}
.ow .card{border-color:transparent}
.card h3{font-size:1.1875rem;line-height:1.3;font-weight:600;letter-spacing:-.01em}
.card p{color:var(--mu);margin-top:12px}
.num{font-size:.8125rem;font-weight:600;letter-spacing:.12em;color:var(--fr)}
.pain{background:var(--ow);border:0}
.pain .sol{margin-top:auto;padding-top:20px}
.pain .sol div{border-top:1px solid #dcd6cc;padding-top:16px}
.pain .sol small{display:block;font-size:.6875rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--fr);margin-bottom:6px}
.pain .sol p{margin:0;color:var(--ink);font-weight:500;font-size:.9375rem}
@media (min-width:700px){.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){.g3{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:699px){.snap{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 calc(var(--pad)*-1);padding:0 var(--pad) 8px;scrollbar-width:none;-webkit-overflow-scrolling:touch}.snap::-webkit-scrollbar{display:none}.snap>*{flex:0 0 86%;scroll-snap-align:center}}

.sys .top{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:24px}
.sys .tag{font-size:.8125rem;font-weight:600;padding:6px 12px;border-radius:999px;background:var(--ow)}
.sys h3{font-size:clamp(1.25rem,1.1rem + .5vw,1.5rem)}
.ticks{display:grid;gap:12px;margin-top:24px;padding-top:24px;border-top:1px solid var(--bd)}
.ticks li{display:flex;gap:12px;align-items:flex-start;font-size:.9375rem;font-weight:500}
.ticks .ic{color:var(--fr);margin-top:.25em}

/* Partnership */
.pm{display:grid;gap:clamp(40px,6vw,72px);align-items:center}
.pm .ticks{border:0;padding:0;margin-top:32px}
.panel{background:var(--fr);color:var(--ow);border-radius:calc(var(--r) + 4px);padding:clamp(24px,4vw,40px)}
.panel .pt{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;padding-bottom:20px;border-bottom:1px solid rgba(244,241,235,.2)}
.panel .pt strong{font-size:1.0625rem;font-weight:600}
.panel .pt span{font-size:.8125rem;opacity:.85}
.panel h3{font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;margin:24px 0 8px;opacity:.85}
.cycle li{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid rgba(244,241,235,.14);font-size:.9375rem}
.cycle li span:first-child{font-family:var(--serif);font-style:italic;font-size:1.0625rem}
.cycle li span:last-child{opacity:.9;text-align:right}
.stats3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:24px}
.stats3 div{background:rgba(244,241,235,.08);border-radius:16px;padding:16px 12px}
.stats3 b{display:block;font-size:clamp(1.5rem,1.2rem + 1vw,2rem);font-weight:600;letter-spacing:-.02em}
.stats3 span{font-size:.75rem;line-height:1.35;display:block;margin-top:4px;opacity:.9}
.brands{display:flex;flex-wrap:wrap;justify-content:center;gap:12px 40px;margin-top:clamp(48px,6vw,72px);padding-top:32px;border-top:1px solid var(--bd)}
.brands li{font-family:var(--serif);font-size:clamp(1.125rem,1rem + .5vw,1.5rem);color:#6f6a64}
@media (min-width:1000px){.pm{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}

/* Statement */
.stmt p{font-size:clamp(1.375rem,1rem + 1.8vw,2.375rem);line-height:1.35;letter-spacing:-.015em;font-weight:500;max-width:30ch;text-wrap:balance}
.stmt em{display:block;margin-top:.6em}

/* Approach */
.ap{display:grid;gap:clamp(40px,6vw,80px)}
.ap .btn{margin-top:32px}
.steps{display:grid;gap:12px;counter-reset:s}
.step{display:grid;grid-template-columns:auto 1fr;gap:16px 20px;padding:clamp(22px,3vw,28px);border-radius:var(--r);background:#fff;border:1px solid var(--bd)}
.step .n{font-family:var(--serif);font-style:italic;font-size:2rem;line-height:1;color:var(--fr);width:2.2ch}
.step h3{font-size:1.1875rem;font-weight:600}
.step p{color:var(--mu);margin-top:8px}
@media (min-width:1000px){.ap{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)}.ap .sticky{position:sticky;top:120px;align-self:start}}

/* Results */
.res .card{background:var(--ow);border:0;justify-content:space-between;min-height:230px}
.res b{font-size:clamp(3rem,2rem + 4vw,4.75rem);line-height:1;font-weight:600;letter-spacing:-.04em;color:var(--fr)}
.res strong{display:block;margin-top:28px;font-weight:600}
.res p{margin-top:6px}

/* Testimonials */
.tq{font-family:var(--serif);font-size:1.1875rem;line-height:1.5;color:var(--ink)}
.tq::before{content:"“";display:block;font-size:3rem;line-height:.6;color:var(--fr);margin-bottom:12px}
.who{display:flex;align-items:center;gap:14px;margin-top:auto;padding-top:28px}
.who img{width:52px;height:52px;border-radius:50%;object-fit:cover;background:var(--ow)}
.who strong{display:block;font-size:.9375rem}
.who span{font-size:.8125rem;color:var(--mu)}
.out{margin-top:16px;align-self:flex-start;font-size:.8125rem;font-weight:500;color:var(--fr);background:var(--ow);border-radius:999px;padding:6px 12px}
.ow .out{background:#F7F5F0}

/* About */
.about{display:grid;gap:clamp(40px,6vw,80px);align-items:center}
.about img{width:100%;max-width:460px;aspect-ratio:4/5;object-fit:cover;object-position:50% 15%;border-radius:var(--r);background:var(--ow)}
.about blockquote{font-family:var(--serif);font-size:clamp(1.5rem,1.1rem + 1.6vw,2.375rem);line-height:1.3;letter-spacing:-.01em}
.about .role{display:block;margin-top:32px;font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--fr)}
.about .name{display:block;font-size:1.25rem;font-weight:600;margin-top:6px}
.about .bio{color:var(--mu);margin-top:16px;max-width:58ch}
@media (min-width:900px){.about{grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)}}

/* Blog */
.post{position:relative;transition:transform .4s var(--ease),box-shadow .4s var(--ease)}
.post:hover{transform:translateY(-4px);box-shadow:0 24px 48px -28px rgba(28,28,28,.35)}
.post .meta{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:.75rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--mu);margin-bottom:16px}
.post .new{background:var(--fr);color:#fff;border-radius:999px;padding:3px 9px;letter-spacing:.1em}
.post h3 a{text-decoration:none}
.post h3 a::after{content:"";position:absolute;inset:0;border-radius:var(--r)}
.post .more{margin-top:auto;padding-top:24px;display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:.9375rem;color:var(--fr)}
.row{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}

/* FAQ */
.faq{display:grid;gap:clamp(32px,5vw,72px)}
.faq details{border-bottom:1px solid var(--bd)}
.faq summary{list-style:none;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:24px 0;cursor:pointer;font-weight:600;font-size:clamp(1.0625rem,1rem + .3vw,1.25rem);min-height:44px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";flex:none;width:28px;height:28px;border-radius:50%;background:var(--ow) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M10 5v10M5 10h10' stroke='%235C1F2B' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E") center/16px no-repeat;transition:transform .3s var(--ease)}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{color:var(--mu);padding:0 0 24px;max-width:62ch}
@media (min-width:1000px){.faq{grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)}}

/* Kontakt */
.contact{display:grid;gap:clamp(40px,6vw,72px)}
.contact .lead strong{color:var(--ink);font-weight:600}
.direct{display:grid;gap:4px;margin-top:32px}
.direct a{display:inline-flex;align-items:center;gap:12px;min-height:44px;text-decoration:none;font-weight:500}
.direct a:hover{color:var(--fr)}
.direct svg{width:20px;height:20px;color:var(--fr)}
.form{background:#fff;border-radius:var(--r);padding:clamp(24px,4vw,40px);border:1px solid var(--bd)}
.form h3{font-size:1.375rem;font-weight:600;letter-spacing:-.01em}
.form h3 em{font-size:1.1em}
.form>p{color:var(--mu);margin:8px 0 24px}
.f2{display:grid;gap:16px}
@media (min-width:600px){.f2{grid-template-columns:1fr 1fr}}
.fld{display:grid;gap:6px;margin-bottom:16px}
.f2 .fld{margin:0}
.fld label{font-size:.8125rem;font-weight:600}
.fld input,.fld textarea{width:100%;font:inherit;font-size:1rem;color:var(--ink);background:var(--bg);border:1px solid #d6d1c8;border-radius:14px;padding:14px 16px;min-height:52px;transition:border-color .2s}
.fld textarea{min-height:140px;resize:vertical;line-height:1.55}
.fld input:focus,.fld textarea:focus{outline:none;border-color:var(--fr);box-shadow:0 0 0 3px rgba(92,31,43,.12)}
.hp{position:absolute!important;left:-9999px;width:1px;height:1px;overflow:hidden}
.form .btn{width:100%;margin-top:8px}
@media (min-width:1000px){.contact{grid-template-columns:minmax(0,1fr) minmax(0,1fr);align-items:start}}

/* Footer */
.ft{background:var(--bg);border-top:1px solid var(--bd);padding:clamp(64px,8vw,96px) 0 32px;font-size:.9375rem}
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
function sc(){hd.classList.toggle('sc',scrollY>8)}addEventListener('scroll',sc,{passive:true});requestAnimationFrame(sc);
function closeNav(){mn.hidden=true;mb.setAttribute('aria-expanded','false');mb.setAttribute('aria-label',mb.dataset.open)}
mb.addEventListener('click',function(){var o=mn.hidden;mn.hidden=!o;mb.setAttribute('aria-expanded',String(o));mb.setAttribute('aria-label',o?mb.dataset.close:mb.dataset.open)});
mn.addEventListener('click',function(e){if(e.target.closest('a'))closeNav()});
d.addEventListener('keydown',function(e){if(e.key==='Escape'){if(!mn.hidden){closeNav();mb.focus()}if(!qz.hidden)toggleQuiz(false)}});
/* Schwebende Knöpfe erst nach dem Startbereich, damit sie den Hauptknopf nicht verdecken */
var fab=d.querySelector('.fab'),hero=d.querySelector('.hero');if('IntersectionObserver'in window){new IntersectionObserver(function(e){fab.classList.toggle('off',e[0].isIntersecting)},{rootMargin:'-35% 0px 0px 0px'}).observe(hero)}else fab.classList.remove('off');
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

    nav = "".join(f'<a href="{h}">{esc(t)}</a>' for h, t in T["nav"])
    lang_link = f'<a class="lang" href="{T["other_path"]}" hreflang="{"en" if L == "de" else "de"}" lang="{"en" if L == "de" else "de"}" aria-label="{T["other_label"]}, {esc(T["other_name"])}">{T["other_label"]}</a>'

    pains = "".join(
        f'<article class="card pain rv"><h3>{esc(h)}</h3><p>{esc(p)}</p><div class="sol"><div><small>{esc(T["solution"])}</small><p>{esc(s)}</p></div></div></article>'
        for h, p, s in T["pains"])

    systems = "".join(
        f'<article class="card sys rv"><div class="top"><span class="num">0{i + 1}</span><span class="tag">{esc(n)}</span></div>'
        f'<h3>{esc(h)}</h3><p>{esc(p)}</p><ul class="ticks">'
        + "".join(f"<li>{ICON_CHECK}<span>{esc(x)}</span></li>" for x in items) + "</ul></article>"
        for i, (n, h, p, items) in enumerate(T["systems"]))

    pm_list = "".join(f"<li>{ICON_CHECK}<span>{esc(x)}</span></li>" for x in T["pm_list"])
    cycle = "".join(f"<li><span>{esc(a)}</span><span>{esc(b)}</span></li>" for a, b in T["pm_cycle"])
    stats3 = "".join(f"<div><b>{esc(a)}</b><span>{esc(b)}</span></div>" for a, b in T["pm_stats"])
    brands = "".join(f"<li>{esc(b)}</li>" for b in T["brands"])

    steps = "".join(
        f'<li class="step rv"><span class="n" aria-hidden="true">0{i + 1}</span><div><h3>{esc(h)}</h3><p>{esc(p)}</p></div></li>'
        for i, (h, p) in enumerate(T["steps"]))

    results = "".join(
        f'<div class="card rv"><b>{esc(n)}</b><div><strong>{esc(u)}</strong><p>{esc(d)}</p></div></div>'
        for n, u, d in T["results"])

    testis = "".join(
        f'<figure class="card rv"><blockquote class="tq"><p>{esc(q)}</p></blockquote><span class="out">→ {esc(o)}</span>'
        f'<figcaption class="who"><img src="/images/opt/{img}-96.webp" srcset="/images/opt/{img}-96.webp 96w, /images/opt/{img}-192.webp 192w" sizes="52px" width="52" height="52" alt="{esc(name)}" loading="lazy" decoding="async">'
        f'<span><strong>{esc(name)}</strong><span>{esc(role)}</span></span></figcaption></figure>'
        for (img, name), (q, role, o) in zip(PEOPLE, T["testis"]))

    posts = "".join(
        f'<article class="card post rv"><p class="meta"><span class="new">{T["new"]}</span><span>{esc(c)}</span></p>'
        f'<h3><a href="{u}">{esc(t)}</a></h3><p>{esc(x)}</p><span class="more" aria-hidden="true">{esc(T["read"])} {ICON_ARROW}</span></article>'
        for u, c, t, x in T["posts"])

    faq_html = ""
    if T["faq"]:
        items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in T["faq"])
        faq_html = (f'<section class="sec" id="faq" aria-labelledby="faq-h"><div class="wrap faq"><div><p class="label">{T["faq_label"]}</p>'
                    + h2(T["faq_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="faq-h">') + f'</div><div class="rv">{items}</div></div></section>')

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
<link rel="preload" href="/images/opt/mediha-600.webp" as="image" type="image/webp" imagesrcset="/images/opt/mediha-400.webp 400w, /images/opt/mediha-600.webp 600w, /images/opt/mediha-768.webp 768w" imagesizes="(min-width:900px) 360px, (min-width:460px) 420px, 92vw" fetchpriority="high">
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
<div class="wrap">
<div>
<div class="chips"><span class="chip"><span class="dot" aria-hidden="true"></span>{esc(T["hero_label"])}</span><span class="chip dark">{esc(T["region"])}</span></div>
<h1 class="h1" id="h1">{esc(T["h1a"])} <em>{esc(T["h1b"])}</em></h1>
<p class="lead">{esc(T["hero_sub"])}</p>
<div class="acts"><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a><a class="btn ghost" href="#systems">{esc(T["hero_btn2"])}</a></div>
<div class="trust"><div class="faces">{face_imgs}</div><a class="link" href="#stories">{esc(T["stories_link"])} {ICON_ARROW}</a></div>
</div>
<figure class="portrait">
<img src="/images/opt/mediha-600.webp" srcset="/images/opt/mediha-400.webp 400w, /images/opt/mediha-600.webp 600w, /images/opt/mediha-768.webp 768w" sizes="(min-width:900px) 360px, (min-width:460px) 420px, 92vw" width="600" height="750" alt="{esc(T["ceo_alt"])}" fetchpriority="high" decoding="async">
<figcaption><span><strong>Mediha Mujcin</strong><span>CEO &amp; Founder</span></span><a class="link" href="#about" aria-label="{esc(T["about"])}: Mediha Mujcin">{ICON_ARROW}</a></figcaption>
</figure>
</div>
</section>

<div class="mq"><ul>{principles}</ul></div>

<section class="sec" aria-labelledby="pain-h">
<div class="wrap">
<div class="head"><p class="label">{esc(T["pain_label"])}</p>{h2(T["pain_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="pain-h">')}</div>
<div class="grid g3 snap">{pains}</div>
</div>
</section>

<section class="sec ow" id="systems" aria-labelledby="sys-h">
<div class="wrap">
<div class="head"><p class="label">{esc(T["sys_label"])}</p>{h2(T["sys_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="sys-h">')}<p class="lead">{esc(T["sys_sd"])}</p></div>
<div class="grid g2">{systems}</div>
</div>
</section>

<section class="sec" aria-labelledby="pm-h">
<div class="wrap">
<div class="pm">
<div><p class="label">{esc(T["pm_label"])}</p>{h2(T["pm_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="pm-h">')}<p class="lead">{esc(T["pm_sd"])}</p><ul class="ticks">{pm_list}</ul></div>
<div class="panel rv"><div class="pt"><strong>{esc(T["pm_panel"])}</strong><span>powered by <b>impact.com</b></span></div><h3>{esc(T["pm_cycle_t"])}</h3><ul class="cycle">{cycle}</ul><div class="stats3">{stats3}</div></div>
</div>
<ul class="brands">{brands}</ul>
</div>
</section>

<section class="sec {stmt_bg} stmt"><div class="wrap"><p class="rv">{esc(T["stmt"])} <em>{esc(T["stmt_em"])}</em></p></div></section>

<section class="sec" id="approach" aria-labelledby="ap-h">
<div class="wrap ap">
<div class="sticky"><p class="label">{esc(T["ap_label"])}</p>{h2(T["ap_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="ap-h">')}<p class="lead">{esc(T["ap_sd"])}</p><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta"])} {ICON_ARROW}</a></div>
<ol class="steps" style="list-style:none;padding:0;margin:0">{steps}</ol>
</div>
</section>

<section class="sec res" id="results" aria-labelledby="res-h" style="padding-top:0">
<div class="wrap">
<div class="head"><p class="label">{esc(T["res_label"])}</p>{h2(T["res_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="res-h">')}<p class="lead">{esc(T["res_sd"])}</p></div>
<div class="grid g3">{results}</div>
</div>
</section>

<section class="sec ow" id="stories" aria-labelledby="t-h">
<div class="wrap">
<div class="head"><p class="label">{esc(T["t_label"])}</p>{h2(T["t_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="t-h">')}</div>
<div class="grid g3 snap">{testis}</div>
</div>
</section>

<section class="sec" id="about" aria-label="Mediha Mujcin">
<div class="wrap about">
<img src="/images/opt/mediha-600.webp" srcset="/images/opt/mediha-400.webp 400w, /images/opt/mediha-600.webp 600w, /images/opt/mediha-768.webp 768w" sizes="(min-width:900px) 40vw, 92vw" width="600" height="750" alt="{esc(T["ceo_alt"])}" loading="lazy" decoding="async">
<div class="rv"><blockquote>{esc(T["ceo_quote"])}</blockquote><span class="role">CEO &amp; Founder</span><span class="name">Mag. (FH) Mediha Mujcin</span><p class="bio">{esc(T["ceo_bio"])}</p><a class="link" href="{LI}" target="_blank" rel="noopener">LinkedIn {ICON_ARROW}</a></div>
</div>
</section>

<section class="sec ow" aria-labelledby="blog-h">
<div class="wrap">
<div class="head row"><div><p class="label">{esc(T["blog_label"])}</p>{h2(T["blog_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="blog-h">')}</div><a class="btn ghost" href="{T["blog_index"]}">{esc(T["all_posts"])} {ICON_ARROW}</a></div>
<div class="grid g3">{posts}</div>
</div>
</section>

{faq_html}

<section class="sec ow" id="kontakt" aria-labelledby="cta-h">
<div class="wrap contact">
<div><p class="label">{esc(T["cta_label"])}</p>{h2(T["cta_h2"]).replace('<h2 class="h2">', '<h2 class="h2" id="cta-h">')}<p class="lead">{esc(T["cta_sd"])} <strong>{esc(T["cta_strong"])}</strong></p>
<div class="acts"><a class="btn" href="{CAL}" target="_blank" rel="noopener">{esc(T["cta30"])} {ICON_ARROW}</a></div>
<div class="direct"><a href="mailto:{MAIL}"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="m4 7 8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>{MAIL}</a><a href="tel:{TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 3.5h3l1.5 4-2 1.3a11 11 0 0 0 6.2 6.2l1.3-2 4 1.5v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>{TEL_TXT}</a><a href="{WA}" target="_blank" rel="noopener">{ICON_WA}WhatsApp</a></div>
</div>
<form class="form rv" name="contact" method="POST" action="/success" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="contact">
<p class="hp"><label>Bot <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<h3>{esc(T["form_h"][0])} <em>{esc(T["form_h"][1])}</em></h3>
<p>{esc(T["form_sd"])}</p>
<div class="f2"><div class="fld"><label for="f-name">{esc(T["f_name"])}</label><input id="f-name" type="text" name="name" autocomplete="name" required{p_("name")}></div><div class="fld"><label for="f-mail">{esc(T["f_mail"])}</label><input id="f-mail" type="email" name="email" autocomplete="email" inputmode="email" required{p_("email")}></div></div>
<div class="fld" style="margin-top:16px"><label for="f-co">{esc(T["f_company"])}</label><input id="f-co" type="text" name="company" autocomplete="organization"{p_("company")}></div>
<div class="fld"><label for="f-msg">{esc(T["f_msg"])}</label><textarea id="f-msg" name="message" required{p_("message")}></textarea></div>
<button class="btn" type="submit">{esc(T["f_send"])} {ICON_ARROW}</button>
</form>
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


def main():
    (ROOT / "index.html").write_text(page(DE), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page(EN), encoding="utf-8")
    for p in ("index.html", "en/index.html"):
        print(p, (ROOT / p).stat().st_size, "Bytes")


if __name__ == "__main__":
    main()
