# NIM/Nama: 16026289/Abdus Salam Faiz
# Tanggal: 30 September 2026
# Deskripsi: Program ini menghitung jumlah kembalian yang harus diberikan kepada Nona Sal dalam bentuk pecahan uang.

a = int(input("Masukkan jumlah pembayaran (rupiah): "))
b = int(input("Masukkan harga barang (rupiah): "))

kembalian = a - b

uang50 = kembalian // 50000
sisa50 = kembalian % 50000

uang20 = sisa50 // 20000
sisa20 = sisa50 % 20000

uang10 = sisa20 // 10000
sisa10 = sisa20 % 10000

uang5 = sisa10 // 5000
sisa5 = sisa10 % 5000

uang1 = sisa5 // 1000

print(f"Nona Sal perlu memberikan {uang50} lembar uang Rp 50.000, {uang20} lembar uang Rp 20.000, {uang10} lembar uang Rp 10.000, {uang5} lembar uang Rp 5.000, dan {uang1} lembar uang Rp 1.000.")