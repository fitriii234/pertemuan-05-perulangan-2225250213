# 01 - Tabel Perkalian

print("=== TABEL PERKALIAN ===")

n = int(input("Masukkan bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")