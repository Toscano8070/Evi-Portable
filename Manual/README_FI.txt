==================================================================================
  Evi Portable — Käyttöopas (yleiskatsaus)
  Asiakirja: englanti • Koskee tämän kansion mukana saamaasi koontiversiota
==================================================================================

Laita tänne myös omat pidemmät oppaasi tai käännökset (esim. EN_User_Manual.pdf,
DE_Handbuch.txt). Tämä tiedosto on valinnainen Eville; se on sinun luettavaksesi
tai tulostaa.

Lokalisoidut kopiot: README_<LANG>.txt ja FEHLERSUCHE_<LANG>.txt tässä kansiossa
(samat kielikoodit kuin verkkosivuston käyttöliittymässä). Englanninkielinen yleiskatsaus: tämä README.txt;
Englanninkielinen vianetsintä: FEHLERSUCHE_FI.txt. Saksalainen vianetsintä on myös
ylläpidetään käsin muodossa FEHLERSUCHE_DE.txt.

Kansiohakemisto (tiedostonimet, generaattori): README.md

---------------------------------------------------------------------------------
  Käyttöjärjestelmä
---------------------------------------------------------------------------------

Evi Portable on tarkoitettu vain Microsoft Windows 10:lle ja Windows 11:lle. Se ei ole
tuettu Windows 7/8-, macOS-, Linux- tai mobiilikäyttöjärjestelmissä.

---------------------------------------------------------------------------------
  Ensimmäinen aloitus – latauksesta Evin käynnistämiseen
---------------------------------------------------------------------------------

1) Asennuspaikka
   Kopioi tai pura koko Evi-kansio hallitsemaasi paikkaan – esimerkiksi
   työpöydällesi, asiakirjoihin tai USB-tikulle. Säilytä kansiorakenne muodossa
   toimitettu (älä poista alikansioita, joita et ole itse luonut).

2) Kielimalli (pakollinen)
   Evi tarvitsee kansioon yhden päämallitiedoston (laajennus .gguf):
   mallit\llm\
   Katso mallit\llm\README.txt kokosuosituksia varten. Kun tiedosto on siellä,
   aloita Evi; se tunnistaa mallin automaattisesti, kun mahdollista.

3) Ensimmäinen käynnistys — aktivointi
   Kun käynnistät Evin ensimmäisen kerran, näkyviin tulee aktivointiikkuna.
   • Tietokoneessasi on konetunnus (ainutlaatuinen tälle laitteistolle).
   • Kopioi koneen tunnus (painike: "Kopioi koneen tunnus") ja lähetä se sähköpostitse osoitteeseen:
     Brielbeck@hotmail.de
   • Saat sarjaavaimen, joka toimii vain samassa tietokoneessa
     (avain on sidottu laitteistoosi).
   • Liitä avain aktivointiikkunaan ja valitse Aktivoi.

   Jos muutat suurta laitteistoa tai siirrät levyä tavalla, joka muuttaa tunnuksen,
   saatat tarvita uuden avaimen – ota yhteyttä samaan osoitteeseen.

4) Aktivoinnin jälkeen
   Pääikkuna avautuu. Valitse kieli, mikrofoni ja ääni vasemmalta
   asetuspaneeli. Sano "avaa huijauslehti" milloin tahansa saadaksesi komennon esimerkkejä
   (katso cheatsheets\en.txt ja muiden kielten sisartiedostot).

5) Valinnainen: avaa tämä opas Windowsista
   Siirry Resurssienhallinnassa Evi-kansioon, sitten Manual\README.txt ja avaa se
   Muistiolla tai millä tahansa tekstinkatseluohjelmalla.

---------------------------------------------------------------------------------
  Käyttöliittymän kieli (GUI)
---------------------------------------------------------------------------------

Käyttöliittymä noudattaa yläreunan Kieli-kohdassa valitsemaasi kieltä
vasemmasta asetuspaneelista (sivupalkin ensimmäinen lohko). Kun olet valinnut a
kieli, valikot, painikkeet, tarrat ja useimmat näytön tekstit siirtyvät siihen
kielellä, missä käännöksiä on olemassa. Voit muuttaa sen milloin tahansa; vain
sanamuoto muuttuu, ei ulkoasu.

Vihje: Cheatsheets\-kansiossa olevat komennot cheat sheets on lueteltu per
kielikoodi (en.txt, de.txt, …). Katso lisätietoja osoitteesta cheatsheets\README.txt.
Tämä Manual\-kansio on pidempi tuotekatsaus; huijauslevyt ovat
nopea "mitä sanoa" -luettelo.

---------------------------------------------------------------------------------
  Grafiikkakortti (GPU) – pikaopas
---------------------------------------------------------------------------------

Vahva keskivalinta on NVIDIA GeForce RTX 4070 Ti 12 Gt videolla
muisti: hyvä tasapaino nopeuden, kontekstin koon ja tilan suuremmille malleille.

Kortit noin RTX 3060 - RTX 5090 voivat toimia hyvin; paras istuvuus riippuu
RAM-muistista, suorittimesta, jäähdytyksestä ja asennetusta mallitiedostosta. Käytä GPU-esiasetusta
Evin sivupalkki vastaamaan laitteistoasi.

Toimiminen vain suorittimella (esiasetukset "CPU … GB RAM") on hätävara:
Evi pysyy käyttökelpoisena ilman sopivaa näytönohjainta, mutta vastaukset ovat paljon hitaampia.
Suosi todellista GPU:ta aina kun mahdollista.

---------------------------------------------------------------------------------
  Täysin kannettava – kun tarvitset Internetiä
---------------------------------------------------------------------------------

Evi on rakennettu kannettavaksi: kopioi koko kansio toiselle asemalle, USB-tikulle,
tai PC:llä ja käynnistä se sieltä. Chatit, muistot, asetukset, suojaustiedot ja sinun
aktivointitiedosto pysyy tavallisesti kyseisessä kansiossa (aktivointi on sidottu
PC, ei kansion polku).

Internet on tarkoitettu pääasiassa ladattaville asioille (mallitiedostot, valinnainen
äänet tai lisät, päivitykset) ja valinnaisille ominaisuuksille, kuten verkkohaku, sähköposti,
suoratoisto tai sää, kun sallit pääsyn verkkoon.

Ydinkeskustelu, muisti, muistiinpanot, ajastimet, tiedostotyökalut sallitussa kansiossa, paikallinen
puheentunnistus, paikallinen äänilähtö ja yksityisyyslukko toimivat laitteessasi
koneeseen lähettämättä keskustelujasi pilvipalveluun. Valinnainen verkossa
ominaisuudet toimivat vain, kun verkkoyhteys on päällä ja käytät niitä.

---------------------------------------------------------------------------------
  Suojaus: PIN-koodi ja puhelukituksen avaus (kopioinnin esto)
---------------------------------------------------------------------------------

Evi voi käyttää turva-PIN-koodia ja valinnaista äänirekisteröintiä laitteellasi.

Kun puhelukituksen avaus on käytössä, jokainen yritys voi pyytää lyhyitä satunnaisia sanoja
joka muuttuu joka kerta - ei yksi kiinteä lause ikuisesti. Se estää helpon
temppu toistaa yksi vanha äänitallenne. PIN-koodisi pysyy a
erillinen puolustuslinja.

Tämä on suunniteltu estämään satunnainen väärinkäyttö; mikään kuluttajatuote ei voi luvata
täydellisyyttä kaikkia hyökkäyksiä vastaan (esimerkiksi joku, jolla on sekä PIN-koodisi että
hienostunut äänen matkiminen). Pidä PIN-koodi yksityisenä ja suorita asetukset loppuun
sovellus opastaa sinua.

---------------------------------------------------------------------------------
  Vianetsintä (lyhyt tarkistuslista)
---------------------------------------------------------------------------------

• Ei AI-vastauksia / mallivirhe
  → Vähintään yksi sopiva .gguf malleissa\llm\ ? Katso mallit\llm\README.txt.
  → Kokeile pienempää mallia tai suorittimen esiasetusta sivupalkissa, jos GPU-polku epäonnistuu.

• Ei mikrofonia
  → Windowsin ääniasetukset: testaa mikrofonia. Evissä valitse laite alta
    Mikrofoni ja Tallenna.

• Ei äänilähtöä
  → Tarkista, että kielesi äänitiedostot ovat Piper\-kansiossa ja
    valitse ääni sivupalkista.

• Web tai YouTube epäonnistuu
  → Poista käytöstä "Estä kaikki liikenne" sivupalkista, jos haluat online-ominaisuuksia.
  → YouTube-toistoa varten tarvitaan yleensä VLC Portable ja verkkoyhteys.

• Huijausarkkien muokkaamisen jälkeen
  → Käynnistä Evi uudelleen, jotta kaikki tekstiapulaiset havaitsevat muutokset luotettavasti.

---------------------------------------------------------------------------------
  Vianetsintä (laajennettu viite)
---------------------------------------------------------------------------------

Pikatarkastukset (aina ensin)
  • Windows 10 tai 11 64-bittinen, päivitetty, käynnistetty uudelleen suurten muutosten jälkeen?
  • Evi toimii täysin puretusta kansiosta – ei arkiston sisältä?
  • Vältä pilvi-synkronoituja kansioita (OneDrive jne.) live-datakansiossa ollessaan
    Evi toimii — käytä paikallista polkua, kuten C:\EviPortable tai D:\Tools\Evi, kun
    mahdollista.
  • Onko tarpeeksi vapaata levytilaa mallille, keskusteluille ja päivityksille?
  • Kun olet vaihtanut mallia, ääniä tai huijauslehtiä: sulje Evi kokonaan ja aloita
    uudelleen.

1) Käyttöjärjestelmä
  • Evi on tarkoitettu vain Windows 10:lle ja 11:lle; muita käyttöjärjestelmäversioita ei tueta.
  • Jos sovellus ei käynnisty ollenkaan, pura paketti kokonaan, tarkista virustorjunta
    lokit estetyistä suoritettavista tiedostoista ja kokeile lyhyempää asennuspolkua ilman harvinaisia
    Vain Unicode-merkit.

2) Kansion polku, virustorjunta, siirrettävyys
  • Lisää poissulkeminen Evi-juurikansiollesi suojausohjelmistossa, jos skannaukset tekevät
    käynnistys erittäin hidas tai lukitse tiedostot latauksen aikana.
  • USB-tikut: mieluummin USB 3 + NTFS; erittäin hidas media tekee suurista malleista tuskallisia.

3) Kielimalli (.gguf)
  • Oireet: ei vastauksia, mallivirheet, välitön lataus epäonnistui.
  • Korjaukset: varmista, että mallit\llm\ sisältää täydellisen .gguf-tiedoston (ei 0 tavua); lataa uudelleen
tarvittaessa; sovita mallin koko VRAM-muistiin komennolla models\llm\README.txt; jos olet epävarma,
    säilytä kansiossa yksi testattu q4_k_m-tiedosto.
  • useita .gguf-tiedostoja: Evi voi valita suurimman, joka sopii VRAM-muistiisi – jos sinä
    epäile ristiriitaa, testaa vain yhdellä tiedostolla.

4) GPU, CUDA, ajurit, muisti loppu
  • Päivitä NVIDIA-ohjain; kannettavissa tietokoneissa, pakota erillinen GPU / suorituskyky
    Evi-tila, jossa Windows sallii.
  • Jos näet OOM- tai GPU-kaatumiset, käytä pienempää tarkistuspistettä, sulje muut GPU-sovellukset,
    alhaisempi lämpötila tai vaihda suorittimen esiasetukseen (hitaampi mutta vakaampi).

5) Vain CPU -tila
  • Odotetaan olevan hidas; tarpeeksi vapaata järjestelmän RAM-muistia; sulje raskaat taustatehtävät;
    käytä tehosuunnitelmaa "High performance" pitkien istuntojen aikana.

6) Aktivointi
  • Liitä avaimet huolellisesti (ei ylimääräisiä välilyöntejä); avaimet on sidottu yhteen konetunnukseen.
  • Suurten laitteistomuutosten jälkeen saatat tarvita vaihtoavaimen — käytä tukea
    osoite tietojesi kanssa.

7) Mikrofoni
  • Windowsin tietosuoja → Mikrofoni → salli työpöytäsovellukset.
  • Aseta oikea oletustallennuslaite; Valitse Evissä sama laite ja Tallenna.
  • Bluetooth-kuulokkeet voivat lisätä viivettä — testaa USB-mikrofonilla, jos olet epävarma.
  • Toisessa sovelluksessa voi olla yksinoikeustila – sulje kokousohjelmisto väliaikaisesti.

8) Puheentunnistus (paikallinen)
  • Jos tunnistus ei lopu koskaan, varmista, että mallitiedostot kohdassa models\whisper ovat
    ehjänä ja salli verkko ensimmäisen mallihaun yhteydessä, jos kokoonpanosi tarvitsee sitä.

9) Äänilähtö (Piper / TTS)
  • Vahvista, että piper\ sisältää äänipaketin käyttöliittymäkielellesi; valitse ääni
    sivupalkki; tarkista Windowsin äänenvoimakkuuden mikseri - Evi voi olla mykistetty sovelluskohtaisesti.

10) Verkko ja "Estä kaikki liikenne"
  • Poista verkko-, sähköposti-, sää- tai latausten esto käytöstä.
  • Yritysten välityspalvelimet tai VPN-verkot saattavat tarvita IT-apua sallittujen luetteloihin.

11) YouTube ja media
  • Säilytä mukana toimitettu VLC Portable -asettelu; mahdollistaa pääsy verkkoon; lue
    Kannettava\VLCKannettava opastus, jos polkua on siirretty.

12) Käyttöliittymän kieli ja huijausarkit
  • Huijausarkit ovat kielikohtaisia tiedostoja kohdassa Cheatsheets\ — katso cheatsheets\README.txt.
  • Tallenna muutokset UTF-8-muodossa; käynnistä Evi uudelleen muokkauksen jälkeen.

13) Suojaus (PIN / puhelukko)
  • Käytä hiljaista ympäristöä; tarkista mikrofonin vahvistus uudelleen; koskaan jaa PIN-koodiasi.
  • Satunnaiset sanakehotteet ovat tahallisia – vanhojen äänitallenteiden lukitusta ei pitäisi avata.

14) Suorituskyky, jäätyy, kaatuu
  • Pienennä mallin kokoa, paranna jäähdytystä, lue kaikki crash.log-tiedostot puusta, jos sinun
    build luo sellaisen ja peruuta viimeksi tekemäsi muutoksen ennen epäonnistumisia.

15) Kun otat yhteyttä tukeen
  • Sisällytä koneen tunnus, Windows-versio, GPU-malli + VRAM + ohjain, joka .gguf
    käyttämäsi virheteksti (ei salaisia avaimia).

Täydellinen vianmääritysviite (tämä kieli): Manual\FEHLERSUCHE_FI.txt

---------------------------------------------------------------------------------
  Tuki – sarjaavaimet ja koneen tunnus
---------------------------------------------------------------------------------

Sähköposti: Brielbeck@hotmail.de
Liitä aina konetunnuksesi aktivointinäytöstä pyytäessäsi a
sarjaavain tai korvaava avain laitteistomuutosten jälkeen.

==================================================================================