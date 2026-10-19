sulit1 = int(input("Masukkan tingkat kesulitan backlog 1: "))
estimasi1 = int(input("Masukkan estimasi waktu backlog 1: "))

sulit2 = int(input("Masukkan tingkat kesulitan backlog 2: "))
estimasi2 = int(input("Masukkan estimasi waktu backlog 2: "))

sulit3 = int(input("Masukkan tingkat kesulitan backlog 3: "))
estimasi3 = int(input("Masukkan estimasi waktu backlog 3: "))

sulit4 = int(input("Masukkan tingkat kesulitan backlog 4: "))
estimasi4 = int(input("Masukkan estimasi waktu backlog 4: "))

if sulit1 == sulit2 or sulit1 == sulit3 or sulit2 == sulit3:
    if estimasi1 < estimasi2:
        
elif sulit1 == 3:
    print(f"Backlog yang dikerjakan oleh senior adalah backlog 1 dengan waktu estimasi {estimasi1} hari")
elif sulit2 == 3:
    print(f"Backlog yang dikerjakan oleh senior adalah backlog 2 dengan waktu estimasi {estimasi1} hari")
elif sulit3 == 3:
    print(f"Backlog yang dikerjakan oleh senior adalah backlog 1 dengan waktu estimasi {estimasi1} hari")