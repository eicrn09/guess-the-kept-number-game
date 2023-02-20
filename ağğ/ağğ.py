import random 
sayi=random.randint(1,100)

hak=5
sayac=0
ipucusayisi=1

if sayi%2==0:
    ipucu='cift'
else:
    ipucu='tek'

while hak>0:
    hak-=1
    sayac+=1
    tahmin=input('tahmininiz: ')
    if int(tahmin)==sayi:
        print('Tebrikler'+' '+str(sayac)+'.'+' seferde bildiniz')
    elif int(tahmin)<sayi:
        print('yukari')
        if (int(ipucusayisi)>0):
             a=input('Ipucu ister misin? ')
             if a=='evet':
                 print(ipucu)
                 ipucusayisi-=1
    else:
        print('asagi')
        if (int(ipucusayisi)>0):
             b=input('Ipucu ister misin? ')
        if b=='evet':
            print(ipucu)
            ipucusayisi-=1
    if hak==0:
        print('Hakkiniz bitti :( Tutulan sayi: '+str(sayi))
        break
