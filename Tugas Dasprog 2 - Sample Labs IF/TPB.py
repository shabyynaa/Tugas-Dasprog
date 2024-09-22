# Input angka n
N = int(input())

# misal angka itu prima
is_prime = True

# identifikasi n bilangan prima atau tidak
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        is_prime = False
        break

if is_prime:
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")