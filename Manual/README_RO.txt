=================================================================================
  Evi Portable — Manual de utilizare (prezentare generală)
  Document: engleză • Se aplică pentru versiunea primită cu acest folder
=================================================================================

Puneți și aici propriile ghiduri sau traduceri mai lungi (de exemplu, EN_User_Manual.pdf,
DE_Handbuch.txt). Acest fișier este opțional pentru ca Evi să ruleze; este pentru tine să citești
sau tipăriți.

Copii localizate: README_<LANG>.txt și FEHLERSUCHE_<LANG>.txt în acest folder
(aceleași coduri de limbă ca și interfața de utilizare a site-ului web). Prezentare generală în limba engleză: acest README.txt;
Depanare în limba engleză: FEHLERSUCHE_EN.txt. Depanarea germană este, de asemenea
întreținut manual ca FEHLERSUCHE_DE.txt.

Index de foldere (denumirea fișierelor, generator): README.md

------------------------------------------------------------------------------
  Sistem de operare
------------------------------------------------------------------------------

Evi Portable este numai pentru Microsoft Windows 10 și Windows 11. Nu este
acceptat pe Windows 7/8, macOS, Linux sau sisteme de operare mobile.

------------------------------------------------------------------------------
  Prima pornire — de la descărcare până la rularea Evi
------------------------------------------------------------------------------

1) Locația de instalare
   Copiați sau extrageți întregul folder Evi într-un loc pe care îl controlați - de exemplu
   Desktop-ul, Documentele sau un stick USB. Păstrați structura folderului ca
   livrat (nu ștergeți subdosarele pe care nu le-ați creat singur).

2) Model de limbă (obligatoriu)
   Evi are nevoie de un fișier model AI principal (extensia .gguf) în folder:
   modele\llm\
   Consultați modelele\llm\README.txt pentru recomandări de dimensiune. După ce dosarul este acolo,
   începe Evi; detectează automat modelul atunci când este posibil.

3) Prima lansare — activare
   Când porniți Evi prima dată, apare o fereastră de activare.
   • PC-ul dvs. afișează un ID de mașină (unic pentru acest hardware).
   • Copiați ID-ul mașinii (butonul: „Copiați ID-ul mașinii”) și trimiteți-l prin e-mail la:
     Brielbeck@hotmail.de
   • Veți primi o cheie de serie care funcționează numai pe același computer
     (cheia este legată de hardware-ul dvs.).
   • Lipiți cheia în fereastra de activare și alegeți Activare.

   Dacă schimbați hardware-ul major sau mutați discul într-un mod care modifică ID-ul,
   este posibil să aveți nevoie de o cheie nouă — contactați aceeași adresă.

4) După activare
   Se deschide fereastra principală. Alegeți limba, microfonul și vocea din stânga
   panoul de setări. Spuneți „deschideți foaia de cheat” oricând pentru exemple de comandă
   (vezi cheatsheets\en.txt și fișierele surori pentru alte limbi).

5) Opțional: deschideți acest manual din Windows
   În File Explorer, accesați folderul Evi, apoi Manual\README.txt și deschideți-l
   cu Notepad sau orice vizualizator de text.

------------------------------------------------------------------------------
  Limbajul interfeței (GUI)
------------------------------------------------------------------------------

Interfața de utilizator urmează limba pe care o alegeți sub Limbă din partea de sus
din panoul de setări din stânga (primul bloc din bara laterală). După ce selectați a
limba, meniurile, butoanele, etichetele și majoritatea textului de pe ecran comută la aceasta
limba oriunde există traduceri. Îl poți schimba oricând; doar cel
se modifică formularea, nu aspectul.

Sfat: Cheat sheets pentru comandă din folderul cheatsheets\ sunt listate pentru
cod de limbă (en.txt, de.txt, …). Pentru detalii, consultați cheatsheets\README.txt.
Acest folder Manual\ este prezentarea mai lungă a produsului; cheat sheets sunt cele
listă rapidă „ce să spun”.

------------------------------------------------------------------------------
  Placă grafică (GPU) — ghid rapid
------------------------------------------------------------------------------

O alegere de mijloc puternică este un NVIDIA GeForce RTX 4070 Ti cu 12 GB de video
memorie: echilibru bun de viteză, dimensiunea contextului și spațiu pentru modele mai mari.

Cardurile de la aproximativ RTX 3060 până la RTX 5090 pot funcționa bine; cea mai bună potrivire depinde
pe RAM, CPU, răcire și fișierul model pe care îl instalați. Utilizați presetarea GPU-ului
Bara laterală a lui Evi să se potrivească cu hardware-ul tău.

Rularea numai pe CPU (presetările „CPU … GB RAM”) este o rezervă de urgență:
Evi rămâne utilizabil fără o placă grafică adecvată, dar răspunsurile sunt mult mai lente.
Preferați un GPU adevărat ori de câte ori puteți.

------------------------------------------------------------------------------
  Complet portabil - atunci când aveți nevoie de internet
------------------------------------------------------------------------------

Evi este construit pentru a fi portabil: copiați întregul folder pe o altă unitate, stick USB,
sau PC, apoi porniți-l acolo. Chat-uri, amintiri, setări, date de securitate și dvs
fișierul de activare rămâne în mod normal în acel folder (activarea este legată de fișierul
PC, nu calea folderului).

Internetul este în principal pentru lucruri pe care alegeți să le descărcați (fișiere de model, opțional
voci sau extra, actualizări) și pentru funcții opționale precum căutarea pe web, e-mail,
streaming sau vremea când permiteți accesul la rețea.

Chat de bază, memorie, note, temporizatoare, instrumente de fișiere din dosarul permis, local
recunoașterea vorbirii, ieșirea vocală locală și blocarea confidențialității rulează pe dvs
aparat fără a trimite conversațiile către un serviciu cloud. Opțional online
funcțiile rulează numai când accesul la rețea este activat și le utilizați.

------------------------------------------------------------------------------
  Securitate: PIN și deblocare vocală (anti-copie)
------------------------------------------------------------------------------

Evi poate folosi un PIN de securitate și înregistrarea vocală opțională pe dispozitiv.

Când se utilizează deblocarea vocală, fiecare încercare poate solicita un set scurt de cuvinte aleatorii
care se schimbă de fiecare dată – nu o frază fixă pentru totdeauna. Asta blochează ușor
truc de a reda o singură înregistrare veche a vocii tale. PIN-ul dvs. rămâne a
linie separată de apărare.

Acesta este conceput pentru a opri abuzul ocazional; niciun produs de consum nu poate promite
perfecțiunea împotriva oricărui atac (de exemplu, cineva care are atât codul tău PIN, cât și
mimica sofisticată a vocii). Păstrați codul PIN privat și completați configurarea ca
aplicația te ghidează.

------------------------------------------------------------------------------
  Depanare (listă de verificare scurtă)
------------------------------------------------------------------------------

• Fără răspunsuri AI / eroare de model
  → Cel puțin un .gguf potrivit în modele\llm\ ? Vedeți modelele\llm\README.txt.
  → Încercați un model mai mic sau un procesor presetat în bara laterală dacă calea GPU eșuează.

• Fără microfon
  → Setări de sunet Windows: testați microfonul. În Evi, alegeți dispozitivul de sub
    Microfon și Salvare.

• Fără ieșire vocală
  → Verificați dacă fișierele vocale pentru limba dvs. există în folderul piper\ și
    alege o voce din bara laterală.

• Web sau YouTube eșuează
  → Dezactivați „Blocați tot traficul” din bara laterală dacă doriți funcții online.
  → Pentru redarea pe YouTube, de obicei sunt necesare VLC Portable și acces la rețea.

• După editarea cheat sheets
  → Reporniți Evi, astfel încât toți ajutoarele de text să preia modificările în mod fiabil.

------------------------------------------------------------------------------
  Depanare (referință extinsă)
------------------------------------------------------------------------------

Verificări rapide (întotdeauna primele)
  • Windows 10 sau 11 pe 64 de biți, actualizat, repornit după schimbări mari?
  • Evi rulează dintr-un folder complet extras - nu din interiorul unei arhive?
  • Evitați folderele sincronizate în cloud (OneDrive etc.) pentru folderul de date live în timp ce
    Evi rulează — utilizați o cale locală, cum ar fi C:\EviPortable sau D:\Tools\Evi atunci când
    posibil.
  • Suficient spațiu liber pe disc pentru model, chat și actualizări?
  • După ce ați schimbat modelele, vocile sau foile de cheat: părăsiți complet Evi și începeți
    din nou.

1) Sistem de operare
  • Evi este doar pentru Windows 10 și 11; alte versiuni ale sistemului de operare nu sunt acceptate.
  • Dacă aplicația nu pornește deloc, extrageți complet pachetul, verificați antivirusul
    jurnalele pentru executabile blocate și încercați o cale de instalare mai scurtă, fără rare
    Caractere numai Unicode.

2) Calea folderului, antivirus, portabilitate
  • Adăugați o excludere pentru folderul rădăcină Evi în software-ul de securitate dacă se efectuează scanări
    porniți foarte lent sau blocați fișierele în timpul descărcărilor.
  • Stick-uri USB: prefer USB 3 + NTFS; media foarte lente face modelele mari dureroase.

3) Model de limbă (.gguf)
  • simptome: fără răspunsuri, erori de model, eșec instantaneu la încărcare.
  • remedieri: verificați că modelele\llm\ conține un .gguf complet (nu 0 octeți); re-descărcați
dacă este necesar; potriviți dimensiunea modelului cu VRAM folosind modelele\llm\README.txt; dacă nesigur,
    păstrați un singur fișier q4_k_m testat în folder.
  • mai multe fișiere .gguf: Evi poate alege cel mai mare care se potrivește VRAM-ului dvs. — dacă dvs
    suspectați un conflict, testați cu un singur fișier.

4) GPU, CUDA, drivere, memorie lipsită
  • Actualizați driverul NVIDIA; pe laptopuri, forțați GPU / performanță discretă
    modul pentru Evi unde Windows permite.
  • Dacă vedeți blocări OOM sau GPU, utilizați un punct de control mai mic, închideți alte aplicații GPU,
    temperatură mai scăzută sau comutați la o presetare a procesorului (mai lent, dar mai constant).

5) Modul numai pentru procesor
  • Se așteaptă să fie lent; RAM de sistem suficient de liberă; închide sarcini grele de fundal;
    utilizați planul de alimentare „Performanță ridicată” în timpul sesiunilor lungi.

6) Activare
  • Lipiți cheile cu atenție (fără spații suplimentare); cheile sunt legate de un ID de mașină.
  • După modificări majore de hardware, este posibil să aveți nevoie de o cheie de înlocuire — utilizați suportul
    adresa cu detaliile dvs.

7) Microfon
  • Confidențialitate Windows → Microfon → permite aplicații desktop.
  • Setați dispozitivul de înregistrare implicit corect; în Evi alegeți același dispozitiv și Salvați.
  • Căștile Bluetooth pot adăuga latență — testați cu un microfon USB dacă nu sunteți sigur.
  • O altă aplicație poate deține modul exclusiv – închideți temporar software-ul pentru întâlniri.

8) Recunoașterea vorbirii (locală)
  • Dacă recunoașterea nu se termină niciodată, asigurați-vă că fișierele model de sub modele\șoaptă sunt
    intactă și permiteți rețeaua la preluarea modelului pentru prima dată, dacă construcția dvs. are nevoie.

9) Ieșire vocală (Piper / TTS)
  • Confirmați că piper\ conține un pachet de voce pentru limba dvs. UI; alege o voce înăuntru
    bara laterală; verificați mixerul de volum Windows - Evi poate fi dezactivat per-aplicație.

10) Rețea și „Blocați tot traficul”
  • Dezactivați blocarea pentru web, asistență prin e-mail, vreme sau descărcări.
  • Proxy-urile corporative sau VPN-urile pot necesita ajutor IT pentru listele de permise.

11) YouTube și media
  • Păstrați aspectul VLC Portable inclus; permite accesul la rețea; citeste
    Portable\VLCPortable ghidare dacă calea a fost mutată.

12) Limbajul UI și foile de cheat
  • Cheatsheets sunt pentru fiecare fișier de limbă sub cheatsheets\ — vezi cheatsheets\README.txt.
  • Salvați editările ca UTF-8; reporniți Evi după editări.

13) Securitate (PIN / deblocare vocală)
  • Folosiți un mediu liniștit; verificați din nou câștigul microfonului; nu vă împărtășiți niciodată codul PIN.
  • Solicitările cu cuvinte aleatorii sunt intenționate — înregistrările vocale vechi nu ar trebui să se deblocheze.

14) Performanță, blocări, blocări
  • Reduceți dimensiunea modelului, îmbunătățiți răcirea, citiți orice crash.log din arbore dacă sunteți
    build creează unul și derulează înapoi ultima modificare pe care ați făcut-o înainte de eșecuri.

15) Când contactați asistența
  • Includeți ID-ul mașinii, versiunea Windows, modelul GPU + VRAM + driver, care .gguf
    pe care îl utilizați și textul de eroare exact (nu cheile secrete).

Referință completă de depanare (această limbă): Manual\FEHLERSUCHE_RO.txt

------------------------------------------------------------------------------
  Asistență — chei seriale și ID mașină
------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Includeți întotdeauna ID-ul mașinii de pe ecranul de activare atunci când solicitați a
cheie de serie sau o cheie de înlocuire după modificări hardware.

=================================================================================