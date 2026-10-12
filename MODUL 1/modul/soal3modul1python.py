#NIM/Nama: 16026289/Abdus Salam Faiz
#Tanggal: 30 September 2026
#Deskripsi: Program ini menghitung total denda keterlambatan berdasarkan waktu keterl

a = int(input("Waktu keterlambatan (menit): "))

denda1hari = (a // 1440) * 800000
sisa_denda1hari = a % 1440

denda1jam = (sisa_denda1hari // 60) * 25000
sisa_denda1jam = sisa_denda1hari % 60

denda5menit = (sisa_denda1jam // 5) * 1000

total_denda = denda1hari + denda1jam + denda5menit

print(f"Total denda yang harus dibayar: Rp {total_denda}")