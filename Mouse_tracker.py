import pyautogui
import time
import random

# Güvenlik ayarları
pyautogui.PAUSE = 1  # Her işlem arasında 1 saniye bekle
pyautogui.FAILSAFE = True  # Fareyi köşeye götürerek programı durdurabilirsiniz

# Rastgele mesaj listesi
mesajlar = [
    "Merhaba! Nasılsın?",
    "Bugün hava çok güzel!",
    "Python öğreniyorum, harika şeyler yapıyorum",
    "Acaba bugün ne yapsam?",
    "Kahve içmeye ne dersin?",
    "Bu bir otomatik mesajdır 😊",
    "Spam değil, dostluk mesajı!",
    "Biliyor muydun? Bu mesaj bir bot tarafından gönderildi",
    "Teknoloji harika değil mi?",
    "Bir gün robotlar dünyayı ele geçirecek mi sence?"
]

# WhatsApp Web'i açın ve QR kodu tarayın (manuel olarak)
input("WhatsApp Web'i açtıktan ve QR kodu taradıktan sonra Enter'a basın...")

# Kişiyi seçme
pyautogui.click(1200, 200)  # Arama kutusu konumu (kendi ekranınıza göre ayarlayın)
pyautogui.write("Ömer")  # Mesaj atılacak kişi adı
time.sleep(2)
pyautogui.press('enter')

# Rastgele mesaj gönderme döngüsü
for i in range(20):  # 20 mesaj gönder
    mesaj = random.choice(mesajlar)
    pyautogui.write(mesaj)
    pyautogui.press('enter')
    time.sleep(random.uniform(0.5, 2))  # Rastgele bekleme süresi (0.5-2 saniye)
    
    # Bazen emoji ekle (rastgele)
    if random.random() > 0.7:  # %30 olasılıkla emoji gönder
        emojiler = ["😊", "👍", "🎉", "❤️", "🤖"]
        pyautogui.write(random.choice(emojiler))
        pyautogui.press('enter')
        time.sleep(0.5)

print("Mesaj gönderme tamamlandı!")