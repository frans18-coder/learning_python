def konversi_mata_uang(nilai, kurs):
    return nilai * kurs

nilai = float(input("Masukkan nilai: "))
kurs = float(input("Masukkan kurs: "))

print("Hasil konversi:", konversi_mata_uang(nilai, kurs))
