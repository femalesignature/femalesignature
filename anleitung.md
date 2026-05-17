# Female Signature — Website Live bringen

## Deine Dateien

```
female-signature-website/
├── index.html              ← Die komplette Website
├── images/
│   ├── logo.png            ← Dein Logo (schwarz, transparent)
│   ├── ceo-mediha.jpg      ← Dein Porträtfoto (s/w)
│   ├── signatur.png        ← Deine Handschrift-Signatur (transparent)
│   ├── hero.jpg            ← ⚠️ MUSST DU HERUNTERLADEN (siehe unten)
│   ├── services.jpg        ← ⚠️ MUSST DU HERUNTERLADEN (siehe unten)
│   ├── technology.jpg      ← ⚠️ MUSST DU HERUNTERLADEN (siehe unten)
│   └── about.jpg           ← ⚠️ MUSST DU HERUNTERLADEN (siehe unten)
```

---

## Schritt 1: Unsplash-Bilder herunterladen

Öffne diese 4 Links, klicke auf „Download free" und speichere sie mit den angegebenen Dateinamen in den `images/` Ordner:

| Dateiname | Link | Beschreibung |
|-----------|------|-------------|
| **hero.jpg** | https://unsplash.com/photos/photo-1586281380349-632531db7ed4 | Hände am Laptop, weißer Desk |
| **services.jpg** | https://unsplash.com/photos/photo-1552664730-d307ca884978 | Team Brainstorming, weißer Tisch |
| **technology.jpg** | https://unsplash.com/photos/photo-1460925895917-afdab827c52f | Laptop mit Analytics |
| **about.jpg** | https://unsplash.com/photos/photo-1553877522-43269d4ea984 | Frauen im Meeting |

> **Tipp:** Falls dir eines der Bilder nicht gefällt, suche auf unsplash.com ein anderes und benenne es einfach gleich. Die Website lädt das Bild automatisch.

---

## Schritt 2: Domain einrichten

Deine Domain `female-signature.com` brauchst du bei einem Domain-Registrar (z.B. bei deinem bestehenden Hosting-Anbieter). Falls du noch keine hast, empfehle ich:
- **Cloudflare Registrar** (günstigste Preise, schnellstes DNS)
- **Namecheap**

---

## Schritt 3: Hosting wählen (3 Optionen)

### Option A: Netlify (empfohlen — am einfachsten)

1. Gehe zu **https://netlify.com** und erstelle ein kostenloses Konto
2. Auf dem Dashboard: **"Add new site" → "Deploy manually"**
3. Ziehe den gesamten `female-signature-website/` Ordner in das Upload-Feld
4. Deine Seite ist sofort live unter einer `xxx.netlify.app` URL
5. **Custom Domain verbinden:**
   - Gehe zu "Domain management" → "Add custom domain"
   - Gib `female-signature.com` ein
   - Netlify zeigt dir DNS-Einstellungen (Nameserver oder CNAME)
   - Trage diese bei deinem Domain-Registrar ein
   - SSL-Zertifikat wird automatisch erstellt (HTTPS)

**Kosten: Gratis** (für diese Art von Website reicht der Free-Plan)

---

### Option B: Vercel

1. Gehe zu **https://vercel.com** und erstelle ein Konto
2. **"Add New" → "Project" → "Upload"**
3. Lade den Ordner hoch
4. Custom Domain unter "Settings → Domains" hinzufügen

**Kosten: Gratis**

---

### Option C: Traditionelles Hosting (z.B. Strato, World4You, All-Inkl)

Falls du bereits ein Hosting-Paket hast:

1. Verbinde dich per **FTP** (z.B. mit FileZilla)
   - Host: steht in deinen Hosting-Zugangsdaten
   - User/Passwort: vom Hosting-Anbieter
2. Lade alle Dateien in den `public_html/` oder `htdocs/` Ordner hoch
3. Die Seite ist sofort unter deiner Domain erreichbar

---

## Schritt 4: Testen

Nach dem Deploy, prüfe:

- [ ] Seite lädt unter `https://female-signature.com`
- [ ] Alle Bilder werden angezeigt
- [ ] Navigation-Links scrollen korrekt
- [ ] Mobil-Version testen (Hamburger-Menu, Bilder, Layout)
- [ ] Gold-Partikel-Animation im Hero funktioniert
- [ ] Infographic-Card rotiert automatisch
- [ ] CTA-Button „Kostenloses Strategiegespräch" öffnet Mail-Client
- [ ] Telefonnummer ist klickbar
- [ ] SSL/HTTPS aktiv (Schloss-Symbol im Browser)

---

## Schritt 5: SEO & Meta-Tags (bereits eingebaut)

Die index.html hat bereits:
- `<title>` Tag mit Keywords
- `<meta description>` für Google-Snippet
- Semantisches HTML (`<nav>`, `<section>`, `<footer>`)
- Alt-Texte auf allen Bildern

### Zusätzlich empfohlen:
- **Google Search Console** einrichten: https://search.google.com/search-console
- **Sitemap** erstellen (nicht nötig für Single-Page, aber gut für Crawling)
- **Open Graph Tags** für Social Media Sharing (kann ich ergänzen)

---

## Schritt 6: E-Mail einrichten

Die Website verweist auf `contact@female-signature.com`. 
Stelle sicher, dass diese Adresse existiert und Mails empfangen kann.

---

## Spätere Updates

Wenn du Texte oder Bilder ändern willst:

**Bei Netlify/Vercel:** Ändere die Dateien lokal, dann lade den Ordner erneut hoch (Drag & Drop) — fertig.

**Bei FTP-Hosting:** Lade die geänderten Dateien per FTP hoch und überschreibe die alten.

---

## Meine Empfehlung

**Netlify** ist die schnellste und einfachste Option. Du brauchst:
1. Unsplash-Bilder herunterladen (5 Minuten)
2. Netlify-Account erstellen (2 Minuten)  
3. Ordner hochladen (30 Sekunden)
4. Domain verbinden (10 Minuten)

**→ In unter 20 Minuten ist deine Seite live.**
