================================================================================
  Evi Portable — Felhasználói kézikönyv (áttekintés)
  Dokumentum: angol • Az ezzel a mappával kapott buildre vonatkozik
================================================================================

Tegye ide saját hosszabb útmutatóit vagy fordításait is (pl. EN_User_Manual.pdf,
DE_Handbuch.txt). Ez a fájl nem kötelező az Evi számára; neked kell elolvasnod
vagy nyomtasd ki.

Lokalizált másolatok: README_<LANG>.txt és FEHLERSUCHE_<LANG>.txt ebben a mappában
(ugyanazok a nyelvi kódok, mint a webhely felhasználói felületén). Angol áttekintés: ez a README.txt;
angol nyelvű hibaelhárítás: FEHLERSUCHE_EN.txt. Német hibaelhárítás is
kézzel karbantartva FEHLERSUCHE_DE.txt formátumban.

Mappaindex (fájl elnevezése, generátor): README.md

---------------------------------------------------------------------------------
  Operációs rendszer
---------------------------------------------------------------------------------

Az Evi Portable csak Microsoft Windows 10 és Windows 11 rendszerekhez használható. Nem az
támogatott Windows 7/8, macOS, Linux vagy mobil operációs rendszereken.

---------------------------------------------------------------------------------
  Első kezdés – a letöltéstől az Evi futtatásáig
---------------------------------------------------------------------------------

1) Telepítési hely
   Másolja vagy bontsa ki a teljes Evi mappát egy Ön által irányított helyre – például
   az asztalra, a dokumentumokra vagy egy USB-meghajtóra. Tartsa meg a mappaszerkezetet
   kézbesítve (ne törölje azokat az almappákat, amelyeket nem saját maga hozott létre).

2) Nyelvi modell (kötelező)
   Évinek szüksége van egy fő AI-modellfájlra (.gguf kiterjesztésű) a mappában:
   modellek\llm\
   A méretekre vonatkozó javaslatokért lásd a models\llm\README.txt fájlt. Miután a fájl ott van,
   start Évi; lehetőség szerint automatikusan felismeri a modellt.

3) Első indítás – aktiválás
   Amikor először indítja el az Evi-t, megjelenik egy aktiváló ablak.
   • A számítógépén megjelenik egy gépazonosító (ez a hardver egyedi).
   • Másolja ki a gépazonosítót (gomb: "Gépazonosító másolása"), és küldje el e-mailben a következő címre:
     Brielbeck@hotmail.de
   • Kap egy soros kulcsot, amely csak ugyanazon a számítógépen működik
     (a kulcs a hardverhez van kötve).
   • Illessze be a kulcsot az aktiváló ablakba, és válassza az Aktiválás lehetőséget.

   Ha jelentős hardvert cserél, vagy a lemezt úgy mozgatja, hogy megváltozzon az azonosító,
   lehet, hogy új kulcsra van szüksége – vegye fel a kapcsolatot ugyanazon a címen.

4) Aktiválás után
   Megnyílik a főablak. Válassza ki a nyelvet, a mikrofont és a hangot a bal oldalon
   beállítások panel. Parancspéldákért mondja ki bármikor, hogy „nyissa meg a csalólapot”.
   (más nyelvekhez lásd a cheatsheets\en.txt és testvérfájlokat).

5) Nem kötelező: nyissa meg ezt a kézikönyvet a Windows rendszerből
   A Fájlkezelőben lépjen az Evi mappába, majd a Manual\README.txt fájlba, és nyissa meg
   Jegyzettömbbel vagy bármilyen szövegnézegetővel.

---------------------------------------------------------------------------------
  Interfész nyelve (GUI)
---------------------------------------------------------------------------------

A felhasználói felület a felül található Nyelv alatt kiválasztott nyelvet követi
a bal oldali beállítási panelen (első blokk az oldalsávon). Miután kiválasztotta a
a nyelv, a menük, a gombok, a címkék és a legtöbb képernyőn megjelenő szöveg átvált erre
nyelven, ahol létezik fordítás. Bármikor megváltoztathatja; csak a
szövege változik, nem az elrendezés.

Tipp: A cheatsheets\ mappában található cheat sheets parancsok listája szerint
nyelvi kód (en.txt, de.txt, …). A részletekért lásd a cheatsheets\README.txt fájlt.
Ez a kézikönyv\ mappa a termék hosszabb áttekintése; csaló lapok a
gyors "mit mondjak" lista.

---------------------------------------------------------------------------------
  Grafikus kártya (GPU) – gyors útmutató
---------------------------------------------------------------------------------

Erős középső választás az NVIDIA GeForce RTX 4070 Ti 12 GB videóval
memória: jó egyensúly a sebesség, a kontextus méret és a nagyobb modellek számára.

Az RTX 3060-tól RTX 5090-ig terjedő kártyák jól működhetnek; a legjobb illeszkedés attól függ
a RAM-ról, a CPU-ról, a hűtésről és a telepített modellfájlról. Használja az előre beállított GPU-t
Evi oldalsávja, hogy illeszkedjen a hardverhez.

A csak a CPU-n való futás (a "CPU … GB RAM" előre beállított értékek) vészhelyzeti tartalék:
Évi használható grafikus kártya nélkül is használható, de a válaszok sokkal lassabbak.
Amikor csak teheti, részesítse előnyben az igazi GPU-t.

---------------------------------------------------------------------------------
  Teljesen hordozható – amikor internetre van szüksége
---------------------------------------------------------------------------------

Az Evi hordozhatóra készült: másolja át a teljes mappát egy másik meghajtóra, USB-meghajtóra,
vagy PC-n, majd indítsa el ott. Csevegések, emlékek, beállítások, biztonsági adatok és az Ön
az aktiváló fájl általában ebben a mappában marad (az aktiválás a
PC, nem a mappa elérési útja).

Az internet főként a letöltött dolgokra szolgál (modellfájlok, opcionális
hangok vagy extrák, frissítések) és az olyan választható funkciókhoz, mint az internetes keresés, a levelezés,
streaming vagy időjárás, ha engedélyezi a hálózati hozzáférést.

Alapvető csevegés, memória, jegyzetek, időzítők, fájleszközök az engedélyezett mappában, helyi
a beszédfelismerés, a helyi hangkimenet és az adatvédelmi zár fut rajta
gépet anélkül, hogy a beszélgetéseit felhőszolgáltatásba küldené. Opcionális online
a funkciók csak akkor futnak, ha a hálózati hozzáférés be van kapcsolva, és Ön használja őket.

---------------------------------------------------------------------------------
  Biztonság: PIN-kód és hangalapú feloldás (másolásgátló)
---------------------------------------------------------------------------------

Evi használhat biztonsági PIN-kódot és opcionális hangregisztrációt a készülékén.

Hangos feloldás használata esetén minden kísérlet kérhet egy rövid véletlenszerű szókészletet
ez minden alkalommal változik – nem egy állandó kifejezés örökre. Ez blokkolja a könnyűt
trükk egyetlen régi hangfelvétel visszajátszására. A PIN-kód továbbra is a
külön védelmi vonal.

Ennek célja az alkalmi visszaélések megállítása; egyetlen fogyasztói termék sem ígérhet
tökéletes minden támadás ellen (például valaki, aki rendelkezik mind a PIN-kóddal, mind a
kifinomult hangmimika). Tartsa magánjellegű PIN-kódját, és fejezze be a beállítást
alkalmazás végigvezeti Önt.

---------------------------------------------------------------------------------
  Hibaelhárítás (rövid ellenőrző lista)
---------------------------------------------------------------------------------

• Nincs AI válasz / modellhiba
  → Legalább egy megfelelő .gguf a modellekben\llm\ ? Lásd a models\llm\README.txt fájlt.
  → Ha a GPU elérési útja sikertelen, próbáljon ki egy kisebb modellt vagy egy előre beállított CPU-t az oldalsávon.

• Nincs mikrofon
  → Windows hangbeállítások: tesztelje a mikrofont. Az Eviben válassza ki az eszközt az alatt
    Mikrofon és Mentés.

• Nincs hangkimenet
  → Ellenőrizze, hogy az Ön nyelvéhez tartozó hangfájlok léteznek-e a piper\ mappában és
    válasszon egy hangot az oldalsávon.

• A web vagy a YouTube nem működik
  → Ha online funkciókat szeretne, kapcsolja ki az "Összes forgalom blokkolása" lehetőséget az oldalsávon.
  → A YouTube lejátszásához általában VLC Portable és hálózati hozzáférés szükséges.

• Csalólapok szerkesztése után
  → Indítsa újra az Evi-t, hogy minden szöveges segítő megbízhatóan fogadja a változásokat.

---------------------------------------------------------------------------------
  Hibaelhárítás (bővített referencia)
---------------------------------------------------------------------------------

Gyors ellenőrzések (mindig először)
  • Windows 10 vagy 11 64 bites, frissítve, nagy változások után újraindítva?
  • Az Evi egy teljesen kibontott mappából fut – nem egy archívumból?
  • Kerülje a felhővel szinkronizált mappákat (OneDrive stb.) az élő adatmappához
    Az Evi fut – használjon helyi elérési utat, például C:\EviPortable vagy D:\Tools\Evi, amikor
    lehetséges.
  • Elég szabad lemezterület a modellhez, a csevegéshez és a frissítésekhez?
  • Modell-, hang- vagy csalólapváltás után: lépjen ki teljesen Evi-ből, és indítsa el
    újra.

1) Operációs rendszer
  • Az Evi csak a Windows 10 és 11 rendszerhez használható; más operációs rendszer verziók nem támogatottak.
  • Ha az alkalmazás egyáltalán nem indul el, teljesen csomagolja ki a csomagot, ellenőrizze a víruskeresőt
    naplózza a blokkolt végrehajtható fájlokat, és próbáljon meg egy rövidebb telepítési útvonalat ritka nélkül
    Csak Unicode karakterek.

2) Mappa elérési útja, víruskereső, hordozhatóság
  • Adjon meg egy kizárást az Evi gyökérmappához a biztonsági szoftverben, ha a vizsgálat eredménye
    nagyon lassú az indítás vagy a fájlok zárolása letöltés közben.
  • USB-meghajtók: előnyben részesítsd az USB 3 + NTFS-t; A nagyon lassú média fájdalmassá teszi a nagy modelleket.

3) Nyelvi modell (.gguf)
  • tünetek: nincs válasz, modellhibák, azonnali betöltési hiba.
  • javítások: ellenőrizze, hogy a models\llm\ teljes .gguf-ot tartalmaz (nem 0 bájtot); töltse le újra
ha szükséges; párosítsa a modell méretét a VRAM-mal a models\llm\README.txt használatával; ha bizonytalan,
    tartson egyetlen tesztelt q4_k_m fájlt a mappában.
  • Több .gguf fájl: Az Evi kiválaszthatja a legnagyobbat, amely belefér a VRAM-ba – ha Ön
    ütközés gyanúja esetén teszteljen csak egy fájllal.

4) GPU, CUDA, illesztőprogramok, nincs memória
  • Frissítse az NVIDIA illesztőprogramot; laptopokon kényszerítse a különálló GPU-t / teljesítményt
    mód Evi számára, ahol a Windows lehetővé teszi.
  • Ha OOM- vagy GPU-összeomlást lát, használjon kisebb ellenőrzőpontot, zárjon be más GPU-alkalmazásokat,
    alacsonyabb hőmérsékletet, vagy váltson előre beállított CPU-ra (lassabb, de egyenletesebb).

5) Csak CPU mód
  • Várhatóan lassú; elég szabad rendszer RAM; nehéz háttérfeladatok bezárása;
    hosszú munkamenetek során használja a „Nagy teljesítmény” energiatervet.

6) Aktiválás
  • Gondosan illessze be a kulcsokat (nincs felesleges szóköz); a kulcsok egy gépazonosítóhoz vannak kötve.
  • Nagyobb hardvermódosítások után szükség lehet cserekulcsra – használja a támogatást
    címet az adataiddal.

7) Mikrofon
  • Windows Adatvédelem → Mikrofon → asztali alkalmazások engedélyezése.
  • Állítsa be a megfelelő alapértelmezett rögzítőeszközt; az Eviben válassza ki ugyanazt az eszközt, és Mentse.
  • A Bluetooth fejhallgatók késleltetést növelhetnek – tesztelje USB-mikrofonnal, ha nem biztos benne.
  • Előfordulhat, hogy egy másik alkalmazás rendelkezik exkluzív móddal – ideiglenesen zárja be az értekezlet-szoftvert.

8) Beszédfelismerés (helyi)
  • Ha a felismerés soha nem fejeződik be, győződjön meg arról, hogy a model\whisper alatti modellfájlok megvannak
    sértetlen, és engedélyezze a hálózatot az első modelllekérések alkalmával, ha a buildnek szüksége van rá.

9) Hangkimenet (Piper / TTS)
  • Győződjön meg arról, hogy a piper\ hangcsomagot tartalmaz a felhasználói felület nyelvéhez; válassz hangot
    az oldalsáv; ellenőrizze a Windows hangerőkeverőjét – az Evi alkalmazásonként elnémítható.

10) Hálózat és "Minden forgalom blokkolása"
  • Kapcsolja ki a tiltást a webes, e-mail segítők, időjárás vagy letöltések esetén.
  • A vállalati proxyknak vagy VPN-eknek szükségük lehet informatikai segítségre az engedélyezési listákhoz.

11) YouTube és média
  • Tartsa meg a mellékelt VLC Portable elrendezést; hálózati hozzáférés engedélyezése; olvasni
    Hordozható\VLCHordozható útmutatás, ha az útvonalat áthelyezték.

12) UI nyelv és csalólapok
  • A csalólapok nyelvi fájlonként találhatók a cheatsheets\ alatt – lásd a cheatsheets\README.txt fájlt.
  • A szerkesztések mentése UTF-8 formátumban; a szerkesztések után indítsa újra Évit.

13) Biztonság (PIN/hang feloldás)
  • Használjon csendes környezetet; ellenőrizze újra a mikrofon erősítését; soha ne ossza meg PIN-kódját.
  • A véletlenszerű szavas felszólítások szándékosak – a régi hangfelvételeket nem szabad feloldani.

14) Teljesítmény, lefagy, összeomlik
  • Csökkentse a modell méretét, javítsa a hűtést, olvasson el bármilyen crash.log fájlt a fában, ha Ön
    build létrehoz egyet, és visszaállítja a hibák előtt végzett legutóbbi változtatást.

15) Amikor kapcsolatba lép az ügyfélszolgálattal
  • Tartalmazza a gépazonosítót, a Windows verziót, a GPU-modell + VRAM + illesztőprogramot, amely .gguf
    és a pontos hibaszöveg (nem titkos kulcsok).

Teljes hibaelhárítási hivatkozás (ezen a nyelven): Manual\FEHLERSUCHE_HU.txt

---------------------------------------------------------------------------------
  Támogatás – soros kulcsok és gépazonosító
---------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Mindig adja meg gépazonosítóját az aktiválási képernyőn, amikor kéri a
soros kulcsot vagy cserekulcsot a hardver módosítása után.

================================================================================