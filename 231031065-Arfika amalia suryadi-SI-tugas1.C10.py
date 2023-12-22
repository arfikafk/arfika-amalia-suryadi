while True:
    try:
        A = int(input('Masukkan Angka bilangan A: '))
        if A == 3:
            print('Terima kasih')
            break
        elif A % 3 == 0:

             print(f'{A} adalah angka GENAP !')
        else:
            print(f'{A} adalah angka GANJIL!')
    except ValueError:
        print('Masukkan angka yang valid.')