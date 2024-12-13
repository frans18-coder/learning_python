def urutkan_bilangan(angka, jenis_urutan):
    if jenis_urutan == "asc":
        return sorted(angka)
    elif jenis_urutan == "desc":
        return sorted(angka, reverse=True)

angka = [64, 34, 25, 12, 22, 11, 90]
jenis_urutan = input("Pilih urutan (asc/desc): ")
print(urutkan_bilangan(angka, jenis_urutan))
