#NIM/Nama: 16026289/Abdus Salam Faiz
#Tanggal: 30 September 2026
#Deskripsi: Program ini menghitung waktu selesai dari proses yang dimulai pada jam dan menit tertentu dengan durasi proses tertentu.

jam = int(input("Jam mulai (H): "))
menit = int(input("Menit mulai (M): "))
proses = int(input("Durasi proses (T) (menit): "))

jam_proses = proses // 60
menit_proses = proses % 60

total_jam = jam + jam_proses
total_menit = menit + menit_proses

hari = total_jam // 24

jam_selesai = total_jam % 24
menit_selesai = total_menit % 60

print(f"Hari dilewati: {hari}")
print(f"Waktu selesai: {jam_selesai}:{menit_selesai}")