def urutkan_nama(nama):
    return sorted(nama)

nama = input("Masukkan nama (pisahkan dengan spasi): ").split()
print("Nama terurut:", urutkan_nama(nama))
