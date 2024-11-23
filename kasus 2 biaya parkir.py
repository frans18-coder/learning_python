jam_masuk = int(input("Masukkan jam masuk (1-12)  = "))
jam_keluar = int(input("Masukkan jam keluar (1-12) = "))

if jam_keluar >= jam_masuk :
    total_jam = jam_keluar - jam_masuk
    
else :
    total_jam = (12 - jam_masuk) + jam_keluar
    
if total_jam <= 2 :
    biaya_parkir = 2000
    
else :
    biaya_parkir = 2000 + ((jam_keluar - 2) * 500)
    
print(f"Lama parkir  : {total_jam} jam")
print(f"Biaya parkir: Rp {biaya_parkir}")