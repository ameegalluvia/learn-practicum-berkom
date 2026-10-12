#Nama/NIM: Abdus Salam Faiz/16026289
#Deskripsi: Program ini digunakan untuk menghitung jumlah voucher yang didapatkan oleh Nona Sal berdasarkan jumlah poin yang dimasukkan. Voucher A bernilai 50 poin, Voucher B bernilai 30 poin, dan Voucher C bernilai 10 poin. Program akan menghitung berapa banyak masing-masing voucher yang bisa didapatkan dan sisa poin yang tersisa setelah penukaran. 

poin = int(input("Masukkan jumlah poin Nona Sal: "))

a = 0
b = 0
c = 0

if poin >= 50:
    a = poin // 50
    poin = poin % 50
    
if poin >= 30:
    b = poin // 30
    poin = poin % 30

if poin >= 10:
    c = poin // 10
    poin = poin % 10
else:
    print("Poin Nona Sal tidak cukup untuk ditukar dengan voucher apapun.")
    exit()

print(f"Nona Sal mendapat {a} Voucher A, {b} Voucher B, dan {c} Voucher C dengan sisa poin {poin}.")