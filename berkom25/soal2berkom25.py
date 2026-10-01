# NIM/Nama: 16026289/Abdus Salam Faiz
# Tanggal: 30 September 2026
# Deskripsi: Program ini menghitung total pendapatan dari penjualan barang A, B, dan C dengan harga bundle identik dan harga spesial per item.

A = int(input("Jumlah barang A (a): "))
B = int(input("Jumlah barang B (b): "))
C = int(input("Jumlah barang C (c): "))
K = int(input("Jumlah bundle identik (k): "))
Hb = int(input("Harga bundle identik (hb):  "))
Hs = int(input("Harga spesial per item (hs):  "))

bundle_special = (A % K) + (B % K) + (C % K)

total_harga = Hb * K + Hs * bundle_special

print("Total Pendapatan:", total_harga)