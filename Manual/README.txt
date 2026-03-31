================================================================================
  Evi Portable — User manual (overview)
  Document: English • Applies to the build you received with this folder
================================================================================

Put your own longer guides or translations here too (e.g. EN_User_Manual.pdf,
DE_Handbuch.txt). This file is optional for Evi to run; it is for you to read
or print.

Localized copies: README_<LANG>.txt and FEHLERSUCHE_<LANG>.txt in this folder
(same language codes as the website UI). English overview: this README.txt;
English troubleshooting: FEHLERSUCHE_EN.txt. German troubleshooting is also
maintained by hand as FEHLERSUCHE_DE.txt.

Folder index (file naming, generator): README.md

--------------------------------------------------------------------------------
  Operating system
--------------------------------------------------------------------------------

Evi Portable is for Microsoft Windows 10 and Windows 11 only. It is not
supported on Windows 7/8, macOS, Linux, or mobile operating systems.

--------------------------------------------------------------------------------
  First start — from download to running Evi
--------------------------------------------------------------------------------

1) Install location
   Copy or extract the whole Evi folder to a place you control — for example
   your Desktop, Documents, or a USB stick. Keep the folder structure as
   delivered (do not delete subfolders you did not create yourself).

2) Language model (required)
   Evi needs one main AI model file (extension .gguf) in the folder:
   models\llm\
   See models\llm\README.txt for size recommendations. After the file is there,
   start Evi; it detects the model automatically when possible.

3) First launch — activation
   When you start Evi the first time, an activation window appears.
   • Your PC shows a Machine ID (unique to this hardware).
   • Copy the Machine ID (button: "Copy Machine ID") and send it by e-mail to:
     Brielbeck@hotmail.de
   • You will receive a serial key that works only on that same PC
     (the key is bound to your hardware).
   • Paste the key into the activation window and choose Activate.

   If you change major hardware or move the disk in a way that changes the ID,
   you may need a new key — contact the same address.

4) After activation
   The main window opens. Choose language, microphone, and voice in the left
   settings panel. Say "open the cheat sheet" anytime for command examples
   (see cheatsheets\en.txt and sister files for other languages).

5) Optional: open this manual from Windows
   In File Explorer go to the Evi folder, then Manual\README.txt, and open it
   with Notepad or any text viewer.

--------------------------------------------------------------------------------
  Interface language (GUI)
--------------------------------------------------------------------------------

The user interface follows the language you choose under Language at the top
of the left settings panel (first block in the sidebar). After you select a
language, menus, buttons, labels, and most on-screen text switch to that
language wherever translations exist. You can change it any time; only the
wording changes, not the layout.

Tip: The command cheat sheets in the cheatsheets\ folder are listed per
language code (en.txt, de.txt, …). For details see cheatsheets\README.txt.
This Manual\ folder is the longer product overview; cheat sheets are the
quick "what to say" list.

--------------------------------------------------------------------------------
  Graphics card (GPU) — quick guide
--------------------------------------------------------------------------------

A strong middle choice is an NVIDIA GeForce RTX 4070 Ti with 12 GB of video
memory: good balance of speed, context size, and room for larger models.

Cards from about RTX 3060 through RTX 5090 can work well; the best fit depends
on RAM, CPU, cooling, and which model file you install. Use the GPU preset in
Evi's sidebar to match your hardware.

Running on the CPU only (the "CPU … GB RAM" presets) is an emergency fallback:
Evi stays usable without a suitable graphics card, but answers are much slower.
Prefer a real GPU whenever you can.

--------------------------------------------------------------------------------
  Fully portable — when you need the Internet
--------------------------------------------------------------------------------

Evi is built to be portable: copy the whole folder to another drive, USB stick,
or PC, then start it there. Chats, memories, settings, security data, and your
activation file normally stay inside that folder (activation is tied to the
PC, not the folder path).

The Internet is mainly for things you choose to download (model files, optional
voices or extras, updates) and for optional features like web search, mail,
streaming, or weather when you allow network access.

Core chat, memory, notes, timers, file tools inside your allowed folder, local
speech recognition, local voice output, and the privacy lock run on your
machine without sending your conversations to a cloud service. Optional online
features only run when network access is on and you use them.

--------------------------------------------------------------------------------
  Security: PIN and voice unlock (anti-copy)
--------------------------------------------------------------------------------

Evi can use a security PIN and optional voice enrolment on your device.

When voice unlock is used, each attempt can ask for a short set of random words
that changes every time — not one fixed phrase forever. That blocks the easy
trick of replaying a single old recording of your voice. Your PIN remains a
separate line of defence.

This is designed to stop casual abuse; no consumer product can promise
perfection against every attack (for example someone who has both your PIN and
sophisticated voice mimicry). Keep your PIN private and complete setup as the
app guides you.

--------------------------------------------------------------------------------
  Troubleshooting (short checklist)
--------------------------------------------------------------------------------

• No AI answers / model error
  → At least one suitable .gguf in models\llm\ ? See models\llm\README.txt.
  → Try a smaller model or a CPU preset in the sidebar if the GPU path fails.

• No microphone
  → Windows sound settings: test the mic. In Evi, pick the device under
    Microphone and Save.

• No voice output
  → Check that voice files for your language exist in the piper\ folder and
    pick a voice in the sidebar.

• Web or YouTube fails
  → Turn off "Block all traffic" in the sidebar if you want online features.
  → For YouTube playback, VLC Portable and network access are usually required.

• After editing cheat sheets
  → Restart Evi so all text helpers pick up changes reliably.

--------------------------------------------------------------------------------
  Troubleshooting (extended reference)
--------------------------------------------------------------------------------

Quick checks (always first)
  • Windows 10 or 11 64-bit, updated, rebooted after big changes?
  • Evi running from a fully extracted folder — not from inside an archive?
  • Avoid cloud-synced folders (OneDrive, etc.) for the live data folder while
    Evi runs — use a local path such as C:\EviPortable or D:\Tools\Evi when
    possible.
  • Enough free disk space for the model, chats, and updates?
  • After changing models, voices, or cheat sheets: exit Evi completely and start
    again.

1) Operating system
  • Evi is for Windows 10 and 11 only; other OS versions are unsupported.
  • If the app will not start at all, fully extract the package, check antivirus
    logs for blocked executables, and try a shorter install path without rare
    Unicode-only characters.

2) Folder path, antivirus, portability
  • Add an exclusion for your Evi root folder in security software if scans make
    startup very slow or lock files during downloads.
  • USB sticks: prefer USB 3 + NTFS; very slow media make large models painful.

3) Language model (.gguf)
  • symptoms: no replies, model errors, instant failure to load.
  • fixes: verify models\llm\ contains a complete .gguf (not 0 bytes); re-download
    if needed; match model size to VRAM using models\llm\README.txt; if unsure,
    keep a single tested q4_k_m file in the folder.
  • multiple .gguf files: Evi can pick the largest that fits your VRAM — if you
    suspect a conflict, test with only one file.

4) GPU, CUDA, drivers, out-of-memory
  • Update the NVIDIA driver; on laptops, force the discrete GPU / performance
    mode for Evi where Windows allows.
  • If you see OOM or GPU crashes, use a smaller checkpoint, close other GPU apps,
    lower temperature, or switch to a CPU preset (slower but steadier).

5) CPU-only mode
  • Expected to be slow; free enough system RAM; close heavy background tasks;
    use power plan "High performance" during long sessions.

6) Activation
  • Paste keys carefully (no extra spaces); keys are tied to one Machine ID.
  • After major hardware changes you may need a replacement key — use the support
    address with your details.

7) Microphone
  • Windows Privacy → Microphone → allow desktop apps.
  • Set the correct default recording device; in Evi choose the same device and Save.
  • Bluetooth headsets can add latency — test with a USB microphone if unsure.
  • Another app may hold exclusive mode — close meeting software temporarily.

8) Speech recognition (local)
  • If recognition never finishes, ensure model files under models\whisper are
    intact and allow network on first-time model fetches if your build needs it.

9) Voice output (Piper / TTS)
  • Confirm piper\ contains a voice pack for your UI language; pick a voice in
    the sidebar; check Windows volume mixer — Evi may be muted per-app.

10) Network and "Block all traffic"
  • Turn the block off for web, mail helpers, weather, or downloads.
  • Corporate proxies or VPNs may require IT help for allowlists.

11) YouTube and media
  • Keep the bundled VLC Portable layout; enable network access; read
    Portable\VLCPortable guidance if the path was moved.

12) UI language and cheat sheets
  • Cheat sheets are per language file under cheatsheets\ — see cheatsheets\README.txt.
  • Save edits as UTF-8; restart Evi after edits.

13) Security (PIN / voice unlock)
  • Use a quiet environment; re-check microphone gain; never share your PIN.
  • Random-word prompts are intentional — old voice recordings should not unlock.

14) Performance, freezes, crashes
  • Reduce model size, improve cooling, read any crash.log in the tree if your
    build creates one, and roll back the last change you made before failures.

15) When contacting support
  • Include Machine ID, Windows version, GPU model + VRAM + driver, which .gguf
    you use, and the exact error text (not secret keys).

Full troubleshooting reference (this language): FEHFILE_REF

--------------------------------------------------------------------------------
  Support — serial keys and Machine ID
--------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Always include your Machine ID from the activation screen when requesting a
serial key or a replacement key after hardware changes.

================================================================================
