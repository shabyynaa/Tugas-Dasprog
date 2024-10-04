#DILARANG MENGGUNAKAN IMPORT LIBRARY, JIKA MENGGUNAKAN MAKA AKAN DIANGGAP SALAH!
# input bilangan bulat a dan b
a, b = map(int, input().split())

# bilangan c dan d
c = a
d = b

# calculate 
jawaban= (c*d // a) + (c*d // b)

#print output
print(jawaban)