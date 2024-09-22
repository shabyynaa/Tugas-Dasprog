# read panjang halaman
Panjang_Halaman = int(input("Masukkan panjang halaman: "))

# read lebar halaman 
Lebar_Halaman = int(input("Masukkan lebar halaman: "))

# read panjang rumah
Panjang_Rumah = int(input("Masukkan panjang rumah: "))

# read lebar rumah 
Lebar_Rumah = int(input("Masukkan lebar rumah: "))

# calculate luas halaman 
Luas_Halaman = Panjang_Halaman * Lebar_Halaman

# calculate luas rumah 
Luas_Rumah = Panjang_Rumah * Lebar_Rumah

# calculate luas daerah potong rumput
Luas = Luas_Halaman - Luas_Rumah

rate = 2

# calculate time
waktu = Luas / rate

# print output
print("Waktu yang dibutuhkan untuk memotong rumput dengan luas", Luas, "adalah", waktu, "detik")