# NIM/Nama : 16026289 / Abdus Salam Faiz
# Tanggal : 29 Oktober 2026
# Deskripsi : Program yang mengecek apakah volume genangan melebihi toleransi tidak, kalau lebih maka kaktus tuan ky membusuk, jika tidak lebih maka aman

n = int(input("Masukkan panjang kebun: "))
h = list(map(int, input("Masukkan array ketinggian tanah: ").split()))
t = int(input("Masukkan batas toleransi air: "))

maks = h[0]
kiri = h[0]
kanan = h[-1]

volume = 0

for i in range(len(h) - 1):
    if h[i] > maks:
        maks = h[i]

for i in range(len(h) - 1):
    if kiri != maks:
        if i == 0 or i == len(h) - 1:
            volume += 0
        elif h[i] <= maks:
            if h[i] < kiri and h[i] < maks:
                volume += kiri - h[i]
            if h[i] == maks:
                kiri = maks
    else:
        if h[i] < kanan and h[i] < maks:
            volume += kanan - h[i]

print(f"Total volume genangan air adalah {volume}")

if volume > t:
    print("Kaktus Tuan Ky mati membusuk!")
else:
    print("Kaktus Tuan Ky selamat!")
