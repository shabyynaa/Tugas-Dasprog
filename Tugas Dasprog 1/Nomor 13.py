# read jumlah siswa
Siswa = int(input("Masukkan jumlah siswa: "))

bagian = 30

# calculate kelompok
kelompok = Siswa // bagian

# calculate sisa
sisa = Siswa % bagian

# print output
print("Jumlah siswa yang mendaftar adalah: ", Siswa)
print("Jumlah bagian yang dibutuhkan adalah: ", kelompok)
print("Jumlah sisa siswa adalah: ", sisa)