# Input waktu GMT+2
HH, MM, SS = map(int, input().split(":"))

# Input waktu GMT+7
CH, CM, CS = map(int, input().split(":"))

# Convert semua waktu ke detik (GMT+7 - GMT+2 = 5 jam)
waktu_tayang = (HH * 3600 + MM * 60 + SS) + (5 * 3600)
waktu_sekarang = CH * 3600 + CM * 60 + CS

# calculate selisih waktu
selisih_waktu = waktu_tayang - waktu_sekarang

# identifikasi apakah Ali bisa menonton acaranya atau tidak
if selisih_waktu > 0:
    H = selisih_waktu // 3600
    selisih_waktu %= 3600
    M = selisih_waktu // 60
    S = selisih_waktu % 60
    print(H, "hours", M, "Minute", S, "Second")

else:
     print("See you on the next Pear Event!")