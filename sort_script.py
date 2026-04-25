import os
import shutil  # Dosya taşıma işlemleri için gerekli olan standart kütüphane

# ─────────────────────────────────────────────
# SABIT TANIMLAMALAR
# ─────────────────────────────────────────────

# Bu script'in yalnızca belirli bir klasör içinde çalışmasını istiyoruz.
# Aşağıdaki değişken, script'in çalışmasına izin verilen klasörün adını tutar.
# Eğer script farklı bir klasörde çalıştırılırsa, hata mesajı verip durur.
REQUIRED_FOLDER = "folder_script"

# ─────────────────────────────────────────────
# ÇALIŞMA DİZİNİ KONTROLÜ
# ─────────────────────────────────────────────

# os.getcwd()  → Script'in çalıştırıldığı tam dizin yolunu döndürür.
#                Örnek: "/home/kullanici/belgeler/folder_script"
# os.path.basename() → Tam yolun yalnızca son parçasını (klasör adını) alır.
#                      Örnek: "folder_script"
current_folder = os.path.basename(os.getcwd())

# Eğer mevcut klasör adı, belirlediğimiz zorunlu klasör adıyla eşleşmiyorsa:
if current_folder != REQUIRED_FOLDER:
    # Kullanıcıya hangi klasörde çalışması gerektiğini belirten hata mesajı yazdır.
    # f-string kullanılarak değişken değeri mesaj içine yerleştirilir.
    print(f"Hata: Bu script yalnızca '{REQUIRED_FOLDER}' klasöründe çalıştırılmalıdır!")
    
    # exit() → Python yorumlayıcısını durdurur, aşağıdaki hiçbir kod çalışmaz.
    # Bu sayede yanlış dizinde yanlışlıkla dosya taşınmasının önüne geçilir.
    exit()

# Buraya ulaşıldıysa klasör kontrolü başarıyla geçilmiş demektir.
print(f"Script '{current_folder}' klasöründe çalışıyor. Her şey yolunda.\n")

# ─────────────────────────────────────────────
# SIRALAMA KURALLARI
# ─────────────────────────────────────────────

# SORTING_RULES: Hangi dosya uzantısının hangi klasöre taşınacağını tanımlar.
# Yapı: { "hedef_klasör_adı": [".uzantı1", ".uzantı2", ...] }
#
# Örnek eşleşmeler:
#   "resim.jpg"   → "images"    klasörüne taşınır
#   "rapor.pdf"   → "documents" klasörüne taşınır
#   "müzik.mp3"   → Hiçbir kuralla eşleşmez, olduğu yerde kalır
#
# Yeni bir kategori eklemek için sözlüğe yeni bir anahtar-değer çifti eklemek yeterlidir.
# Örnek: "videos": [".mp4", ".avi", ".mkv"]
SORTING_RULES = {
    "images":    [".jpg", ".png"],               # Görsel dosyalar
    "documents": [".doc", ".docx", ".pdf"]       # Ofis ve PDF belgeleri
}

# ─────────────────────────────────────────────
# HEDEF KLASÖRLER OLUŞTURMA
# ─────────────────────────────────────────────

# SORTING_RULES içindeki her klasör adı için gerekli dizini oluşturuyoruz.
# .keys() → Sözlüğün yalnızca anahtarlarını döndürür: ["images", "documents"]
for folder in SORTING_RULES.keys():
    # os.makedirs() → Belirtilen klasörü oluşturur.
    # exist_ok=True  → Klasör zaten mevcutsa hata fırlatmaz, sessizce devam eder.
    #                  Bu parametre olmadan var olan klasör için FileExistsError alınır.
    os.makedirs(folder, exist_ok=True)

# ─────────────────────────────────────────────
# DOSYALARI TARAMA VE TAŞIMA
# ─────────────────────────────────────────────

# os.listdir() → Parametre verilmezse mevcut dizindeki tüm öğeleri listeler.
# Dönen liste hem dosyaları hem de alt klasörleri içerir; biz yalnızca dosyaları işleyeceğiz.
for file in os.listdir():

    # os.path.isfile(file) → Öğenin gerçekten bir dosya olup olmadığını kontrol eder.
    # Klasörler (images, documents vb.) bu kontrolden geçemez ve atlanır.
    # Bu kontrol olmazsa klasör adlarını da işlemeye çalışırdık → hata çıkardı.
    if os.path.isfile(file):

        # os.path.splitext(file) → Dosya adını iki parçaya böler: (ad, uzantı)
        # Örnek: "belge.pdf" → ("belge", ".pdf")
        # Biz yalnızca uzantıyla ilgilendiğimiz için [1] indeksini alıyoruz.
        # Uzantısız dosyalar için boş string "" döner.
        file_extension = os.path.splitext(file)[1]

        # Her dosya için tüm kategorileri (images, documents vb.) tek tek kontrol ediyoruz.
        # Bu iç içe döngü yapısı sayesinde yeni kategori eklendiğinde bu kısma dokunmaya gerek kalmaz.
        for folder, extensions in SORTING_RULES.items():
            # .items() → Sözlükten (anahtar, değer) çiftlerini döndürür.
            # Örnek: folder = "images", extensions = [".jpg", ".png"]

            # Dosyanın uzantısı bu kategorinin uzantı listesinde var mı?
            # "in" operatörü liste içinde arama yapar; büyük/küçük harf duyarlıdır.
            # Not: ".JPG" ile ".jpg" eşleşmez; gerekirse .lower() eklenebilir.
            if file_extension in extensions:

                # os.path.join() → İşletim sistemine uygun yol birleştirir.
                # Windows'ta "\", Linux/Mac'te "/" kullanır; elle birleştirmekten daha güvenlidir.
                # Örnek: os.path.join("images", "resim.jpg") → "images/resim.jpg"
                destination = os.path.join(folder, file)

                # shutil.move(kaynak, hedef) → Dosyayı taşır (kopyalayıp orijinali siler).
                # Hedef zaten aynı adda dosya içeriyorsa üzerine yazar.
                # Dosya başka bir diske taşınıyorsa kopyala+sil mantığıyla çalışır.
                shutil.move(file, destination)

                # Kullanıcıya hangi dosyanın nereye taşındığını bildiriyoruz.
                print(f"Dosya '{file}' başarıyla '{folder}' klasörüne taşındı.")

                # Bir dosya yalnızca bir kategoriye ait olabilir.
                # Eşleşme bulununca iç döngüyü kırarak gereksiz kontrolleri önlüyoruz.
                # Bu satır olmadan eşleşen dosya tüm kategorilerle tekrar karşılaştırılırdı.
                break
