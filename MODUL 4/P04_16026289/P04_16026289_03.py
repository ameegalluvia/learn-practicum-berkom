# NIM/Nama : 16026289 / Abdus Salam Faiz
# Tanggal : 12 November 2026
# Deskripsi : Program untuk menentukan apakah kapasitas truk cukup untuk memuat beban kontainer


def cek_kapasitas(kapasitas, bobot):
    transit = 0
    for i in range(len(bobot)):
        for j in range(len(kapasitas)):
            if bobot[i] <= kapasitas[j]:
                kapasitas[j] -= bobot[i]
                print(f"Kontainer {i+1} ({bobot[i]} ton) dialokasikan ke Truk {j+1}")
                break
        else:
            print(f"Kontainer {i+1} ({bobot[i]} ton) dialihkan ke Gudang Transit")
            transit += 1
    return transit


def main():
    m = int(input("Masukkan jumlah armada truk (M): "))
    kapasitas = []
    simpan = []
    bobot = []
    transit = 0
    for i in range(m):
        a = int(input(f"Kapasitas truk ke-{i+1} (ton): "))
        kapasitas.append(a)
        simpan.append(a)

    n = int(input(f"Masukkan jumlah kontainer (N): "))
    for i in range(n):
        b = int(input(f"Bobot kontainer ke-{i+1} (ton): "))
        bobot.append(b)

    transit = cek_kapasitas(kapasitas, bobot)

    print(f"Jumlah kontainer di gudang transit: {transit}")

    for i in range(m):
        print(
            f"Total muatan Truk {i+1}: {simpan[i]-kapasitas[i]} ton (Sisa kapasitas : {kapasitas[i]} ton)"
        )


main()
