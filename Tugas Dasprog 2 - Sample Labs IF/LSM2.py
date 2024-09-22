# Input jumlah bolah (N) dan urutan pemain (C)
N, C = map(int, input().split())

# Menentukan pemenang berdasarkan jumlah bola (N)
if (N - 1) % 3 == 0:
    if C == 1:
        print("Lili")
    else:
        print("Lala")
else:
    if C == 1:
        print("Lala")
    else:
        print("Lili")