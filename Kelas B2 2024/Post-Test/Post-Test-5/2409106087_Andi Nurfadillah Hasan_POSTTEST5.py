import os
data_siklus = [["24-06-2024", "6 hari"], ["24-07-2024", "6 hari"], ["24-08-2024", "6 hari"], ["23-09-2024", "6 hari"]]

while True:
    os.system('cls || clear')
    print("\n=== Sistem Manajemen Siklus Menstruasi ===")
    print("1. Lihat Data Siklus")
    print("2. Tambah Data Siklus")
    print("3. Ganti Data Siklus")
    print("4. Hapus Data Siklus")
    print("5. Keluar")
    pilih = input("Masukkan pilihan menu: ")

    os.system('cls || clear')

    if pilih == "1":
        print("=== Lihat Data Siklus ===")
        for index, siklus in enumerate(data_siklus):
            print(f"{index + 1}. Tanggal: {siklus[0]}, Durasi: {siklus[1]}")
        input("Tekan Enter untuk kembali ke menu utama")
        os.system('cls || clear')

    elif pilih == "2":
        print("=== Tambah Data Siklus ===")
        tanggal_baru = input("Masukkan tanggal siklus (DD-MM-YYYY): ")
        durasi_baru = input("Masukkan durasi (hari): ") + " hari"
        data_siklus.append([tanggal_baru, durasi_baru])
        print(f"Data siklus pada {tanggal_baru} berhasil ditambahkan!")
        input("Tekan Enter untuk kembali ke menu utama")
        os.system('cls || clear')

    elif pilih == "3":
        print("=== Ganti Data Siklus ===")
        for index, siklus in enumerate(data_siklus):
            print(f"{index + 1}. Tanggal: {siklus[0]}, Durasi: {siklus[1]}")
        index = input("Masukkan nomor data siklus yang ingin diganti: ")
        tanggal_baru = input("Masukkan tanggal baru (DD-MM-YYYY): ")
        durasi_baru = input("Masukkan durasi baru (hari): ") + " hari"
        data_siklus[int(index) - 1] = [tanggal_baru, durasi_baru]
        print(f"Data siklus pada {tanggal_baru} berhasil diperbarui!")
        input("Tekan Enter untuk kembali ke menu utama")
        os.system('cls || clear')

    elif pilih == "4":
        print("=== Hapus Data Siklus ===")
        for index, siklus in enumerate(data_siklus):
            print(f"{index + 1}. Tanggal: {siklus[0]}, Durasi: {siklus[1]}")
        index = input("Masukkan nomor data siklus yang ingin dihapus: ")
        
        index_hapus = int(index) - 1
        data_siklus_baru = []
        for i in range(len(data_siklus)):
            if i != index_hapus:
                data_siklus_baru.append(data_siklus[i])
        
        data_siklus = data_siklus_baru
        print(f"Data siklus pada {siklus[0]} telah dihapus!")
        input("Tekan Enter untuk kembali ke menu utama")
        os.system('cls || clear')

    elif pilih == "5":
        print("Anda memilih keluar. Terima kasih!")
        exit()

    else:
        print(f"Menu {pilih} tidak tersedia.")
        input("Tekan Enter untuk kembali ke menu utama")
        os.system('cls || clear')