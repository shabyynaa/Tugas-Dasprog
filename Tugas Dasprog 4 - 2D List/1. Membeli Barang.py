# Input bilangan bulat 
N, M = map(int, input().split())

# Input N bilangan bulat Pi (harga b)
harga_barang = list(map(int, input().split()))

# Input M bilangan bulat Ci (nilai uang)
nilai_uang = list(map(int, input().split()))

# Hitung total harga barang yang dibeli 
total_harga = 0
for harga in harga_barang:
    if harga > 0:
        total_harga += harga

# Hitung uang yang dimiliki Bu Chanek
total_uang = 0
for uang in nilai_uang: 
    if uang < 0:
        total_uang += uang

# Hitung Kemungkinan hutang terbanyak
hutang = total_uang - total_harga

# print output 
print(hutang)