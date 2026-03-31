=================================================================================
  Evi Portable — Kullanım kılavuzu (genel bakış)
  Belge: İngilizce • Bu klasörle birlikte aldığınız yapı için geçerlidir
=================================================================================

Kendi uzun kılavuzlarınızı veya çevirilerinizi de buraya koyun (örn. EN_User_Manual.pdf,
DE_Handbuch.txt). Bu dosya Evi'nin çalıştırılması için isteğe bağlıdır; okuman senin için
veya yazdırın.

Yerelleştirilmiş kopyalar: Bu klasördeki README_<LANG>.txt ve FEHLERSUCHE_<LANG>.txt
(web sitesi kullanıcı arayüzüyle aynı dil kodları). İngilizce genel bakış: bu README.txt;
İngilizce sorun giderme: FEHLERSUCHE_EN.txt. Almanca sorun giderme de
FEHLERSUCHE_DE.txt olarak elle tutulur.

Klasör dizini (dosya adlandırma, oluşturucu): README.md

------------------------------------------------------------------
  İşletim sistemi
------------------------------------------------------------------

Evi Portable yalnızca Microsoft Windows 10 ve Windows 11 içindir. öyle değil
Windows 7/8, macOS, Linux veya mobil işletim sistemlerinde desteklenir.

------------------------------------------------------------------
  İlk başlangıç — indirmeden Evi çalıştırmaya kadar
------------------------------------------------------------------

1) Kurulum yeri
   Evi klasörünün tamamını kontrol ettiğiniz bir yere kopyalayın veya çıkarın; örneğin
   Masaüstünüz, Belgeleriniz veya bir USB çubuğunuz. Klasör yapısını şu şekilde tutun
   teslim edildi (kendiniz oluşturmadığınız alt klasörleri silmeyin).

2) Dil modeli (gerekli)
   Evi'nin klasörde bir ana AI model dosyasına (uzantısı .gguf) ihtiyacı vardır:
   modeller\llm\
   Boyut önerileri için models\llm\README.txt dosyasına bakın. Dosya oraya geldikten sonra,
   Evi'yi başlat; mümkün olduğunda modeli otomatik olarak algılar.

3) İlk başlatma – etkinleştirme
   Evi'yi ilk kez başlattığınızda bir aktivasyon penceresi görünür.
   • PC'niz bir Makine Kimliği gösterir (bu donanıma özel).
   • Makine Kimliğini kopyalayın (düğme: "Makine Kimliğini Kopyala") ve e-postayla şu adrese gönderin:
     Brielbeck@hotmail.de
   • Yalnızca aynı bilgisayarda çalışan bir seri anahtar alacaksınız
     (anahtar donanımınıza bağlıdır).
   • Anahtarı etkinleştirme penceresine yapıştırın ve Etkinleştir'i seçin.

   Büyük donanımı değiştirirseniz veya diski kimliği değiştirecek şekilde hareket ettirirseniz,
   yeni bir anahtara ihtiyacınız olabilir; aynı adresle iletişime geçin.

4) Aktivasyondan sonra
   Ana pencere açılır. Sol taraftan dili, mikrofonu ve sesi seçin
   ayarlar paneli. Komut örnekleri için istediğiniz zaman "hile sayfasını aç" deyin
   (diğer diller için hile sayfalarına\en.txt ve kardeş dosyalara bakın).

5) İsteğe bağlı: bu kılavuzu Windows'tan açın
   Dosya Gezgini'nde Evi klasörüne, ardından Manual\README.txt dosyasına gidin ve dosyayı açın.
   Not Defteri veya herhangi bir metin görüntüleyici ile.

------------------------------------------------------------------
  Arayüz dili (GUI)
------------------------------------------------------------------

Kullanıcı arayüzü üstteki Dil altında seçtiğiniz dili takip eder
sol ayarlar panelinin (kenar çubuğundaki ilk blok). Bir seçim yaptıktan sonra
dil, menüler, düğmeler, etiketler ve ekrandaki metinlerin çoğu buna geçer
Çevirilerin olduğu her yerde dil. İstediğiniz zaman değiştirebilirsiniz; sadece
düzen değil, ifadeler değişir.

İpucu: Hile sayfaları\ klasöründeki komut kopya sayfaları, her birine göre listelenir.
dil kodu (en.txt, de.txt,…). Ayrıntılar için hile sayfaları\README.txt'ye bakın.
Bu Kılavuz\ klasörü ürüne daha uzun bir genel bakıştır; hile sayfaları
hızlı "ne söylenmeli" listesi.

------------------------------------------------------------------
  Grafik kartı (GPU) — hızlı kılavuz
------------------------------------------------------------------

Güçlü bir orta seçenek, 12 GB videoya sahip NVIDIA GeForce RTX 4070 Ti'dir
bellek: hız, bağlam boyutu ve daha büyük modeller için yer arasında iyi bir denge.

Yaklaşık RTX 3060'tan RTX 5090'a kadar olan kartlar iyi çalışabilir; en iyi uyum bağlıdır
RAM, CPU, soğutma ve hangi model dosyasını yüklediğinize bağlı. GPU ön ayarını kullanın
Evi'nin kenar çubuğu donanımınızla eşleşecek.

Yalnızca CPU üzerinde çalışmak ("CPU… GB RAM" ön ayarları) acil bir geri dönüştür:
Evi uygun bir grafik kartı olmadan kullanılabilir durumda kalır ancak yanıtlar çok daha yavaş olur.
Mümkün olduğunda gerçek bir GPU'yu tercih edin.

------------------------------------------------------------------
  Tamamen taşınabilir — İnternet'e ihtiyaç duyduğunuzda
------------------------------------------------------------------

Evi taşınabilir olacak şekilde tasarlandı: klasörün tamamını başka bir sürücüye, USB belleğe,
veya PC, ardından oradan başlatın. Sohbetler, anılar, ayarlar, güvenlik verileri ve
etkinleştirme dosyası normalde bu klasörün içinde kalır (etkinleştirme,
PC, klasör yolu değil).

İnternet esas olarak indirmeyi seçtiğiniz şeyler içindir (model dosyaları, isteğe bağlı
sesler veya ekstralar, güncellemeler) ve web araması, e-posta gibi isteğe bağlı özellikler için
ağ erişimine izin verdiğinizde akış veya hava durumu.

İzin verilen klasörünüzdeki çekirdek sohbet, bellek, notlar, zamanlayıcılar, dosya araçları, yerel
konuşma tanıma, yerel ses çıkışı ve cihazınızda çalışan gizlilik kilidi
konuşmalarınızı bir bulut hizmetine göndermeden makineye aktarın. İsteğe bağlı çevrimiçi
özellikler yalnızca ağ erişimi açıkken ve siz bunları kullandığınızda çalışır.

------------------------------------------------------------------
  Güvenlik: PIN ve sesle kilit açma (kopyalamayı önleme)
------------------------------------------------------------------

Evi, cihazınızda bir güvenlik PIN'i ve isteğe bağlı ses kaydı kullanabilir.

Sesle kilit açma kullanıldığında, her denemede kısa bir rastgele kelime seti istenebilir
bu her zaman değişir - sonsuza kadar sabit bir cümle değil. Bu kolay olanı engeller
sesinizin eski bir kaydını tekrar çalmanın hilesi. PIN'iniz bir
ayrı savunma hattı

Bu, gündelik istismarı durdurmak için tasarlanmıştır; hiçbir tüketici ürünü söz veremez
Her saldırıya karşı mükemmellik (örneğin hem PIN'inizi hem de
gelişmiş ses taklidi). PIN'inizi gizli tutun ve kurulumu tamamlayın.
uygulama size rehberlik eder.

------------------------------------------------------------------
  Sorun giderme (kısa kontrol listesi)
------------------------------------------------------------------

• AI yanıtı yok / model hatası
  → Modellerde en az bir uygun .gguf\llm\ ? Modeller\llm\README.txt dosyasına bakın.
  → GPU yolu başarısız olursa daha küçük bir modeli veya kenar çubuğundaki CPU ön ayarını deneyin.

• Mikrofon yok
  → Windows ses ayarları: mikrofonu test edin. Evi'nde, altından cihazı seçin
    Mikrofon ve Kaydet.

• Ses çıkışı yok
  → Dilinize uygun ses dosyalarının piper\ klasöründe mevcut olup olmadığını kontrol edin ve
    kenar çubuğundan bir ses seçin.

• Web veya YouTube başarısız oluyor
  → Çevrimiçi özellikleri istiyorsanız kenar çubuğundaki "Tüm trafiği engelle" seçeneğini kapatın.
  → YouTube oynatmak için genellikle VLC Portable ve ağ erişimi gerekir.

• Hile sayfalarını düzenledikten sonra
  → Tüm metin yardımcılarının değişiklikleri güvenilir bir şekilde alabilmesi için Evi'yi yeniden başlatın.

------------------------------------------------------------------
  Sorun giderme (genişletilmiş referans)
------------------------------------------------------------------

Hızlı kontroller (her zaman ilk)
  • Windows 10 veya 11 64-bit, güncellendi mi, büyük değişikliklerden sonra yeniden başlatıldı mı?
  • Evi bir arşivin içinden değil, tamamen çıkartılmış bir klasörden mi çalışıyor?
  • Canlı veri klasörü için bulutla senkronize edilmiş klasörlerden (OneDrive vb.) kaçının.
    Evi çalıştırıldığında C:\EviPortable veya D:\Tools\Evi gibi yerel bir yol kullanın.
    mümkün.
  • Model, sohbetler ve güncellemeler için yeterli boş disk alanı var mı?
  • Modelleri, sesleri veya kopya kağıtlarını değiştirdikten sonra: Evi'nden tamamen çıkın ve başlayın
    tekrar.

1) İşletim sistemi
  • Evi yalnızca Windows 10 ve 11 içindir; diğer işletim sistemi sürümleri desteklenmez.
  • Uygulama hiç başlamazsa paketin tamamını çıkarın, antivirüs yazılımını kontrol edin
    engellenen yürütülebilir dosyaların günlüklerini tutun ve nadir olmayan daha kısa bir yükleme yolunu deneyin
    Yalnızca Unicode karakterler.

2) Klasör yolu, antivirüs, taşınabilirlik
  • Taramalar gerçekleşirse, güvenlik yazılımında Evi kök klasörünüz için bir hariç tutma ekleyin
    açılış çok yavaş veya indirme sırasında dosyalar kilitleniyor.
  • USB bellekler: USB 3 + NTFS'yi tercih edin; çok yavaş ortam, büyük modelleri acı verici hale getirir.

3) Dil modeli (.gguf)
  • belirtiler: yanıt yok, model hataları, yükleme anında başarısızlık.
  • düzeltmeler: modellerin\llm\'nin tam bir .gguf (0 bayt değil) içerdiğini doğrulayın; yeniden indir
gerekirse; models\llm\README.txt dosyasını kullanarak model boyutunu VRAM ile eşleştirin; emin değilseniz,
    test edilmiş tek bir q4_k_m dosyasını klasörde tutun.
  • birden fazla .gguf dosyası: Evi, VRAM'inize en uygun olanı seçebilir — eğer isterseniz
    Bir çakışma olduğundan şüpheleniyorsanız yalnızca tek bir dosyayla test edin.

4) GPU, CUDA, sürücüler, yetersiz bellek
  • NVIDIA sürücüsünü güncelleyin; dizüstü bilgisayarlarda ayrı GPU'yu / performansı zorlayın
    Windows'un izin verdiği yerde Evi için mod.
  • OOM veya GPU'nun kilitlendiğini görürseniz daha küçük bir kontrol noktası kullanın, diğer GPU uygulamalarını kapatın,
    sıcaklığı düşürün veya bir CPU ön ayarına geçin (daha yavaş ama daha istikrarlı).

5) Yalnızca CPU modu
  • Yavaş olması bekleniyor; yeterince boş sistem RAM'i; ağır arka plan görevlerini kapatın;
    Uzun oturumlar sırasında "Yüksek performans" güç planını kullanın.

6) Etkinleştirme
  • Anahtarları dikkatlice yapıştırın (fazladan boşluk bırakmayın); anahtarlar bir Makine Kimliğine bağlıdır.
  • Büyük donanım değişikliklerinden sonra yedek anahtara ihtiyacınız olabilir; desteği kullanın
    ayrıntılarınızla birlikte adresinizi belirtin.

7) Mikrofon
  • Windows Gizliliği → Mikrofon → masaüstü uygulamalarına izin verin.
  • Doğru varsayılan kayıt cihazını ayarlayın; Evi'nde aynı cihazı seçip Kaydet'e tıklayın.
  • Bluetooth kulaklıklar gecikmeye neden olabilir; emin değilseniz USB mikrofonla test edin.
  • Başka bir uygulama özel modda olabilir; toplantı yazılımını geçici olarak kapatın.

8) Konuşma tanıma (yerel)
  • Tanıma hiç bitmezse modeller\fısıltı altındaki model dosyalarının tamamlandığından emin olun.
    sağlam ve yapınızın buna ihtiyacı varsa ilk kez model alımında ağa izin ver.

9) Ses çıkışı (Piper / TTS)
  • Piper\'ın kullanıcı arayüzü diliniz için bir ses paketi içerdiğini doğrulayın; bir ses seç
    kenar çubuğu; Windows ses karıştırıcısını kontrol edin — Evi uygulama bazında sessize alınabilir.

10) Ağ ve "Tüm trafiği engelle"
  • Web, posta yardımcıları, hava durumu veya indirmeler için engellemeyi kapatın.
  • Kurumsal proxy'ler veya VPN'ler, izin verilenler listeleri için BT yardımına ihtiyaç duyabilir.

11) YouTube ve medya
  • Birlikte verilen VLC Portable düzenini koruyun; ağ erişimini etkinleştirin; okumak
    Yol taşınmışsa Taşınabilir\VLCTaşınabilir rehberlik.

12) Kullanıcı arayüzü dili ve hile sayfaları
  • Kopya sayfaları, kopya sayfaları\ altındaki dil dosyası başınadır — bkz. kopya sayfaları\README.txt.
  • Düzenlemeleri UTF-8 olarak kaydedin; Düzenlemelerden sonra Evi'yi yeniden başlatın.

13) Güvenlik (PIN / sesle kilit açma)
  • Sessiz bir ortam kullanın; mikrofon kazancını yeniden kontrol edin; PIN'inizi asla paylaşmayın.
  • Rastgele sözcük istemleri kasıtlıdır — eski ses kayıtlarının kilidi açılmamalıdır.

14) Performans, donmalar, çökmeler
  • Model boyutunu küçültün, soğutmayı iyileştirin, eğer
    build bir tane oluşturur ve hatalardan önce yaptığınız son değişikliği geri alır.

15) Destekle iletişime geçtiğinizde
  • .gguf olan Makine Kimliğini, Windows sürümünü, GPU modelini + VRAM + sürücüsünü ekleyin
    kullandığınızı ve tam hata metnini (gizli anahtarlar değil) belirtin.

Tam sorun giderme referansı (bu dil): Manual\FEHLERSUCHE_TR.txt

------------------------------------------------------------------
  Destek — seri anahtarlar ve Makine Kimliği
------------------------------------------------------------------

E-posta: Brielbeck@hotmail.de
Bir istekte bulunurken her zaman aktivasyon ekranından Makine Kimliğinizi ekleyin.
donanım değişikliklerinden sonra seri anahtar veya yedek anahtar.

=================================================================================