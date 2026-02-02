import os
import platform
import datetime

print("=== APLIKASI CATATAN HARIAN TROUBLE(AUTO TIME) ===")

file_csv = "log_trouble.csv"
if not os.path.exists(file_csv):
    with open(file_csv, "w") as file:
        file.write("Timestamp,Username,PC,Urgensi,Trouble\n")
kamus_urgensi = {
    "1": "Low",
    "2": "Medium",
    "3": "HIGH/CRITICAL"
}

def simpan_catatan():
    print("\n--- MASUK MODE PENCATATAN ---")
    print("Ketik 'stop' untuk kembali ke menu utama.")
    while True:
        catatan = input("Masukkan trouble hari ini: ")
        if catatan.lower() == "stop":
            print("Selesai")
            break
        print("Level Urgensi: [1] Low  [2] Medium  [3] HIGH/CRITICAL")
        pilih = input("Pilih level (1-3): ")
        user_login = os.getlogin()
        nama_pc = platform.node()
        tgl_jam = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Dicatat: {tgl_jam} - {catatan}")
        try:
            with open(file_csv, "a") as file:
                catatan_aman = catatan.replace(",", ";")
                file.write(f"{tgl_jam},{user_login},{nama_pc},{kamus_urgensi.get(pilih, 'Unknown')},{catatan_aman}\n")
        except FileNotFoundError:
            print(f"Gagal menyimpan catatan: {catatan}")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == "admin" and password == "12345":
        print("Login berhasil!")
        return True
    else:
        print("Login gagal. Coba lagi.")
        return False

def menu():
    sudah_login = False
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Login")
        print("2. Keluar")
        pilih = input("Pilih menu (1-2): ")
        if pilih == "1":
            if login():
                sudah_login = True
                while True:
                    print("\n--- MENU ADMIN ---")
                    print("1. Simpan Catatan")
                    print("2. Pencarian Catatan")
                    print("3. Laporan Hari Ini")
                    print("4. Keluar")
                    pilih = input("Pilih menu (1-4): ")
                    if pilih == "1":
                        simpan_catatan()
                    elif pilih == "2":
                        search_catatan()
                    elif pilih == "3":
                        counter()
                    elif pilih == "4":
                        print("Terima kasih. Selamat tinggal!")
                        break
                    else:
                        print("Pilihan tidak valid. Coba lagi.")
        elif pilih == "2":
            print("Terima kasih. Selamat tinggal!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def search_catatan():
    print("\n--- MASUK MODE PENCARIAN ---")
    print("Ketik 'stop' untuk kembali ke menu utama.")
    while True:
        keyword = input("Masukkan kata kunci: ")
        if keyword.lower() == "stop":
            print("Selesai")
            break
        if not keyword:
            print("Kata kunci tidak boleh kosong. Coba lagi.")
            continue
        print(f"\n[Hasil Pencarian untuk '{keyword}']: ")
        ditemukan=0
        try:
            with open(file_csv, "r") as file:
                header = next(file)
                for line in file:
                    if keyword.lower() in line.lower():
                        parts = line.strip().split(",")
                        if len(parts) >= 5:
                            ditemukan+=1
                            print(f"\n HASIL KE-{ditemukan}")
                            print(f"   - Waktu   : {parts[0]}")
                            print(f"   - User    : {parts[1]}")
                            print(f"   - PC       : {parts[2]}")
                            print(f"   - Level    : {parts[3]}")
                            print(f"   - Masalah  : {parts[4]}")
                        else:
                            pass

                if ditemukan == 0:
                    print("Tidak ditemukan data yang cocok.")
                else:
                    print(f"Total ditemukan: {ditemukan}")
        except FileNotFoundError:
            print("Belum ada data log sama sekali.")
def counter():
    print("======laporan hari ini======")
    hari_ini = datetime.datetime.now().strftime("%Y-%m-%d")
    total_hari_ini = 0
    list_trouble = []

    try:
        with open(file_csv, "r") as file:
            next(file)
            for line in file:
                if line.startswith(hari_ini):
                    total_hari_ini += 1
                    list_trouble.append(line.strip())
        print(f"tanggal: {hari_ini}")
        print(f"Total trouble hari ini: {total_hari_ini}")
        if total_hari_ini > 0:
            print("Detail trouble:")
            for trouble in list_trouble:
                parts = trouble.split(",")
                print(f"->- {parts[3]} - {parts[4]}")
        else:
            print("-> Tidak ada trouble hari ini.")
    except FileNotFoundError:
        print("Gagal membaca catatan. File tidak ditemukan.")
    

if __name__ == "__main__":
    menu()

