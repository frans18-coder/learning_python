a = int(input("masukan nilai 1-100 untuk pengelompokan = "))

if a <= 50:
    if a <= 25:
        print("A1")
    else:
        print("A2")
elif a <= 100:
    if a <= 75:
        print("B1")
    else:
        print("B2")
else:
    print("tidak valid") 



