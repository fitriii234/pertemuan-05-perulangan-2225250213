# 03 - Validasi Input

print("=== VALIDASI NILAI ===")

nilai = float(input("Masukkan nilai (0-100): "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid. Masukkan nilai antara 0 sampai 100.")
    nilai = float(input("Masukkan nilai (0-100): "))

print(f"Nilai {nilai} valid.")