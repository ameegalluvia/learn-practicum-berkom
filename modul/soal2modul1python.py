#NIM/Nama: 16026289/Abdus Salam Faiz
#Tanggal: 30 September 2026
#Deskripsi: Program ini menghitung nomor kursi yang berada di cermin dari kursi yang dipilih oleh Nona Sal.

n = int(input("Jumlah baris kursi (n): "))
m = int(input("Jumlah kolom kursi (m): "))
k = int(input("Nomor kursi yang dipilih (k): "))

x_kursi = (k - 1) // m
y_kursi = (k - 1) % m

x_mirror = (n - 1) - x_kursi
y_mirror = (m - 1) - y_kursi

k_mirror = x_mirror * m + y_mirror + 1

print(f"Kursi yang dipilih: baris {x_kursi + 1}, kolom {y_kursi + 1}")
print(f"Kursi di cermin: baris {x_mirror + 1}, kolom {y_mirror + 1}")
print(f"Nomor kursi di cermin: {k_mirror}")