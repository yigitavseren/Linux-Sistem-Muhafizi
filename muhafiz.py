import os
import subprocess

def sistem_guvenlik_taramasi():
    print(f"\n--- Linux Sistem Muhafızı Operasyonu Başlatıldı ---")
    print("Sistemdeki zayıf noktalar ve yetki açıkları analiz ediliyor...\n")

    # 1. KRİTİK İZİN TARAMASI (777 İzinleri)
    # Dünyaya açık (World-Writable) dosyalar siber güvenlikte en büyük risklerden biridir.
    print("[*] Kritik İzin Taraması Yapılıyor (777)...")
    try:
        # Linux'ta 'find' komutuyla 777 iznine sahip dosyaları buluyoruz
        tehlikeli_dosyalar = subprocess.check_output("find /home -type f -perm 0777", shell=True).decode()
        if tehlikeli_dosyalar:
            print(f"[!] TEHLİKE: Herkesin yazabildiği dosyalar bulundu:\n{tehlikeli_dosyalar}")
        else:
            print("[+] Temiz: /home dizininde 777 iznine sahip dosya bulunamadı.")
    except Exception:
        print("[-] İzin taraması sırasında bir kısıtlamaya takıldık.")

    # 2. SUDO YETKİ KONTROLÜ
    # Sistemde kimlerin 'Kral yetkisiyle' (Root) işlem yapabildiğini görmemiz lazım.
    print("\n[*] Sudo Yetkisine Sahip Kullanıcılar Hesaplanıyor...")
    try:
        with open("/etc/group", "r") as f:
            for line in f:
                if line.startswith("sudo:") or line.startswith("wheel:"):
                    print(f"[!] YETKİLİ GRUP: {line.strip()}")
    except Exception:
        print("[-] Grup dosyası okunamadı (Yetki yetersiz).")

    # 3. SİSTEM BİLGİSİ VE ÇEKİRDEK (KERNEL) VERSİYONU
    # Eski bir kernel versiyonu demek, bilinen zafiyetlere (Exploit) davetiye çıkarmaktır.
    print("\n[*] İşletim Sistemi ve Kernel Bilgisi:")
    kernel = os.uname().release
    print(f"  -> Kernel Sürümü: {kernel}")
    
    print("\n--- Tarama Tamamlandı. Güvenli Kalın Agam! ---")

if __name__ == "__main__":
    sistem_guvenlik_taramasi()
