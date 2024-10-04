# Input bilangan bulat N, r, c
N, r, c = map(int, input().split())
posisi_siswa= {} 

# Input nomor urut siswa dan posisi duduk siswa
for i in range (N):
    x, a, b = map(int, input().split())
    posisi_siswa[a, b] = x

# Cek yang bersebelahan
for i in range (1, N + 1):
    ada = False
    for (a, b), siswa in posisi_siswa.items():
        if siswa == i:
            if (a, b - 1) in posisi_siswa:
                print(posisi_siswa[(a, b - 1)])
                ada = True
            elif (a, b + 1) in posisi_siswa:
                print(posisi_siswa[(a, b + 1)]) 
                ada = True
            break
    if not ada:
        print(0)
# print(posisi_siswa)