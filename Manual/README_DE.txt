===========================================================================
  Evi Portable – Bedienungsanleitung (Übersicht)
  Dokument: Englisch • Gilt für den Build, den Sie mit diesem Ordner erhalten haben
===========================================================================

Fügen Sie hier auch Ihre eigenen längeren Anleitungen oder Übersetzungen ein (z. B. EN_User_Manual.pdf,
DE_Handbuch.txt). Die Ausführung dieser Datei durch Evi ist optional. Es liegt an Ihnen, es zu lesen
oder ausdrucken.

Lokalisierte Kopien: README_<LANG>.txt und FEHLERSUCHE_<LANG>.txt in diesem Ordner
(gleiche Sprachcodes wie die Benutzeroberfläche der Website). Englische Übersicht: diese README.txt;
Englische Fehlerbehebung: FEHLERSUCHE_EN.txt. Deutsche Fehlerbehebung gibt es auch
Von Hand gepflegt als FEHLERSUCHE_DE.txt.

Ordnerindex (Dateibenennung, Generator): README.md

---------------------------------------------------------------------------------
  Betriebssystem
---------------------------------------------------------------------------------

Evi Portable ist nur für Microsoft Windows 10 und Windows 11. Das ist es nicht
Unterstützt auf Windows 7/8, macOS, Linux oder mobilen Betriebssystemen.

---------------------------------------------------------------------------------
  Erster Start – vom Download bis zum Ausführen von Evi
---------------------------------------------------------------------------------

1) Installationsort
   Kopieren oder extrahieren Sie beispielsweise den gesamten Evi-Ordner an einen von Ihnen kontrollierten Ort
   Ihren Desktop, Dokumente oder einen USB-Stick. Behalten Sie die Ordnerstruktur bei
   geliefert (löschen Sie keine Unterordner, die Sie nicht selbst erstellt haben).

2) Sprachmodell (erforderlich)
   Evi benötigt eine Haupt-KI-Modelldatei (Erweiterung .gguf) im Ordner:
   Modelle\llm\
   Größenempfehlungen finden Sie unter models\llm\README.txt. Nachdem die Datei vorhanden ist,
   starte Evi; Es erkennt das Modell nach Möglichkeit automatisch.

3) Erster Start – Aktivierung
   Wenn Sie Evi zum ersten Mal starten, erscheint ein Aktivierungsfenster.
   • Ihr PC zeigt eine Maschinen-ID (eindeutig für diese Hardware).
   • Kopieren Sie die Maschinen-ID (Schaltfläche: „Maschinen-ID kopieren“) und senden Sie diese per E-Mail an:
     Brielbeck@hotmail.de
   • Sie erhalten einen Serienschlüssel, der nur auf demselben PC funktioniert
     (Der Schlüssel ist an Ihre Hardware gebunden).
   • Fügen Sie den Schlüssel in das Aktivierungsfenster ein und wählen Sie „Aktivieren“.

   Wenn Sie wichtige Hardware ändern oder die Festplatte so verschieben, dass sich die ID ändert,
   Möglicherweise benötigen Sie einen neuen Schlüssel. Wenden Sie sich dazu an dieselbe Adresse.

4) Nach der Aktivierung
   Das Hauptfenster öffnet sich. Wählen Sie links Sprache, Mikrofon und Stimme
   Einstellungsfeld. Sagen Sie jederzeit „Spickzettel öffnen“, um Befehlsbeispiele zu erhalten
   (Siehe Cheatsheets\en.txt und Schwesterdateien für andere Sprachen).

5) Optional: Öffnen Sie dieses Handbuch unter Windows
   Gehen Sie im Datei-Explorer zum Evi-Ordner, dann zu Manual\README.txt und öffnen Sie ihn
   mit Notepad oder einem beliebigen Textbetrachter.

---------------------------------------------------------------------------------
  Schnittstellensprache (GUI)
---------------------------------------------------------------------------------

Die Benutzeroberfläche folgt der Sprache, die Sie oben unter Sprache auswählen
des linken Einstellungsbereichs (erster Block in der Seitenleiste). Nachdem Sie a ausgewählt haben
Sprache, Menüs, Schaltflächen, Beschriftungen und die meisten Bildschirmtexte werden darauf umgestellt
Sprache überall dort, wo es Übersetzungen gibt. Sie können es jederzeit ändern; nur die
Der Wortlaut ändert sich, nicht das Layout.

Tipp: Die Befehls-Spickzettel im Ordner „cheatssheets\“ werden pro aufgelistet
Sprachcode (en.txt, de.txt, …). Einzelheiten finden Sie unter Cheatsheets\README.txt.
Dieser Handbuch\-Ordner ist die längere Produktübersicht; Spickzettel sind die
kurze „Was soll ich sagen“-Liste.

---------------------------------------------------------------------------------
  Grafikkarte (GPU) – Kurzanleitung
---------------------------------------------------------------------------------

Eine starke mittlere Wahl ist eine NVIDIA GeForce RTX 4070 Ti mit 12 GB Video
Speicher: Gutes Gleichgewicht zwischen Geschwindigkeit, Kontextgröße und Platz für größere Modelle.

Karten von etwa RTX 3060 bis RTX 5090 können gut funktionieren; Die beste Passform hängt davon ab
über RAM, CPU, Kühlung und welche Modelldatei Sie installieren. Verwenden Sie die GPU-Voreinstellung in
Evis Seitenleiste passend zu Ihrer Hardware.

Die Ausführung nur auf der CPU (die „CPU … GB RAM“-Voreinstellungen) ist ein Notfall-Fallback:
Evi bleibt auch ohne passende Grafikkarte nutzbar, allerdings sind die Antworten deutlich langsamer.
Bevorzugen Sie eine echte GPU, wann immer Sie können.

---------------------------------------------------------------------------------
  Vollständig portabel – wenn Sie das Internet benötigen
---------------------------------------------------------------------------------

Evi ist portabel: Kopieren Sie den gesamten Ordner auf ein anderes Laufwerk, einen USB-Stick usw.
oder PC, dann starten Sie es dort. Chats, Erinnerungen, Einstellungen, Sicherheitsdaten und Ihre
Die Aktivierungsdatei bleibt normalerweise in diesem Ordner (die Aktivierung ist an die Datei gebunden).
PC, nicht der Ordnerpfad).

Das Internet dient hauptsächlich zum Herunterladen von Dingen (Modelldateien, optional).
Stimmen oder Extras, Updates) und für optionale Funktionen wie Websuche, E-Mail,
Streaming oder Wetter, wenn Sie den Netzwerkzugriff zulassen.

Kernchat, Speicher, Notizen, Timer, Dateitools in Ihrem zulässigen Ordner, lokal
Spracherkennung, lokale Sprachausgabe und die Privatsphärensperre laufen auf Ihrem
Maschine, ohne Ihre Gespräche an einen Cloud-Dienst zu senden. Optional online
Funktionen werden nur ausgeführt, wenn der Netzwerkzugriff aktiviert ist und Sie sie verwenden.

---------------------------------------------------------------------------------
  Sicherheit: PIN und Sprachentsperrung (Kopierschutz)
---------------------------------------------------------------------------------

Evi kann eine Sicherheits-PIN und optionale Sprachregistrierung auf Ihrem Gerät verwenden.

Wenn die Sprachentsperrung verwendet wird, kann bei jedem Versuch eine kurze Reihe zufälliger Wörter abgefragt werden
Das ändert sich jedes Mal – kein fester Satz für immer. Das blockiert das Einfache
Trick, eine einzelne alte Aufnahme Ihrer Stimme abzuspielen. Ihre PIN bleibt bestehen
separate Verteidigungslinie.

Dadurch soll Gelegenheitsmissbrauch verhindert werden; Kein Verbraucherprodukt kann es versprechen
Perfektion gegen jeden Angriff (z. B. jemand, der sowohl Ihre PIN als auch Ihre PIN hat).
ausgefeilte Stimmmimikry). Halten Sie Ihre PIN geheim und schließen Sie die Einrichtung ab
App führt Sie.

---------------------------------------------------------------------------------
  Fehlerbehebung (kurze Checkliste)
---------------------------------------------------------------------------------

• Keine KI-Antworten / Modellfehler
  → Mindestens eine passende .gguf in models\llm\ ? Siehe models\llm\README.txt.
  → Probieren Sie ein kleineres Modell oder eine CPU-Voreinstellung in der Seitenleiste aus, wenn der GPU-Pfad fehlschlägt.

• Kein Mikrofon
  → Windows-Soundeinstellungen: Testen Sie das Mikrofon. Wählen Sie in Evi unten das Gerät aus
    Mikrofon und Speichern.

• Keine Sprachausgabe
  → Überprüfen Sie, ob im Ordner „piper\“ Sprachdateien für Ihre Sprache vorhanden sind
    Wählen Sie in der Seitenleiste eine Stimme aus.

• Web oder YouTube schlägt fehl
  → Deaktivieren Sie „Gesamten Datenverkehr blockieren“ in der Seitenleiste, wenn Sie Online-Funktionen wünschen.
  → Für die YouTube-Wiedergabe sind in der Regel VLC Portable und Netzwerkzugriff erforderlich.

• Nach dem Bearbeiten von Spickzetteln
  → Starten Sie Evi neu, damit alle Texthelfer Änderungen zuverlässig übernehmen.

---------------------------------------------------------------------------------
  Fehlerbehebung (erweiterte Referenz)
---------------------------------------------------------------------------------

Schnellchecks (immer zuerst)
  • Windows 10 oder 11 64-Bit, aktualisiert, nach großen Änderungen neu gestartet?
  • Evi läuft aus einem vollständig extrahierten Ordner – nicht aus einem Archiv?
  • Vermeiden Sie Cloud-synchronisierte Ordner (OneDrive usw.) für den Live-Datenordner
    Evi wird ausgeführt – verwenden Sie einen lokalen Pfad wie C:\EviPortable oder D:\Tools\Evi, wenn
    möglich.
  • Genügend freier Speicherplatz für das Modell, Chats und Updates?
  • Nach dem Ändern von Modellen, Stimmen oder Spickzetteln: Beenden Sie Evi vollständig und starten Sie
    wieder.

1) Betriebssystem
  • Evi ist nur für Windows 10 und 11; Andere Betriebssystemversionen werden nicht unterstützt.
  • Wenn die App überhaupt nicht startet, extrahieren Sie das Paket vollständig und überprüfen Sie das Antivirenprogramm
    Protokolle für blockierte ausführbare Dateien und versuchen Sie es mit einem kürzeren Installationspfad ohne Rare
    Nur Unicode-Zeichen.

2) Ordnerpfad, Antivirus, Portabilität
  • Fügen Sie in der Sicherheitssoftware einen Ausschluss für Ihren Evi-Stammordner hinzu, wenn Scans durchgeführt werden
    Starten Sie sehr langsam oder sperren Sie Dateien während des Downloads.
  • USB-Sticks: bevorzugen Sie USB 3 + NTFS; Sehr langsame Medien machen große Modelle schmerzhaft.

3) Sprachmodell (.gguf)
  • Symptome: keine Antworten, Modellfehler, sofortiger Ladefehler.
  • Korrekturen: Überprüfen Sie, ob models\llm\ eine vollständige .gguf-Datei (nicht 0 Byte) enthält. erneut herunterladen
bei Bedarf; Passen Sie die Modellgröße mithilfe von models\llm\README.txt an den VRAM an. Wenn Sie unsicher sind,
    Behalten Sie eine einzelne getestete q4_k_m-Datei im Ordner.
  • mehrere .gguf-Dateien: Evi kann die größte auswählen, die zu Ihrem VRAM passt – wenn Sie möchten
    vermuten Sie einen Konflikt, testen Sie mit nur einer Datei.

4) GPU, CUDA, Treiber, nicht genügend Arbeitsspeicher
  • Aktualisieren Sie den NVIDIA-Treiber. Erzwingen Sie bei Laptops die separate GPU/Leistung
    Modus für Evi, sofern Windows dies zulässt.
  • Wenn OOM- oder GPU-Abstürze auftreten, verwenden Sie einen kleineren Prüfpunkt, schließen Sie andere GPU-Apps.
    niedrigere Temperatur oder wechseln Sie zu einer CPU-Voreinstellung (langsamer, aber stabiler).

5) Nur-CPU-Modus
  • Voraussichtlich langsam; genügend System-RAM freigeben; schwere Hintergrundaufgaben schließen;
    Verwenden Sie bei langen Sitzungen den Energieplan „Hohe Leistung“.

6) Aktivierung
  • Fügen Sie die Schlüssel sorgfältig ein (keine zusätzlichen Leerzeichen); Schlüssel sind an eine Maschinen-ID gebunden.
  • Nach größeren Hardwareänderungen benötigen Sie möglicherweise einen Ersatzschlüssel – nutzen Sie den Support
    Adresse mit Ihren Daten.

7) Mikrofon
  • Windows-Datenschutz → Mikrofon → Desktop-Apps zulassen.
  • Stellen Sie das richtige Standardaufnahmegerät ein. Wählen Sie in Evi dasselbe Gerät und speichern Sie es.
  • Bluetooth-Headsets können die Latenz erhöhen – testen Sie es mit einem USB-Mikrofon, wenn Sie sich nicht sicher sind.
  • Möglicherweise verfügt eine andere App über den exklusiven Modus – schließen Sie die Besprechungssoftware vorübergehend.

8) Spracherkennung (lokal)
  • Wenn die Erkennung nie abgeschlossen wird, stellen Sie sicher, dass sich die Modelldateien unter models\whisper befinden
    intakt und erlauben Sie das Netzwerk bei erstmaligen Modellabrufen, wenn Ihr Build dies benötigt.

9) Sprachausgabe (Piper / TTS)
  • Bestätigen Sie, dass Piper\ ein Sprachpaket für Ihre UI-Sprache enthält; Wählen Sie eine Stimme aus
    die Seitenleiste; Überprüfen Sie den Windows-Lautstärkemixer – Evi ist möglicherweise pro App stummgeschaltet.

10) Netzwerk und „Gesamten Datenverkehr blockieren“
  • Deaktivieren Sie die Blockierung für Web, E-Mail-Helper, Wetter oder Downloads.
  • Unternehmens-Proxys oder VPNs benötigen möglicherweise IT-Hilfe für Zulassungslisten.

11) YouTube und Medien
  • Behalten Sie das mitgelieferte VLC Portable-Layout bei; Netzwerkzugriff aktivieren; lesen
    Portable\VLCPortable-Anleitung, wenn der Pfad verschoben wurde.

12) UI-Sprache und Spickzettel
  • Spickzettel finden Sie pro Sprachdatei unter „cheatssheets\“ – siehe „cheatssheets\README.txt“.
  • Änderungen als UTF-8 speichern; Starten Sie Evi nach den Änderungen neu.

13) Sicherheit (PIN / Sprachentriegelung)
  • Nutzen Sie eine ruhige Umgebung; Überprüfen Sie die Mikrofonverstärkung erneut. Geben Sie niemals Ihre PIN weiter.
  • Eingabeaufforderungen mit zufälligen Wörtern sind beabsichtigt – alte Sprachaufnahmen sollten nicht entsperrt werden.

14) Leistung, Einfrieren, Abstürze
  • Reduzieren Sie die Modellgröße, verbessern Sie die Kühlung und lesen Sie ggf. alle crash.logs im Baum
    Build erstellt eine und macht die letzte Änderung, die Sie vor Fehlern vorgenommen haben, rückgängig.

15) Bei der Kontaktaufnahme mit dem Support
  • Geben Sie Maschinen-ID, Windows-Version, GPU-Modell + VRAM + Treiber an, einschließlich .gguf
    Sie verwenden, und den genauen Fehlertext (keine geheimen Schlüssel).

Vollständige Referenz zur Fehlerbehebung (diese Sprache): Manual\FEHLERSUCHE_DE.txt

---------------------------------------------------------------------------------
  Support – Serienschlüssel und Maschinen-ID
---------------------------------------------------------------------------------

E-Mail: Brielbeck@hotmail.de
Geben Sie bei der Anfrage immer Ihre Maschinen-ID vom Aktivierungsbildschirm an
Serienschlüssel oder einen Ersatzschlüssel nach Hardwareänderungen.

===========================================================================