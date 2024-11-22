def pangkat(bilangan, eksponen):
    return bilangan ** eksponen

bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))
print(f"{bilangan} pangkat {eksponen} adalah {pangkat(bilangan, eksponen)}")