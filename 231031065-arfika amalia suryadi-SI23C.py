import os
os.system ('clear')
import random as rd

print('Program tebak angka dari 1 sampai 10')

angka = [1,2,3,4,5,6,7,8,9,10]
tebak = rd.choice (angka)
a = True
limit =3
i = 0

while a:
    i += 1
    pilih = input('Masukkan pilihan angka: [1,2,3,4,5,6,7,8,9,10]:')
    if pilih == tebak:
        print(f'Pilihan anda benar yaitu {pilih}')
        a = False
    else:
        if i < limit:
            print('Tebakan anda salah! coba lagi')
            print(f'Kesempatan anda tersisa {limit-i} kali')
            a = True
        else:
            print('Kesempatan anda habis!')
            a = False