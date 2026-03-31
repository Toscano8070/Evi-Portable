=================================================================================
  Evi Portable — Instrukcja obsługi (przegląd)
  Dokument: angielski • Dotyczy kompilacji otrzymanej w tym folderze
=================================================================================

Tutaj też możesz umieścić swoje dłuższe poradniki lub tłumaczenia (np. EN_User_Manual.pdf,
DE_Handbuch.txt). Uruchomienie tego pliku jest opcjonalne dla Evi; to dla ciebie do przeczytania
lub wydrukuj.

Zlokalizowane kopie: README_<LANG>.txt i FEHLERSUCHE_<LANG>.txt w tym folderze
(te same kody językowe, co interfejs użytkownika witryny). Przegląd w języku angielskim: ten plik README.txt;
Rozwiązywanie problemów w języku angielskim: FEHLERSUCHE_EN.txt. Rozwiązywanie problemów w języku niemieckim jest również możliwe
utrzymywany ręcznie jako FEHLERSUCHE_DE.txt.

Indeks folderów (nazewnictwo plików, generator): README.md

--------------------------------------------------------------------------------
  System operacyjny
--------------------------------------------------------------------------------

Evi Portable jest przeznaczony wyłącznie dla systemów Microsoft Windows 10 i Windows 11. Tak nie jest
obsługiwane w systemach Windows 7/8, macOS, Linux i mobilnych systemach operacyjnych.

--------------------------------------------------------------------------------
  Pierwsze uruchomienie — od pobrania do uruchomienia Evi
--------------------------------------------------------------------------------

1) Zainstaluj lokalizację
   Skopiuj lub wyodrębnij cały folder Evi do kontrolowanego przez Ciebie miejsca — na przykład
   na pulpicie, dokumentach lub pamięci USB. Zachowaj strukturę folderów jako
   dostarczone (nie usuwaj podfolderów, których sam nie utworzyłeś).

2) Model językowy (wymagane)
   Evi potrzebuje jednego głównego pliku modelu AI (rozszerzenie .gguf) w folderze:
   modele\llm\
   Zalecenia dotyczące rozmiaru można znaleźć w pliku models\llm\README.txt. Po znalezieniu się pliku
   uruchom Evi; wykrywa model automatycznie, jeśli to możliwe.

3) Pierwsze uruchomienie — aktywacja
   Przy pierwszym uruchomieniu Evi pojawi się okno aktywacji.
   • Twój komputer wyświetla identyfikator maszyny (unikalny dla tego sprzętu).
   • Skopiuj ID maszyny (przycisk: „Kopiuj ID maszyny”) i wyślij go e-mailem na adres:
     Brielbeck@hotmail.de
   • Otrzymasz klucz seryjny, który działa tylko na tym samym komputerze
     (klucz jest powiązany ze sprzętem).
   • Wklej klucz w oknie aktywacji i wybierz Aktywuj.

   Jeśli zmienisz główny sprzęt lub przeniesiesz dysk w sposób powodujący zmianę identyfikatora,
   możesz potrzebować nowego klucza — skontaktuj się pod tym samym adresem.

4) Po aktywacji
   Otworzy się główne okno. Wybierz język, mikrofon i głos po lewej stronie
   panelu ustawień. W dowolnym momencie możesz powiedzieć „otwórz ściągawkę”, aby zobaczyć przykłady poleceń
   (zobacz ściągawki\en.txt i pliki siostrzane dla innych języków).

5) Opcjonalnie: otwórz tę instrukcję w systemie Windows
   W Eksploratorze plików przejdź do folderu Evi, następnie Manual\README.txt i otwórz go
   za pomocą Notatnika lub dowolnej przeglądarki tekstu.

--------------------------------------------------------------------------------
  Język interfejsu (GUI)
--------------------------------------------------------------------------------

Interfejs użytkownika jest zgodny z językiem wybranym w obszarze Język u góry
lewego panelu ustawień (pierwszy blok na pasku bocznym). Po wybraniu
język, menu, przyciski, etykiety i większość tekstu na ekranie przełączają się na ten język
wszędzie tam, gdzie istnieją tłumaczenia. Możesz to zmienić w dowolnym momencie; tylko
zmiany brzmienia, a nie układu.

Wskazówka: Lista poleceń ściągawki w folderze cheatsheets\ jest wyświetlana według
kod języka (en.txt, de.txt,…). Aby uzyskać szczegółowe informacje, zobacz ściągawki\README.txt.
Ten folder Manual\ stanowi dłuższy przegląd produktu; ściągawki są
szybka lista „co powiedzieć”.

--------------------------------------------------------------------------------
  Karta graficzna (GPU) — krótki przewodnik
--------------------------------------------------------------------------------

Mocnym środkowym wyborem jest karta NVIDIA GeForce RTX 4070 Ti z 12 GB pamięci wideo
pamięć: dobra równowaga szybkości, rozmiaru kontekstu i miejsca na większe modele.

Karty od około RTX 3060 do RTX 5090 mogą działać dobrze; zależy od najlepszego dopasowania
na temat pamięci RAM, procesora, chłodzenia i pliku modelu, który instalujesz. Użyj ustawień wstępnych GPU w
Pasek boczny Evi pasujący do Twojego sprzętu.

Uruchamianie wyłącznie na procesorze (ustawienia wstępne „CPU… GB RAM”) jest rozwiązaniem awaryjnym:
Evi pozostaje użyteczny bez odpowiedniej karty graficznej, ale odpowiedzi są znacznie wolniejsze.
Kiedy tylko możesz, preferuj prawdziwy procesor graficzny.

--------------------------------------------------------------------------------
  W pełni przenośny — gdy potrzebujesz Internetu
--------------------------------------------------------------------------------

Evi jest przenośny: skopiuj cały folder na inny dysk, pamięć USB,
lub PC, a następnie uruchom go tam. Czaty, wspomnienia, ustawienia, dane bezpieczeństwa i Twoje
plik aktywacyjny zwykle pozostaje w tym folderze (aktywacja jest powiązana z plikiem
PC, a nie ścieżka folderu).

Internet służy głównie do pobierania plików (pliki modeli, opcjonalnie
głosy lub dodatki, aktualizacje) oraz dla funkcji opcjonalnych, takich jak wyszukiwanie w Internecie, poczta,
przesyłanie strumieniowe lub pogoda, jeśli zezwolisz na dostęp do sieci.

Podstawowy czat, pamięć, notatki, liczniki czasu, narzędzia do plików w dozwolonym folderze, lokalnie
rozpoznawanie mowy, lokalne wyjście głosowe i blokada prywatności działają na Twoim urządzeniu
maszynę bez wysyłania rozmów do usługi w chmurze. Opcjonalnie w Internecie
funkcje działają tylko wtedy, gdy dostęp do sieci jest włączony i używasz ich.

--------------------------------------------------------------------------------
  Bezpieczeństwo: odblokowanie PIN-em i głosem (zabezpieczenie przed kopiowaniem)
--------------------------------------------------------------------------------

Evi może używać zabezpieczającego kodu PIN i opcjonalnej rejestracji głosu na Twoim urządzeniu.

Gdy używane jest odblokowanie głosowe, przy każdej próbie może zostać wyświetlony monit o podanie krótkiego zestawu losowych słów
to zmienia się za każdym razem — nie jest to jedno stałe zdanie na zawsze. To blokuje łatwe
sztuczka polegająca na odtworzeniu jednego, starego nagrania Twojego głosu. Twój PIN pozostaje
osobna linia obrony.

Ma to na celu powstrzymanie przypadkowych nadużyć; żaden produkt konsumencki nie jest w stanie tego obiecać
perfekcja przed każdym atakiem (na przykład ktoś, kto ma zarówno Twój PIN, jak i
wyrafinowana mimikra głosu). Zachowaj prywatność swojego kodu PIN i zakończ konfigurację jako
aplikacja Cię poprowadzi.

--------------------------------------------------------------------------------
  Rozwiązywanie problemów (krótka lista kontrolna)
--------------------------------------------------------------------------------

• Brak odpowiedzi AI / błąd modelu
  → Przynajmniej jeden odpowiedni .gguf w modelach\llm\ ? Zobacz modele\llm\README.txt.
  → Wypróbuj mniejszy model lub ustawienie wstępne procesora na pasku bocznym, jeśli ścieżka GPU nie powiedzie się.

• Brak mikrofonu
  → Ustawienia dźwięku systemu Windows: przetestuj mikrofon. W Evi wybierz urządzenie poniżej
    Mikrofon i zapisz.

• Brak głosu
  → Sprawdź, czy w folderze piper\ znajdują się pliki głosowe dla Twojego języka
    wybierz głos na pasku bocznym.

• Awaria Internetu lub YouTube
  → Wyłącz „Blokuj cały ruch” na pasku bocznym, jeśli chcesz korzystać z funkcji online.
  → Do odtwarzania z YouTube zwykle wymagane jest VLC Portable i dostęp do sieci.

• Po edycji ściągawek
  → Uruchom ponownie Evi, aby wszyscy pomocnicy tekstowi niezawodnie wychwytywali zmiany.

--------------------------------------------------------------------------------
  Rozwiązywanie problemów (rozszerzone odniesienie)
--------------------------------------------------------------------------------

Szybkie kontrole (zawsze pierwsze)
  • Windows 10 lub 11 64-bitowy, zaktualizowany, zrestartowany po dużych zmianach?
  • Evi działa z całkowicie rozpakowanego folderu — a nie z archiwum?
  • Unikaj folderów synchronizowanych z chmurą (OneDrive itp.) w przypadku folderu danych na żywo
    Evi działa — użyj ścieżki lokalnej, takiej jak C:\EviPortable lub D:\Tools\Evi, gdy
    możliwe.
  • Wystarczająca ilość wolnego miejsca na dysku dla modelu, czatów i aktualizacji?
  • Po zmianie modeli, głosów lub ściągawek: całkowicie wyjdź z Evi i zacznij
    ponownie.

1) System operacyjny
  • Evi jest przeznaczony wyłącznie dla systemów Windows 10 i 11; inne wersje systemu operacyjnego nie są obsługiwane.
  • Jeśli aplikacja w ogóle się nie uruchomi, całkowicie rozpakuj pakiet i sprawdź program antywirusowy
    logs dla zablokowanych plików wykonywalnych i wypróbuj krótszą ścieżkę instalacji bez rzadkich
    Znaki tylko w Unicode.

2) Ścieżka folderu, program antywirusowy, przenośność
  • Dodaj wykluczenie folderu głównego Evi w oprogramowaniu zabezpieczającym, jeśli skany zostaną wykonane
    uruchamia się bardzo wolno lub blokuje pliki podczas pobierania.
  • Pamięci USB: preferuj USB 3 + NTFS; bardzo powolne media sprawiają, że duże modele są bolesne.

3) Model języka (.gguf)
  • objawy: brak odpowiedzi, błędy modelu, natychmiastowy brak ładowania.
  • poprawki: sprawdź, czy modele\llm\ zawierają kompletny plik .gguf (a nie 0 bajtów); pobierz ponownie
w razie potrzeby; dopasuj rozmiar modelu do pamięci VRAM za pomocą models\llm\README.txt; jeśli nie jesteś pewien,
    przechowuj w folderze pojedynczy testowany plik q4_k_m.
  • wiele plików .gguf: Evi może wybrać największy, który pasuje do Twojej pamięci VRAM — jeśli Ty
    podejrzewaj konflikt, przetestuj tylko z jednym plikiem.

4) GPU, CUDA, sterowniki, brak pamięci
  • Zaktualizuj sterownik NVIDIA; na laptopach wymuś dyskretny procesor graficzny/wydajność
    tryb dla Evi, jeśli pozwala na to system Windows.
  • Jeśli widzisz awarie OOM lub GPU, użyj mniejszego punktu kontrolnego, zamknij inne aplikacje GPU,
    niższą temperaturę lub przełącz się na ustawienie wstępne procesora (wolniejsze, ale stabilniejsze).

5) Tryb tylko procesora
  • Oczekuje się, że będzie powolny; wystarczająca ilość wolnej pamięci RAM; zamknij ciężkie zadania w tle;
    podczas długich sesji używaj planu zasilania „Wysoka wydajność”.

6) Aktywacja
  • Ostrożnie wklej klucze (bez dodatkowych spacji); klucze są powiązane z jednym identyfikatorem maszyny.
  • Po większych zmianach sprzętu możesz potrzebować klucza zastępczego — skorzystaj z pomocy technicznej
    adres ze swoimi danymi.

7) Mikrofon
  • Prywatność systemu Windows → Mikrofon → zezwalaj na aplikacje komputerowe.
  • Ustaw prawidłowe domyślne urządzenie nagrywające; w Evi wybierz to samo urządzenie i Zapisz.
  • Zestawy słuchawkowe Bluetooth mogą zwiększać opóźnienia — w razie wątpliwości przetestuj je za pomocą mikrofonu USB.
  • Inna aplikacja może posiadać tryb wyłączny — tymczasowo zamknij oprogramowanie do spotkań.

8) Rozpoznawanie mowy (lokalne)
  • Jeśli rozpoznawanie nigdy się nie zakończy, upewnij się, że pliki modelu w folderze models\whisper są
    nienaruszone i zezwalaj na pobieranie modelu z sieci po raz pierwszy, jeśli Twoja kompilacja tego potrzebuje.

9) Wyjście głosowe (Piper/TTS)
  • Potwierdź, że Piper\ zawiera pakiet głosowy dla Twojego języka interfejsu użytkownika; wybierz głos
    pasek boczny; sprawdź mikser głośności systemu Windows — Evi może być wyciszony w każdej aplikacji.

10) Sieć i „Blokuj cały ruch”
  • Wyłącz blokowanie Internetu, pomocy pocztowych, pogody i plików do pobrania.
  • Korporacyjne serwery proxy lub sieci VPN mogą wymagać pomocy informatycznej w przypadku osób z list dozwolonych.

11) YouTube i media
  • Zachowaj dołączony układ VLC Portable; umożliwić dostęp do sieci; przeczytaj
    Wskazówki Portable\VLCPortable, jeśli ścieżka została przeniesiona.

12) Język interfejsu użytkownika i ściągawki
  • Ściągawki znajdują się w pliku językowym w sekcji Ściągawki\ — zobacz Ściągawki\README.txt.
  • Zapisz zmiany w formacie UTF-8; uruchom ponownie Evi po edycjach.

13) Bezpieczeństwo (odblokowanie PINem / głosem)
  • Korzystaj z cichego otoczenia; sprawdź ponownie wzmocnienie mikrofonu; nigdy nie udostępniaj swojego PIN-u.
  • Podpowiedzi zawierające losowe słowa są zamierzone — stare nagrania głosowe nie powinny się odblokowywać.

14) Wydajność, zawiesza się, ulega awarii
  • Zmniejsz rozmiar modelu, popraw chłodzenie, przeczytaj wszelkie dzienniki awarii w drzewie, jeśli masz
    build tworzy taki i wycofuje ostatnią zmianę dokonaną przed awarią.

15) Podczas kontaktowania się z pomocą techniczną
  • Dołącz identyfikator komputera, wersję systemu Windows, model procesora graficznego + pamięć VRAM + sterownik, który zawiera plik .gguf
    używasz, oraz dokładny tekst błędu (nie tajne klucze).

Pełne informacje dotyczące rozwiązywania problemów (w tym języku): Manual\FEHLERSUCHE_PL.txt

--------------------------------------------------------------------------------
  Wsparcie — klucze seryjne i identyfikator maszyny
--------------------------------------------------------------------------------

E-mail: Brielbeck@hotmail.de
Zawsze dołączaj identyfikator urządzenia z ekranu aktywacji, gdy żądasz
klucz seryjny lub klucz zastępczy po zmianie sprzętu.

=================================================================================