import os
os.system('clear')

bilangan=10
pangkat= 4
def hitung_pangkat(bilangan,pangkat):
   if pangkat>1:
     return bilangan*hitung_pangkat(bilangan,pangkat-1)
   return bilangan
hasil=hitung_pangkat(bilangan,pangkat)
print(f'Hasil Perpangkatan dari {bilangan}**{pangkat} = {hasil}')

nilai=5
def hitung_faktorial(nilai):
     if nilai>2:
        return nilai*hitung_faktorial(nilai-1)
     return 2

faktorial=hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')

nilai = int(input("Masukkan nilai yang akan dihitung faktorialnya: "))

def hitung_faktorial(nilai):
    if nilai>1:
        return nilai*hitung_faktorial(nilai-1)
    return 1
faktorial = hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')