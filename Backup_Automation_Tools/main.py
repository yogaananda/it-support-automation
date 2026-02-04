import socket
import shutil
import os
import subprocess

print("===========IT SUPPORT BACKUP TOOLS===========")

class BackupManager:
    def __init__(self, user_target):
        self.user_target = user_target
        self.source_dir = f"C:/Users/{self.user_target}/data"
        os.makedirs(self.source_dir, exist_ok=True)
        self.backup_dir = f"D:/backup/{self.user_target}"
        os.makedirs(self.backup_dir, exist_ok=True)
    
    def catat_ip(self):
        ip_address = socket.gethostbyname(socket.gethostname())
        print(f"IP Address: {ip_address}")
    
    def cek_penyimpanan(self):
        total, used, free = shutil.disk_usage(self.source_dir)
        print(f"Penyimpanan: Total: {total // (2**30)} GB, Digunakan: {used // (2**30)} GB, Bebas: {free // (2**30)} GB")
    
    def catat_aplikasi(self):
        try:
            result = subprocess.run(["wmic", "product", "get", "name"], capture_output=True, text=True)
            print("Aplikasi yang terinstal:")
            print(result.stdout)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    
    def copy_paste(self):
        try:
            shutil.copytree(self.source_dir, self.backup_dir, dirs_exist_ok=True)
            print("Pembacaan selesai.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

target_user = input("Masukkan nama pengguna target: ")
app = BackupManager(target_user)
print("IP Address:")
app.catat_ip()
print("Penyimpanan:")
app.cek_penyimpanan()
print("Aplikasi yang terinstal:")
app.catat_aplikasi()
print("Pembacaan selesai.")
app.copy_paste()
