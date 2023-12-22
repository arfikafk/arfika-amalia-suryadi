def faktorial(nilai):
    if nilai == 0 or nilai == 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Input nilai faktorial dari pengguna
input_nilai = int(input("Masukkan nilai faktorial (<= 11): "))

# Program Utama
for i in range(input_nilai + 1):
    result = faktorial(i)
    print('%d ! = %d' % (i, result))
