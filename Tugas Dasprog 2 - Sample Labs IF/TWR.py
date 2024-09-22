# input nomor-nomor topi kucing
a = [int(x) for x in input().split()]

# input jumlah kucing yang lompat dari belakang ke depan
b = int(input())

# input berapa kali kucing lompat
c = int(input())

# indeks yang harus di cek setelah lompat
d, e, f = map(int, input().split())

# pengulangan lompat sebanyak "c" kali
for i in range(c):
    a = a[-b:] + a[:-b]

# output angka yang diminta oleh penyihir
print(a[d], a[e], a[f])
