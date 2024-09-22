# input banyaknya test case
T = int(input()) 
test_case = []

for i in range (T):
    A, B = map(int, input().split())
    test_case.append((A, B))

# Identifikasi angka prima
limit = 10**6
prima = []
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False # karena 0 dan 1 bukan bilangan prima

for angka in range(2, limit + 1):
    if is_prime[angka]:
        prima.append(angka)
    for multiple in range(angka * angka, limit + 1, angka):
        is_prime[multiple] = False

for i in range(T):
    A, B = test_case[i]
    print("Test Case #", i + 1, ":")
    for j in range(A - 1, B):
        print(prima[j])
