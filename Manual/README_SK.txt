=================================================================================
  Evi Portable — Používateľská príručka (prehľad)
  Dokument: angličtina • Platí pre zostavu, ktorú ste dostali s týmto priečinkom
=================================================================================

Vložte sem aj svoje vlastné dlhšie návody alebo preklady (napr. EN_User_Manual.pdf,
DE_Handbuch.txt). Tento súbor je pre Evi voliteľný na spustenie; je na vás, aby ste si to prečítali
alebo vytlačiť.

Lokalizované kópie: README_<LANG>.txt a FEHLERSUCHE_<LANG>.txt v tomto priečinku
(rovnaké kódy jazykov ako používateľské rozhranie webovej stránky). Prehľad v angličtine: tento README.txt;
Riešenie problémov v angličtine: FEHLERSUCHE_EN.txt. Nemecké riešenie problémov je tiež
udržiavané ručne ako FEHLERSUCHE_DE.txt.

Index priečinka (názvy súborov, generátor): README.md

--------------------------------------------------------------------------------
  Operačný systém
--------------------------------------------------------------------------------

Evi Portable je len pre Microsoft Windows 10 a Windows 11. nie je
podporované v operačných systémoch Windows 7/8, macOS, Linux alebo mobilných zariadeniach.

--------------------------------------------------------------------------------
  Prvý štart — od stiahnutia po spustenie Evi
--------------------------------------------------------------------------------

1) Miesto inštalácie
   Skopírujte alebo extrahujte celý priečinok Evi na miesto, ktoré ovládate – napríklad
   vašu pracovnú plochu, dokumenty alebo USB kľúč. Ponechajte štruktúru priečinkov ako
   doručené (neodstraňujte podpriečinky, ktoré ste sami nevytvorili).

2) Jazykový model (povinný)
   Evi potrebuje jeden hlavný súbor modelu AI (prípona .gguf) v priečinku:
   modely\llm\
   Odporúčania týkajúce sa veľkosti nájdete v súbore models\llm\README.txt. Keď je súbor tam,
   začať Evi; ak je to možné, automaticky rozpozná model.

3) Prvé spustenie – aktivácia
   Pri prvom spustení Evi sa zobrazí aktivačné okno.
   • Váš počítač zobrazuje ID stroja (jedinečné pre tento hardvér).
   • Skopírujte ID stroja (tlačidlo: "Kopírovať ID stroja") a pošlite ho e-mailom na adresu:
     Brielbeck@hotmail.de
   • Dostanete sériový kľúč, ktorý funguje len na tom istom počítači
     (kľúč je viazaný na váš hardvér).
   • Vložte kľúč do aktivačného okna a zvoľte Aktivovať.

   Ak zmeníte hlavný hardvér alebo presuniete disk spôsobom, ktorý zmení ID,
   možno budete potrebovať nový kľúč – kontaktujte rovnakú adresu.

4) Po aktivácii
   Otvorí sa hlavné okno. Vľavo vyberte jazyk, mikrofón a hlas
   panel nastavení. Pre príklady príkazov kedykoľvek vyslovte „otvorenie cheatu“.
   (pozri cheatsheets\en.txt a sesterské súbory pre iné jazyky).

5) Voliteľné: otvorte túto príručku v systéme Windows
   V Prieskumníkovi prejdite do priečinka Evi, potom Manual\README.txt a otvorte ho
   pomocou programu Poznámkový blok alebo akéhokoľvek textového prehliadača.

--------------------------------------------------------------------------------
  Jazyk rozhrania (GUI)
--------------------------------------------------------------------------------

Používateľské rozhranie sa riadi jazykom, ktorý si vyberiete v časti Jazyk v hornej časti
na ľavom paneli nastavení (prvý blok na bočnom paneli). Po výbere a
jazyk, ponuky, tlačidlá, štítky a väčšina textu na obrazovke sa prepnú na to
jazyk všade tam, kde existujú preklady. Môžete ho kedykoľvek zmeniť; len ten
sa mení znenie, nie rozloženie.

Tip: Príkazové hárky v priečinku cheatsheets\ sú uvedené podľa
kód jazyka (en.txt, de.txt, ...). Podrobnosti nájdete v cheatsheets\README.txt.
Táto príručka\ priečinok je dlhší prehľad produktov; cheat sheets sú
rýchly zoznam „čo povedať“.

--------------------------------------------------------------------------------
  Grafická karta (GPU) — rýchly sprievodca
--------------------------------------------------------------------------------

Silnou strednou voľbou je NVIDIA GeForce RTX 4070 Ti s 12 GB videa
pamäť: dobrá rovnováha medzi rýchlosťou, veľkosťou kontextu a priestorom pre väčšie modely.

Karty od približne RTX 3060 do RTX 5090 môžu fungovať dobre; najlepšie prispôsobenie závisí
na RAM, CPU, chladenie a súbor modelu, ktorý nainštalujete. Použite predvoľbu GPU v
Bočný panel Evi, ktorý zodpovedá vášmu hardvéru.

Spustenie iba na CPU (predvoľby „CPU … GB RAM“) je núdzová núdzová situácia:
Evi zostáva použiteľná aj bez vhodnej grafickej karty, no odpovede sú oveľa pomalšie.
Kedykoľvek môžete, uprednostňujte skutočný GPU.

--------------------------------------------------------------------------------
  Plne prenosné — keď potrebujete internet
--------------------------------------------------------------------------------

Evi je skonštruovaný tak, aby bol prenosný: skopírujte celý priečinok na iný disk, USB kľúč,
alebo PC, potom ho tam spustite. Chaty, spomienky, nastavenia, bezpečnostné údaje a vaše
aktivačný súbor zvyčajne zostáva v tomto priečinku (aktivácia je spojená s
PC, nie cesta k priečinku).

Internet slúži hlavne na veci, ktoré sa rozhodnete stiahnuť (modelové súbory, voliteľné
hlasy alebo doplnky, aktualizácie) a pre voliteľné funkcie, ako je vyhľadávanie na webe, pošta,
streamovanie alebo počasie, keď povolíte prístup k sieti.

Základný chat, pamäť, poznámky, časovače, nástroje súborov vo vašom povolenom priečinku, lokálne
rozpoznávanie reči, lokálny hlasový výstup a zámok ochrany osobných údajov fungujú na vašom počítači
počítač bez odosielania vašich konverzácií do cloudovej služby. Voliteľné online
funkcie sa spúšťajú iba vtedy, keď je zapnutý prístup k sieti a vy ich používate.

--------------------------------------------------------------------------------
  Zabezpečenie: PIN a hlasové odomknutie (ochrana proti kopírovaniu)
--------------------------------------------------------------------------------

Evi môže na vašom zariadení použiť bezpečnostný PIN a voliteľnú hlasovú registráciu.

Keď sa používa hlasové odomknutie, každý pokus môže požiadať o krátku sadu náhodných slov
ktorá sa zakaždým mení – nie jedna ustálená fráza navždy. To blokuje ľahké
trik s prehratím jednej starej nahrávky vášho hlasu. Váš PIN zostáva a
samostatná obranná línia.

Toto je určené na zastavenie náhodného zneužívania; žiadny spotrebný produkt nemôže sľúbiť
dokonalosť proti každému útoku (napríklad niekomu, kto má váš PIN aj
sofistikovaná hlasová mimika). Udržujte svoj PIN súkromný a dokončite nastavenie ako
aplikácia vás prevedie.

--------------------------------------------------------------------------------
  Riešenie problémov (krátky kontrolný zoznam)
--------------------------------------------------------------------------------

• Žiadne odpovede AI / chyba modelu
  → Aspoň jeden vhodný .gguf v modeloch\llm\ ? Pozrite si models\llm\README.txt.
  → Ak cesta GPU zlyhá, skúste menší model alebo predvoľbu CPU na bočnom paneli.

• Žiadny mikrofón
  → Nastavenia zvuku Windows: otestujte mikrofón. V Evi vyberte zariadenie pod
    Mikrofón a Uložiť.

• Žiadny hlasový výstup
  → Skontrolujte, či v priečinku Piper\ a existujú hlasové súbory pre váš jazyk
    vyberte hlas na bočnom paneli.

• Web alebo YouTube zlyhávajú
  → Ak chcete mať online funkcie, vypnite „Blokovať všetku premávku“ na bočnom paneli.
  → Na prehrávanie YouTube sa zvyčajne vyžaduje VLC Portable a sieťový prístup.

• Po úprave cheatov
  → Reštartujte Evi, aby všetci textoví pomocníci spoľahlivo zachytili zmeny.

--------------------------------------------------------------------------------
  Riešenie problémov (rozšírená referencia)
--------------------------------------------------------------------------------

Rýchle kontroly (vždy prvé)
  • Windows 10 alebo 11 64-bit, aktualizovaný, reštartovaný po veľkých zmenách?
  • Evi beží z úplne extrahovaného priečinka – nie z archívu?
  • Vyhnite sa cloudovým synchronizovaným priečinkom (OneDrive atď.) pre priečinok so živými údajmi
    Evi beží — použite miestnu cestu, ako napríklad C:\EviPortable alebo D:\Tools\Evi, keď
    možné.
  • Dostatok voľného miesta na disku pre model, rozhovory a aktualizácie?
  • Po zmene modelov, hlasov alebo cheatov: úplne ukončite Evi a začnite
    znova.

1) Operačný systém
  • Evi je len pre Windows 10 a 11; iné verzie OS nie sú podporované.
  • Ak sa aplikácia vôbec nespustí, úplne rozbaľte balík a skontrolujte antivírus
    protokoly pre blokované spustiteľné súbory a skúste kratšiu cestu inštalácie bez zriedkavých
    Iba znaky Unicode.

2) Cesta k priečinku, antivírus, prenosnosť
  • Pridajte vylúčenie pre váš koreňový priečinok Evi v bezpečnostnom softvéri, ak sa vykoná skenovanie
    veľmi pomalé spúšťanie alebo uzamknutie súborov počas sťahovania.
  • USB kľúče: uprednostňujte USB 3 + NTFS; veľmi pomalé médiá spôsobujú bolesť veľkých modelov.

3) Jazykový model (.gguf)
  • príznaky: žiadne odpovede, chyby modelu, okamžité zlyhanie načítania.
  • opravy: skontrolujte, či modely\llm\ obsahujú úplný súbor .gguf (nie 0 bajtov); znovu stiahnuť
ak je to potrebné; prispôsobiť veľkosť modelu VRAM pomocou models\llm\README.txt; ak si nie si istý,
    ponechajte jeden testovaný súbor q4_k_m v priečinku.
  • viacero súborov .gguf: Evi si môže vybrať ten najväčší, ktorý vyhovuje vašej VRAM – ak vy
    podozrenie na konflikt, testujte iba s jedným súborom.

4) GPU, CUDA, ovládače, nedostatok pamäte
  • Aktualizujte ovládač NVIDIA; na prenosných počítačoch vynútiť samostatný GPU / výkon
    režim pre Evi, kde to Windows umožňuje.
  • Ak uvidíte zlyhania OOM alebo GPU, použite menší kontrolný bod, zatvorte ostatné aplikácie GPU,
    nižšiu teplotu, alebo prepnite na predvoľbu CPU (pomalšie, ale stabilnejšie).

5) Režim iba pre CPU
  • Očakáva sa, že bude pomalý; uvoľnite dostatok systémovej pamäte RAM; zatvorte náročné úlohy na pozadí;
    počas dlhých sedení používajte plán napájania „Vysoký výkon“.

6) Aktivácia
  • Prilepte kľúče opatrne (bez medzier navyše); kľúče sú spojené s jedným ID stroja.
  • Po veľkých zmenách hardvéru možno budete potrebovať náhradný kľúč – použite podporu
    adresu s vašimi údajmi.

7) Mikrofón
  • Súkromie systému Windows → Mikrofón → povoliť aplikácie pre stolné počítače.
  • Nastavte správne predvolené nahrávacie zariadenie; v Evi vyberte rovnaké zariadenie a Uložiť.
  • Slúchadlá Bluetooth môžu pridať latenciu – ak si nie ste istí, vyskúšajte pomocou mikrofónu USB.
  • Iná aplikácia môže mať exkluzívny režim – dočasne zatvorte softvér na stretnutia.

8) Rozpoznávanie reči (miestne)
  • Ak sa rozpoznávanie nikdy neskončí, skontrolujte, či sú súbory modelov v časti models\whisper
    neporušené a povoľte sieť pri prvom načítaní modelu, ak to vaša zostava potrebuje.

9) Hlasový výstup (Piper / TTS)
  • Potvrďte, že piper\ obsahuje hlasový balík pre váš jazyk používateľského rozhrania; vybrať hlas
    bočný panel; skontrolujte Windows Volume Mixer – Evi môže byť stlmená pre každú aplikáciu.

10) Sieť a „Blokovať všetku premávku“
  • Vypnite blokovanie pre web, poštových pomocníkov, počasie alebo sťahovanie.
  • Firemné servery proxy alebo siete VPN môžu vyžadovať pomoc IT pre zoznamy povolených.

11) YouTube a médiá
  • Ponechajte si pribalené rozloženie VLC Portable; povoliť prístup k sieti; čítať
    Portable\VLCPortable vedenie, ak bola cesta presunutá.

12) Jazyk používateľského rozhrania a cheaty
  • Cheatsheets sú pre jazykový súbor pod cheatsheets\ — pozri cheatsheets\README.txt.
  • Uložiť úpravy ako UTF-8; reštartujte Evi po úpravách.

13) Zabezpečenie (PIN / odomknutie hlasom)
  • Používajte tiché prostredie; znova skontrolujte zisk mikrofónu; nikdy nezdieľajte svoj PIN.
  • Náhodné slová sú zámerné – staré hlasové nahrávky by sa nemali odomknúť.

14) Výkon, zamŕza, padá
  • Zmenšite veľkosť modelu, vylepšite chladenie, prečítajte si akýkoľvek crash.log v strome, ak máte
    build vytvorí jeden a vráti späť poslednú zmenu, ktorú ste vykonali pred zlyhaniami.

15) Pri kontaktovaní podpory
  • Zahrňte ID stroja, verziu systému Windows, model GPU + VRAM + ovládač, ktorý .gguf
    a presný text chyby (nie tajné kľúče).

Úplný odkaz na riešenie problémov (tento jazyk): Manual\FEHLERSUCHE_SK.txt

--------------------------------------------------------------------------------
  Podpora — sériové kľúče a ID stroja
--------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Vždy uveďte svoje ID stroja z aktivačnej obrazovky, keď požadujete a
sériový kľúč alebo náhradný kľúč po zmenách hardvéru.

=================================================================================