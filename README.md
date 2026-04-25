# 🐍 Python ile Otomatik Dosya Sıralama — Rehber
 
> Betik yazımından otomatik dosya yönetimine kapsamlı bir başlangıç kılavuzu.
 
---
 
## 📄 1. Script (Betik) ve Oluşturulması
 
**Nedir?**
Belirli bir görevi (dosya düzenleme, veri çekme vb.) yerine getirmek için yazdığın, Python tarafından satır satır okunan kod dosyasıdır.
 
**Nasıl Oluşturulur?**
`.py` uzantılı bir dosya açarsın, kodunu yazarsın ve kaydedersin.
*(O meşhur beyaz nokta kaybolana kadar!)*
 
---
 
## 🗺️ 2. Mutlak vs. Göreli Yollar (The Path)
 
| Tür | Açıklama | Örnek |
|-----|----------|-------|
| **Mutlak Yol** (Absolute) | Bilgisayarın kök dizininden başlayan tam adres. Taşınamaz, sadece senin bilgisayarında çalışır. | `C:\Kullanıcılar\Deniz\...` |
| **Göreli Yol** (Relative) | O an bulunduğun klasörü baz alan adres. Kodunu her yere taşıyabilirsin, bozulmaz. | `./folder_script/file.txt` |
 
---
 
## ▶️ 3. Python Script Çalıştırma
 
Terminal üzerinden aşağıdaki komutla çalıştırılır:
 
```bash
python3 dosya_adi.py
```
 
> ⚠️ **En Kritik Kural:** Terminalin hangi klasörde olduğu (`cd` komutu) ile dosyanın fiziksel konumunun eşleşmesi gerekir.
 
---
 
## ⚙️ 4. Otomatik Dosya Sıralama — Algoritma Mantığı
 
```
1. KONTROL  →  os.getcwd() + os.path.basename()   →  Doğru klasörde miyiz?
2. HAZIRLIK →  os.makedirs(..., exist_ok=True)     →  Hedef klasörleri oluştur.
3. ANALİZ   →  os.listdir() + os.path.splitext()  →  Dosyaları tara, uzantıları yakala.
4. EYLEM    →  shutil.move()                       →  "Kes-Yapıştır" ile dosyaları gönder.
```
 
---
 
## 🚀 5. Neden Bu Bir Zorunluluk?
 
> Bir programcı veya sistem yöneticisi bunu kesinlikle yapabiliyor olmalı. Hatta bu, günümüz dünyasında bir **"tercih"** değil, bir **"zorunluluk"** haline geldi.
 
### 👨‍💻 Programcılar İçin Neden Şart?
 
Bir programcı sadece kod yazmaz; o kodu test eder, derler, sunucuya yükler ve hataları ayıklar.
 
- ⏱️ **Zaman Tasarrufu** — Her seferinde elle yapılması 10 dakika süren bir işi 1 saniyeye indirmek, bir yazılımcının en büyük verimlilik kaynağıdır.
- ✅ **Hata Payını Sıfırlama** — İnsan yorulur, dikkati dağılır ve bir dosyayı yanlış yere kopyalayabilir. Ama senin yazdığın `shutil.move` kodu, 1000. dosyada bile ilk dosyada olduğu kadar dikkatlidir.
---
 
### 🖥️ Sistem Yöneticileri İçin Neden Hayati?
 
Sistem yöneticileri (SysAdmin) binlerce sunucuyu ve dosyayı yönetir.
 
- 📈 **Ölçeklenebilirlik** — 5 bilgisayarın ismini elle değiştirebilirsin ama 5000 bilgisayar söz konusu olduğunda otomasyon (scripting) tek çaredir.
- 🔍 **Sürekli İzleme** — Bir sistem yöneticisi uyurken bile arka planda çalışan scriptler disk doluluğunu kontrol edebilir veya şüpheli girişleri raporlayabilir.
---
 
*Python ile otomasyon öğrenmek, zamanını geri kazanmaktır.* 🐍
