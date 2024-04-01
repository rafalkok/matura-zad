def szyfr(n,k):#funkcja szyfrująca
    k=k%26
    szyfr=""
    
    for i in n:
        
        if ord(i) - k < 65:#kod litery w przedziale 65-90
            x = ord(i) - 65
            szyfr += chr(91 + x - k)
        else:
            szyfr += chr(ord(i) - k)
    return szyfr

print("Wybierz polecenie (1,2,3)")
a=int(input())

if a>3 or a<0:
    print("Nie wybrano polecenia 1-3")
elif a==1:
    k=107
    with open("dane_6_1.txt", 'r') as p:
        n = p.read()                
        for i in range(len(n)):                       
            f=open("wyniki_6_1.txt",'w')
            f.writelines(szyfr(n,k)+'\n')
            f.close()
elif a==2:
    plik = open('dane_6_2.txt').readlines()
    for wiersz in plik:
        wiersz = wiersz.strip().split()#zmienia wiersz na dwu-elementową listę (słowo, klucz)
        n = wiersz[0]
        k = int(wiersz[1])
        f=open("wyniki_6_2.txt",'a')
        f.writelines(szyfr(n,k)+'\n')
        f.close()
elif a==3:
    plik = open('dane_6_3.txt').readlines()
    for wiersz in plik:
        wiersz = wiersz.strip().split()
        k = 0
        x = wiersz[0][0]
        for i in range(26):#szuka klucza
            if x == wiersz[1][0]:
                klucz = i
                break
            else:
                x = chr(ord(x)+1)
            if ord(x) > 90:
                x = chr(65)
        if szyfr(wiersz[1], i) != wiersz[0]:#wypisuje błędne szyfry
            f=open("wyniki_6_3.txt",'a')
            f.writelines(szyfr(wiersz[0],k)+'\n')
            f.close()