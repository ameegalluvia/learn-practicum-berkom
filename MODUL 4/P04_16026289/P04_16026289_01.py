# NIM/Nama : 16026289 / Abdus Salam Faiz
# Tanggal : 12 November 2026
# Deskripsi : Program untuk menentukan jenis segitiga berdasarkan input pengguna, di mana yang pertama mengecek kevalidan dari segitiga, lalu baru menentukan jenis segitiga


def cek_sisi_terpanjang(sisi):
    max = sisi[0]
    for i in range(len(sisi)):
        if sisi[i] > max:
            max = sisi[i]
    sisi.remove(max)

    return max


def cek_valid(max, sisi):
    if max < sisi[0] + sisi[1]:
        return True
    else:
        return False


def cek_segitiga(max, sisi):
    if max * max == sisi[0] * sisi[0] + sisi[1] * sisi[1]:
        return "Ketiga sisi membentuk segitiga siku-siku."
    elif max * max > sisi[0] * sisi[0] + sisi[1] * sisi[1]:
        return "Ketiga sisi membentuk segitiga tumpul."
    elif max * max < sisi[0] * sisi[0] + sisi[1] * sisi[1]:
        return "Ketiga sisi membentuk segitiga lancip."


def main():
    sisi = []
    for i in range(3):
        s = int(input(f"Masukkan panjang sisi ke-{i+1}: "))
        sisi.append(s)

    max = cek_sisi_terpanjang(sisi)

    if cek_valid(max, sisi):
        print(cek_segitiga(max, sisi))
    else:
        print("Ketiga sisi tidak dapat membentuk segitiga.")


main()
