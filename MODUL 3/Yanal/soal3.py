n = int(input("Masukkan banyaknya reels: "))

likes = []

for i in range(n):
    a = int(input(f"Masukkan total likes reels ke-{i+1}: "))
    likes.append(a)

for i in range(n-1):
    if 