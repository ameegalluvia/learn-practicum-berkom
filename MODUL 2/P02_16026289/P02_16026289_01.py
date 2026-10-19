# NIM/Nama  : 16026289/Abdus Salam Faiz
# Tanggal   : 15 Oktober 2026
# Deskripsi : Program ini mengecek kelayakan laptop Tuan Mik untuk bermain gim.. Dengan melihat ram dan penyimpanan yang diberikan,
#             Kita cek, Apakah RAM lebih dari sama dengan 16 GB dan Penyimpanannya lebih dari sama dengan 512 GB?

ram = int(input("Masukkan RAM (GB): "))
disk = int(input("Masukkan penyimpanan (GB): "))

if ram < 16 and disk >= 512:
    print("Tidak Layak (RAM tidak memenuhi syarat minimal)")
elif disk < 512 and ram >= 16:
    print("Tidak Layak (penyimpanan tidak memenuhi syarat minimal)")
elif ram < 16 and disk < 512:
    print("Tidak Layak (RAM dan penyimpanan tidak memenuhi syarat minimal)")
else:
    print("Layak")