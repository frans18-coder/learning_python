import math

def hitung_jarak(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

print("Jarak:", hitung_jarak(x1, y1, x2, y2))
