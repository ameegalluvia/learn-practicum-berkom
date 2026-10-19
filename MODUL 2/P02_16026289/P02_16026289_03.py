# NIM/Nama  : 16026289/Abdus Salam Faiz
# Tanggal   : 15 Oktober 2026
# Deskripsi : Program untuk mengubah masukan integer ABC digabung menjadi bilangan terbesar dari penyusun penyusunnya

a = int(input("Masukkan kartu A: "))
b = int(input("Masukkan kartu B: "))
c = int(input("Masukkan kartu C: "))

a_baru = 0
b_baru = 0
c_baru = 0

a_new = 0
b_new = 0
c_new = 0

jumlah_digit = 100

#Untuk mengetahui urutan digit
if a >= 10:
    a_baru = a
    jumlah_digit *= 10
else:
    a_baru = a * 11

if b >= 10:
    b_baru = b
    jumlah_digit *= 10
else:
    b_baru = b * 11

if c >= 10:
    c_baru = c
    jumlah_digit *= 10
else:
    c_baru = c * 11



#Urutin jadiin ratusan/ribuan
#Bilangan Pertama
if a_baru > b_baru and a_baru > c_baru:
    if a < 10:
        a_new = a * jumlah_digit
        jumlah_digit = jumlah_digit // 10
    else:
        a_new = a * (jumlah_digit // 10)
        jumlah_digit = jumlah_digit // 100
    a_baru = 0
elif b_baru > a_baru and b_baru > c_baru:
    if  b < 10:
        b_new = b * jumlah_digit
        jumlah_digit = jumlah_digit // 10
    else:
        b_new = b * (jumlah_digit // 10)
        jumlah_digit = jumlah_digit // 100
    b_baru = 0
elif c_baru > a_baru and c_baru > b_baru:
    if c < 10:
        c_new = c * jumlah_digit
        jumlah_digit = jumlah_digit // 10
    else:
        c_new = c * (jumlah_digit // 10)
        jumlah_digit = jumlah_digit // 100
    c_baru = 0
elif a_baru == b_baru:
    if a > b:
        if a < 10:
            a_new = a * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            a_new = a * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        a_baru = 0
    else:
        if  b < 10:
            b_new = b * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            b_new = b * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        b_baru = 0
elif a_baru == c_baru:
    if a > c:
        if a < 10:
            a_new = a * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            a_new = a * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        a_baru = 0
    else:
        if  c < 10:
            c_new = c * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            c_new = c * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        c_baru = 0
elif b_baru == c_baru:
    if b > c:
        if b < 10:
            b_new = b * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            b_new = b * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        b_baru = 0
    else:
        if  c < 10:
            c_new = c * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            c_new = c * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        c_baru = 0


#Urutin jadiin ratusan/ribuan
#Bilangan Kedua
if a_baru > b_baru and a_baru > c_baru:
    if a < 10:
        a_new = a * jumlah_digit
        jumlah_digit = jumlah_digit // 10
    else:
        a_new = a * (jumlah_digit // 10)
        jumlah_digit = jumlah_digit // 100
    a_baru = 0
elif b_baru > a_baru and b_baru > c_baru:
    if  b < 10:
        b_new = b * jumlah_digit
        jumlah_digit = jumlah_digit // 10
    else:
        b_new = b * (jumlah_digit // 10)
        jumlah_digit = jumlah_digit // 100
    b_baru = 0
elif c_baru > a_baru and c_baru > b_baru:
    if c < 10:
        c_new = c * jumlah_digit
        jumlah_digit = jumlah_digit // 10
    else:
        c_new = c * (jumlah_digit // 10)
        jumlah_digit = jumlah_digit // 100
    c_baru = 0
elif a_baru == b_baru:
    if a > b:
        if a < 10:
            a_new = a * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            a_new = a * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        a_baru = 0
    else:
        if  b < 10:
            b_new = b * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            b_new = b * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        b_baru = 0
elif a_baru == c_baru:
    if a > c:
        if a < 10:
            a_new = a * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            a_new = a * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        a_baru = 0
    else:
        if  c < 10:
            c_new = c * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            c_new = c * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        c_baru = 0
elif b_baru == c_baru:
    if b > c:
        if b < 10:
            b_new = b * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            b_new = b * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        b_baru = 0
    else:
        if  c < 10:
            c_new = c * jumlah_digit
            jumlah_digit = jumlah_digit // 10
        else:
            c_new = c * (jumlah_digit // 10)
            jumlah_digit = jumlah_digit // 100
        c_baru = 0

#Urutin jadiin ratusan/ribuan
#Bilangan Ketiga
if a_baru > b_baru and a_baru > c_baru:
    if a < 10:
        a_new = a * jumlah_digit
    else:
        a_new = a * (jumlah_digit // 10)
    a_baru = 0
elif b_baru > a_baru and b_baru > c_baru:
    if  b < 10:
        b_new = b * jumlah_digit
    else:
        b_new = b * (jumlah_digit // 10)
    b_baru = 0
elif c_baru > a_baru and c_baru > b_baru:
    if c < 10:
        c_new = c * jumlah_digit
    else:
        c_new = c * (jumlah_digit // 10)
    c_baru = 0
elif a_baru == b_baru:
    if a > b:
        if a < 10:
            a_new = a * jumlah_digit
        else:
            a_new = a * (jumlah_digit // 10)
        a_baru = 0
    else:
        if  b < 10:
            b_new = b * jumlah_digit
        else:
            b_new = b * (jumlah_digit // 10)
        b_baru = 0
elif a_baru == c_baru:
    if a > c:
        if a < 10:
            a_new = a * jumlah_digit
        else:
            a_new = a * (jumlah_digit // 10)
        a_baru = 0
    else:
        if  c < 10:
            c_new = c * jumlah_digit
        else:
            c_new = c * (jumlah_digit // 10)
        c_baru = 0
elif b_baru == c_baru:
    if b > c:
        if b < 10:
            b_new = b * jumlah_digit
        else:
            b_new = b * (jumlah_digit // 10)
        b_baru = 0
    else:
        if  c < 10:
            c_new = c * jumlah_digit
        else:
            c_new = c * (jumlah_digit // 10)
        c_baru = 0

print(a_new + b_new + c_new)