=================================================================================
  Evi Portable — Användarmanual (översikt)
  Dokument: Engelska • Gäller byggnaden du fick med den här mappen
=================================================================================

Lägg in dina egna längre guider eller översättningar här också (t.ex. EN_User_Manual.pdf,
DE_Handbuch.txt). Den här filen är valfri för Evi att köra; det är för dig att läsa
eller skriva ut.

Lokaliserade kopior: README_<LANG>.txt och FEHLERSUCHE_<LANG>.txt i den här mappen
(samma språkkoder som webbplatsens UI). Engelsk översikt: denna README.txt;
Engelsk felsökning: FEHLERSUCHE_EN.txt. Tysk felsökning är också
underhålls för hand som FEHLERSUCHE_DE.txt.

Mappindex (filnamn, generator): README.md

----------------------------------------------------------------------------------
  Operativsystem
----------------------------------------------------------------------------------

Evi Portable är endast för Microsoft Windows 10 och Windows 11. Det är det inte
stöds på Windows 7/8, macOS, Linux eller mobila operativsystem.

----------------------------------------------------------------------------------
  Första starten — från nedladdning till att köra Evi
----------------------------------------------------------------------------------

1) Installationsplats
   Kopiera eller extrahera hela Evi-mappen till en plats du kontrollerar — till exempel
   ditt skrivbord, dokument eller ett USB-minne. Behåll mappstrukturen som
   levereras (ta inte bort undermappar du inte skapat själv).

2) Språkmodell (obligatoriskt)
   Evi behöver en huvud-AI-modellfil (tillägget .gguf) i mappen:
   modeller\llm\
   Se modeller\llm\README.txt för storleksrekommendationer. När filen är där,
   starta Evi; den känner av modellen automatiskt när det är möjligt.

3) Första start — aktivering
   När du startar Evi första gången visas ett aktiveringsfönster.
   • Din dator visar ett maskin-ID (unik för denna hårdvara).
   • Kopiera maskin-ID (knapp: "Kopiera maskin-ID") och skicka det via e-post till:
     Brielbeck@hotmail.de
   • Du kommer att få en seriell nyckel som bara fungerar på samma dator
     (nyckeln är bunden till din hårdvara).
   • Klistra in nyckeln i aktiveringsfönstret och välj Aktivera.

   Om du ändrar större hårdvara eller flyttar disken på ett sätt som ändrar ID,
   du kan behöva en ny nyckel — kontakta samma adress.

4) Efter aktivering
   Huvudfönstret öppnas. Välj språk, mikrofon och röst till vänster
   inställningspanelen. Säg "öppna cheat sheet" när som helst för kommandoexempel
   (se cheatsheets\en.txt och systerfiler för andra språk).

5) Valfritt: öppna den här handboken från Windows
   Gå till mappen Evi i File Explorer, sedan Manual\README.txt och öppna den
   med Anteckningar eller någon textvisare.

----------------------------------------------------------------------------------
  Gränssnittsspråk (GUI)
----------------------------------------------------------------------------------

Användargränssnittet följer det språk du väljer under Språk högst upp
i den vänstra inställningspanelen (första blocket i sidofältet). När du har valt a
språk, menyer, knappar, etiketter och det mesta på skärmen växlar till det
språk där översättningar finns. Du kan ändra det när som helst; endast den
formuleringsändringar, inte layouten.

Tips: Kommandot cheatsheets i cheatsheets\-mappen listas per
språkkod (en.txt, de.txt, …). För detaljer se cheatsheets\README.txt.
Denna Manual\-mapp är den längre produktöversikten; fuskblad är de
snabb "vad man ska säga" lista.

----------------------------------------------------------------------------------
  Grafikkort (GPU) — snabbguide
----------------------------------------------------------------------------------

Ett starkt mellanval är en NVIDIA GeForce RTX 4070 Ti med 12 GB video
minne: bra balans mellan hastighet, sammanhangsstorlek och utrymme för större modeller.

Kort från ungefär RTX 3060 till RTX 5090 kan fungera bra; den bästa passformen beror på
på RAM, CPU, kylning och vilken modellfil du installerar. Använd GPU-förinställningen i
Evis sidofält för att matcha din hårdvara.

Att endast köra på CPU (förinställningarna "CPU ... GB RAM") är en reserv i nödsituationer:
Evi förblir användbar utan ett lämpligt grafikkort, men svaren är mycket långsammare.
Föredrar en riktig GPU när du kan.

----------------------------------------------------------------------------------
  Fullt bärbar — när du behöver internet
----------------------------------------------------------------------------------

Evi är byggd för att vara portabel: kopiera hela mappen till en annan enhet, USB-minne,
eller PC, starta den där. Chattar, minnen, inställningar, säkerhetsdata och din
aktiveringsfilen stannar normalt i den mappen (aktiveringen är kopplad till
PC, inte mappsökvägen).

Internet är främst till för saker du väljer att ladda ner (modellfiler, valfritt
röster eller extrafunktioner, uppdateringar) och för valfria funktioner som webbsökning, e-post,
streaming eller väder när du tillåter nätverksåtkomst.

Kärnchatt, minne, anteckningar, timers, filverktyg i din tillåtna mapp, lokalt
taligenkänning, lokal röstutgång och sekretesslåset körs på din
maskin utan att skicka dina konversationer till en molntjänst. Valfritt online
funktioner körs bara när nätverksåtkomst är på och du använder dem.

----------------------------------------------------------------------------------
  Säkerhet: PIN-kod och röstupplåsning (antikopiering)
----------------------------------------------------------------------------------

Evi kan använda en säkerhets-PIN och valfri röstregistrering på din enhet.

När röstupplåsning används kan varje försök be om en kort uppsättning slumpmässiga ord
som ändras varje gång - inte en fast fras för alltid. Det blockerar det enkla
knep att spela upp en enda gammal inspelning av din röst. Din PIN-kod förblir en
separat försvarslinje.

Detta är utformat för att stoppa tillfälliga övergrepp; ingen konsumentprodukt kan lova
perfektion mot varje attack (till exempel någon som har både din PIN-kod och
sofistikerad röstmimik). Håll din PIN-kod privat och slutför installationen som
appen guidar dig.

----------------------------------------------------------------------------------
  Felsökning (kort checklista)
----------------------------------------------------------------------------------

• Inga AI-svar/modellfel
  → Minst en lämplig .gguf i modeller\llm\ ? Se modeller\llm\README.txt.
  → Prova en mindre modell eller en CPU-förinställning i sidofältet om GPU-sökvägen misslyckas.

• Ingen mikrofon
  → Windows ljudinställningar: testa mikrofonen. I Evi väljer du enheten under
    Mikrofon och spara.

• Ingen röstutgång
  → Kontrollera att röstfiler för ditt språk finns i mappen piper\ och
    välj en röst i sidofältet.

• Webb eller YouTube misslyckas
  → Stäng av "Blockera all trafik" i sidofältet om du vill ha onlinefunktioner.
  → För YouTube-uppspelning krävs vanligtvis VLC Portable och nätverksåtkomst.

• Efter att ha redigerat cheat sheets
  → Starta om Evi så att alla texthjälpare tar upp ändringar på ett tillförlitligt sätt.

----------------------------------------------------------------------------------
  Felsökning (utökad referens)
----------------------------------------------------------------------------------

Snabbkontroller (alltid först)
  • Windows 10 eller 11 64-bitars, uppdaterat, startat om efter stora förändringar?
  • Evi körs från en helt extraherad mapp — inte inifrån ett arkiv?
  • Undvik molnsynkroniserade mappar (OneDrive, etc.) för livedatamappen medan
    Evi körs — använd en lokal sökväg som C:\EviPortable eller D:\Tools\Evi när
    möjligt.
  • Tillräckligt ledigt diskutrymme för modellen, chattar och uppdateringar?
  • Efter att ha bytt modell, röster eller cheat sheets: avsluta Evi helt och börja
    igen.

1) Operativsystem
  • Evi är endast för Windows 10 och 11; andra OS-versioner stöds inte.
  • Om appen inte startar alls, extrahera paketet helt, kontrollera antivirus
    loggar för blockerade körbara filer, och prova en kortare installationsväg utan sällsynta
    Unicode-tecken.

2) Mappsökväg, antivirus, portabilitet
  • Lägg till ett undantag för din Evi-rotmapp i säkerhetsprogramvaran om skanningar görs
    mycket långsam start eller lås filer under nedladdningar.
  • USB-minnen: föredrar USB 3 + NTFS; mycket långsam media gör stora modeller smärtsamma.

3) Språkmodell (.gguf)
  • symptom: inga svar, modellfel, omedelbart misslyckande att ladda.
  • fixar: verifiera att models\llm\ innehåller en komplett .gguf (inte 0 byte); ladda ner igen
om det behövs; matcha modellstorlek till VRAM med models\llm\README.txt; om du är osäker,
    behåll en enda testad q4_k_m-fil i mappen.
  • flera .gguf-filer: Evi kan välja den största som passar ditt VRAM — om du
    misstänker en konflikt, testa med endast en fil.

4) GPU, CUDA, drivrutiner, slut på minne
  • Uppdatera NVIDIA-drivrutinen; på bärbara datorer, tvinga fram den diskreta GPU/prestanda
    läge för Evi där Windows tillåter.
  • Om du ser OOM eller GPU kraschar, använd en mindre kontrollpunkt, stäng andra GPU-appar,
    lägre temperatur, eller byt till en CPU-förinställning (långsammare men stadigare).

5) Endast CPU-läge
  • Förväntas vara långsam; ledigt tillräckligt med system-RAM; stänga tunga bakgrundsuppgifter;
    använd kraftplan "Hög prestanda" under långa pass.

6) Aktivering
  • Klistra in nycklar noggrant (inga extra mellanslag); nycklar är bundna till ett maskin-ID.
  • Efter större hårdvaruförändringar kan du behöva en ersättningsnyckel — använd supporten
    adress med dina uppgifter.

7) Mikrofon
  • Windows Sekretess → Mikrofon → tillåt skrivbordsappar.
  • Ställ in rätt standardinspelningsenhet; i Evi väljer du samma enhet och sparar.
  • Bluetooth-headset kan lägga till latens — testa med en USB-mikrofon om du är osäker.
  • En annan app kan ha exklusivt läge — stäng mötesprogramvara tillfälligt.

8) Taligenkänning (lokal)
  • Om igenkänningen aldrig slutförs, se till att modellfilerna är under models\whisper are
    intakt och tillåt nätverk vid förstagångsmodellhämtningar om din konstruktion behöver det.

9) Röstutgång (Piper / TTS)
  • Bekräfta att piper\ innehåller ett röstpaket för ditt UI-språk; plocka in en röst
    sidofältet; kontrollera Windows volymmixer — Evi kan stängas av per app.

10) Nätverk och "Blockera all trafik"
  • Stäng av spärren för webb, e-posthjälp, väder eller nedladdningar.
  • Företagsfullmakter eller VPN kan kräva IT-hjälp för godkännandelistor.

11) YouTube och media
  • Behåll den medföljande VLC Portable-layouten; aktivera nätverksåtkomst; läsa
    Portable\VLCPortable vägledning om sökvägen flyttades.

12) UI-språk och fuskblad
  • Fuskblad finns per språkfil under cheatsheets\ — se cheatsheets\README.txt.
  • Spara redigeringar som UTF-8; starta om Evi efter redigeringar.

13) Säkerhet (PIN / röstupplåsning)
  • Använd en lugn miljö; kontrollera mikrofonförstärkningen igen; dela aldrig din PIN-kod.
  • Slumpmässiga ordmeddelanden är avsiktliga – gamla röstinspelningar ska inte låsas upp.

14) Prestanda, fryser, kraschar
  • Minska modellens storlek, förbättra kylningen, läs eventuella crash.log i trädet om din
    build skapar en och rulla tillbaka den senaste ändringen du gjorde före misslyckanden.

15) När du kontaktar support
  • Inkludera maskin-ID, Windows-version, GPU-modell + VRAM + drivrutin, som .gguf
    du använder och den exakta feltexten (inte hemliga nycklar).

Fullständig felsökningsreferens (detta språk): Manual\FEHLERSUCHE_SV.txt

----------------------------------------------------------------------------------
  Support — seriella nycklar och maskin-ID
----------------------------------------------------------------------------------

E-post: Brielbeck@hotmail.de
Inkludera alltid ditt maskin-ID från aktiveringsskärmen när du begär en
seriell nyckel eller en ersättningsnyckel efter maskinvaruändringar.

=================================================================================