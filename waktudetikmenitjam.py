detik = int(input("Masukkan waktu dalam detik: "))
jam = detik // 3600
menit = (detik % 3600) // 60
detik = detik % 60
print(f"{jam} jam {menit} menit {detik} detik")