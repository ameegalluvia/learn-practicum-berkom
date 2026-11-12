n = int(input("Masukkan jumlah titik (N): "))

titik = []
gunung = 0
lembah = 0

naik = False
turun = False

for i in range(n):
    a = int(input(f"Masukkan nilai titik ke-{i+1}: "))
    titik.append(a)

for i in range(1, n - 1):
    if titik[i - 1] < titik[i] and titik[i + 1] < titik[i]:
        gunung += 1
    elif titik[i - 1] > titik[i] and titik[i + 1] > titik[i]:
        lembah += 1


if gunung == 0 and lembah == 0:
    for i in range(n - 1):
        if titik[i] > titik[i + 1]:
            naik = False
            turun = True
        else:
            naik = True
            turun = False
    if naik == True and turun == False:
        print("Grafik selalu naik secara monoton")
    elif naik == False and turun == True:
        print("Grafik selalu turun secara monoton")
    else:
        print("Grafik selalu horizontal")
else:
    print(f"Jumlah gunung: {gunung}")
    print(f"Jumlah lembah: {lembah}")
