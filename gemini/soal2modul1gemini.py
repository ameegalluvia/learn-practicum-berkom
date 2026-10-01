#NIM/Nama: 16026289/Abdus Salam Faiz
#Tanggal: 30 September 2026
#Deskripsi: Program ini menghitung lokasi barang berdasarkan nomor barang yang diberikan.

l = int(input("Jumlah lantai (L): "))
b = int(input("Jumlah baris per lantai (B): "))
k = int(input("Jumlah kotak per baris (K): "))

n = int(input("Nomor barang (N): "))

lantai = (n - 1) // (b * k)
sisa_barang = (n - 1) % (b * k)
baris = sisa_barang // k
kotak = sisa_barang % k

print(f"Barang berada di Lantai {lantai + 1}, Baris {baris + 1}, Kotak {kotak + 1}")