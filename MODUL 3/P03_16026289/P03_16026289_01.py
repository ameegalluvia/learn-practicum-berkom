# NIM/Nama : 16026289 / Abdus Salam Faiz
# Tanggal : 29 Oktober 2026
# Deskripsi : Mengubah urutan dari isi array yang dimasukkan, kaya konsep LIFO (Last In First Out)

n = int(input("Masukkan jumlah dokumen (N): "))

dok = []
hasil = []

for i in range(n):
    isi = int(input(f"Masukkan nomor dokumen ke-{i+1} yang ditumpuk: "))
    dok.append(isi)

for i in range(n):
    hasil.append(str(dok[-(i + 1)]))

print(f"Urutan pemindaian: {" ".join(hasil)}")
