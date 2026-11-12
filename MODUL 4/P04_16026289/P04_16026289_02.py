# NIM/Nama : 16026289 / Abdus Salam Faiz
# Tanggal : 12 November 2026
# Deskripsi : Program untuk menilai kekuatan dari PIN berdasarkan input pengguna dan aturan yang berlaku


def cek_kekuatan(pin):
    poin = 0
    simpan = []
    for i in range(len(pin)):
        if pin[i].isdigit() and pin[i] not in simpan:
            simpan.append(pin[i])
            poin += 4

    if len(pin) >= 8:
        poin += 15
    elif len(pin) >= 6:
        poin += 5

    for i in range(len(pin)):
        if pin[i].isupper():
            poin += 10
            break

    for i in range(len(pin) - 1):
        if pin[i].isdigit() and pin[i + 1].isdigit():
            if (
                int(pin[i]) - int(pin[i + 1]) == 1
                or int(pin[i]) - int(pin[i + 1]) == -1
            ):
                poin -= 5

    return poin


def main():
    n = int(input("Masukkan jumlah kandidat PIN (N): "))
    kuat = 0
    sedang = 0
    lemah = 0
    for i in range(n):
        pin = list(input(f"Kandidat PIN ke-{i+1}: "))
        if cek_kekuatan(pin) >= 40:
            print(f"PIN ke-{i+1} skornya {cek_kekuatan(pin)}, tergolong Kuat.")
            kuat += 1
        elif cek_kekuatan(pin) >= 20:
            print(f"PIN ke-{i+1} skornya {cek_kekuatan(pin)}, tergolong Sedang.")
            sedang += 1
        else:
            print(f"PIN ke-{i+1} skornya {cek_kekuatan(pin)}, tergolong Lemah.")
            lemah += 1

    print(f"Rekap: Kuat {kuat}, Sedang {sedang}, Lemah {lemah}")


main()
