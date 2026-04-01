# -*- coding: utf-8 -*-
"""Build evi-mt-locales.js (UI + manuals). Requires: pip install deep-translator && network."""
import json
import os
import re
import time

import requests

# (connect seconds, read seconds) — generous read so Google Translate can finish on slow links.
TRANSLATE_TIMEOUT_SEC = (20, 150)
_ORIG_REQUESTS_GET = requests.get


def _requests_get_with_timeout(*args, **kwargs):
    kwargs.setdefault("timeout", TRANSLATE_TIMEOUT_SEC)
    return _ORIG_REQUESTS_GET(*args, **kwargs)

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("Run: pip install deep-translator")
    raise

MANUAL_DE = r"""<h2 class="section-title">Evi Portable &mdash; Benutzerhandbuch (&Uuml;berblick)</h2>
    <p class="manual-lead">Dieser &Uuml;berblick entspricht <strong>Manual\README.txt</strong> in Ihrem Build. Er ist zum Lesen oder Ausdrucken; Evi l&auml;uft auch ohne ihn.</p>
    <div class="manual-block">
      <h3>Betriebssystem</h3>
      <p>Evi Portable ist nur f&uuml;r <strong>Microsoft Windows 10 und Windows 11</strong>. Windows 7/8, macOS, Linux und Mobilger&auml;te werden nicht unterst&uuml;tzt.</p>
    </div>
    <div class="manual-block">
      <h3>Erster Start &mdash; vom Download bis Evi l&auml;uft</h3>
      <ol>
        <li><strong>Installationsort.</strong> Kopieren Sie den gesamten Evi-Ordner an einen Ort Ihrer Wahl (Desktop, Dokumente, USB). Ordnerstruktur beibehalten.</li>
        <li><strong>Programm laden.</strong> Nutzen Sie <strong>Evi Portable laden</strong> oder die Download-Karte auf <a href="https://toscano8070.github.io/Evi-Portable/#download-pack">dieser Seite</a>. Das Archiv ist die Anwendung ohne das Haupt-LLM.</li>
        <li><strong>Sprachmodell (Pflicht).</strong> Evi braucht <strong>eine</strong> Haupt-KI-Datei (<code>.gguf</code>) in <code>models\llm\</code>. Auf dieser Seite auf den GGUF-Download klicken, sobald der Link aktiv ist. Bis dahin springt die Schaltfl&auml;che hierher. Siehe <code>models\llm\README.txt</code>.</li>
      </ol>
      <p class="manual-callout"><strong>Richtiges Modell, richtiger Ordner:</strong> Mindestens eine passende <code>.gguf</code> in <code>models\llm\</code> (siehe <code>models\llm\README.txt</code>), dann Evi starten.</p>
      <p style="margin-top:1rem"><a href="#manual-llm" class="btn btn-outline btn-muted evi-llm-download" data-evi-url="llm">KI-Modell herunterladen (GGUF)</a></p>
      <div class="dl-llm-heavy dl-llm-heavy--manual" role="alert">
        <p class="dl-llm-heavy__title">&#9888;&#65039; Nur High-End-NVIDIA-GPUs &mdash; z.&nbsp;B. GeForce RTX-5090-Klasse</p>
        <p class="dl-llm-heavy__body">
          Die <strong>14B-Instruct-GGUF</strong> ist <a class="dl-llm-heavy__dl evi-llm-download" data-evi-url="llm" href="#manual-llm"><code>qwen2.5-14b-instruct-q4_k_m.gguf</code></a> &mdash; Klick startet den <strong>LLM-Download</strong>. Nur f&uuml;r Spitzen-GPUs mit viel VRAM. Sonst normalen Download im <a href="https://toscano8070.github.io/Evi-Portable/#download-pack">Download-Bereich</a> und <code>models\llm\README.txt</code> beachten.
        </p>
      </div>
      <ol start="4">
        <li><strong>Aktivierung.</strong> <strong>Machine ID</strong> kopieren, an <a href="mailto:Brielbeck@hotmail.de?subject=Evi%20Portable%20-%20Machine%20ID">Brielbeck@hotmail.de</a> senden.</li>
        <li><strong>Nach Aktivierung.</strong> Sprache, Mikrofon, Stimme w&auml;hlen. &bdquo;open the cheat sheet&ldquo; f&uuml;r Beispiele (<code>cheatsheets\</code>).</li>
        <li><strong>Handbuch lokal:</strong> <code>Manual\README.txt</code> im Explorer.</li>
      </ol>
    </div>
    <div class="manual-block">
      <h3>Oberfl&auml;chensprache (GUI)</h3>
      <p>Sprache unter <strong>Language</strong> in der linken Leiste.</p>
    </div>
    <div class="manual-block">
      <h3>Grafikkarte (GPU)</h3>
      <p>Z.&nbsp;B. <strong>RTX 4070 Ti</strong> 12&nbsp;GB. GPU-Preset w&auml;hlen; <strong>nur CPU</strong> ist deutlich langsamer.</p>
    </div>
    <div class="manual-block">
      <h3>Portabel &amp; Internet</h3>
      <p>Ordner kopieren. Lizenz am <strong>PC</strong> gebunden.</p>
    </div>
    <div class="manual-block">
      <h3>Sicherheit</h3>
      <p>PIN und Sprach-Unlock mit wechselnden <strong>Zufallsw&ouml;rtern</strong>.</p>
    </div>
    <div class="manual-block">
      <h3>Fehlersuche</h3>
      <p class="manual-lead">Kurzliste, danach Themen im Detail. <strong>Vollst&auml;ndige Druckversion:</strong> <code>Manual\FEHLERSUCHE_DE.txt</code> im Evi-Ordner.</p>
      <ul>
        <li><strong>Keine KI / Modell:</strong> Mindestens eine passende <code>.gguf</code> in <code>models\llm\</code>? Siehe <code>models\llm\README.txt</code>. Kleineres Modell oder <strong>CPU</strong>-Preset in der Seitenleiste, wenn GPU scheitert.</li>
        <li><strong>Kein Mikrofon:</strong> Windows-Datenschutz + Soundtest; in Evi Ger&auml;t unter Mikrofon w&auml;hlen und speichern.</li>
        <li><strong>Keine Stimme:</strong> Stimmen unter <code>piper\</code>; Stimme w&auml;hlen; Lautst&auml;rke-Mixer pr&uuml;fen.</li>
        <li><strong>Web / YouTube:</strong> &bdquo;Block all traffic&ldquo; aus, wenn Online-Helfer gew&uuml;nscht; YouTube braucht Netz + meist VLC Portable.</li>
        <li><strong>Cheat-Sheets:</strong> Nach &Auml;nderungen Evi neu starten; UTF-8; <code>cheatsheets\README.txt</code>.</li>
      </ul>
      <h4>Immer zuerst pr&uuml;fen</h4>
      <p>Windows <strong>10 oder 11</strong> 64-Bit, aktuell; aus <strong>vollst&auml;ndig entpacktem</strong> Ordner starten. <strong>Lokaler Pfad</strong> bevorzugen (keine Live-Daten in stark synchronisierten Cloud-Ordnern). Genug <strong>freier Speicher</strong>. Nach Modell- oder Cheat-Sheet-&Auml;nderung Evi <strong>vollst&auml;ndig beenden und neu starten</strong>.</p>
      <h4>1. Betriebssystem &amp; Pfade</h4>
      <p>Andere Systeme werden nicht unterst&uuml;tzt. Lange Pfade oder strenge Virenscanner k&ouml;nnen blockieren oder bremsen &mdash; ggf. Ordner-Ausnahme. USB: schnelles Medium, NTFS.</p>
      <h4>2. Modell-Datei (.gguf)</h4>
      <p>Unvollst&auml;ndige Downloads (0&nbsp;Byte, abgebrochen) verhindern das Laden. Neu laden. Mehrere <code>.gguf</code> sind m&ouml;glich; Evi kann die gr&ouml;&szlig;te passend zur VRAM w&auml;hlen &mdash; siehe <code>models\llm\README.txt</code>. Bei Zweifeln: nur <strong>eine</strong> bekannte Datei testen.</p>
      <h4>3. GPU, Treiber, Speicher</h4>
      <p><strong>NVIDIA</strong>-Treiber aktualisieren. Notebooks: <strong>dedizierte / H&ouml;chstleistungs</strong>-GPU f&uuml;r Evi. <strong>OOM</strong>: kleineres Modell, andere GPU-Apps schlie&szlig;en, k&uuml;hlen, oder CPU-Preset. <strong>TDR</strong>: Last und Temperatur senken; kein instabiles &Uuml;bertakten.</p>
      <h4>4. Nur CPU</h4>
      <p>Langsame Antworten sind normal. RAM freihalten; Energieplan &bdquo;H&ouml;chstleistung&ldquo;; Hintergrundlast reduzieren.</p>
      <h4>5. Aktivierung</h4>
      <p>Seriennummer sauber einf&uuml;gen (keine Leerzeichen). Key ist an <strong>eine Machine ID</strong> gebunden. Nach gro&szlig;em Hardwarewechsel ggf. Ersatzschl&uuml;ssel beim Support mit Kaufnachweis.</p>
      <h4>6. Mikrofon &amp; Spracheingabe</h4>
      <p>Einstellungen &rarr; Datenschutz &rarr; Mikrofon &rarr; Desktop-Apps erlauben. Richtiges Aufnahmeger&auml;t. Bluetooth erh&ouml;ht Latenz &mdash; USB-Mikro testen. Exklusivmodus anderer Apps (Meetings) blockiert das Ger&auml;t.</p>
      <h4>7. Piper / TTS</h4>
      <p>Passende Sprachdateien unter <code>piper\</code>. Stimme w&auml;hlen; im Mixer pr&uuml;fen, ob Evi stumm ist.</p>
      <h4>8. Netzwerk</h4>
      <p>Globale Sperre in Evi deaktivieren f&uuml;r Web/Mail/Wetter/Downloads. Firmen-<strong>VPN/Proxy</strong> ggf. durch IT freischalten.</p>
      <h4>9. Medien / YouTube</h4>
      <p>VLC-Portable-Struktur nicht l&ouml;schen; Netzwerk f&uuml;r Streaming-Helfer erlauben.</p>
      <h4>10. Sicherheit (PIN / Stimme)</h4>
      <p>Ruhiger Raum; Zufallsw&ouml;rter sind Anti-Replay. PIN niemals weitergeben.</p>
      <h4>11. Abst&uuml;rze / Langsamkeit</h4>
      <p>Thermal-Drosselung, SSD-Platz, ggf. <code>crash.log</code> im Build pr&uuml;fen. Letzte &Auml;nderung zur&uuml;cknehmen.</p>
      <h4>12. Support</h4>
      <p><strong>Machine ID</strong>, Windows-Version, GPU + VRAM + Treiber, welche <code>.gguf</code>, Schritte, Fehlertext senden (keine Schl&uuml;ssel &ouml;ffentlich posten).</p>
    </div>
    <div class="manual-block">
      <h3>Support</h3>
      <p><a href="mailto:Brielbeck@hotmail.de?subject=Evi%20Portable%20-%20Machine%20ID">Brielbeck@hotmail.de</a> &mdash; <strong>Machine ID</strong> angeben.</p>
    </div>"""

EN_FLAT = {
    "nav_features": "Features",
    "nav_languages": "Languages",
    "nav_accessibility": "Accessibility",
    "nav_requirements": "Windows & activation",
    "nav_pricing": "Pricing",
    "nav_activation": "License activation",
    "nav_manual": "Manual",
    "nav_setup": "Under the Hood",
    "nav_download": "Download",
    "hero_title": "Evi &mdash; your voice-first digital secretary.<br><em>Private, portable, built for sustained use.</em>",
    "hero_sub": "Evi behaves like a skilled secretary: it drafts and revises mail, prepares replies in the right tone, helps you insert appointments and blocks into your calendar, and chases reminders so nothing slips. Ask by voice or keyboard &mdash; it answers clearly, reads context and mood, and learns your preferences over time. Long-term memory holds people, projects, and facts so you can recall them later from local storage, not public search. Optional network tools unlock checking inboxes and sending messages; the heavy lifting still runs on your PC inside a portable folder (USB-ready).",
    "hero_dl": "\u2b07 Get Evi Portable",
    "hero_langs": "See all languages",
    "hero_note": "*Requires Windows 10 or Windows 11. NVIDIA GPU strongly recommended for responsive performance. Personal vs commercial licensing may apply.",
    "soc_llm": "Voice &amp;<br>text",
    "soc_voice": "Context<br>aware",
    "soc_mem": "Long-term<br>memory",
    "soc_tools": "Mail &amp;<br>calendar",
    "soc_priv": "Local &amp;<br>private",
    "feat_title": "Why Evi Portable?",
    "f1_h": "USB Portable",
    "f1_p": "No system installation required. Deploy to a USB drive or folder, run the launcher. Embedded runtime and relative paths keep data and models together.",
    "f2_h": "100% Privacy",
    "f2_p": "AI runs locally. Optional network only when you enable it. PIN lock and privacy toggles when you want them.",
    "f3_h": "Media and preferences",
    "f3_p": "Manage playback, playlists, and stations. Evi learns your listening patterns and uses them to give relevant suggestions and context in conversation.",
    "f4_h": "Correspondence and drafting",
    "f4_p": "Turn bullet points into complete e-mails, adjust formality, and refine replies before you send. With optional network tools enabled, Evi can support inbox triage and outbound mail &mdash; you stay in control of what goes out.",
    "f5_h": "Calendar and scheduling",
    "f5_p": "Dictate or type new meetings; Evi helps place them on your timeline, set follow-ups, and surface conflicts. Covers appointments, deadlines, bills, habits, wellness prompts, and recurring work &mdash; with reminders tuned to how you operate. Export calendar data (e.g. .ics) when you need to share or archive.",
    "f6_h": "Long-term memory and recall",
    "f6_p": "Information you provide is retained and retrieved on demand &mdash; across sessions and over time &mdash; from your local store, not public search. Supports 40+ interface languages; mail and other integrations when optional network tools are enabled.",
    "lang_title": "40+ Languages, One App",
    "lang_sub": "Work in your language; the interface follows. Speech synthesis and conversation data remain under your control on the device.",
    "acc_title": "Built for Everyone",
    "acc_sub": "Whether you are focused on typing or on extended voice sessions, Evi switches input modes while preserving context and your profile.",
    "ac1_h": "&#x2328;&#xFE0F; Chat & voice together",
    "ac1_p": "Switch between keyboard and microphone without losing context. Great for quiet rooms, shared spaces, or accessibility needs.",
    "ac2_h": "&#x1F510; You stay in charge",
    "ac2_p": "Offline-first by design. Serial-key editions for distribution. Optional cloud helpers only if you configure them.",
    "term_block": "[SYSTEM] Initializing...\n[USB]    Mode: Portable\n[GPU]    LLM: local GGUF ready\n[AI]     Whisper / TTS: ready\n[PRIVACY] Network: your choice\n[STATUS] Evi is ready.",
    "hood_title": "Under the Hood",
    "hood1_h": "AI brain:",
    "hood1_p": "Swappable GGUF models via llama.cpp &mdash; configurable context and GPU presets.",
    "hood2_h": "NVIDIA GPU:",
    "hood2_p": "Dedicated NVIDIA graphics recommended (e.g. RTX 3060 or better) for responsive chat and speech.",
    "hood3_h": "Memory:",
    "hood3_p": "Structured retrieval across notes, appointments, context, media habits, and saved correspondence &mdash; queried on demand from local storage.",
    "hood4_h": "Agent:",
    "hood4_p": "Tools for files, media, optional web, timers, translation &mdash; and secretary-style flows: calendar maintenance, mail drafting and (when allowed) send/receive, contacts and notes. llama-cpp-agent available for structured tool use.",
    "hood5_h": "Portable stack:",
    "hood5_p": "Bundled helpers (VLC, portable browser) and strict portable mode if you want zero system fallbacks.",
    "hood_btn": "Read the manual",
    "document_title": "Evi Portable — Local secretary: mail, calendar, voice assistant",
    "footer_tag": "Draft your mail, fill your calendar, and keep your week on track &mdash; a local secretary you can carry on a stick.",
    "footer_manual": "Manual",
    "footer_setup": "Download & setup",
    "footer_contact": "Contact",
    "footer_paypal": "Pay with PayPal",
    "footer_disc": "Made by Hardy Brielbeck",
    "req_win": "<strong>System:</strong> Evi Portable requires <strong>Microsoft Windows 10 or Windows 11</strong>. Other operating systems are not supported.",
    "req_activation": "<strong>Activation:</strong> When you first start Evi, copy your <strong>Machine ID</strong> from the activation window and e-mail it to <a href=\"mailto:Brielbeck@hotmail.de?subject=Evi%20Portable%20-%20Machine%20ID\">Brielbeck@hotmail.de</a>. You will receive a serial key <strong>tied to that PC</strong>.",
    "act_title": "How to activate your license",
    "act_intro": "After purchase, activate with <strong>Machine ID</strong> by e-mail (steps below). The full <a href=\"https://toscano8070.github.io/Evi-Portable/#manual\">user manual</a> on this site is the same overview as <code>Manual\\README.txt</code> in your Evi folder &mdash; first start, LLM setup, GPU notes, security, troubleshooting.",
    "act_s1": "<strong>Purchase</strong> &mdash; Choose your package and pay securely via <a href=\"https://www.paypal.com/donate/?hosted_button_id=CYAHBMQ6VKGEY\" target=\"_blank\" rel=\"noopener noreferrer\">PayPal</a>.",
    "act_s2": "<strong>Launch Evi</strong> &mdash; On first start, the license activation window appears.",
    "act_s3": "<strong>Copy Machine ID</strong> &mdash; The app generates a unique Machine ID for this computer. Click <strong>Copy Machine ID</strong>.",
    "act_s4": "<strong>E-mail your ID</strong> &mdash; Send your Machine ID and proof of purchase to <a href=\"mailto:Brielbeck@hotmail.de?subject=Evi%20Portable%20-%20Machine%20ID\">Brielbeck@hotmail.de</a>.",
    "act_s5": "<strong>Receive serial key</strong> &mdash; You receive your personalized key within about 24&ndash;48 hours.",
    "act_s6": "<strong>Activate!</strong> &mdash; Paste the serial key into the activation window and click <strong>Activate</strong>. Done!",
    "act_format": "EVI-XXXXX-XXXXX-XXXXX-XXXXX<small>Serial key format (provided after purchase &mdash; example placeholder)</small>",
    "pricing_badge": "Introductory offer &mdash; limited time",
    "pricing_title": "One payment. Your secretary for years.",
    "pricing_detail": "<span class=\"pricing-price\">35 Euro</span> For a limited time, lock in this launch price: pay once&mdash;no subscriptions, no hidden fees. Includes <strong>1 year of updates</strong>. Windows&nbsp;10/11 only. Pay with PayPal, then activate with your Machine ID below.",
    "hero_team_aria": "Your desk team — mail, calendar, and concierge-style assistance",
    "hero_llm_dl": "Download AI model (GGUF)",
    "hero_dl_hint": "Download the <strong>program archive</strong> first. Then click <strong>Download AI model (GGUF)</strong> &mdash; the official package link will appear on this button when published. Until then it scrolls to the manual below. Put exactly one suitable <code>.gguf</code> in <code>models\\llm\\</code> before chatting; see <code>models\\llm\\README.txt</code> in the folder.",
    "dl_pack_title": "Download Evi Portable",
    "dl_pack_before_title": "Before you download",
    "dl_chk_1": "I have an NVIDIA GPU (RTX 3060 or better)",
    "dl_chk_2": "I have ~50 GB of free disk space",
    "dl_chk_3": "I will download the LLM model separately (instructions above &amp; in the manual)",
    "dl_btn_program": "&#x2B07; Download Evi Portable (~37 GB)",
    "dl_btn_llm": "&#x2B07; Download LLM model (~9.1 GB)",
    "dl_hostnote": "Download buttons go <strong>directly to the file host</strong> in this tab (no long URL shown here). Confirm the download on the next screen &mdash; we cannot force the file into your browser without that one host step.",
    "dl_14b_heading": "14B GGUF (inside the LLM package) &mdash; <code>qwen2.5-14b-instruct-q4_k_m.gguf</code> &mdash; RTX 5090 class only (read warning)",
    "dl_tbl_file": "File",
    "dl_tbl_size": "Size",
    "dl_tbl_r1f": "Evi Portable",
    "dl_tbl_r1s": "~37 GB",
    "dl_tbl_r2f": "LLM model",
    "dl_tbl_r2s": "~9.1 GB",
    "dl_tbl_total": "Total",
    "dl_tbl_totals": "~46 GB",
    "dl_txl_note": "Your browser may save each download under an auto-generated name (often a <code>.zip</code>). Extract the archives first, then place the main app folder where you want it and move the <code>.gguf</code> into <code>models\\llm\\</code> as described in the manual.",
    "dl_llm_heavy": "<p class=\"dl-llm-heavy__title\">&#9888;&#65039; High-end NVIDIA GPUs only &mdash; e.g. GeForce RTX 5090 class</p><p class=\"dl-llm-heavy__body\">The <strong>14B instruct GGUF</strong> is <a class=\"dl-llm-heavy__dl evi-llm-download\" data-evi-url=\"llm\" href=\"#manual-llm\"><code>qwen2.5-14b-instruct-q4_k_m.gguf</code></a> &mdash; click the filename to start the <strong>LLM model download</strong> (that archive contains this file). For <strong>top-tier cards with plenty of VRAM</strong> (think <strong>RTX 5090</strong> and similar) only. <strong>Do not use this checkpoint on weaker GPUs</strong> &mdash; expect OOM, extreme slowness, or crashes. Otherwise use the <strong>standard LLM download</strong> above and a smaller model per <code>models\\llm\\README.txt</code>.</p>",
    "man_llm_heavy": "<p class=\"dl-llm-heavy__title\">&#9888;&#65039; High-end NVIDIA GPUs only &mdash; e.g. GeForce RTX 5090 class</p><p class=\"dl-llm-heavy__body\">The <strong>14B instruct GGUF</strong> is <a class=\"dl-llm-heavy__dl evi-llm-download\" data-evi-url=\"llm\" href=\"#manual-llm\"><code>qwen2.5-14b-instruct-q4_k_m.gguf</code></a> &mdash; click the filename to start the <strong>LLM model download</strong> (that archive contains this file). For <strong>top-tier cards with plenty of VRAM</strong> (think <strong>RTX 5090</strong> and similar) only. <strong>Do not use this checkpoint on weaker GPUs</strong> &mdash; OOM, extreme slowness, or crashes. Otherwise the <strong>standard LLM download</strong> on <a href=\"https://toscano8070.github.io/Evi-Portable/#download-pack\">the Download section</a> and a smaller model per <code>models\\llm\\README.txt</code>.</p>",
}

LANGS = [
    ("JA", "ja"), ("KO", "ko"), ("ZH", "zh-CN"), ("ZH-TW", "zh-TW"),
    ("ES", "es"), ("FR", "fr"), ("IT", "it"), ("PT", "pt"), ("PT-BR", "pt"),
    ("RU", "ru"), ("UK", "uk"), ("PL", "pl"), ("NL", "nl"),
    ("SV", "sv"), ("DA", "da"), ("NO", "no"), ("FI", "fi"),
    ("CS", "cs"), ("SK", "sk"), ("RO", "ro"), ("HU", "hu"),
    ("EL", "el"), ("TR", "tr"), ("AR", "ar"), ("VI", "vi"),
]

TAG_TOKEN_RE = re.compile(r"<[^>]+>")


def protect_tags(s):
    tags = []

    def repl(_m):
        tags.append(_m.group(0))
        return " [[HTM%i]] " % (len(tags) - 1)

    return TAG_TOKEN_RE.sub(repl, s), tags


def restore_tags(s, tags):
    for i, tag in enumerate(tags):
        for pat in (
            "[[HTM%i]]" % i,
            "[[ HTM%i ]]" % i,
            "[[HTM%i ]]" % i,
            "[[ HTM%i]]" % i,
            "[[ HTM%i ]]" % i,
        ):
            s = s.replace(pat, tag)
    return s


def translate_val(tr, text):
    if not text or not str(text).strip():
        return text or ""
    original = text
    text = (
        text.replace("&mdash;", "\u2014")
        .replace("&ndash;", "\u2013")
        .replace("&hellip;", "\u2026")
        .replace("&ldquo;", "\u201c")
        .replace("&rdquo;", "\u201d")
        .replace("&bdquo;", "\u201e")
        .replace("&rsquo;", "\u2019")
        .replace("&amp;", " {AMP} ")
    )
    prot, tags = protect_tags(text)
    t = None
    for attempt in range(4):
        try:
            t = tr.translate(prot)
            break
        except Exception as e:
            msg = str(e).encode("ascii", "replace").decode("ascii")
            print("  translate error:", msg, flush=True)
            t = None
            time.sleep(1.4 * (attempt + 1))
    if t is None:
        return original
    out = restore_tags(t.strip(), tags)
    for pat in (" {AMP} ", "{AMP}", " {AMP}", "{AMP} "):
        out = out.replace(pat, "&amp;")
    return out


def translate_manual_inner(tr, html):
    parts = re.split(r"(<[^>]+>)", html)
    out = []
    for p in parts:
        if p is None:
            continue
        if p.startswith("<"):
            out.append(p)
        elif p.strip():
            v = translate_val(tr, p)
            out.append(v if v is not None else p)
        else:
            out.append(p)
    return "".join(out)


def translate_manual(tr, html):
    if len(html) <= 3200:
        return translate_manual_inner(tr, html)
    chunks = []
    i, n = 0, len(html)
    while i < n:
        end = min(i + 3200, n)
        if end < n:
            cut = html.rfind("<", i + 2000, end)
            if cut > i:
                end = cut
        chunks.append(html[i:end])
        i = end
    return "".join(translate_manual_inner(tr, c) for c in chunks if c)


def main():
    requests.get = _requests_get_with_timeout
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        frag = os.path.join(base, "manual_en_fragment.html")
        with open(frag, "r", encoding="utf-8") as f:
            manual_en = f.read()

        keys_order = list(EN_FLAT.keys())
        all_extra = {}

        for code, gt in LANGS:
            print("===", code, gt, flush=True)
            tr = GoogleTranslator(source="en", target=gt)
            patch = {}
            for k in keys_order:
                patch[k] = translate_val(tr, EN_FLAT[k])
                time.sleep(0.05)
            print("  manual ...", flush=True)
            patch["manual_html"] = translate_manual(tr, manual_en)
            if code == "AR":
                patch["manual_html"] = (
                    '<div dir="rtl">' + patch["manual_html"] + "</div>"
                )
            all_extra[code] = patch
            time.sleep(0.35)

        outpath = os.path.join(base, "evi-mt-locales.js")
        payload = json.dumps(all_extra, ensure_ascii=False)
        js = (
            "/* Generated by gen_evi_locales.py — machine translation; review before release. */\n"
            "window.EVI_MT_LOCALES = window.EVI_MT_LOCALES || {};\n"
            "Object.assign(window.EVI_MT_LOCALES, "
            + payload
            + ");\n"
        )
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(js)
        print("Wrote", outpath, "size", os.path.getsize(outpath))
    finally:
        requests.get = _ORIG_REQUESTS_GET


if __name__ == "__main__":
    main()
