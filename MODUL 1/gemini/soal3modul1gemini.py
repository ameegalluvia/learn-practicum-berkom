#NIM/Nama: 16026289/Abdus Salam Faiz
#Tanggal: 30 September 2026
#Deskripsi: Program ini menghitung PIN baru berdasarkan PIN lama dan nilai kunci yang diberikan.


pin_lama = int(input("Masukkan PIN lama: "))
nilai_kunci = int(input("Masukkan nilai kunci: "))

digit1 = pin_lama % 10
digit2 = (pin_lama // 10) % 10
digit3 = (pin_lama // 100) % 10
digit4 = (pin_lama // 1000) % 10

baru1 = (digit1 + nilai_kunci) % 10
baru2 = (digit2 + nilai_kunci) % 10
baru3 = (digit3 + nilai_kunci) % 10
baru4 = (digit4 + nilai_kunci) % 10

print(f"PIN baru: {baru1}{baru2}{baru3}{baru4}")