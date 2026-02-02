# Aplikasi Catatan Harian Trouble (Auto Time)

Aplikasi berbasis CLI (Command Line Interface) sederhana menggunakan Python untuk mencatat log permasalahan teknis (*troubleshoot*) secara otomatis dan terorganisir.

## 🚀 Fitur Utama

* **Auto Logging:** Mencatat otomatis waktu (*Timestamp*), nama pengguna (*Username*), dan nama perangkat (*PC*).
* **Security:** Sistem login sederhana untuk membatasi akses ke menu admin.
* **Database CSV:** Menyimpan semua data ke dalam file `log_trouble.csv` yang bisa dibuka di Excel.
* **Search Engine:** Fitur pencarian riwayat masalah berdasarkan kata kunci tertentu.
* **Daily Report:** Ringkasan otomatis jumlah kendala yang terjadi pada hari yang sama.

---

## 🛠️ Instalasi

Aplikasi ini hanya menggunakan library bawaan Python (*Standard Library*), jadi Anda tidak perlu menginstal dependensi tambahan.

1. Pastikan Anda sudah menginstal [Python 3.x](https://www.python.org/).
2. Unduh atau salin kode skrip ke komputer Anda.
3. Simpan dengan nama file, misalnya: `app_trouble.py`.

---

## 📖 Cara Penggunaan

1.  Buka terminal atau Command Prompt (CMD).
2.  Jalankan aplikasi dengan perintah:
    ```bash
    python app_trouble.py
    ```
3.  **Login Admin:**
    * **Username:** `admin`
    * **Password:** `12345`
4.  Pilih menu yang tersedia (1-4) untuk mulai bekerja.
5.  Gunakan kata kunci `stop` saat berada di mode input untuk kembali ke menu utama.

---

## 📂 Struktur Data

Aplikasi akan otomatis membuat file `log_trouble.csv` saat pertama kali dijalankan. Format datanya adalah:


 **Timestamp**  : Tanggal dan waktu saat data diinput

**Username** : Nama user yang sedang login di Windows/Linux 

**PC** : Nama identitas perangkat (Computer Name) 

**Urgensi** : Tingkat keparahan (Low, Medium, HIGH/CRITICAL) 

**Trouble** : Detail deskripsi permasalahan teknis 

---

## 🤝 Kontribusi

Tarik permintaan (*Pull requests*) sangat dipersilakan. Untuk perubahan besar, harap buka *issue* terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

## 📄 Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
