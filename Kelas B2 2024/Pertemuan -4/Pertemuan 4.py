# ulang = 10
# for i in range(ulang):
#     print("Perulangan ke-"+str(i)+ " kali")
#     print(f"Perulangan ke--(i) kali")

# for i in range(1, 11, 3):
#     print(f"Perulangan ke--(i) kali")

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i)

# print(simpan[2])

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{1} x {j} = {j * j}")
#     print()

# for i in range(1, 6, 2):
#     for j in range (1, 6, 2):
#         print(f"{i} x {j} = {j * j}")
#     print()

# Buat perulangan Anak ayam turun 10

# for i in range(10, -1, -1 ):
#     print(f"Anak ayam turun {i}")

# ulang = "ya"
# hitung = 0
# while ulang == "ya":
#     print(f"Perulangan ke {hitung}")
#     ulang = input("Apakah anda masih ingin mengulang?")
#     hitung +=1
# print("Perulangan selesai")

# x = 0
# while x < 5:
#     print(x)
#     #x+=1

# hitung = 1
# while True:
#     print(f"Perulangan ke {hitung}")
#     ulang = input("Apakah anda masih ingin mengulang?")
#     if ulang == "tidak":
#         print("perulangan berhenti")
#         break
#     hitung +=1

# print(f"Total Perulangan: {hitung}")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         break # Langsung keluar dari perulangan (iterasi)
#     if i == 5:
#         continue #Lompat ke iterasi selanjutnya
#     print(i)

# Buat program login, jika salahnya sebanyak 3x, maka program berhenti

# usn = "admin"
# pw = "admin123"
# salah = 0

# while salah < 3:
#     username = input("Masukkan Username: ")
#     password = input("Masukkan Password: ")
#     if usn == username and pw == password:
#         print("Login berhasil")
#         break
#     else:
#         print("Login gagal")
#         salah +=1