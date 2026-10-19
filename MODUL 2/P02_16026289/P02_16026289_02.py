# NIM/Nama  : 16026289/Abdus Salam Faiz
# Tanggal   : 15 Oktober 2026
# Deskripsi : Program untuk mengecek hasil jenit racikan mantra yang dibuat Tuan Ky menurut buku materi peracikan mantra
#             Dengan input tanaman 1 dan 2 lalu jenis pelarut.. dan Outputnya adalah jenis mantra yang dihasilkan

tanaman1 = str(input("Masukkan tanaman pertama: "))
tanaman2 = str(input("Masukkan tanaman kedua: "))

pelarut = str(input("Masukkan cairan pelarut: "))

if ((tanaman1 == "jahe" and tanaman2 == "kunyit") or (tanaman1 == "kunyit" and tanaman2 == "jahe")) and (pelarut == "air"):
    print("Tuan Ky berhasil meracik mantra kilat.")
elif ((tanaman1 == "kunyit" and tanaman2 == "kencur") or (tanaman1 == "kencur" and tanaman2 == "kunyit")) and (pelarut == "susu"):
    print("Tuan Ky berhasil meracik mantra penyembuh.")
elif ((tanaman1 == "jahe" and tanaman2 == "kencur") or (tanaman1 == "kencur" and tanaman2 == "jahe")) and (pelarut == "minyak"):
    print("Tuan Ky berhasil meracik mantra racun.")
else:
    print("Tuan Ky gagal meracik mantra.")
