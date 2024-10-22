import os
data_siklus = {"24-06-2024": "6 hari", "24-07-2024": "6 hari", "24-08-2024": "6 hari", "23-09-2024": "6 hari"}
users = {"Dilla": "87", "user1": "user123"}
login_attempts = 0

def login_system(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

def logout():
    print("Anda telah keluar dari sistem.")
    exit()

def hitung_siklus(data, counter=0):
    if not data:
        return counter
    else:
        return hitung_siklus(list(data)[1:], counter + 1)

def menu_admin():
    os.system('cls || clear')
    print("\n=== Sistem Manajemen Siklus Menstruasi (Admin) ===")
    print(f"Jumlah total data siklus: {hitung_siklus(data_siklus)}")
    print("1. Lihat Data Siklus")
    print("2. Tambah Data Siklus")
    print("3. Ganti Data Siklus")
    print("4. Hapus Data Siklus")
    print("5. Keluar")

def lihat_data_siklus():
    print("=== Lihat Data Siklus ===")
    for tanggal, durasi in data_siklus.items():
        print(f"Tanggal: {tanggal}, Durasi: {durasi}")
    input("Tekan Enter untuk kembali ke menu utama")

while True:
    os.system('cls || clear')
    print("=== Login Sistem ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if login_system(username, password):
        if username == "Dilla":
            while True:
                os.system('cls || clear')
                menu_admin()
                pilih = input("Masukkan pilihan menu: ")

                os.system('cls || clear')

                if pilih == "1":
                    lihat_data_siklus()

                elif pilih == "2":
                    print("=== Tambah Data Siklus ===")
                    tanggal_baru = input("Masukkan tanggal siklus (DD-MM-YYYY): ")
                    durasi_baru = input("Masukkan durasi (hari): ") + " hari"
                    
                    if tanggal_baru == "" or durasi_baru == " hari":
                        print("Input tidak boleh kosong!")
                    else:
                        data_siklus[tanggal_baru] = durasi_baru
                        print(f"Data siklus pada {tanggal_baru} berhasil ditambahkan!")
                    input("Tekan Enter untuk kembali ke menu utama")

                elif pilih == "3":
                    print("=== Ganti Data Siklus ===")
                    for tanggal, durasi in data_siklus.items():
                        print(f"Tanggal: {tanggal}, Durasi: {durasi}")
                    
                    tanggal_ganti = input("Masukkan tanggal siklus yang ingin diganti: ")
                    if tanggal_ganti in data_siklus:
                        tanggal_baru = input("Masukkan tanggal baru (DD-MM-YYYY): ")
                        durasi_baru = input("Masukkan durasi baru (hari): ") + " hari"
                        
                        if tanggal_baru == "" or durasi_baru == " hari":
                            print("Input tidak boleh kosong!")
                        else:
                            del data_siklus[tanggal_ganti]
                            data_siklus[tanggal_baru] = durasi_baru
                            print(f"Data siklus pada {tanggal_baru} berhasil diperbarui!")
                    else:
                        print("Data tidak ditemukan!")
                    input("Tekan Enter untuk kembali ke menu utama")

                elif pilih == "4":
                    print("=== Hapus Data Siklus ===")
                    for tanggal, durasi in data_siklus.items():
                        print(f"Tanggal: {tanggal}, Durasi: {durasi}")
                    
                    tanggal_hapus = input("Masukkan tanggal siklus yang ingin dihapus: ")
                    if tanggal_hapus in data_siklus:
                        del data_siklus[tanggal_hapus]  
                        print(f"Data siklus pada {tanggal_hapus} telah dihapus!")
                    else:
                        print("Data tidak ditemukan!")
                    input("Tekan Enter untuk kembali ke menu utama")

                elif pilih == "5":
                    logout()

                else:
                    print(f"Menu {pilih} tidak tersedia.")
                    input("Tekan Enter untuk kembali ke menu utama")
    
        elif username == "user1":
            os.system('cls || clear')
            print("\n=== Sistem Manajemen Siklus Menstruasi (Pengguna) ===")
            lihat_data_siklus()  

    else:
        login_attempts += 1  
        if login_attempts >= 3:  
            print("Anda sudah mencoba 3 kali, program akan keluar!")
            logout()
        else:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter untuk mencoba lagi...")