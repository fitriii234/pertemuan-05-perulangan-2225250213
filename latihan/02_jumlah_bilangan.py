# 02 - Jumlah Bilangan

print("=== JUMLAH BILANGAN ===")

n = int(input("Masukkan bilangan n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah bilangan 1 sampai {n} = {total}")