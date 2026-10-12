#Nama/NIM: Abdus Salam Faiz/16026289
#Deskripsi: Program ini digunakan untuk menentukan apakah ruas garis yang dibentuk oleh dua titik (x1, y1) dan (x2, y2) merupakan ruas garis rizz atau bukan. Ruas garis rizz didefinisikan sebagai ruas garis yang memiliki kemiringan (m) antara -1 dan 1, serta tidak melewati sumbu x atau sumbu y.

x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))

m = (y2 - y1) / (x2 - x1)

if (x1 > 0 and x2 < 0) or (x1 < 0 and x2 > 0) or (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0):
    print("Bukan ruas garis rizz")
elif m >= -1 and m <= 1:
    print("Ruas garis tersebut merupakan ruas garis rizz")
else:
    print("Bukan ruas garis rizz")
