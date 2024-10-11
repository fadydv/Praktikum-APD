# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])


# daftar_buku = {}

# daftar_buku["novel 1"] = "Senyum pertama di pagi hari Airin"
# daftar_buku[1] = "Matahari"
# # print (daftar_buku)


# daftar_buku = dict(Buku1 = "Harry Potter", Buku2 = "Percy Jackson")
# print (daftar_buku)


# print(daftar_buku["Buku2"])
# print(daftar_buku.get("Buku2"))


# nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# # for i in nilai:
# #     print(i)

# print(nilai.items())
# for i, j in nilai.items():
#     print(i,j)

# nilai["Struktur Data"] = 99
# nilai["Matematika"] = 99

# nilai.update({"struktur data" : 99} )
# nilai.update({"Matematika" : 69} )

# print (nilai)

# nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(nilai)
# print()
# trashbin = nilai.pop("Matematika")

# print(nilai)
# print()
# print(type(trashbin))

# del nilai["Fisika"]
# print()
# print(nilai)

# nilai.clear()
# print(nilai)

# nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(f"jumlah elemen dari variabel dict nilai adalah {len(nilai)}")

# daftar_nilai = nilai.copy()
# print(daftar_nilai)
# import os

# os.system{"cls"}
# key = "motor", "mobil", "sepeda"
# value = 2
# daftar_kendaraan = dict.fromkeys(key, value)

# print(daftar_kendaraan)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# # Mengakses key dan value dari dictionary
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     # Mengambil nilai dari list
#     for song in j:
#         print(song)
#         print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# for key, value in mahasiswa.items():
#     print("ID Mhasiswa : ", key)
#     for key_a, value_a in value.items():
#        print(key_a, " : ", value_a)
#        print("")
    
# print(mahasiswa[111]["Hobi"][-1])
