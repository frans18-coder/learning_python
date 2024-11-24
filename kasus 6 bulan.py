bulan_sekarang = int(input("Masukkan bulan saat ini (1-12): "))
bulan_ke_depan = int(input("Masukkan berapa bulan ke depan: "))

bulan_pernikahan = bulan_sekarang + bulan_ke_depan

if bulan_pernikahan > 12:
    bulan_pernikahan = bulan_pernikahan - 12

print(f"Bulan pernikahan adalah bulan ke-{bulan_pernikahan}")