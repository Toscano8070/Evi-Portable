# Evi Portable — `Manual` folder

This folder holds the **text user manual** and the **extended troubleshooting** reference. Evi does not require these files to run; they are for reading or printing.

## Files

| Pattern | Purpose |
|--------|---------|
| **README.txt** | English overview (canonical source for translations). |
| **`README_<LANG>.txt`** | Same manual in another language (machine-translated except where noted). |
| **FEHLERSUCHE_EN.txt** | English extended troubleshooting. |
| **FEHLERSUCHE_DE.txt** | German extended troubleshooting (maintained by hand). |
| **`FEHLERSUCHE_<LANG>.txt`** | Same troubleshooting in other languages (machine-translated; DE is not overwritten). |

**Language codes** match the Evi website locales, for example: `DE`, `JA`, `KO`, `ZH`, `ZH-TW`, `ES`, `FR`, `IT`, `PT`, `PT-BR`, `RU`, `UK`, `PL`, `NL`, `SV`, `DA`, `NO`, `FI`, `CS`, `SK`, `RO`, `HU`, `EL`, `TR`, `AR`, `VI`.

Paths inside the manuals use Windows-style backslashes (`models\llm\`, etc.) as in the app.

## Regenerating translated `.txt` files

Requires Python, `pip install deep-translator`, and network access:

```bash
python gen_manual_locales.py
```

This refreshes all `README_<LANG>.txt` and `FEHLERSUCHE_<LANG>.txt` from `README.txt` and `FEHLERSUCHE_EN.txt`, and **does not replace** `FEHLERSUCHE_DE.txt`.

---

*Kurz (DE): Siehe `README.txt` (EN) bzw. `README_DE.txt` — Fehlersuche „lang“: `FEHLERSUCHE_DE.txt` oder `FEHLERSUCHE_<SPRACHE>.txt`.*
