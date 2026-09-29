# Kuis 2 - Deret Aritmetika

print("=== DERET ARITMETIKA ===")

a = float(input("Masukkan suku pertama (a): "))
d = float(input("Masukkan beda (d): "))
n = int(input("Masukkan banyak suku (n): "))

while n <= 0:
    print("Banyak suku harus lebih dari 0.")
    n = int(input("Masukkan banyak suku (n): "))

total = 0

for i in range(n):
    suku = a + (i * d)
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Total deret = {total:.2f}")