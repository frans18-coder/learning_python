n = int(input("Jumlah karyawan: "))

total_gaji_perusahaan = 0

for i in range(1, n + 1):
    jam_kerja = int(input(f"Jam kerja karyawan {i}: "))
    
    gaji_per_jam = 10000
    if jam_kerja > 7:
        jam_lembur = jam_kerja - 7
        total_gaji = (7 * gaji_per_jam) + (jam_lembur * (1.5 * gaji_per_jam))
    else:
        total_gaji = jam_kerja * gaji_per_jam
    
    print(f"Total Gaji: {total_gaji}")
    
    total_gaji_perusahaan += total_gaji
    
print(f"Total Gaji karyawan: {total_gaji_perusahaan}")