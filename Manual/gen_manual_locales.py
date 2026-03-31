# -*- coding: utf-8 -*-
"""Generate README_<LANG>.txt and FEHLERSUCHE_<LANG>.txt from English sources.

Requires: pip install deep-translator network access.

Preserves existing FEHLERSUCHE_DE.txt (does not overwrite with machine translation).
"""
from __future__ import annotations

import os
import time

import requests

TRANSLATE_TIMEOUT_SEC = (20, 150)
_ORIG_REQUESTS_GET = requests.get

FEH_TOKEN = "FEHFILE_REF"
MAX_CHUNK = 4200

MANUAL_DIR = os.path.dirname(os.path.abspath(__file__))


def _requests_get_with_timeout(*args, **kwargs):
    kwargs.setdefault("timeout", TRANSLATE_TIMEOUT_SEC)
    return _ORIG_REQUESTS_GET(*args, **kwargs)


try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("Run: pip install deep-translator")
    raise

# Same language codes as Evi_Page/gen_evi_locales.py, plus DE (hand FEHLERSUCHE on disk).
MANUAL_LANGS = [
    ("DE", "de"),
    ("JA", "ja"),
    ("KO", "ko"),
    ("ZH", "zh-CN"),
    ("ZH-TW", "zh-TW"),
    ("ES", "es"),
    ("FR", "fr"),
    ("IT", "it"),
    ("PT", "pt"),
    ("PT-BR", "pt"),
    ("RU", "ru"),
    ("UK", "uk"),
    ("PL", "pl"),
    ("NL", "nl"),
    ("SV", "sv"),
    ("DA", "da"),
    ("NO", "no"),
    ("FI", "fi"),
    ("CS", "cs"),
    ("SK", "sk"),
    ("RO", "ro"),
    ("HU", "hu"),
    ("EL", "el"),
    ("TR", "tr"),
    ("AR", "ar"),
    ("VI", "vi"),
]


def split_chunks(text: str) -> list[str]:
    lines = text.split("\n")
    chunks: list[str] = []
    buf: list[str] = []
    n = 0
    for line in lines:
        line_len = len(line) + 1
        if n + line_len > MAX_CHUNK and buf:
            chunks.append("\n".join(buf))
            buf = [line]
            n = line_len
        else:
            buf.append(line)
            n += line_len
    if buf:
        chunks.append("\n".join(buf))
    return chunks


def translate_plain(tr: GoogleTranslator, text: str) -> str:
    if not text.strip():
        return text
    parts: list[str] = []
    for ch in split_chunks(text):
        t = None
        for attempt in range(4):
            try:
                t = tr.translate(ch)
                break
            except Exception as e:
                msg = str(e).encode("ascii", "replace").decode("ascii")
                print("  translate error:", msg[:160], flush=True)
                time.sleep(1.4 * (attempt + 1))
        parts.append(t if t is not None else ch)
        time.sleep(0.05)
    return "\n".join(parts)


def post_replace_feh_ref(s: str, code: str) -> str:
    fe_path = f"Manual\\FEHLERSUCHE_{code}.txt"
    out = s.replace(FEH_TOKEN, fe_path)
    if FEH_TOKEN not in s and fe_path not in s:
        for guess in ("FEHFILE REF", "FEHFILE-REF", "fehfile_ref"):
            out = out.replace(guess, fe_path)
    return out


def main() -> None:
    requests.get = _requests_get_with_timeout
    readme_path = os.path.join(MANUAL_DIR, "README.txt")
    fe_en_path = os.path.join(MANUAL_DIR, "FEHLERSUCHE_EN.txt")
    fe_de_path = os.path.join(MANUAL_DIR, "FEHLERSUCHE_DE.txt")

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_en = f.read()
    with open(fe_en_path, "r", encoding="utf-8") as f:
        fe_en = f.read()

    for code, gtarget in MANUAL_LANGS:
        print("===", code, gtarget, flush=True)
        readme_dest = os.path.join(MANUAL_DIR, f"README_{code}.txt")
        fe_dest = os.path.join(MANUAL_DIR, f"FEHLERSUCHE_{code}.txt")

        if code == "PT-BR":
            pt_readme = os.path.join(MANUAL_DIR, "README_PT.txt")
            pt_fe = os.path.join(MANUAL_DIR, "FEHLERSUCHE_PT.txt")
            with open(pt_readme, "r", encoding="utf-8") as f:
                readme_out = f.read()
            readme_out = readme_out.replace(
                "FEHLERSUCHE_PT.txt", "FEHLERSUCHE_PT-BR.txt"
            )
            with open(readme_dest, "w", encoding="utf-8", newline="\n") as f:
                f.write(readme_out)
            print("  wrote", os.path.basename(readme_dest), "(from PT)", flush=True)
            with open(pt_fe, "r", encoding="utf-8") as f:
                fe_br = f.read()
            with open(fe_dest, "w", encoding="utf-8", newline="\n") as f:
                f.write(fe_br)
            print("  wrote", os.path.basename(fe_dest), "(from PT)", flush=True)
            time.sleep(0.35)
            continue

        tr = GoogleTranslator(source="en", target=gtarget)

        readme_out = translate_plain(tr, readme_en)
        readme_out = post_replace_feh_ref(readme_out, code)
        with open(readme_dest, "w", encoding="utf-8", newline="\n") as f:
            f.write(readme_out)
        print("  wrote", os.path.basename(readme_dest), flush=True)

        if code == "DE" and os.path.isfile(fe_de_path):
            print("  keep FEHLERSUCHE_DE.txt (hand-crafted)", flush=True)
        else:
            fe_out = translate_plain(tr, fe_en)
            with open(fe_dest, "w", encoding="utf-8", newline="\n") as f:
                f.write(fe_out)
            print("  wrote", os.path.basename(fe_dest), flush=True)

        time.sleep(0.35)

    print("Done.", flush=True)


if __name__ == "__main__":
    main()
