=================================================================================
  Evi Portable — Brukerhåndbok (oversikt)
  Dokument: Engelsk • Gjelder bygget du mottok med denne mappen
=================================================================================

Sett dine egne lengre veiledninger eller oversettelser her også (f.eks. EN_User_Manual.pdf,
DE_Handbuch.txt). Denne filen er valgfri for Evi å kjøre; det er opp til deg å lese
eller skriv ut.

Lokaliserte kopier: README_<LANG>.txt og FEHLERSUCHE_<LANG>.txt i denne mappen
(samme språkkoder som brukergrensesnittet på nettstedet). Engelsk oversikt: denne README.txt;
Engelsk feilsøking: FEHLERSUCHE_EN.txt. Tysk feilsøking er også
vedlikeholdes for hånd som FEHLERSUCHE_DE.txt.

Mappeindeks (filnavn, generator): README.md

--------------------------------------------------------------------------
  Operativsystem
--------------------------------------------------------------------------

Evi Portable er kun for Microsoft Windows 10 og Windows 11. Det er det ikke
støttes på Windows 7/8, macOS, Linux eller mobile operativsystemer.

--------------------------------------------------------------------------
  Første start - fra nedlasting til å kjøre Evi
--------------------------------------------------------------------------

1) Installasjonssted
   Kopier eller pakk ut hele Evi-mappen til et sted du kontrollerer - for eksempel
   skrivebordet, dokumenter eller en USB-pinne. Behold mappestrukturen som
   levert (ikke slett undermapper du ikke har laget selv).

2) Språkmodell (påkrevd)
   Evi trenger én hoved-AI-modellfil (utvidelse .gguf) i mappen:
   modeller\llm\
   Se modeller\llm\README.txt for størrelsesanbefalinger. Etter at filen er der,
   start Evi; den oppdager modellen automatisk når det er mulig.

3) Første lansering — aktivering
   Når du starter Evi første gang, vises et aktiveringsvindu.
   • PC-en din viser en maskin-ID (unikt for denne maskinvaren).
   • Kopier maskin-ID (knapp: "Kopier maskin-ID") og send den på e-post til:
     Brielbeck@hotmail.de
   • Du vil motta en seriell nøkkel som bare fungerer på den samme PC-en
     (nøkkelen er bundet til maskinvaren din).
   • Lim inn nøkkelen i aktiveringsvinduet og velg Aktiver.

   Hvis du endrer hovedmaskinvare eller flytter disken på en måte som endrer ID-en,
   det kan hende du trenger en ny nøkkel – kontakt samme adresse.

4) Etter aktivering
   Hovedvinduet åpnes. Velg språk, mikrofon og stemme til venstre
   innstillingspanelet. Si "åpne juksearket" når som helst for kommandoeksempler
   (se cheatsheets\en.txt og søsterfiler for andre språk).

5) Valgfritt: åpne denne håndboken fra Windows
   I Filutforsker går du til Evi-mappen, deretter Manual\README.txt, og åpner den
   med Notisblokk eller en hvilken som helst tekstvisning.

--------------------------------------------------------------------------
  Grensesnittspråk (GUI)
--------------------------------------------------------------------------

Brukergrensesnittet følger språket du velger under Språk øverst
i venstre innstillingspanel (første blokk i sidefeltet). Etter at du har valgt en
språk, menyer, knapper, etiketter og det meste av tekst på skjermen bytter til det
språk der det finnes oversettelser. Du kan endre det når som helst; bare
ordlydendringer, ikke oppsettet.

Tips: Kommando-juksearkene i cheatsheets\-mappen er oppført pr
språkkode (en.txt, de.txt, …). For detaljer se cheatsheets\README.txt.
Denne Manual\-mappen er den lengre produktoversikten; jukseark er
rask "hva skal jeg si"-liste.

--------------------------------------------------------------------------
  Grafikkort (GPU) — hurtigveiledning
--------------------------------------------------------------------------

Et sterkt mellomvalg er en NVIDIA GeForce RTX 4070 Ti med 12 GB video
minne: god balanse mellom hastighet, kontekststørrelse og plass til større modeller.

Kort fra ca. RTX 3060 til RTX 5090 kan fungere bra; den beste passformen avhenger
på RAM, CPU, kjøling, og hvilken modellfil du installerer. Bruk GPU-forhåndsinnstillingen i
Evis sidefelt for å matche maskinvaren din.

Å kjøre kun på CPU (forhåndsinnstillingene "CPU ... GB RAM") er en nødsituasjon:
Evi forblir brukbar uten et passende grafikkort, men svarene er mye tregere.
Foretrekk en ekte GPU når du kan.

--------------------------------------------------------------------------
  Fullt bærbar - når du trenger Internett
--------------------------------------------------------------------------

Evi er bygget for å være bærbar: kopier hele mappen til en annen stasjon, USB-pinne,
eller PC, og start den der. Chatter, minner, innstillinger, sikkerhetsdata og dine
aktiveringsfilen forblir normalt i den mappen (aktivering er knyttet til
PC, ikke mappebanen).

Internett er hovedsakelig for ting du velger å laste ned (modellfiler, valgfritt
stemmer eller ekstramateriale, oppdateringer) og for valgfrie funksjoner som nettsøk, e-post,
strømming eller vær når du tillater nettverkstilgang.

Kjernechat, minne, notater, tidtakere, filverktøy i din tillatte mappe, lokalt
talegjenkjenning, lokal stemmeutgang og personvernlåsen kjører på din
maskin uten å sende samtalene dine til en skytjeneste. Valgfritt på nett
funksjoner kjører bare når nettverkstilgang er på og du bruker dem.

--------------------------------------------------------------------------
  Sikkerhet: PIN-kode og stemmelås (antikopi)
--------------------------------------------------------------------------

Evi kan bruke en sikkerhets-PIN og valgfri stemmeregistrering på enheten din.

Når stemmeopplåsing brukes, kan hvert forsøk be om et kort sett med tilfeldige ord
som endres hver gang - ikke en fast setning for alltid. Det blokkerer det enkle
trikset med å spille av et enkelt gammelt opptak av stemmen din. PIN-koden din forblir en
egen forsvarslinje.

Dette er designet for å stoppe tilfeldig misbruk; ingen forbrukerprodukter kan love
perfeksjon mot hvert angrep (for eksempel noen som har både PIN-koden din og
sofistikert stemmemimikk). Hold PIN-koden din privat og fullfør oppsettet som
appen veileder deg.

--------------------------------------------------------------------------
  Feilsøking (kort sjekkliste)
--------------------------------------------------------------------------

• Ingen AI-svar / modellfeil
  → Minst en passende .gguf i modellene\llm\ ? Se modeller\llm\README.txt.
  → Prøv en mindre modell eller en CPU-forhåndsinnstilling i sidefeltet hvis GPU-banen mislykkes.

• Ingen mikrofon
  → Windows lydinnstillinger: test mikrofonen. I Evi velger du enheten under
    Mikrofon og lagre.

• Ingen stemmeutgang
  → Sjekk at talefiler for språket ditt finnes i piper\-mappen og
    velg en stemme i sidefeltet.

• Web eller YouTube mislykkes
  → Slå av «Blokker all trafikk» i sidefeltet hvis du vil ha nettfunksjoner.
  → For YouTube-avspilling kreves vanligvis VLC Portable og nettverkstilgang.

• Etter å ha redigert jukseark
  → Start Evi på nytt slik at alle teksthjelpere fanger opp endringer pålitelig.

--------------------------------------------------------------------------
  Feilsøking (utvidet referanse)
--------------------------------------------------------------------------

Raske kontroller (alltid først)
  • Windows 10 eller 11 64-bit, oppdatert, omstartet etter store endringer?
  • Evi kjører fra en fullstendig utpakket mappe — ikke fra innsiden av et arkiv?
  • Unngå skysynkroniserte mapper (OneDrive, etc.) for live data-mappen mens
    Evi kjører — bruk en lokal bane som C:\EviPortable eller D:\Tools\Evi når
    mulig.
  • Nok ledig diskplass til modellen, chatter og oppdateringer?
  • Etter å ha byttet modell, stemmer eller jukseark: Avslutt Evi helt og start
    igjen.

1) Operativsystem
  • Evi er kun for Windows 10 og 11; andre OS-versjoner støttes ikke.
  • Hvis appen ikke starter i det hele tatt, trekk ut pakken fullstendig, sjekk antivirus
    logger for blokkerte kjørbare filer, og prøv en kortere installasjonsbane uten sjelden
    Unicode-tegn.

2) Mappebane, antivirus, portabilitet
  • Legg til en ekskludering for Evi-rotmappen i sikkerhetsprogramvaren hvis skanninger gjør det
    oppstart veldig sakte eller lås filer under nedlastinger.
  • USB-pinner: foretrekker USB 3 + NTFS; svært trege medier gjør store modeller smertefulle.

3) Språkmodell (.gguf)
  • symptomer: ingen svar, modellfeil, umiddelbar feil ved innlasting.
  • rettelser: verifiser at models\llm\ inneholder en komplett .gguf (ikke 0 byte); last ned på nytt
om nødvendig; match modellstørrelse til VRAM ved hjelp av models\llm\README.txt; hvis usikker,
    hold en enkelt testet q4_k_m-fil i mappen.
  • flere .gguf-filer: Evi kan velge den største som passer til VRAM-en din – hvis du
    mistenker en konflikt, test med bare én fil.

4) GPU, CUDA, drivere, tom for minne
  • Oppdater NVIDIA-driveren; på bærbare datamaskiner, tving den diskrete GPUen / ytelsen
    modus for Evi der Windows tillater det.
  • Hvis du ser OOM- eller GPU-krasj, bruk et mindre sjekkpunkt, lukk andre GPU-apper,
    lavere temperatur, eller bytt til en CPU-forhåndsinnstilling (langsommere, men jevnere).

5) Bare CPU-modus
  • Forventet å være treg; ledig nok system-RAM; lukke tunge bakgrunnsoppgaver;
    bruk strømplan "Høy ytelse" under lange økter.

6) Aktivering
  • Lim inn nøkler forsiktig (ingen ekstra mellomrom); nøkler er knyttet til én maskin-ID.
  • Etter større maskinvareendringer kan det hende du trenger en erstatningsnøkkel — bruk støtten
    adresse med dine opplysninger.

7) Mikrofon
  • Windows Personvern → Mikrofon → tillat skrivebordsapper.
  • Angi riktig standard opptaksenhet; i Evi velger du den samme enheten og lagrer.
  • Bluetooth-hodesett kan legge til ventetid — test med en USB-mikrofon hvis du er usikker.
  • En annen app kan ha eksklusiv modus – lukk møteprogramvare midlertidig.

8) Talegjenkjenning (lokal)
  • Hvis gjenkjenningen aldri fullfører, sørg for at modellfiler under models\whisper are
    intakt og tillat nettverk på førstegangsmodellhentinger hvis bygget trenger det.

9) Stemmeutgang (Piper / TTS)
  • Bekreft at piper\ inneholder en talepakke for brukergrensesnittspråket ditt; ta en stemme inn
    sidefeltet; sjekk Windows volummikser - Evi kan dempes per app.

10) Nettverk og "Blokker all trafikk"
  • Slå av blokkeringen for web, e-posthjelpere, vær eller nedlastinger.
  • Bedriftsfullmakter eller VPN-er kan kreve IT-hjelp for godkjenningslister.

11) YouTube og media
  • Behold det medfølgende VLC Portable-oppsettet; aktivere nettverkstilgang; lese
    Portable\VLCPortable veiledning hvis banen ble flyttet.

12) UI-språk og jukseark
  • Jukseark er per språkfil under jukseark\ — se jukseark\README.txt.
  • Lagre redigeringer som UTF-8; start Evi på nytt etter redigeringer.

13) Sikkerhet (PIN / stemmelås)
  • Bruk et rolig miljø; sjekk mikrofonforsterkningen på nytt; del aldri PIN-koden din.
  • Tilfeldige ordmeldinger er tilsiktet – gamle stemmeopptak skal ikke låses opp.

14) Ytelse, fryser, krasjer
  • Reduser modellstørrelsen, forbedre kjølingen, les eventuell crash.logg i treet hvis din
    build oppretter en, og rulle tilbake den siste endringen du gjorde før feil.

15) Når du kontakter support
  • Inkluder maskin-ID, Windows-versjon, GPU-modell + VRAM + driver, som .gguf
    du bruker, og den eksakte feilteksten (ikke hemmelige nøkler).

Fullstendig feilsøkingsreferanse (dette språket): Manual\FEHLERSUCHE_NO.txt

--------------------------------------------------------------------------
  Støtte — serienøkler og maskin-ID
--------------------------------------------------------------------------

E-post: Brielbeck@hotmail.de
Inkluder alltid din maskin-ID fra aktiveringsskjermen når du ber om en
seriell nøkkel eller en erstatningsnøkkel etter maskinvareendringer.

=================================================================================