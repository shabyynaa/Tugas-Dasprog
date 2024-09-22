# Input banyak mobil di depan, di belakang dan waktu
M, N, T = map(int, input().split())

# Input traffic light duration
Red_Light = 20
Yellow_Light = 5
Green_Light = 60

# Total waktu traffic light
Total_Traffic_Light = Red_Light + Yellow_Light + Green_Light

# Mobil yang bisa lewat setiap 5 detik lampu hijau
mobil_per_5_detik = Green_Light // 5

# Berapa kali siklus dalam T detik
Jumlah_siklus = T // Total_Traffic_Light

# Hitung sisa waktu yang tidak habis dalam satu siklus
sisa_waktu = T % Total_Traffic_Light

# Mobil yang bisa lewat setiap 5 detik lampu hijau
mobil_per_5_detik = Jumlah_siklus * (Green_Light // 5)

# Jika sisa waktu lebih dari lampu merah dan kuning, berarti ada waktu hijau tersisa
if sisa_waktu > Red_Light + Yellow_Light:
    waktu_hijau = sisa_waktu - (Red_Light + Yellow_Light)
    mobil_per_5_detik += waktu_hijau // 5

# Identifikasi apakah kita bisa melewati lampu merah 
if mobil_per_5_detik >= M:
    print("YES!")

else: 
    print("NO!")

# calculate mobil sisa
sisa_mobil = max(0, M + N - mobil_per_5_detik)
print(sisa_mobil)    
