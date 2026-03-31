/* German manual + merge for flag locales. Regenerate full UI: python gen_evi_locales.py */
(function () {
  var MANUAL_DE_HTML = "<h2 class=\"section-title\">Evi Portable &mdash; Benutzerhandbuch (&Uuml;berblick)</h2>\n    <p class=\"manual-lead\">Dieser &Uuml;berblick entspricht <strong>Manual\\README.txt</strong> in Ihrem Build. Er ist zum Lesen oder Ausdrucken; Evi l&auml;uft auch ohne ihn.</p>\n    <div class=\"manual-block\">\n      <h3>Betriebssystem</h3>\n      <p>Evi Portable ist nur f&uuml;r <strong>Microsoft Windows 10 und Windows 11</strong>. Andere Systeme werden nicht unterst&uuml;tzt.</p>\n    </div>\n    <div class=\"manual-block\">\n      <h3>Erster Start</h3>\n      <ol>\n        <li><strong>Ordner.</strong> Gesamten Evi-Ordner kopieren (Desktop, USB). Struktur beibehalten.</li>\n        <li><strong>Programm.</strong> <strong>Evi Portable laden</strong> oder Download-Karte auf <a href=\"https://toscano8070.github.io/Evi-Portable/#download-pack\">dieser Seite</a>. Archiv = App ohne Haupt-LLM.</li>\n        <li><strong>KI-Modell.</strong> <strong>Eine</strong> <code>.gguf</code> nach <code>models\\llm\\</code>. Auf GGUF-Download klicken wenn verlinkt. Siehe <code>models\\llm\\README.txt</code>.</li>\n      </ol>\n      <p class=\"manual-callout\"><strong>Richtiges Modell:</strong> <strong>Genau eine</strong> passende <code>.gguf</code> in <code>models\\llm\\</code>, dann starten.</p>\n      <p style=\"margin-top:1rem\"><a href=\"#manual-llm\" class=\"btn btn-outline btn-muted evi-llm-download\" data-evi-url=\"llm\">KI-Modell herunterladen (GGUF)</a></p>\n      <div class=\"dl-llm-heavy dl-llm-heavy--manual\" role=\"alert\">\n        <p class=\"dl-llm-heavy__title\">&#9888;&#65039; Nur High-End-NVIDIA-GPUs</p>\n        <p class=\"dl-llm-heavy__body\">14B-GGUF <a class=\"dl-llm-heavy__dl evi-llm-download\" data-evi-url=\"llm\" href=\"#manual-llm\"><code>qwen2.5-14b-instruct-q4_k_m.gguf</code></a> &mdash; nur mit viel VRAM. Sonst normalen LLM-Download und <code>models\\llm\\README.txt</code>.</p>\n      </div>\n      <ol start=\"4\">\n        <li><strong>Aktivierung.</strong> <strong>Machine ID</strong> an <a href=\"mailto:Brielbeck@hotmail.de?subject=Evi%20Portable%20-%20Machine%20ID\">Brielbeck@hotmail.de</a>.</li>\n        <li><strong>Danach:</strong> Sprache, Mikrofon, Stimme w&auml;hlen.</li>\n        <li><strong>Lokal:</strong> <code>Manual\\README.txt</code> im Explorer.</li>\n      </ol>\n    </div>\n    <div class=\"manual-block\"><h3>GUI-Sprache</h3><p><strong>Language</strong> in der linken Leiste.</p></div>\n    <div class=\"manual-block\"><h3>GPU</h3><p>RTX-4070-Klasse empfohlen. GPU-Preset w&auml;hlen.</p></div>\n    <div class=\"manual-block\"><h3>Portabel</h3><p>Lizenz am <strong>PC</strong> gebunden.</p></div>\n    <div class=\"manual-block\"><h3>Sicherheit</h3><p>PIN und Sprach-Unlock mit Zufallsw&ouml;rtern.</p></div>\n    <div class=\"manual-block\"><h3>Fehlersuche</h3><ul><li><strong>Keine KI:</strong> <code>models\\llm\\</code> pr&uuml;fen.</li><li><strong>Mikrofon:</strong> Windows / Evi.</li><li><strong>Stimme:</strong> <code>piper\\</code>.</li><li><strong>Web:</strong> &bdquo;Block all traffic&ldquo; aus.</li></ul></div>\n    <div class=\"manual-block\"><h3>Support</h3><p><a href=\"mailto:Brielbeck@hotmail.de?subject=Evi%20Portable%20-%20Machine%20ID\">Brielbeck@hotmail.de</a></p></div>";

  window.applyEviLocaleBundle = function (I18N) {
    if (!I18N || !I18N.EN) return;
    if (I18N.DE && MANUAL_DE_HTML) I18N.DE.manual_html = MANUAL_DE_HTML;
    function mergeFromEn(patch) {
      var o = {}, k;
      for (k in I18N.EN) {
        if (Object.prototype.hasOwnProperty.call(I18N.EN, k)) o[k] = I18N.EN[k];
      }
      for (k in patch) {
        if (Object.prototype.hasOwnProperty.call(patch, k)) o[k] = patch[k];
      }
      return o;
    }
    if (typeof window.EVI_MT_LOCALES === "object" && window.EVI_MT_LOCALES) {
      var c;
      for (c in window.EVI_MT_LOCALES) {
        if (Object.prototype.hasOwnProperty.call(window.EVI_MT_LOCALES, c)) {
          I18N[c] = mergeFromEn(window.EVI_MT_LOCALES[c]);
        }
      }
    }
  };
})();
