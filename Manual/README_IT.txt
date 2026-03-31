================================================================================
  Evi Portable — Manuale dell'utente (panoramica)
  Documento: inglese • Si applica alla build ricevuta con questa cartella
================================================================================

Inserisci qui anche le tue guide o traduzioni più lunghe (ad esempio EN_User_Manual.pdf,
DE_Handbuch.txt). Questo file è facoltativo per l'esecuzione di Evi; spetta a te leggerlo
o stampare.

Copie localizzate: README_<LANG>.txt e FEHLERSUCHE_<LANG>.txt in questa cartella
(stessi codici lingua dell'interfaccia utente del sito web). Panoramica in inglese: questo README.txt;
Risoluzione dei problemi in inglese: FEHLERSUCHE_EN.txt. Anche la risoluzione dei problemi in tedesco lo è
mantenuto a mano come FEHLERSUCHE_DE.txt.

Indice delle cartelle (denominazione dei file, generatore): README.md

--------------------------------------------------------------------------------
  Sistema operativo
--------------------------------------------------------------------------------

Evi Portable è solo per Microsoft Windows 10 e Windows 11. Non lo è
supportato su Windows 7/8, macOS, Linux o sistemi operativi mobili.

--------------------------------------------------------------------------------
  Primo avvio: dal download all'esecuzione di Evi
--------------------------------------------------------------------------------

1) Posizione di installazione
   Copia o estrai l'intera cartella Evi in una posizione che controlli, ad esempio
   sul desktop, sui documenti o su una chiavetta USB. Mantieni la struttura delle cartelle come
   consegnato (non eliminare le sottocartelle che non hai creato tu stesso).

2) Modello linguistico (richiesto)
   Evi ha bisogno di un file del modello AI principale (estensione .gguf) nella cartella:
   modelli\llm\
   Vedi models\llm\README.txt per consigli sulle dimensioni. Una volta che il file è lì,
   avvia Evi; rileva il modello automaticamente quando possibile.

3) Primo avvio: attivazione
   Quando avvii Evi per la prima volta, viene visualizzata una finestra di attivazione.
   • Il PC mostra un ID macchina (univoco per questo hardware).
   • Copiare l'ID Macchina (pulsante: "Copia ID Macchina") e inviarlo via e-mail a:
     Brielbeck@hotmail.de
   • Riceverai una chiave seriale che funziona solo sullo stesso PC
     (la chiave è legata al tuo hardware).
   • Incolla la chiave nella finestra di attivazione e scegli Attiva.

   Se si modifica l'hardware principale o si sposta il disco in modo da modificare l'ID,
   potresti aver bisogno di una nuova chiave: contatta lo stesso indirizzo.

4) Dopo l'attivazione
   Si apre la finestra principale. Scegli la lingua, il microfono e la voce a sinistra
   pannello delle impostazioni. Dì "apri il cheat sheet" in qualsiasi momento per esempi di comandi
   (vedi cheatsheets\en.txt e file gemelli per altre lingue).

5) Opzionale: aprire questo manuale da Windows
   In Esplora file vai alla cartella Evi, quindi Manual\README.txt e aprilo
   con Blocco note o qualsiasi visualizzatore di testo.

--------------------------------------------------------------------------------
  Lingua dell'interfaccia (GUI)
--------------------------------------------------------------------------------

L'interfaccia utente segue la lingua scelta in Lingua in alto
del pannello delle impostazioni di sinistra (primo blocco nella barra laterale). Dopo aver selezionato a
la lingua, i menu, i pulsanti, le etichette e la maggior parte del testo sullo schermo passano a quello
lingua ovunque esistano traduzioni. Puoi cambiarlo in qualsiasi momento; solo il
cambia la formulazione, non il layout.

Suggerimento: i cheat sheet dei comandi nella cartella cheatsheets\ sono elencati per
codice della lingua (en.txt, de.txt, …). Per i dettagli vedere cheatsheets\README.txt.
Questa cartella Manual\ è la panoramica più lunga del prodotto; i cheat sheet sono i
un rapido elenco di "cosa dire".

--------------------------------------------------------------------------------
  Scheda grafica (GPU): guida rapida
--------------------------------------------------------------------------------

Una buona scelta intermedia è una NVIDIA GeForce RTX 4070 Ti con 12 GB di video
memoria: buon equilibrio tra velocità, dimensione del contesto e spazio per modelli più grandi.

Le schede da RTX 3060 a RTX 5090 possono funzionare bene; la soluzione migliore dipende
su RAM, CPU, raffreddamento e quale file di modello installi. Utilizza la preimpostazione GPU in
Barra laterale di Evi adatta al tuo hardware.

L'esecuzione solo sulla CPU (le preimpostazioni "CPU … GB RAM") è un fallback di emergenza:
Evi rimane utilizzabile senza una scheda grafica adatta, ma le risposte sono molto più lente.
Preferisci una vera GPU ogni volta che puoi.

--------------------------------------------------------------------------------
  Completamente portatile: quando hai bisogno di Internet
--------------------------------------------------------------------------------

Evi è progettato per essere portatile: copia l'intera cartella su un'altra unità, chiavetta USB,
o PC, quindi avvialo da lì. Chat, ricordi, impostazioni, dati di sicurezza e i tuoi
il file di attivazione normalmente rimane all'interno di quella cartella (l'attivazione è legata al file
PC, non il percorso della cartella).

Internet è principalmente per cose che scegli di scaricare (file di modelli, facoltativi
voci o extra, aggiornamenti) e per funzionalità opzionali come ricerca web, posta,
streaming o meteo quando consenti l'accesso alla rete.

Chat principale, memoria, note, timer, strumenti di file all'interno della cartella consentita, locale
il riconoscimento vocale, l'output vocale locale e il blocco della privacy vengono eseguiti sul tuo
macchina senza inviare le conversazioni a un servizio cloud. Facoltativo in linea
le funzionalità vengono eseguite solo quando l'accesso alla rete è attivo e le utilizzi.

--------------------------------------------------------------------------------
  Sicurezza: PIN e sblocco vocale (anti-copia)
--------------------------------------------------------------------------------

Evi può utilizzare un PIN di sicurezza e la registrazione vocale opzionale sul tuo dispositivo.

Quando viene utilizzato lo sblocco vocale, ogni tentativo può richiedere un breve set di parole casuali
che cambia ogni volta, non una frase fissa per sempre. Ciò blocca il facile
trucco di riprodurre una singola vecchia registrazione della tua voce. Il tuo PIN rimane a
linea di difesa separata.

Questo è progettato per fermare gli abusi occasionali; nessun prodotto di consumo può promettere
perfezione contro ogni attacco (ad esempio qualcuno che ha sia il tuo PIN che
mimica vocale sofisticata). Mantieni il tuo PIN privato e completa la configurazione come
l'app ti guida.

--------------------------------------------------------------------------------
  Risoluzione dei problemi (breve lista di controllo)
--------------------------------------------------------------------------------

• Nessuna risposta AI/errore del modello
  → Almeno un .gguf adatto in models\llm\ ? Vedere modelli\llm\README.txt.
  → Prova un modello più piccolo o una preimpostazione CPU nella barra laterale se il percorso GPU fallisce.

• Nessun microfono
  → Impostazioni audio di Windows: prova il microfono. In Evi, scegli il dispositivo sotto
    Microfono e salva.

• Nessuna uscita vocale
  → Controlla che nella cartella piper\ esistano file vocali per la tua lingua
    scegli una voce nella barra laterale.

• Web o YouTube falliscono
  → Disattiva "Blocca tutto il traffico" nella barra laterale se desideri funzionalità online.
  → Per la riproduzione su YouTube, in genere sono necessari VLC Portable e l'accesso alla rete.

• Dopo aver modificato i foglietti illustrativi
  → Riavvia Evi in modo che tutti gli aiutanti di testo raccolgano le modifiche in modo affidabile.

--------------------------------------------------------------------------------
  Risoluzione dei problemi (riferimento esteso)
--------------------------------------------------------------------------------

Controlli rapidi (sempre prima)
  • Windows 10 o 11 a 64 bit, aggiornato, riavviato dopo grandi modifiche?
  • Evi in ​​esecuzione da una cartella completamente estratta, non dall'interno di un archivio?
  • Evitare le cartelle sincronizzate nel cloud (OneDrive, ecc.) per la cartella dei dati in tempo reale
    Evi viene eseguito: utilizza un percorso locale come C:\EviPortable o D:\Tools\Evi quando
    possibile.
  • Spazio libero su disco sufficiente per il modello, le chat e gli aggiornamenti?
  • Dopo aver cambiato modelli, voci o cheat sheet: esci completamente da Evi e inizia
    di nuovo.

1) Sistema operativo
  • Evi è solo per Windows 10 e 11; altre versioni del sistema operativo non sono supportate.
  • Se l'app non si avvia affatto, estrai completamente il pacchetto e controlla l'antivirus
    logs per gli eseguibili bloccati e provare un percorso di installazione più breve senza rari
    Caratteri solo Unicode.

2) Percorso della cartella, antivirus, portabilità
  • Aggiungere un'esclusione per la cartella principale Evi nel software di sicurezza se vengono effettuate scansioni
    avvio molto lento o blocco dei file durante i download.
  • Chiavette USB: preferire USB 3 + NTFS; i media molto lenti rendono dolorosi i modelli di grandi dimensioni.

3) Modello linguistico (.gguf)
  • sintomi: nessuna risposta, errori del modello, mancato caricamento istantaneo.
  • correzioni: verifica models\llm\ contiene un .gguf completo (non 0 byte); scaricare nuovamente
se necessario; abbinare le dimensioni del modello alla VRAM utilizzando models\llm\README.txt; se non sei sicuro,
    conservare un singolo file q4_k_m testato nella cartella.
  • più file .gguf: Evi può scegliere quello più grande che si adatta alla tua VRAM, se tu
    sospetta un conflitto, prova con un solo file.

4) GPU, CUDA, driver, memoria insufficiente
  • Aggiorna il driver NVIDIA; sui laptop, forza la GPU/prestazioni discrete
    modalità per Evi laddove Windows lo consente.
  • Se noti arresti anomali di OOM o GPU, utilizza un checkpoint più piccolo, chiudi altre app GPU,
    abbassare la temperatura o passare a una preimpostazione della CPU (più lenta ma più stabile).

5) Modalità solo CPU
  • Si prevede che sarà lento; RAM di sistema sufficiente libera; chiudere attività in background pesanti;
    utilizzare il piano di alimentazione "Alte prestazioni" durante le sessioni lunghe.

6) Attivazione
  • Incollare le chiavi con cura (senza spazi aggiuntivi); le chiavi sono legate a un ID macchina.
  • Dopo importanti modifiche hardware potrebbe essere necessaria una chiave sostitutiva: utilizza il supporto
    indirizzo con i tuoi dati

7) Microfono
  • Privacy di Windows → Microfono → consenti app desktop.
  • Impostare il corretto dispositivo di registrazione predefinito; in Evi scegli lo stesso dispositivo e salva.
  • Gli auricolari Bluetooth possono aggiungere latenza: se non sei sicuro, prova con un microfono USB.
  • Un'altra app potrebbe contenere la modalità esclusiva: chiudere temporaneamente il software per riunioni.

8) Riconoscimento vocale (locale)
  • Se il riconoscimento non termina mai, assicurarsi che i file del modello in models\whisper lo siano
    intatto e consenti la rete al primo recupero del modello se la tua build lo richiede.

9) Uscita vocale (Piper / TTS)
  • Conferma che piper\ contiene un pacchetto vocale per la tua lingua dell'interfaccia utente; scegli una voce
    la barra laterale; controlla il mixer del volume di Windows: l'audio di Evi potrebbe essere disattivato per ogni app.

10) Rete e "Blocca tutto il traffico"
  • Disattiva il blocco per web, helper di posta, meteo o download.
  • I proxy aziendali o le VPN potrebbero richiedere assistenza IT per le liste consentite.

11) YouTube e media
  • Mantenere il layout VLC Portable in bundle; abilitare l'accesso alla rete; leggere
    Guida Portable\VLCPortable se il percorso è stato spostato.

12) Linguaggio dell'interfaccia utente e trucchi
  • I cheat sheet sono per file di lingua in cheatsheets\ — vedere cheatsheets\README.txt.
  • Salva le modifiche come UTF-8; riavvia Evi dopo le modifiche.

13) Sicurezza (PIN/sblocco vocale)
  • Utilizzare un ambiente tranquillo; ricontrollare il guadagno del microfono; non condividere mai il tuo PIN.
  • I suggerimenti di parole casuali sono intenzionali: le vecchie registrazioni vocali non dovrebbero sbloccarsi.

14) Prestazioni, blocchi, arresti anomali
  • Riduci le dimensioni del modello, migliora il raffreddamento, leggi eventuali crash.log nell'albero, se tuo
    build ne crea uno e ripristina l'ultima modifica apportata prima degli errori.

15) Quando si contatta l'assistenza
  • Include ID macchina, versione Windows, modello GPU + VRAM + driver, quale .gguf
    che usi e il testo esatto dell'errore (non le chiavi segrete).

Riferimento completo per la risoluzione dei problemi (questa lingua): Manual\FEHLERSUCHE_IT.txt

--------------------------------------------------------------------------------
  Supporto: chiavi seriali e ID macchina
--------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Includere sempre l'ID macchina dalla schermata di attivazione quando si richiede a
chiave seriale o una chiave sostitutiva dopo modifiche hardware.

================================================================================