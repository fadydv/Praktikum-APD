import os
data_siklus = {"24-06-2024": "6 hari","24-07-2024": "6 hari","24-08-2024": "6 hari","23-09-2024": "6 hari"}
users = {"Dilla": "87", "user1": "user123"}

os.system('cls || clear')
print("=== Login Sistem ===")
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in users and users[username] == password:
    if username == "Dilla":
        while True:
            os.system('cls || clear')
            print("\n=== Sistem Manajemen Siklus Menstruasi (Admin) ===")
            print("1. Lihat Data Siklus")
            print("2. Tambah Data Siklus")
            print("3. Ganti Data Siklus")
            print("4. Hapus Data Siklus")
            print("5. Keluar")
            pilih = input("Masukkan pilihan menu: ")

            os.system('cls || clear')

            if pilih == "1":
                print("=== Lihat Data Siklus ===")
                for tanggal, durasi in data_siklus.items():
                    print(f"Tanggal: {tanggal}, Durasi: {durasi}")
                input("Tekan Enter untuk kembali ke menu utama")

            elif pilih == "2":
                print("=== Tambah Data Siklus ===")
                tanggal_baru = input("Masukkan tanggal siklus (DD-MM-YYYY): ")
                durasi_baru = input("Masukkan durasi (hari): ") + " hari"
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
                print("Anda memilih keluar. Terima kasih!")
                break

            else:
                print(f"Menu {pilih} tidak tersedia.")
                input("Tekan Enter untuk kembali ke menu utama")
    
    elif username == "user1":

        os.system('cls || clear')
        print("\n=== Sistem Manajemen Siklus Menstruasi (Pengguna) ===")
        print("=== Lihat Data Siklus ===")
        for tanggal, durasi in data_siklus.items():
            print(f"Tanggal: {tanggal}, Durasi: {durasi}")
        input("Tekan Enter untuk keluar")

else:
    print("Login gagal! Username atau password salah.")