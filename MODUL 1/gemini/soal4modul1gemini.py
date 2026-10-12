#NIM/Nama: 16026289/Abdus Salam Faiz
#Tanggal: 30 September 2026
#Deskripsi: Program ini menghitung pemain akhir pemegang bola dan banyak putaran penuh berdasarkan jumlah pemain dan banyak lemparan.

#Input nilai jumlah pemain (P) dan banyak lemparan (K)
p = int(input("Jumlah pemain (P): "))
k = int(input("Banyak lemparan (K): "))

#Menghitung pemain akhir pemegang bola dan banyak putaran penuh
pemain = k % p
putaran = k // p

#Output hasil perhitungan
print(f"Pemain akhir pemegang bola: {pemain + 1}")
print(f"Banyak putaran penuh: {putaran}")
