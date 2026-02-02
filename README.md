# 🛠️ IT Support Automation Tools

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Internship_Project-orange?style=for-the-badge)

## 📌 Tentang Project Ini

Repositori ini berisi kumpulan skrip otomatisasi, alat bantu (tools), dan dokumentasi teknis yang saya kembangkan selama menjalani **Magang IT Support (6 Bulan)**.

Tujuan utama dari repositori ini adalah untuk:
1.  **Efisiensi:** Mengotomatiskan tugas-tugas repetitif harian IT Support.
2.  **Dokumentasi:** Mencatat troubleshooting dan pemeliharaan perangkat secara terstruktur.
3.  **Pembelajaran:** Menerapkan logika pemrograman (Python) untuk memecahkan masalah infrastruktur nyata.

---

## 📂 Struktur Repositori & Modul

Berikut adalah daftar modul yang tersedia atau sedang direncanakan dalam repositori ini:

* **[`/daily_logging`](./daily_logging)** (✅ **Aktif**)
    Aplikasi CLI untuk mencatat log trouble harian, user request, dan maintenance ke dalam CSV secara otomatis. Modul ini membantu rekapitulasi laporan tanpa input manual berulang.
    > [Lihat Dokumentasi Modul](./daily_logging/README.md)

* **`/network_scripts`** (🚧 **Soon**)
    *(Planned)* Kumpulan skrip untuk keperluan jaringan, seperti:
    * Ping massal untuk cek koneksi.
    * IP Scanner sederhana.
    * Monitoring stabilitas WiFi.

* **`/hardware_audit`** (🚧 **Soon**)
    *(Planned)* Tools untuk mengambil data spesifikasi PC user (RAM, Disk, Processor) secara cepat untuk keperluan inventaris/audit aset.

---

## 🚀 Fitur Unggulan: Daily Logging

Saat ini, alat utama yang sudah beroperasi penuh adalah **Daily Logging System**.

**Fitur:**
* Auto-detect User Login & Hostname.
* Pencatatan waktu (Timestamp) real-time.
* Export database ke `.csv` untuk laporan mingguan/bulanan.

---

## 💻 Tech Stack

* **Language:** Python 3.10+
* **Libraries:** `os`, `platform`, `datetime`, `pandas` (untuk analisis data)
* **Data Storage:** CSV (Comma Separated Values)

---

## 🔧 Cara Menggunakan

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/yogaananda/it-support-automation.git](https://github.com/yogaananda/it-support-automation.git)
    ```
2.  **Masuk ke folder modul yang diinginkan:**
    ```bash
    cd daily_logging
    ```
3.  **Jalankan skrip:**
    Ikuti panduan `README.md` yang ada di dalam masing-masing folder modul.

---

## 📝 Roadmap Magang

Rencana pengembangan selama periode magang:

- [x] Membuat sistem pencatatan log otomatis.
- [ ] Membuat skrip backup data user otomatis.
- [ ] Analisis data trouble paling sering (Top 10 Issues) menggunakan Pandas.
- [ ] Automasi setup printer sharing.

---

<div align="center">
  <small>Dikembangkan oleh <b>Yoga Ananda</b> | IT Support Intern</small>
</div>
