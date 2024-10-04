# input titik pusat lingkaran
x1, y1 = map(int, input().split())

# input titik awal
xs, ys = map(int, input().split())

# input titik akhir 
xf, yf = map(int, input().split())

# hitung jarak titik awal ke titik akhir
jarak_akhir = (xs - xf) ** 2 + (ys - yf) ** 2

# hitung jarak titik awal ke pusat lingkaran
jarak_pusat = (x1 - xf) ** 2 + (y1 - yf) ** 2

# identifikasi apakah King bisa sampai ke tempat tujuan
if jarak_pusat > jarak_akhir:
    print("Yes")
else:
    print("No")