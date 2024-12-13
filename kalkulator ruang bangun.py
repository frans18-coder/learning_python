def hitung_luas(p, l):
    return p * l

def hitung_volume(p, l, t):
    return p * l * t

p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
t = float(input("Masukkan tinggi: "))

print("Luas:", hitung_luas(p, l))
print("Volume:", hitung_volume(p, l, t))
