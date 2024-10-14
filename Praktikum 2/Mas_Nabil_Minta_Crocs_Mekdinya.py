# Input bilangan
N = int(input())          
B = list(map(int, input().split())) 

# Variabel untuk menyimpan hasil perkalian
hasil = 1

# Menghitung nilai XOR
for i in range(N):
    for j in range(i + 1, N):
        xor_value = B[i] ^ B[j]
        hasil *= xor_value
        
       
        if hasil == 0:
            break
   
    if hasil == 0:
        break

# Print output
print(hasil)
