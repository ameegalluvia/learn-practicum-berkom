koin = 1
level = []
j = 1
trap = 0
total = 0

while koin != 0:
    koin = int(input(f"Level {j} - Koin yang didapat (0 untuk berhenti): "))
    if koin < 0:
        trap += 1
    level.append(koin)
    j += 1

max = level[0]

for i in range(len(level)):
    if level[i] > max:
        max = level[i]
        k = i
    total += level[i]
    if total < 0:
        cum = True

print(f"Total koin terkumpul: {total} koin")
print(f"Level terbaik: Level {k + 1} dengan {max} koin")
print(f"Jumlah trap yang dilewati: {trap} trap")


if cum == True:
    print("COMEBACK! Kamu berhasil bangkit dari koin negatif!")
elif total >= 0:
    print("Status Tidak ada comeback (koin selalu positif)")
else:
    print("Status Kalah (koin selalu negatif)")
