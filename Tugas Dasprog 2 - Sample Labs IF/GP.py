# Input kemampuan lompat B dan jarak antar tiang
n, A, B, C, D = map(int, input().split())

# identifikasi apakah jarak semua antar tiang bisa dilompati
if A <= n and B <= n and C <= n and D <= n: 
    print("YES HE CAN")

else:
    print("NO HE CAN'T")