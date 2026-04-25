1. Script (Betik) ve Oluşturulması
Nedir? Belirli bir görevi (dosya düzenleme, veri çekme vb.) yerine getirmek için yazdığın, Python tarafından satır satır okunan kod dosyasıdır.

Oluşturma: .py uzantılı bir dosya açarsın, kodunu yazarsın ve kaydedersin. (O meşhur beyaz nokta kaybolana kadar!)

2. Mutlak vs. Göreli Yollar (The Path)
Mutlak Yol (Absolute): Bilgisayarın kök dizininden başlayan tam adres. C:\Kullanıcılar\Deniz\... gibi. Taşınamaz, sadece senin bilgisayarında çalışır.

Göreli Yol (Relative): O an bulunduğun klasörü baz alan adres. ./folder_script/file.txt gibi. Kodunu her yere taşıyabilirsin, bozulmaz.

3. Python Script Çalıştırma
Terminal üzerinden python3 dosya_adi.py komutuyla çalıştırılır.

En Kritik Kural: Terminalin hangi klasörde olduğu (cd komutu) ile dosyanın fiziksel konumunun eşleşmesi gerekir.

4. Otomatik Dosya Sıralama (Algoritma Mantığı)

Kontrol: os.getcwd() ve os.path.basename() ile doğru klasörde miyiz bak.

Hazırlık: os.makedirs(..., exist_ok=True) ile hedef klasörleri hazırla.

Analiz: os.listdir() ile dosyaları tara ve os.path.splitext() ile uzantılarını yakala.

Eylem: shutil.move() (Şa-tıl move) ile dosyaları "Kes-Yapıştır" yaparak yerlerine gönder.
