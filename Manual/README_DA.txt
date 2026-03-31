=================================================================================
  Evi Portable — Brugervejledning (oversigt)
  Dokument: Engelsk • Gælder den build, du har modtaget med denne mappe
=================================================================================

Læg også dine egne længere vejledninger eller oversættelser her (f.eks. EN_User_Manual.pdf,
DE_Handbuch.txt). Denne fil er valgfri for Evi at køre; det er op til dig at læse
eller print.

Lokaliserede kopier: README_<LANG>.txt og FEHLERSUCHE_<LANG>.txt i denne mappe
(samme sprogkoder som webstedets UI). Engelsk oversigt: denne README.txt;
Engelsk fejlfinding: FEHLERSUCHE_EN.txt. Tysk fejlfinding er også
vedligeholdes i hånden som FEHLERSUCHE_DE.txt.

Mappeindeks (filnavn, generator): README.md

--------------------------------------------------------------------------
  Operativsystem
--------------------------------------------------------------------------

Evi Portable er kun til Microsoft Windows 10 og Windows 11. Det er det ikke
understøttet på Windows 7/8, macOS, Linux eller mobile operativsystemer.

--------------------------------------------------------------------------
  Første start - fra download til at køre Evi
--------------------------------------------------------------------------

1) Installationssted
   Kopier eller udpak hele Evi-mappen til et sted, du kontrollerer - for eksempel
   dit skrivebord, dokumenter eller en USB-stick. Behold mappestrukturen som
   leveret (slet ikke undermapper, du ikke selv har oprettet).

2) Sprogmodel (påkrævet)
   Evi har brug for én hoved-AI-modelfil (udvidelsen .gguf) i mappen:
   modeller\llm\
   Se models\llm\README.txt for størrelsesanbefalinger. Når filen er der,
   start Evi; den registrerer modellen automatisk, når det er muligt.

3) Første lancering — aktivering
   Når du starter Evi første gang, vises et aktiveringsvindue.
   • Din pc viser et maskin-id (unik for denne hardware).
   • Kopier maskin-id'et (knap: "Kopier maskin-id") og send det via e-mail til:
     Brielbeck@hotmail.de
   • Du vil modtage en seriel nøgle, der kun virker på den samme pc
     (nøglen er bundet til din hardware).
   • Indsæt nøglen i aktiveringsvinduet og vælg Aktiver.

   Hvis du ændrer større hardware eller flytter disken på en måde, der ændrer ID'et,
   du skal muligvis have en ny nøgle — kontakt den samme adresse.

4) Efter aktivering
   Hovedvinduet åbnes. Vælg sprog, mikrofon og stemme til venstre
   indstillingspanel. Sig "åbn snydearket" når som helst for kommandoeksempler
   (se cheatsheets\en.txt og søsterfiler for andre sprog).

5) Valgfrit: Åbn denne manual fra Windows
   Gå til mappen Evi i File Explorer, derefter Manual\README.txt, og åbn den
   med Notesblok eller en hvilken som helst tekstfremviser.

--------------------------------------------------------------------------
  Interface sprog (GUI)
--------------------------------------------------------------------------

Brugergrænsefladen følger det sprog, du vælger under Sprog øverst
i det venstre indstillingspanel (første blok i sidebjælken). Når du har valgt en
sprog, menuer, knapper, etiketter og det meste af tekst på skærmen skifter til det
sprog, hvor der findes oversættelser. Du kan ændre det til enhver tid; kun den
ordlydsændringer, ikke layoutet.

Tip: Kommandosnydearkene i cheatsheets\-mappen er opført pr
sprogkode (en.txt, de.txt, …). For detaljer se cheatsheets\README.txt.
Denne Manual\-mappe er den længere produktoversigt; snydeark er de
hurtig "hvad skal man sige" liste.

--------------------------------------------------------------------------
  Grafikkort (GPU) — hurtig guide
--------------------------------------------------------------------------

Et stærkt mellemvalg er en NVIDIA GeForce RTX 4070 Ti med 12 GB video
Hukommelse: god balance mellem hastighed, kontekststørrelse og plads til større modeller.

Kort fra omkring RTX 3060 til RTX 5090 kan fungere godt; den bedste pasform afhænger
på RAM, CPU, køling, og hvilken modelfil du installerer. Brug GPU-forudindstillingen i
Evis sidebjælke, der matcher din hardware.

Kun at køre på CPU'en (forudindstillingerne "CPU ... GB RAM") er en nødsituation:
Evi forbliver brugbar uden et passende grafikkort, men svarene er meget langsommere.
Foretrække en rigtig GPU, når du kan.

--------------------------------------------------------------------------
  Fuldt bærbar - når du har brug for internettet
--------------------------------------------------------------------------

Evi er bygget til at være bærbar: kopier hele mappen til et andet drev, USB-stick,
eller pc, så start den der. Chats, minder, indstillinger, sikkerhedsdata og dine
aktiveringsfil forbliver normalt i den mappe (aktivering er knyttet til
pc, ikke mappestien).

Internettet er primært til ting, du vælger at downloade (modelfiler, valgfrit
stemmer eller ekstramateriale, opdateringer) og for valgfri funktioner som websøgning, mail,
streaming eller vejr, når du tillader netværksadgang.

Kernechat, hukommelse, noter, timere, filværktøjer i din tilladte mappe, lokalt
talegenkendelse, lokal stemmeoutput og privatlivslåsen kører på din
maskine uden at sende dine samtaler til en skytjeneste. Valgfri online
funktioner kører kun, når netværksadgang er aktiveret, og du bruger dem.

--------------------------------------------------------------------------
  Sikkerhed: PIN-kode og stemmeoplåsning (anti-kopi)
--------------------------------------------------------------------------

Evi kan bruge en sikkerhedspinkode og valgfri stemmetilmelding på din enhed.

Når stemmeoplåsning bruges, kan hvert forsøg bede om et kort sæt tilfældige ord
der ændrer sig hver gang - ikke en fast sætning for altid. Det blokerer det nemme
trick til at afspille en enkelt gammel optagelse af din stemme. Din pinkode forbliver en
separat forsvarslinje.

Dette er designet til at stoppe tilfældigt misbrug; intet forbrugerprodukt kan love
perfektion mod ethvert angreb (for eksempel en person, der har både din PIN-kode og
sofistikeret stemmemimik). Hold din PIN-kode privat og fuldfør opsætningen som
app guider dig.

--------------------------------------------------------------------------
  Fejlfinding (kort tjekliste)
--------------------------------------------------------------------------

• Ingen AI-svar/modelfejl
  → Mindst en passende .gguf i modeller\llm\ ? Se modeller\llm\README.txt.
  → Prøv en mindre model eller en CPU-forudindstilling i sidebjælken, hvis GPU-stien fejler.

• Ingen mikrofon
  → Windows lydindstillinger: test mikrofonen. I Evi skal du vælge enheden under
    Mikrofon og Gem.

• Ingen stemmeudgang
  → Kontroller, at stemmefiler til dit sprog findes i piper\-mappen og
    vælg en stemme i sidebjælken.

• Web eller YouTube fejler
  → Slå "Bloker al trafik" fra i sidebjælken, hvis du vil have onlinefunktioner.
  → Til YouTube-afspilning kræves normalt VLC Portable og netværksadgang.

• Efter redigering af snydeark
  → Genstart Evi, så alle teksthjælpere opfanger ændringer pålideligt.

--------------------------------------------------------------------------
  Fejlfinding (udvidet reference)
--------------------------------------------------------------------------

Hurtige kontroller (altid først)
  • Windows 10 eller 11 64-bit, opdateret, genstartet efter store ændringer?
  • Evi kører fra en fuldt udpakket mappe — ikke inde fra et arkiv?
  • Undgå sky-synkroniserede mapper (OneDrive osv.) til livedatamappen mens
    Evi kører — brug en lokal sti såsom C:\EviPortable eller D:\Tools\Evi, når
    muligt.
  • Nok ledig diskplads til modellen, chats og opdateringer?
  • Efter at have skiftet model, stemmer eller snydeark: Afslut Evi helt og start
    igen.

1) Operativsystem
  • Evi er kun til Windows 10 og 11; andre OS-versioner understøttes ikke.
  • Hvis appen slet ikke starter, skal du helt udpakke pakken, kontrollere antivirus
    logfiler for blokerede eksekverbare filer, og prøv en kortere installationssti uden sjældne
    Unicode-tegn.

2) Mappesti, antivirus, portabilitet
  • Tilføj en udelukkelse for din Evi-rodmappe i sikkerhedssoftware, hvis scanninger gør det
    opstart meget langsom eller lås filer under downloads.
  • USB-sticks: foretrækker USB 3 + NTFS; meget langsomme medier gør store modeller smertefulde.

3) Sprogmodel (.gguf)
  • symptomer: ingen svar, modelfejl, øjeblikkelig fejl ved indlæsning.
  • rettelser: kontroller, at models\llm\ indeholder en komplet .gguf (ikke 0 bytes); gen-download
hvis nødvendigt; match modelstørrelse til VRAM ved hjælp af models\llm\README.txt; hvis usikker,
    behold en enkelt testet q4_k_m-fil i mappen.
  • flere .gguf-filer: Evi kan vælge den største, der passer til din VRAM — hvis du
    mistanke om en konflikt, test med kun én fil.

4) GPU, CUDA, drivere, ude af hukommelse
  • Opdater NVIDIA-driveren; på bærbare computere, tvinge den diskrete GPU / ydeevne
    tilstand for Evi, hvor Windows tillader det.
  • Hvis du ser OOM- eller GPU-nedbrud, skal du bruge et mindre kontrolpunkt, lukke andre GPU-apps,
    lavere temperatur, eller skift til en CPU-forudindstilling (langsommere, men mere stabil).

5) Kun CPU-tilstand
  • Forventes at være langsom; fri nok system-RAM; lukke tunge baggrundsopgaver;
    brug strømplanen "Høj ydeevne" under lange sessioner.

6) Aktivering
  • Indsæt nøgler forsigtigt (ingen ekstra mellemrum); nøgler er bundet til ét maskin-id.
  • Efter større hardwareændringer skal du muligvis have en erstatningsnøgle — brug supporten
    adresse med dine oplysninger.

7) Mikrofon
  • Windows Privatliv → Mikrofon → tillad desktop-apps.
  • Indstil den korrekte standardoptageenhed; i Evi vælg den samme enhed og Gem.
  • Bluetooth-headset kan tilføje latency — test med en USB-mikrofon, hvis du er usikker.
  • En anden app har muligvis eksklusiv tilstand — luk mødesoftware midlertidigt.

8) Talegenkendelse (lokal)
  • Hvis genkendelsen aldrig afsluttes, skal du sikre dig, at modelfilerne under models\whisper are
    intakt og tillad netværk på førstegangsmodelhentninger, hvis din build har brug for det.

9) Stemmeoutput (Piper / TTS)
  • Bekræft, at piper\ indeholder en stemmepakke til dit brugergrænsefladesprog; vælge en stemme ind
    sidebjælken; tjek Windows volume mixer — Evi kan være slået fra pr. app.

10) Netværk og "Bloker al trafik"
  • Slå spærringen fra for web, mailhjælpere, vejr eller downloads.
  • Virksomhedsfuldmagter eller VPN'er kan kræve IT-hjælp til tilladelseslister.

11) YouTube og medier
  • Behold det medfølgende VLC Portable-layout; aktiver netværksadgang; læse
    Portable\VLCPortable vejledning, hvis stien blev flyttet.

12) UI-sprog og snydeark
  • Snydeark er pr. sprogfil under cheatsheets\ — se cheatsheets\README.txt.
  • Gem redigeringer som UTF-8; genstart Evi efter redigeringer.

13) Sikkerhed (PIN / stemmeoplåsning)
  • Brug et roligt miljø; tjek mikrofonforstærkningen igen; del aldrig din pinkode.
  • Tilfældige ord-prompter er bevidste – gamle stemmeoptagelser bør ikke låses op.

14) Ydeevne, fryser, går ned
  • Reducer modelstørrelse, forbedre køling, læs enhver crash.log i træet, hvis din
    build opretter en, og rulle tilbage den sidste ændring, du lavede før fejl.

15) Ved henvendelse til support
  • Inkluder Machine ID, Windows-version, GPU-model + VRAM + driver, som .gguf
    du bruger, og den nøjagtige fejltekst (ikke hemmelige nøgler).

Fuld fejlfindingsreference (dette sprog): Manual\FEHLERSUCHE_DA.txt

--------------------------------------------------------------------------
  Support — serielle nøgler og maskin-id
--------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Inkluder altid dit maskin-id fra aktiveringsskærmen, når du anmoder om en
seriel nøgle eller en erstatningsnøgle efter hardwareændringer.

=================================================================================