===============================================================================
  Evi Portable — Manuel d'utilisation (aperçu)
  Document : anglais • S'applique à la version que vous avez reçue avec ce dossier
===============================================================================

Mettez ici également vos propres guides ou traductions plus longs (par exemple EN_User_Manual.pdf,
DE_Handbuch.txt). Ce fichier est facultatif pour l'exécution d'Evi ; c'est à toi de lire
ou imprimer.

Copies localisées : README_<LANG>.txt et FEHLERSUCHE_<LANG>.txt dans ce dossier
(mêmes codes de langue que l'interface utilisateur du site Web). Aperçu en anglais : ce README.txt ;
Dépannage en anglais : FEHLERSUCHE_EN.txt. Le dépannage allemand est également
maintenu à la main sous le nom FEHLERSUCHE_DE.txt.

Index du dossier (nommage du fichier, générateur) : README.md

--------------------------------------------------------------------------------
  Système d'exploitation
--------------------------------------------------------------------------------

Evi Portable est uniquement destiné à Microsoft Windows 10 et Windows 11. Ce n'est pas
pris en charge sur Windows 7/8, macOS, Linux ou les systèmes d'exploitation mobiles.

--------------------------------------------------------------------------------
  Premier démarrage : du téléchargement à l'exécution d'Evi
--------------------------------------------------------------------------------

1) Emplacement d'installation
   Copiez ou extrayez l'intégralité du dossier Evi vers un endroit que vous contrôlez, par exemple
   votre bureau, vos documents ou une clé USB. Conservez la structure des dossiers telle que
   livré (ne supprimez pas les sous-dossiers que vous n'avez pas créés vous-même).

2) Modèle de langage (obligatoire)
   Evi a besoin d'un fichier de modèle d'IA principal (extension .gguf) dans le dossier :
   modèles\llm\
   Voir models\llm\README.txt pour les recommandations de taille. Une fois le fichier là,
   démarrez Evi ; il détecte le modèle automatiquement lorsque cela est possible.

3) Premier lancement – activation
   Lorsque vous démarrez Evi pour la première fois, une fenêtre d'activation apparaît.
   • Votre PC affiche un ID de machine (unique à ce matériel).
   • Copiez l'ID Machine (bouton : "Copier l'ID Machine") et envoyez-le par e-mail à :
     Brielbeck@hotmail.de
   • Vous recevrez une clé de série qui fonctionne uniquement sur ce même PC
     (la clé est liée à votre matériel).
   • Collez la clé dans la fenêtre d'activation et choisissez Activer.

   Si vous modifiez un matériel majeur ou déplacez le disque d'une manière qui modifie l'ID,
   vous aurez peut-être besoin d’une nouvelle clé – contactez la même adresse.

4) Après activation
   La fenêtre principale s'ouvre. Choisissez la langue, le microphone et la voix à gauche
   panneau de paramètres. Dites « ouvrez l'aide-mémoire » à tout moment pour obtenir des exemples de commandes.
   (voir les feuilles de triche\en.txt et les fichiers frères pour les autres langues).

5) Facultatif : ouvrez ce manuel depuis Windows
   Dans l'Explorateur de fichiers, accédez au dossier Evi, puis à Manual\README.txt et ouvrez-le.
   avec le Bloc-notes ou n'importe quelle visionneuse de texte.

--------------------------------------------------------------------------------
  Langage d'interface (GUI)
--------------------------------------------------------------------------------

L'interface utilisateur suit la langue que vous choisissez sous Langue en haut
du panneau de paramètres de gauche (premier bloc dans la barre latérale). Après avoir sélectionné un
la langue, les menus, les boutons, les étiquettes et la plupart des textes à l'écran y basculent
langue partout où des traductions existent. Vous pouvez le modifier à tout moment ; seulement le
le libellé change, pas la mise en page.

Astuce : Les feuilles de triche de commande dans le dossier cheatsheets\ sont répertoriées par
code de langue (en.txt, de.txt, …). Pour plus de détails, consultez les feuilles de triche\README.txt.
Ce dossier Manuel\ est la présentation la plus longue du produit ; les aide-mémoire sont les
liste rapide de « quoi dire ».

--------------------------------------------------------------------------------
  Carte graphique (GPU) – guide rapide
--------------------------------------------------------------------------------

Un bon choix intermédiaire est une NVIDIA GeForce RTX 4070 Ti avec 12 Go de vidéo
mémoire : bon équilibre entre vitesse, taille du contexte et espace pour des modèles plus grands.

Les cartes d’environ RTX 3060 à RTX 5090 peuvent bien fonctionner ; le meilleur ajustement dépend
sur la RAM, le processeur, le refroidissement et le fichier de modèle que vous installez. Utilisez le préréglage GPU dans
La barre latérale d'Evi pour correspondre à votre matériel.

L'exécution sur le CPU uniquement (les préréglages "CPU … GB RAM") constitue une solution de secours :
Evi reste utilisable sans carte graphique adaptée, mais les réponses sont beaucoup plus lentes.
Préférez un vrai GPU chaque fois que vous le pouvez.

--------------------------------------------------------------------------------
  Entièrement portable – lorsque vous avez besoin d'Internet
--------------------------------------------------------------------------------

Evi est conçu pour être portable : copiez l'intégralité du dossier sur un autre lecteur, une clé USB,
ou PC, puis démarrez-le là. Chats, souvenirs, paramètres, données de sécurité et votre
Le fichier d'activation reste normalement dans ce dossier (l'activation est liée au
PC, pas le chemin du dossier).

Internet est principalement destiné aux éléments que vous choisissez de télécharger (fichiers de modèles, fichiers facultatifs).
voix ou extras, mises à jour) et pour des fonctionnalités optionnelles telles que la recherche sur le Web, la messagerie,
le streaming ou la météo lorsque vous autorisez l’accès au réseau.

Chat principal, mémoire, notes, minuteries, outils de fichiers dans votre dossier autorisé, local
la reconnaissance vocale, la sortie vocale locale et le verrouillage de confidentialité fonctionnent sur votre
machine sans envoyer vos conversations à un service cloud. En ligne en option
les fonctionnalités ne s'exécutent que lorsque l'accès au réseau est activé et que vous les utilisez.

--------------------------------------------------------------------------------
  Sécurité : PIN et déverrouillage vocal (anti-copie)
--------------------------------------------------------------------------------

Evi peut utiliser un code PIN de sécurité et une inscription vocale facultative sur votre appareil.

Lorsque le déverrouillage vocal est utilisé, chaque tentative peut demander un court ensemble de mots aléatoires
cela change à chaque fois – pas une phrase fixe pour toujours. Cela bloque le facile
astuce consistant à rejouer un seul ancien enregistrement de votre voix. Votre code PIN reste un
ligne de défense distincte.

Ceci est conçu pour mettre fin aux abus occasionnels ; aucun produit de consommation ne peut promettre
perfection contre chaque attaque (par exemple quelqu'un qui a à la fois votre code PIN et votre
mimétisme vocal sophistiqué). Gardez votre code PIN privé et complétez la configuration comme
l'application vous guide.

--------------------------------------------------------------------------------
  Dépannage (courte liste de contrôle)
--------------------------------------------------------------------------------

• Aucune réponse IA/erreur de modèle
  → Au moins un .gguf approprié dans models\llm\ ? Voir models\llm\README.txt.
  → Essayez un modèle plus petit ou un préréglage CPU dans la barre latérale si le chemin GPU échoue.

• Pas de microphone
  → Paramètres son Windows : testez le micro. Dans Evi, sélectionnez l'appareil sous
    Microphone et Enregistrer.

• Aucune sortie vocale
  → Vérifiez que les fichiers vocaux pour votre langue existent dans le dossier piper\ et
    choisissez une voix dans la barre latérale.

• Échec du Web ou de YouTube
  → Désactivez « Bloquer tout le trafic » dans la barre latérale si vous souhaitez des fonctionnalités en ligne.
  → Pour la lecture YouTube, VLC Portable et un accès réseau sont généralement requis.

• Après avoir modifié les aide-mémoire
  → Redémarrez Evi pour que tous les assistants de texte reprennent les modifications de manière fiable.

--------------------------------------------------------------------------------
  Dépannage (référence étendue)
--------------------------------------------------------------------------------

Vérifications rapides (toujours en premier)
  • Windows 10 ou 11 64 bits, mis à jour, redémarré après de gros changements ?
  • Evi exécuté à partir d'un dossier entièrement extrait — et non à partir d'une archive ?
  • Évitez les dossiers synchronisés avec le cloud (OneDrive, etc.) pour le dossier de données en direct lorsque
    Evi s'exécute — utilisez un chemin local tel que C:\EviPortable ou D:\Tools\Evi lorsque
    possibles.
  • Assez d'espace disque libre pour le modèle, les discussions et les mises à jour ?
  • Après avoir changé de modèle, de voix ou d'aide-mémoire : quittez complètement Evi et démarrez
    encore une fois.

1) Système d'exploitation
  • Evi est uniquement destiné à Windows 10 et 11 ; les autres versions du système d'exploitation ne sont pas prises en charge.
  • Si l'application ne démarre pas du tout, extrayez complètement le package, vérifiez l'antivirus.
    journaux pour les exécutables bloqués et essayez un chemin d'installation plus court sans rare
    Caractères Unicode uniquement.

2) Chemin du dossier, antivirus, portabilité
  • Ajoutez une exclusion pour votre dossier racine Evi dans le logiciel de sécurité si les analyses effectuent
    démarrage très lent ou verrouillage des fichiers pendant les téléchargements.
  • Clés USB : préférez USB 3 + NTFS ; les médias très lents rendent les grands modèles pénibles.

3) Modèle de langage (.gguf)
  • Symptômes : pas de réponse, erreurs de modèle, échec instantané du chargement.
  • correctifs : vérifiez que models\llm\ contient un .gguf complet (et non 0 octet) ; retélécharger
si nécessaire ; faire correspondre la taille du modèle à la VRAM à l'aide de models\llm\README.txt ; en cas de doute,
    conservez un seul fichier q4_k_m testé dans le dossier.
  • plusieurs fichiers .gguf : Evi peut choisir le plus grand qui correspond à votre VRAM — si vous
    suspectez un conflit, testez avec un seul fichier.

4) GPU, CUDA, pilotes, manque de mémoire
  • Mettez à jour le pilote NVIDIA ; sur les ordinateurs portables, forcez le GPU/performance discret
    mode pour Evi là où Windows le permet.
  • Si vous constatez des pannes de MOO ou de GPU, utilisez un point de contrôle plus petit, fermez les autres applications GPU,
    baissez la température ou passez à un préréglage du processeur (plus lent mais plus stable).

5) Mode CPU uniquement
  • On s'attend à ce que ce soit lent ; libérer suffisamment de RAM système ; fermer les tâches lourdes en arrière-plan ;
    utiliser le plan d'alimentation "Hautes performances" lors de longues sessions.

6)Activation
  • Collez soigneusement les clés (sans espaces supplémentaires) ; les clés sont liées à un seul ID de machine.
  • Après des modifications matérielles majeures, vous aurez peut-être besoin d'une clé de remplacement : utilisez le support
    adresse avec vos coordonnées.

7) Micro
  • Confidentialité Windows → Microphone → autoriser les applications de bureau.
  • Définissez le périphérique d'enregistrement par défaut correct ; dans Evi, choisissez le même appareil et enregistrez.
  • Les casques Bluetooth peuvent ajouter de la latence : testez avec un microphone USB en cas de doute.
  • Une autre application peut proposer un mode exclusif : fermez temporairement le logiciel de réunion.

8) Reconnaissance vocale (locale)
  • Si la reconnaissance ne se termine jamais, assurez-vous que les fichiers de modèle sous models\whisper sont
    intact et autorisez le réseau lors des premières récupérations de modèle si votre build en a besoin.

9) Sortie vocale (Piper / TTS)
  • Confirmez que piper\ contient un pack vocal pour la langue de votre interface utilisateur ; choisissez une voix dans
    la barre latérale ; vérifiez le mélangeur de volume Windows – Evi peut être désactivé par application.

10) Réseau et "Bloquer tout le trafic"
  • Désactivez le blocage du Web, des assistants de messagerie, de la météo ou des téléchargements.
  • Les proxys d'entreprise ou les VPN peuvent nécessiter une aide informatique pour les listes autorisées.

11) YouTube et médias
  • Conservez la disposition VLC Portable fournie ; activer l'accès au réseau ; lire
    Portable\VLCPortable guidage si le chemin a été déplacé.

12) Langue de l'interface utilisateur et aide-mémoire
  • Les aide-mémoire sont par fichier de langue sous cheatsheets\ — voir cheatsheets\README.txt.
  • Enregistrez les modifications au format UTF-8 ; redémarrez Evi après les modifications.

13) Sécurité (PIN / déverrouillage vocal)
  • Utilisez un environnement calme; revérifiez le gain du microphone ; ne partagez jamais votre code PIN.
  • Les invites de mots aléatoires sont intentionnelles : les anciens enregistrements vocaux ne doivent pas se déverrouiller.

14) Performances, blocages, plantages
  • Réduisez la taille du modèle, améliorez le refroidissement, lisez tout crash.log dans l'arborescence si votre
    build en crée un et annule la dernière modification que vous avez apportée avant l'échec.

15) Lorsque vous contactez le support
  • Inclure l'ID de la machine, la version de Windows, le modèle de GPU + la VRAM + le pilote, dont .gguf
    que vous utilisez et le texte d'erreur exact (pas les clés secrètes).

Référence de dépannage complète (cette langue) : Manual\FEHLERSUCHE_FR.txt

--------------------------------------------------------------------------------
  Prise en charge : clés de série et ID de machine
--------------------------------------------------------------------------------

E-mail : Brielbeck@hotmail.de
Incluez toujours votre ID de machine à partir de l'écran d'activation lorsque vous demandez un
clé de série ou une clé de remplacement après des modifications matérielles.

===============================================================================