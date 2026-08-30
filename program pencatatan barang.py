Daftar_Barang = []



print("=== PROGRAM PENCATAT BARANG ===")

Jumlah = int(input("berapa barang yang ingin kamu catat? "))

for i in range(Jumlah):
    nama_barang = input(f"masukkan nama barang ke-{i + 1}: ")
    Daftar_Barang.append(nama_barang)

print("\nHASIL CATATAN BARANG:")

for Barang in Daftar_Barang:
    if len(Barang) > 5:
        print(f"- {Barang} (Barang dengan jumlah huruf lebih dari 5)")
    else:
        print(f"- {Barang} (barang dengan jumlah huruf kurang dari 5)")

print(f"total: {len(Daftar_Barang)} barang.")
