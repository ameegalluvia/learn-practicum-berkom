# NIM/Nama: 16026289/Abdus Salam Faiz
# Tanggal: 30 September 2026
# Deskripsi: Program ini menghitung total ongkos kirim berdasarkan ongkos dasar, jarak, dan biaya tambahan. 

B = int(input("Masukkan ongkos kirim dasar: "))
D = int(input("Masukkan jarak pengiriman (dalam km): "))
S = int(input("Masukkan biaya tambahan layanan: "))

total_ongkos = B * D + S
print(f"Total ongkos kirim adalah {total_ongkos} IDR.")