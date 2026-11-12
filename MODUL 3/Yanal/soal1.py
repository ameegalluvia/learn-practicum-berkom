n = int(input("Masukkan jumlah dokumen (N): "))

dok = []
hasil = []

for i in range(n):
    isi = int(input(f"Masukkan nomor dokumen ke-{i+1} yang ditumpuk: "))
    dok.append(isi)

for i in range(n):
    hasil.append(str(dok[-(i + 1)]))

print(f"Urutan pemindaian: {" ".join(hasil)}")
