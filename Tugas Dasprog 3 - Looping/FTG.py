# Input panjang dan tebal bingkai
N, M = map(int, input().split())

# Baris pertama bingkai
for i in range(M):
    print('*' * N)

# Baris tengah bingkai
for _ in range(N - 2 * M):
    print('*' * M + ' ' * (N - 2 * M) + '*' * M)

# Baris terakhir bingkai
for i in range(M):
    print('*' * N) 

