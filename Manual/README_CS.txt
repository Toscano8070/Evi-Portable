=================================================================================
  Evi Portable — Uživatelská příručka (přehled)
  Dokument: Angličtina • Platí pro sestavení, které jste obdrželi s touto složkou
=================================================================================

Vložte sem i své vlastní delší návody nebo překlady (např. EN_User_Manual.pdf,
DE_Handbuch.txt). Tento soubor je pro Evi volitelný ke spuštění; je na vás, abyste si to přečetli
nebo tisknout.

Lokalizované kopie: README_<LANG>.txt a FEHLERSUCHE_<LANG>.txt v této složce
(stejné kódy jazyků jako uživatelské rozhraní webu). Přehled v angličtině: tento README.txt;
Řešení problémů v angličtině: FEHLERSUCHE_EN.txt. Německé řešení problémů je také
udržovaný ručně jako FEHLERSUCHE_DE.txt.

Index složky (názvy souborů, generátor): README.md

--------------------------------------------------------------------------------
  Operační systém
--------------------------------------------------------------------------------

Evi Portable je pouze pro Microsoft Windows 10 a Windows 11. není
podporováno v operačních systémech Windows 7/8, macOS, Linux nebo mobilních.

--------------------------------------------------------------------------------
  První spuštění — od stažení po spuštění Evi
--------------------------------------------------------------------------------

1) Místo instalace
   Zkopírujte nebo extrahujte celou složku Evi na místo, které ovládáte – například
   vaši plochu, dokumenty nebo USB flash disk. Udržujte strukturu složek jako
   doručeno (neodstraňujte podsložky, které jste sami nevytvořili).

2) Jazykový model (vyžadováno)
   Evi potřebuje jeden hlavní soubor modelu AI (přípona .gguf) ve složce:
   modely\llm\
   Doporučená velikost viz models\llm\README.txt. Poté, co je soubor tam,
   spustit Evi; pokud je to možné, automaticky detekuje model.

3) První spuštění — aktivace
   Při prvním spuštění Evi se zobrazí aktivační okno.
   • Váš počítač zobrazuje ID stroje (jedinečné pro tento hardware).
   • Zkopírujte ID stroje (tlačítko: "Kopírovat ID stroje") a odešlete jej e-mailem na adresu:
     Brielbeck@hotmail.de
   • Obdržíte sériový klíč, který funguje pouze na stejném počítači
     (klíč je vázán na váš hardware).
   • Vložte klíč do aktivačního okna a zvolte Aktivovat.

   Pokud změníte hlavní hardware nebo přesunete disk způsobem, který změní ID,
   možná budete potřebovat nový klíč – kontaktujte stejnou adresu.

4) Po aktivaci
   Otevře se hlavní okno. Vlevo vyberte jazyk, mikrofon a hlas
   panel nastavení. Pro příklady příkazů kdykoli řekněte „otevřít cheat sheet“.
   (viz cheatsheets\en.txt a sesterské soubory pro jiné jazyky).

5) Volitelné: otevřete tuto příručku ze systému Windows
   V Průzkumníku souborů přejděte do složky Evi, poté Manual\README.txt a otevřete ji
   s Poznámkovým blokem nebo jakýmkoli textovým prohlížečem.

--------------------------------------------------------------------------------
  Jazyk rozhraní (GUI)
--------------------------------------------------------------------------------

Uživatelské rozhraní se řídí jazykem, který vyberete v části Jazyk nahoře
levého panelu nastavení (první blok na postranním panelu). Poté, co vyberete a
jazyk, nabídky, tlačítka, štítky a většina textu na obrazovce se přepnou na to
jazyk všude tam, kde existují překlady. Můžete jej kdykoli změnit; pouze
se mění znění, nikoli rozložení.

Tip: Cheat sheets příkazů ve složce cheatsheets\ jsou uvedeny podle
kód jazyka (en.txt, de.txt, …). Podrobnosti najdete v cheatsheets\README.txt.
Tato složka Manual\ je delším přehledem produktů; cheat listy jsou
rychlý seznam „co říct“.

--------------------------------------------------------------------------------
  Grafická karta (GPU) — rychlý průvodce
--------------------------------------------------------------------------------

Silnou střední volbou je NVIDIA GeForce RTX 4070 Ti s 12 GB videem
paměť: dobrá rovnováha mezi rychlostí, velikostí kontextu a prostorem pro větší modely.

Karty od RTX 3060 do RTX 5090 mohou fungovat dobře; závisí na tom nejlepší přizpůsobení
na RAM, CPU, chlazení a soubor modelu, který nainstalujete. Použijte předvolbu GPU v
Postranní panel Evi, aby odpovídal vašemu hardwaru.

Spuštění pouze na CPU (přednastavení „CPU … GB RAM“) je nouzové řešení:
Evi zůstává použitelná i bez vhodné grafické karty, ale odpovědi jsou mnohem pomalejší.
Kdykoli můžete, dejte přednost skutečnému GPU.

--------------------------------------------------------------------------------
  Plně přenosný — když potřebujete internet
--------------------------------------------------------------------------------

Evi je navržen tak, aby byl přenosný: zkopírujte celou složku na jiný disk, USB flash disk,
nebo PC, pak to tam spusťte. Chaty, vzpomínky, nastavení, bezpečnostní data a vaše
aktivační soubor normálně zůstává v této složce (aktivace je vázána na
PC, nikoli cestu ke složce).

Internet je hlavně pro věci, které se rozhodnete stáhnout (modelové soubory, volitelné
hlasy nebo doplňky, aktualizace) a pro volitelné funkce, jako je vyhledávání na webu, pošta,
streamování nebo počasí, když povolíte přístup k síti.

Základní chat, paměť, poznámky, časovače, souborové nástroje ve vaší povolené složce, místní
na vašem počítači běží rozpoznávání řeči, místní hlasový výstup a zámek soukromí
zařízení bez odesílání vašich konverzací do cloudové služby. Volitelné online
funkce se spouštějí, pouze když je zapnutý přístup k síti a používáte je.

--------------------------------------------------------------------------------
  Zabezpečení: PIN a hlasové odemykání (ochrana proti kopírování)
--------------------------------------------------------------------------------

Evi může na vašem zařízení použít bezpečnostní PIN a volitelnou hlasovou registraci.

Při použití hlasového odemykání může každý pokus požádat o krátkou sadu náhodných slov
která se mění pokaždé – žádná ustálená fráze navždy. To blokuje snadné
trik přehrání jediné staré nahrávky vašeho hlasu. Váš PIN zůstává a
samostatná obranná linie.

To je navrženo tak, aby zastavilo náhodné zneužívání; žádný spotřební produkt nemůže slíbit
dokonalost proti každému útoku (například někomu, kdo má jak váš PIN, tak
sofistikovaná hlasová mimika). Udržujte svůj PIN soukromý a dokončete nastavení jako
aplikace vás provede.

--------------------------------------------------------------------------------
  Odstraňování problémů (krátký kontrolní seznam)
--------------------------------------------------------------------------------

• Žádné odpovědi AI / chyba modelu
  → Alespoň jeden vhodný .gguf v models\llm\ ? Viz models\llm\README.txt.
  → Pokud cesta GPU selže, vyzkoušejte menší model nebo předvolbu CPU na postranním panelu.

• Žádný mikrofon
  → Nastavení zvuku Windows: otestujte mikrofon. V Evi vyberte zařízení pod
    Mikrofon a Uložit.

• Žádný hlasový výstup
  → Zkontrolujte, zda existují hlasové soubory pro váš jazyk ve složce piper\ a
    vyberte hlas na postranním panelu.

• Web nebo YouTube selže
  → Pokud chcete online funkce, vypněte na postranním panelu „Blokovat veškerý provoz“.
  → Pro přehrávání YouTube je obvykle vyžadován VLC Portable a síťový přístup.

• Po úpravě cheatů
  → Restartujte Evi, aby všichni textoví pomocníci spolehlivě zachytili změny.

--------------------------------------------------------------------------------
  Odstraňování problémů (rozšířená reference)
--------------------------------------------------------------------------------

Rychlé kontroly (vždy první)
  • Windows 10 nebo 11 64bitové, aktualizované, restartované po velkých změnách?
  • Evi běžící z plně extrahované složky – nikoli z archivu?
  • Vyhněte se složkám synchronizovaným s cloudem (OneDrive atd.) pro složku živých dat
    Evi běží – použijte místní cestu, jako je C:\EviPortable nebo D:\Tools\Evi, když
    možné.
  • Dostatek volného místa na disku pro model, chaty a aktualizace?
  • Po změně modelů, hlasů nebo cheatů: úplně ukončete Evi a začněte
    znovu.

1) Operační systém
  • Evi je pouze pro Windows 10 a 11; ostatní verze OS nejsou podporovány.
  • Pokud se aplikace vůbec nespustí, plně rozbalte balíček, zkontrolujte antivirus
    protokoly pro blokované spustitelné soubory a zkuste kratší instalační cestu bez rare
    Znaky pouze Unicode.

2) Cesta ke složce, antivirus, přenositelnost
  • Přidejte výjimku pro kořenovou složku Evi v bezpečnostním softwaru, pokud probíhají kontroly
    velmi pomalé spouštění nebo zamykání souborů během stahování.
  • USB klíčenky: preferujte USB 3 + NTFS; velmi pomalá média způsobují bolest u velkých modelů.

3) Jazykový model (.gguf)
  • příznaky: žádné odpovědi, chyby modelu, okamžité selhání načítání.
  • opravy: ověřte, že modely\llm\ obsahují úplný soubor .gguf (nikoli 0 bajtů); znovu stáhnout
v případě potřeby; přizpůsobit velikost modelu paměti VRAM pomocí models\llm\README.txt; pokud si nejste jisti,
    ponechat jeden testovaný soubor q4_k_m ve složce.
  • více souborů .gguf: Evi může vybrat ten největší, který vyhovuje vaší paměti VRAM – pokud vy
    podezření na konflikt, testujte pouze s jedním souborem.

4) GPU, CUDA, ovladače, nedostatek paměti
  • Aktualizujte ovladač NVIDIA; u notebooků vynutit diskrétní GPU / výkon
    režim pro Evi, kde to Windows umožňuje.
  • Pokud vidíte selhání OOM nebo GPU, použijte menší kontrolní bod, zavřete ostatní aplikace GPU,
    nižší teplotu, nebo přepněte na předvolbu CPU (pomalejší, ale stabilnější).

5) Režim pouze pro CPU
  • Očekává se, že bude pomalý; uvolnit dostatek systémové paměti RAM; zavřít náročné úkoly na pozadí;
    používejte plán napájení „Vysoký výkon“ během dlouhých sezení.

6) Aktivace
  • Vkládejte klíče opatrně (bez mezer navíc); klíče jsou svázány s jedním ID stroje.
  • Po větších hardwarových změnách budete možná potřebovat náhradní klíč — využijte podporu
    adresu s vašimi údaji.

7) Mikrofon
  • Soukromí systému Windows → Mikrofon → povolit aplikace pro stolní počítače.
  • Nastavte správné výchozí záznamové zařízení; v Evi vyberte stejné zařízení a uložte.
  • Náhlavní soupravy Bluetooth mohou přidat latenci — pokud si nejste jisti, vyzkoušejte pomocí mikrofonu USB.
  • Jiná aplikace může mít exkluzivní režim – dočasně zavřete software pro schůzky.

8) Rozpoznávání řeči (místní)
  • Pokud rozpoznávání nikdy neskončí, zajistěte, aby byly soubory modelu v části models\whisper
    neporušené a povolit síť při prvním načtení modelu, pokud to vaše sestava potřebuje.

9) Hlasový výstup (Piper / TTS)
  • Potvrďte, že piper\ obsahuje hlasový balíček pro váš jazyk uživatelského rozhraní; vybrat hlas
    postranní panel; zkontrolujte směšovač hlasitosti systému Windows – Evi může být v jednotlivých aplikacích ztlumena.

10) Síť a "Blokovat veškerý provoz"
  • Vypněte blokování webu, pomocníků pošty, počasí nebo stahování.
  • Firemní proxy nebo VPN mohou vyžadovat IT pomoc pro seznamy povolených.

11) YouTube a média
  • Ponechte si přiložené rozložení VLC Portable; povolit přístup k síti; číst
    Portable\VLCPortable vodítko, pokud byla cesta přesunuta.

12) Jazyk uživatelského rozhraní a cheaty
  • Cheatsheety jsou pro jazykový soubor pod cheatsheets\ — viz cheatsheets\README.txt.
  • Uložit úpravy jako UTF-8; restartujte Evi po úpravách.

13) Zabezpečení (PIN / odemknutí hlasem)
  • Používejte tiché prostředí; znovu zkontrolujte zisk mikrofonu; nikdy nesdělujte svůj PIN.
  • Náhodné výzvy jsou záměrné — staré hlasové nahrávky by se neměly odemykat.

14) Výkon, zamrzání, pády
  • Zmenšete velikost modelu, vylepšete chlazení, přečtěte si jakýkoli crash.log ve stromu, pokud máte
    build vytvoří jeden a vrátí zpět poslední změnu, kterou jste provedli před selháním.

15) Při kontaktování podpory
  • Zahrnout ID stroje, verzi Windows, model GPU + VRAM + ovladač, který .gguf
    a přesný text chyby (nikoli tajné klíče).

Úplný odkaz na odstraňování problémů (tento jazyk): Manual\FEHLERSUCHE_CS.txt

--------------------------------------------------------------------------------
  Podpora — sériové klíče a ID stroje
--------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Vždy uveďte své ID stroje z aktivační obrazovky, když požadujete a
sériový klíč nebo náhradní klíč po změnách hardwaru.

=================================================================================