# Input string
s = input()

# menghitung batu, total kerugian dan total batu yang hancur
batu = []
total_kerugian = 0 
total_batu_hancur = 0 

# Identifikasi batunya satu persatu
for i in s:
    if batu and batu [-1] == i:
        batu.pop()
        total_batu_hancur += 1
        total_kerugian += ord(i) * 1000 * 2

    else:
        batu.append(i) 

# Menghitung sisa batu
sisa_batu = len(batu)

print("Di gudang tersisa", sisa_batu, "batu")

if total_batu_hancur > 0:
    print("Total kerugian: ", total_kerugian, "Dolar Imbu")

else:
    print("Wah, Jotaro Joemama tidak jadi dipecat")