===========================================================================
  Evi Portable — Gebruikershandleiding (overzicht)
  Document: Engels • Geldt voor de build die u bij deze map heeft ontvangen
===========================================================================

Plaats hier ook uw eigen langere handleidingen of vertalingen (bijv. EN_User_Manual.pdf,
DE_Handboek.txt). Dit bestand is optioneel voor Evi om uit te voeren; het is aan jou om te lezen
of afdrukken.

Gelokaliseerde kopieën: README_<LANG>.txt en FEHLERSUCHE_<LANG>.txt in deze map
(dezelfde taalcodes als de gebruikersinterface van de website). Engels overzicht: deze README.txt;
Probleemoplossing in het Engels: FEHLERSUCHE_EN.txt. Duitse probleemoplossing is dat ook
handmatig onderhouden als FEHLERSUCHE_DE.txt.

Mapindex (bestandsnaamgeving, generator): README.md

-----------------------------------------------------------------------
  Besturingssysteem
-----------------------------------------------------------------------

Evi Portable is alleen voor Microsoft Windows 10 en Windows 11. Dat is het niet
ondersteund op Windows 7/8, macOS, Linux of mobiele besturingssystemen.

-----------------------------------------------------------------------
  Eerste start — van downloaden tot het uitvoeren van Evi
-----------------------------------------------------------------------

1) Installatielocatie
   Kopieer of extraheer bijvoorbeeld de hele Evi-map naar een plaats die u beheert
   uw bureaublad, documenten of een USB-stick. Behoud de mapstructuur zoals
   afgeleverd (verwijder geen submappen die u niet zelf heeft aangemaakt).

2) Taalmodel (vereist)
   Evi heeft één hoofd-AI-modelbestand (extensie .gguf) nodig in de map:
   modellen\llm\
   Zie models\llm\README.txt voor maataanbevelingen. Nadat het bestand daar is,
   begin Evi; het detecteert het model indien mogelijk automatisch.

3) Eerste lancering – activering
   Wanneer je Evi de eerste keer opstart, verschijnt er een activatievenster.
   • Uw pc toont een machine-ID (uniek voor deze hardware).
   • Kopieer de Machine-ID (knop: "Machine-ID kopiëren") en stuur deze per e-mail naar:
     Brielbeck@hotmail.de
   • U ontvangt een seriële sleutel die alleen op diezelfde pc werkt
     (de sleutel is gebonden aan uw hardware).
   • Plak de sleutel in het activeringsvenster en kies Activeren.

   Als u belangrijke hardware wijzigt of de schijf zodanig verplaatst dat de ID verandert,
   Mogelijk hebt u een nieuwe sleutel nodig. Neem contact op met hetzelfde adres.

4) Na activering
   Het hoofdvenster wordt geopend. Kies links taal, microfoon en stem
   instellingenpaneel. Zeg op elk gewenst moment "open het spiekbriefje" voor commandovoorbeelden
   (zie cheatsheets\en.txt en zusterbestanden voor andere talen).

5) Optioneel: open deze handleiding vanuit Windows
   Ga in Verkenner naar de map Evi, vervolgens naar Manual\README.txt en open deze
   met Kladblok of een andere tekstviewer.

-----------------------------------------------------------------------
  Interfacetaal (GUI)
-----------------------------------------------------------------------

De gebruikersinterface volgt de taal die u kiest onder Taal bovenaan
van het linker instellingenpaneel (eerste blok in de zijbalk). Nadat u een
taal, menu's, knoppen, labels en de meeste tekst op het scherm schakelen daarnaartoe
taal waar vertalingen bestaan. Je kunt het op elk moment wijzigen; alleen de
de formulering verandert, niet de lay-out.

Tip: De commando-spiekbriefjes in de map spiekbriefjes\ staan per
taalcode (en.txt, de.txt, …). Voor details zie cheatsheets\README.txt.
Deze Handleiding\ map is het langere productoverzicht; spiekbriefjes zijn de
snelle "wat te zeggen" lijst.

-----------------------------------------------------------------------
  Grafische kaart (GPU) — korte handleiding
-----------------------------------------------------------------------

Een sterke middenkeuze is een NVIDIA GeForce RTX 4070 Ti met 12 GB video
geheugen: goede balans tussen snelheid, contextgrootte en ruimte voor grotere modellen.

Kaarten van ongeveer RTX 3060 tot en met RTX 5090 kunnen goed werken; de beste pasvorm hangt ervan af
over RAM, CPU, koeling en welk modelbestand u installeert. Gebruik de GPU-voorinstelling in
Evi's zijbalk die bij uw hardware past.

Alleen draaien op de CPU (de voorinstellingen "CPU … GB RAM") is een noodterugval:
Evi blijft bruikbaar zonder een geschikte grafische kaart, maar de antwoorden zijn veel langzamer.
Geef de voorkeur aan een echte GPU wanneer je maar kunt.

-----------------------------------------------------------------------
  Volledig draagbaar – wanneer u internet nodig heeft
-----------------------------------------------------------------------

Evi is gebouwd om draagbaar te zijn: kopieer de hele map naar een andere schijf, USB-stick,
of pc en start het daar. Chats, herinneringen, instellingen, beveiligingsgegevens en uw
activeringsbestand blijft normaal gesproken in die map (activatie is gekoppeld aan de
PC, niet het mappad).

Het internet is vooral bedoeld voor dingen die u wilt downloaden (modelbestanden, optioneel).
stemmen of extra's, updates) en voor optionele functies zoals zoeken op internet, e-mail,
streaming of het weer wanneer u netwerktoegang toestaat.

Kernchat, geheugen, notities, timers, bestandshulpmiddelen in uw toegestane map, lokaal
spraakherkenning, lokale stemuitvoer en de privacyvergrendeling worden op uw computer uitgevoerd
machine zonder uw gesprekken naar een cloudservice te sturen. Optioneel online
functies werken alleen als netwerktoegang is ingeschakeld en u deze gebruikt.

-----------------------------------------------------------------------
  Beveiliging: pincode en spraakontgrendeling (kopieerbeveiliging)
-----------------------------------------------------------------------

Evi kan een beveiligingspincode en optionele spraakinschrijving op uw apparaat gebruiken.

Wanneer stemontgrendeling wordt gebruikt, kan bij elke poging om een korte reeks willekeurige woorden worden gevraagd
dat verandert elke keer – niet voor altijd één vaste zin. Dat blokkeert het gemakkelijke
truc om een enkele oude opname van je stem opnieuw af te spelen. Uw pincode blijft een
aparte verdedigingslinie.

Dit is bedoeld om incidenteel misbruik te stoppen; geen enkel consumentenproduct kan dit beloven
perfectie tegen elke aanval (bijvoorbeeld iemand die zowel uw pincode als
geavanceerde stemimitatie). Houd uw pincode privé en voltooi de installatie zoals de
app begeleidt u.

-----------------------------------------------------------------------
  Probleemoplossing (korte checklist)
-----------------------------------------------------------------------

• Geen AI-antwoorden / modelfout
  → Minstens één geschikte .gguf in models\llm\ ? Zie modellen\llm\README.txt.
  → Probeer een kleiner model of een CPU-voorinstelling in de zijbalk als het GPU-pad mislukt.

• Geen microfoon
  → Windows-geluidsinstellingen: test de microfoon. In Evi kies je het apparaat hieronder
    Microfoon en opslaan.

• Geen stemuitvoer
  → Controleer of er spraakbestanden voor uw taal aanwezig zijn in de map piper\ en
    kies een stem in de zijbalk.

• Web of YouTube faalt
  → Schakel 'Alle verkeer blokkeren' uit in de zijbalk als je online functies wilt.
  → Voor het afspelen van YouTube zijn meestal VLC Portable en netwerktoegang vereist.

• Na het bewerken van spiekbriefjes
  → Start Evi opnieuw op, zodat alle teksthelpers de wijzigingen betrouwbaar oppikken.

-----------------------------------------------------------------------
  Problemen oplossen (uitgebreide referentie)
-----------------------------------------------------------------------

Snelle controles (altijd eerst)
  • Windows 10 of 11 64-bit, bijgewerkt, opnieuw opgestart na grote veranderingen?
  • Evi draait vanuit een volledig uitgepakte map — niet vanuit een archief?
  • Vermijd tijdens het gebruik cloud-gesynchroniseerde mappen (OneDrive, enz.) voor de map met livegegevens
    Evi wordt uitgevoerd: gebruik een lokaal pad zoals C:\EviPortable of D:\Tools\Evi wanneer
    mogelijk.
  • Voldoende vrije schijfruimte voor het model, chats en updates?
  • Na het wisselen van modellen, stemmen of spiekbriefjes: sluit Evi volledig af en begin
    opnieuw.

1) Besturingssysteem
  • Evi is alleen voor Windows 10 en 11; andere besturingssysteemversies worden niet ondersteund.
  • Als de app helemaal niet start, pak dan het pakket volledig uit en controleer de antivirussoftware
    logs voor geblokkeerde uitvoerbare bestanden en probeer een korter installatiepad zonder zeldzaam
    Alleen Unicode-tekens.

2) Mappad, antivirus, draagbaarheid
  • Voeg een uitsluiting toe voor uw Evi-hoofdmap in beveiligingssoftware als er scans worden gemaakt
    start erg langzaam op of vergrendelt bestanden tijdens het downloaden.
  • USB-sticks: voorkeur voor USB 3 + NTFS; zeer trage media maken grote modellen pijnlijk.

3) Taalmodel (.gguf)
  • symptomen: geen antwoorden, modelfouten, onmiddellijke fout bij het laden.
  • oplossingen: controleer of models\llm\ een volledige .gguf bevat (niet 0 bytes); opnieuw downloaden
indien nodig; koppel de modelgrootte aan VRAM met behulp van models\llm\README.txt; indien onzeker,
    bewaar één enkel getest q4_k_m-bestand in de map.
  • meerdere .gguf-bestanden: Evi kan de grootste kiezen die bij uw VRAM past - als u dat wilt
    vermoed een conflict, test met slechts één bestand.

4) GPU, CUDA, stuurprogramma's, onvoldoende geheugen
  • Update het NVIDIA-stuurprogramma; op laptops forceer je de afzonderlijke GPU/prestaties
    modus voor Evi waar Windows dit toestaat.
  • Als u OOM- of GPU-crashes ziet, gebruik dan een kleiner controlepunt, sluit andere GPU-apps,
    lagere temperatuur, of schakel over naar een CPU-voorinstelling (langzamer maar stabieler).

5) Alleen CPU-modus
  • Naar verwachting langzaam; voldoende systeem-RAM vrij; zware achtergrondtaken afsluiten;
    gebruik energieplan "Hoge prestaties" tijdens lange sessies.

6) Activering
  • Plak sleutels zorgvuldig (geen extra spaties); sleutels zijn gekoppeld aan één machine-ID.
  • Na grote hardwarewijzigingen heeft u mogelijk een vervangende sleutel nodig: maak gebruik van de ondersteuning
    adres met uw gegevens.

7) Microfoon
  • Windows Privacy → Microfoon → bureaublad-apps toestaan.
  • Stel het juiste standaard opnameapparaat in; kies in Evi hetzelfde apparaat en Opslaan.
  • Bluetooth-headsets kunnen latentie toevoegen. Test het met een USB-microfoon als u het niet zeker weet.
  • Een andere app heeft mogelijk de exclusieve modus: sluit de vergadersoftware tijdelijk.

8) Spraakherkenning (lokaal)
  • Als de herkenning nooit wordt voltooid, zorg er dan voor dat de modelbestanden onder models\whisper staan
    intact en sta netwerk toe bij het voor de eerste keer ophalen van modellen als uw build dit nodig heeft.

9) Stemuitvoer (Piper / TTS)
  • Bevestig dat piper\ een spraakpakket bevat voor uw UI-taal; kies een stem
    de zijbalk; controleer Windows-volumemixer - Evi kan per app worden gedempt.

10) Netwerk en "Blokkeer al het verkeer"
  • Schakel de blokkering uit voor internet, e-mailhelpers, het weer of downloads.
  • Bedrijfsproxy's of VPN's hebben mogelijk IT-hulp nodig voor toelatingslijsten.

11) YouTube en media
  • Behoud de gebundelde VLC Portable-indeling; netwerktoegang inschakelen; lees
    Portable\VLCPortable begeleiding als het pad is verplaatst.

12) UI-taal en spiekbriefjes
  • Cheatsheets staan per taalbestand onder cheatsheets\ — zie cheatsheets\README.txt.
  • Bewerkingen opslaan als UTF-8; herstart Evi na bewerkingen.

13) Beveiliging (PIN / spraakontgrendeling)
  • Gebruik een rustige omgeving; controleer de microfoonversterking opnieuw; Deel nooit uw pincode.
  • Prompts in willekeurige woorden zijn opzettelijk: oude spraakopnamen mogen niet worden ontgrendeld.

14) Prestaties, vastlopen, crashes
  • Verklein de modelgrootte, verbeter de koeling, lees eventueel crash.log in de boomstructuur
    build maakt er een, en draait de laatste wijziging terug die u vóór de mislukkingen hebt aangebracht.

15) Wanneer u contact opneemt met ondersteuning
  • Inclusief machine-ID, Windows-versie, GPU-model + VRAM + stuurprogramma, welke .gguf
    die u gebruikt, en de exacte fouttekst (geen geheime sleutels).

Volledige referentie voor het oplossen van problemen (deze taal): Manual\FEHLERSUCHE_NL.txt

-----------------------------------------------------------------------
  Ondersteuning — seriële sleutels en machine-ID
-----------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Vermeld altijd uw Machine-ID uit het activeringsscherm wanneer u een aanvraag indient
seriële sleutel of een vervangende sleutel na hardwarewijzigingen.

===========================================================================