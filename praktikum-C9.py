import os

def judul():
    os.system('cls')
    print('PROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN')
    print('BANGUN RUANG BALOK')
    print()

def inputan():
    p = float(input('Masukkan Panjang:'))
    l = float(input('Masukkan Lebar:'  ))
    t = float(input('Masukkan Tinggi:' ))
    return p,l,t

def perhitungan(p,l,t):
    vol= p * l * t
    luas = 2*(p*l + p*t + l*t)
    luas_tanpa_tutup = luas - p*l

def tampilkan(jenis,nilai):
    print(f'Nilai dari {jenis} adalah : {nilai}')

def pilihan():
    pilih = input('Apakah lanjutakan? [y/n]')
    if pilih == 'y':
         a = True
    else:
         a = False
         print('Sampai jumpa lagi.')
    return a

def main():
    judul()
    p,l,t = inputan()
    # perhitungan
    vol,luas,luas_tanpa_tutup = perhitungan(p,l,t)
    # tampilkan
    tampilkan ('volume',vol)
    tampilkan ('luas permukaan',luas)
    tampilkan ('luas permukaan tanpa tutup',luas_tanpa_tutup)
    a = pilihan() # pilihan

a = True
while a:
    main()