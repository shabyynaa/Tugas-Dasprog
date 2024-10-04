# Input bilangan bulat r, c, N
r, c, N = map(int, input().split())

# Input jumlah emas di setiap petak
hutan = []
for _ in range(r):
    hutan.append(list(map(int, input().split())))

# Input gerakan Pak Dengklek
gerakan = input()

# Posisi awal Pak Dengklek
i, j = 0, 0

# Emas awal yang diambil di posisi awal
emas = hutan[i][j]

# Proses setiap gerakan Pak Dengklek 
for langkah in gerakan:
    if langkah == 'L':  
        j -= 1
        emas -= 2
    elif langkah == 'R': 
        j += 1
        emas += 3
    elif langkah == 'D': 
        i += 1
        emas -= 2
    elif langkah == 'U': 
        i -= 1
        emas += 3

    # Cek Pak Dengklek keluar dari area hutan
    if i < 0 or i >= r or j < 0 or j >= c:
        print("gerakanmu salah bung!")
        break
    else:
        emas += hutan[i][j]

# Print Output
else:
    print(emas)
