warna = input("Masukkan warna lampu (merah, kuning, hijau): ").lower()

if warna == "merah":
    print("Lampu merah! Berhenti.")
elif warna == "kuning":
    print("Lampu kuning! Bersiap-siap.")
elif warna == "hijau":
    print("Lampu hijau! Jalan.")
else:
    print("Warna tidak valid! Harap masukkan merah, kuning, atau hijau.")
