t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    q = int(input())

    # Cari nilai maksimum
    if q == 1:
        maksimal = float('-inf')
        for i in range(n):
            current_sum = 0
            for j in range(i, min(i + k, n)):
                current_sum += A[j]
                maksimal = max(maksimal, current_sum)
        print(maksimal)
    # Cari nilai minimum
    else:
        minimal = float('inf')
        for i in range(n):
            current_sum = 0
            for j in range (i, min(i + k, n)):
                current_sum += A[j]
                minimal = min(minimal, current_sum)
        print(minimal)