# 🛠️ IT Support Backup Automation Tools

Tools berbasis Python untuk mengotomatisasi pekerjaan IT Support sebelum melakukan instal ulang Windows pada PC User.

## 🚀 Fitur Utama
1.  **Auto IP Logging**: Mencatat IP Address komputer secara otomatis.
2.  **Storage Check**: Mengecek sisa kapasitas penyimpanan source & destination.
3.  **App Scanner**: Mencatat semua aplikasi yang terinstall (via WMIC) untuk referensi install ulang.
4.  **Auto Backup**: Menyalin data user secara aman menggunakan `shutil`.

## 📋 Prasyarat
* OS: Windows 10/11
* Python 3.x terinstall
* Target Drive Backup (Default: Drive D:/)

## ⚙️ Cara Penggunaan
1.  Clone repo ini.
2.  Jalankan script:
    ```bash
    python backup_tools.py
    ```
3.  Masukkan nama folder user target saat diminta (contoh: `Yoga`).
4.  Tunggu proses scanning aplikasi (memakan waktu 10-30 detik).

## ⚠️ Catatan
Script ini menggunakan perintah `wmic` yang mungkin berjalan agak lambat saat scan aplikasi. Harap tunggu hingga proses selesai.
