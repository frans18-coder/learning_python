harga_barang = float(input("Masukkan total harga barang: "))
if harga_barang >= 100000:
    diskon = harga_barang * 0.05
    harga_setelah_diskon = harga_barang - diskon
    print(f"Diskon 5%: {diskon}")
    print(f"Total yang harus dibayar setelah diskon: {harga_setelah_diskon}")
else:
    print("Tidak ada diskon, total harga: ", harga_barang)