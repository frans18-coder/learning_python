jumlah_peserta = int(input("Masukkan jumlah peserta: "))

kapasitas_minibus = 7

jumlah_minibus = jumlah_peserta // kapasitas_minibus

if jumlah_peserta % kapasitas_minibus != 0:
    jumlah_minibus += 1

print(f"Jumlah minibus yang diperlukan: {jumlah_minibus}")