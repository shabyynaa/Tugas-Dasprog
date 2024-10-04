# Input N (Jenis buah) dan K (Uang yang dimiliki Pak Dengklek)
N, K = map(int, input().split())

# Input Harga Buah
harga_buah = list(map(int, input().split()))

# Kemungkinan buah yang bisa dibeli
jumlah_buah = 0
for harga in harga_buah:
    if harga <= K:
        jumlah_buah += 1

# Print output
print(jumlah_buah)

