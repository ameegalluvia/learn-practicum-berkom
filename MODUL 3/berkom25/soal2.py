surat = list(input("Masukkan isi surat: ").split())

larang = input("Masukkan kata terlarang: ").lower()

i = 0

for kata in surat:
    masuksurat = kata.lower()
    if larang in masuksurat:
        surat[i] = str("*" * len(kata))
    i += 1

keluaran = " ".join(surat)
print(f"Isi surat setelah sensor: {keluaran}")
