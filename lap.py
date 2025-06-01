from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://d0a72fc00e1905cbdbf4__cr.it:16a271cc21b51cef@gw.dataimpulse.com:10206',
        'https': 'https://d0a72fc00e1905cbdbf4__cr.it:16a271cc21b51cef@gw.dataimpulse.com:10206',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920, 1200")
# Hapus '--headless' untuk melihat apakah ekstensi berjalan dengan benar dalam mode normal
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-background-networking")  # Mencegah koneksi jaringan di latar belakang
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--disable-client-side-phishing-detection")  # Nonaktifkan deteksi phishing
chrome_options.add_argument("--disable-default-apps")  # Nonaktifkan aplikasi bawaan Chrome
chrome_options.add_argument("--disable-features=NetworkPrediction")  # Nonaktifkan prediksi jaringan
chrome_options.add_argument("--disable-sync")  # Nonaktifkan sinkronisasi
chrome_options.add_argument("--metrics-recording-only")  # Nonaktifkan pengumpulan data
chrome_options.add_argument("--safebrowsing-disable-auto-update")  # Nonaktifkan pembaruan otomatis Safe Browsing
chrome_options.add_argument("--disable-component-update")  # Nonaktifkan pembaruan komponen
chrome_options.add_argument("--disable-domain-reliability")  # Nonaktifkan keandalan domain

# --- Argumen tambahan untuk memblokir koneksi ke Google Optimization Guide ---
# Menonaktifkan fitur-fitur yang terkait dengan Optimization Guide dan sejenisnya
chrome_options.add_argument("--disable-features=OptimizationHints,OptimizationTargetPrediction,SafeBrowsing")
chrome_options.add_argument("--disable-features=Translate,InterestCohortFeaturePolicy")
chrome_options.add_argument("--disable-background-timer-throttling") # Mencegah throttling timer di latar belakang
chrome_options.add_argument("--disable-ipc-flooding-protection") # Melindungi dari serangan flooding IPC
chrome_options.add_argument("--disable-site-specific-hsts-bypass") # Menonaktifkan bypass HSTS
chrome_options.add_argument("--disable-hang-monitor") # Menonaktifkan monitor hang
chrome_options.add_argument("--disable-popup-blocking") # Menonaktifkan pemblokiran popup
chrome_options.add_argument("--disable-prompt-on-repost") # Menonaktifkan prompt saat memposting ulang
chrome_options.add_argument("--disable-web-security") # Menonaktifkan keamanan web (gunakan dengan hati-hati)
chrome_options.add_argument("--no-first-run") # Mencegah menjalankan proses 'first run'
chrome_options.add_argument("--no-default-browser-check") # Mencegah pemeriksaan browser default
chrome_options.add_argument("--disable-blink-features=AutomationControlled") # Menyembunyikan bahwa browser dikontrol oleh otomatisasi
# --- Akhir argumen tambahan ---

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/29e11fe4-5a63-4180-9214-3dd5e9512ff9")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
