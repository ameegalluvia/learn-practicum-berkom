# NIM/Nama: 16026289/Abdus Salam Faiz
# Tanggal: 30 September 2026
# Deskripsi: Program ini menghitung password baru berdasarkan password lama dan nilai x.

password_lama = int(input("Password lama: "))
nilai_x = int(input("Nilai x: "))

#Digit Satuan dari Password lama
d1 = password_lama % 10
d2 = (password_lama // 10) % 10
d3 = (password_lama // 100) % 10
d4 = (password_lama // 1000) % 10
d5 = (password_lama // 10000) % 10

#Digit Satuan dikalikan dengan nilai x
s1 = (d1 * nilai_x) % 10
s2 = (d2 * nilai_x) % 10
s3 = (d3 * nilai_x) % 10
s4 = (d4 * nilai_x) % 10
s5 = (d5 * nilai_x) % 10

tambahan = s1 + s2 + s3 + s4 + s5
password_baru = password_lama + tambahan

print(f"Password baru: {password_baru}")