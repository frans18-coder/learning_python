def cek_palindrom(n):
    return str(n) == str(n)[::-1]

for i in range(1, 101):
    if cek_palindrom(i):
        print(i)
