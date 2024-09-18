print("Informasi Transaksi Belanja")
namabarang = input("Masukkan nama barang: ")
hargabarang = float(input("Masukkan harga barang: "))
jumlahbarang = int(input("Masukkan jumlah barang: "))
diskon = float(input("Diskon: "))

totalhargasebelumdiskon = jumlahbarang*hargabarang
totaldiskon = diskon/100*totalhargasebelumdiskon
totalhargasetelahdiskon = totalhargasebelumdiskon-totaldiskon
sisapembagian = diskon % 3

print("anda membeli", jumlahbarang, namabarang, "dengan harga satuan", hargabarang, "total sebelum diskon adalah", totalhargasebelumdiskon, "total diskon adalah", totaldiskon, "dan total yang harus dibayar adalah", totalhargasetelahdiskon, "diskon")
print("sisa pembagian diskon dengan 3 adalah", sisapembagian)