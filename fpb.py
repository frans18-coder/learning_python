def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
print("FPB:", fpb(a, b))
