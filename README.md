# 🛡️ Linux Sistem Muhafızı (Security Analyzer)

Bu proje, bir Linux işletim sistemindeki kritik güvenlik açıklarını, yetki suistimallerini ve dosya sistemi zayıflıklarını tespit etmek amacıyla Python kullanılarak geliştirilmiş bir **Sistem Güvenlik Analiz** aracıdır.

## 🛠️ Temel Analiz Yetenekleri
* **Kritik İzin Denetimi (777):** Sistemde herkesin okuyabildiği, yazabildiği ve çalıştırabildiği (`rwxrwxrwx`) riskli dosyaları tespit eder.
* **Yetki Hiyerarşisi Analizi:** `/etc/group` dosyasını tarayarak sistemde `sudo` veya `wheel` yetkisine sahip, "Root" gücünü kullanabilen kullanıcıları raporlar.
* **Çekirdek (Kernel) Denetimi:** Sistemde çalışan Kernel versiyonunu belirleyerek, bilinen çekirdek zafiyetlerine karşı ön keşif yapar.

## 📖 Mühendislik Notları (Linux Sınav Hazırlığı)
Bu araç geliştirilirken aşağıdaki Linux sistem mimarisi temelleri baz alınmıştır:
* **Dosya İzinleri:** 777 (4+2+1) izinlerinin siber güvenlikteki risk analizi.
* **Kullanıcı Grupları:** Linux yetkilendirme modelinin temel taşı olan grup dosyalarının okunması.
* **Subprocess Yönetimi:** Python üzerinden Bash komutlarının (find, uname vb.) otomatize edilmesi.

## 🚀 Çalıştırma
```bash
# Aracı ateşlemek için
python3 muhafiz.py

⚖️ Yasal Uyarı

Bu araç tamamen eğitim ve savunma amaçlı (White Hat) geliştirilmiştir. Yalnızca yetkiniz dahilindeki sistemlerde analiz yapmak için kullanınız.
