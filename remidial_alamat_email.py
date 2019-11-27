# def cekNamaUser():
# x= 'linda_andiyani@gma-il.com5'
# print(x.split('-'))
x= input('ketikkan alamat email : ')



hurufAgkarakter= ['-','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
hurufAngka=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
karakter = ['@','.']
for i in x:
    if i == '@':
        indeksUser = int(x.index(i))
        # print(indeks)
        # print(x.index(i))
    if i == '.':
        indeksHosting = int(x.index(i))
        # print(indeksHosting)

def cekNamaUser(x):
    # email= False
    for i in x[0:indeksUser]:
        # print(i)
        if i in hurufAgkarakter:
            email= True
            # print('email invalid')
            # break
        else: 
            email = False
            break
    # print(email)
    return email

def cekHosting(x):
    # email= False
    for i in x[indeksUser+1:indeksHosting]:
        # print(i)
        if  i.lower() in hurufAngka:
            email = True
        else:
            email= False
            break
    # print(email)
    return email

def cekEkstensi(x):
    panjangekstensi = len(x[indeksHosting+1:])
    # print(panjangekstensi)
    for i in x[indeksHosting+1:]:
        # print(i)
        if i.lower() in huruf and panjangekstensi <= 5:
            email = True
        else:
            email= False
    # print(email)
    return email
# cekNamaUser(x)
# cekHosting(x)
# cekEkstensi(x)
def cekAwal(x):
    status= True
    for i in x:
        if i in  karakter:
            status= True
            break
        else:
            status = False
    return status
def cekEmail(x):
    # semuaValid = False
    awalan= cekAwal(x)
    if awalan == True:
        cekUser = cekNamaUser(x)
        cekHost = cekHosting(x)
        cekEkst = cekEkstensi(x)
        if cekUser and cekHost and cekEkst == True:
            # semuaValid = True
            print('Email  VALID')
        else:
            print('email TIDAK VALID')
    else: 
        print('email tidak valid')

cekEmail(x)



