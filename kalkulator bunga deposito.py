def hitung_bunga(saldo, suku_bunga, waktu):
    return saldo * suku_bunga / 100 * waktu

saldo = float(input("Masukkan saldo: "))
suku_bunga = float(input("Masukkan suku bunga (%): "))
waktu = float(input("Masukkan waktu (tahun): "))

print("Bunga:", hitung_bunga(saldo, suku_bunga, waktu))
