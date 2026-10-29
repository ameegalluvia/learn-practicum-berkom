# NIM/Nama : 16026289 / Abdus Salam Faiz
# Tanggal : 29 Oktober 2026
# Deskripsi : Program yang melihat tumpukan buku dari sisi kanan dan kiri, di mana jika dilihat dari kiri buku awal jadi acuan pertama, lalu looping jika tinggi buku kedua lebih dari atau sama dengan buku pertama, maka buku kedua bisa dilihat.. dan buku kedua jadi acuan baru..
# Tetapi kalau saya itu cari dulu nilai tinggi maks dari buku.. Kemudian saat mencapai tinggi maks, baik dilihat dari kiri maupun kanan, itu bakal distop loopingannya

n = int(input("Masukkan jumlah tumpukan buku (N): "))

tinggi = []

kiri = 0
kanan = 0

for i in range(n):
    data = int(input(f"Masukkan tinggi tumpukan ke-{i+1}: "))
    tinggi.append(data)

awal = tinggi[0]
akhir = tinggi[-1]

acuan = tinggi[0]

maks = tinggi[0]

estetik = True


# cari nilai maks
for i in range(n):
    if tinggi[i] > maks:
        maks = tinggi[i]
    elif tinggi[i] == maks:
        estetik = False

# tambahin kiri dan kanan dengan adanya titik acuan dan maks
for i in range(n):
    if tinggi[i] == maks:
        kiri += 1
        break
    elif tinggi[i] >= acuan:
        acuan = tinggi[i]
        kiri += 1

for i in range(n):
    if tinggi[-(i + 1)] == maks:
        kanan += 1
        break
    elif tinggi[-(i + 1)] >= akhir:
        acuan = tinggi[-(i + 1)]
        kanan += 1


print(f"Terlihat dari kiri: {kiri} tumpukan.")
print(f"Terlihat dari kiri: {kanan} tumpukan.")

if kiri == kanan and estetik == True:
    print("Susunan buku sudah estetik.")
else:
    print("Susunan buku belum estetik.")
