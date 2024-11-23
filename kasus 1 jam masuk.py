jam_masuk = int(input("Masukkan jam masuk (1-12)  = "))
jam_pulang = int(input("Masukkan jam pulang (1-12) = "))

if jam_pulang >= jam_masuk:
    lama_kerja = jam_pulang - jam_masuk
else:
    lama_kerja = (12 - jam_masuk) + jam_pulang

print(f"Lama bekerja =  {lama_kerja} jam")