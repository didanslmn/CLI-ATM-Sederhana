user_id = 0
loop = "n"
user =  [
            {   
              "id":"1234",
              "no_rekening":"1234567890",
              "username":"Contoh",
              "pin":"4321",
              "saldo":0
            },
            {   
              "id":"4321",
              "no_rekening":"0987654321",
              "username":"contoh",
              "pin":"1234",
              "saldo":50000000
            }
        ]
status_login = False
pakai_atm = "y"
 
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False       
     
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1
 
def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
def tranfer_uang(uang,no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp."+str(uang)+" ke Rekening "+no_rekening)
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Maaf saldo anda tidak cukup")
             
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Maaf saldo anda tidak cukup")

def Tagihan_listrik():
    index1 = cek_user(user_id)
    print ("Pembayaran Tagihan Listrik")
    print ("==============================================")
    print ("Golongan 1 = 1500")
    print ("Golongan 2 = 2000")
    print ("Golongan 3 = 2500")
    i =int(input("masukan pilihan anda : "))
    if i == 1:
        GOL = 1500
    elif i == 2:
        GOL = 2000
    elif i == 3:
        GOL = 2500
    n=input("Nomor Register : ")
    nm=input("Nama Pelanggan  : ")
    jl=input("Jumlah KWH anda :")
    bayar = int(jl)*int(GOL)
    user[index1]['saldo'] =user[index1]['saldo'] - bayar
    print ("                  Daftar Bayar Listrik        ")
    print ("==============================================")
    print ("|| Nomor Register    :",n)
    print ("|| Nama Pelanggan    :",nm)
    print ("|| Total yang dibayar:",bayar)
    print ("|| Jumlah KWH        :",jl)
    print ("|| Sisa Saldo anda   :Rp.",user[index1]['saldo'])
    print ("==============================================")

def Tagihan_air():
    index1 = cek_user(user_id)
    print ("Pembayaran Tagihan Listrik")
    print ("==============================================")
    print ("Golongan 1 = 2000")
    print ("Golongan 2 = 3000")
    print ("Golongan 3 = 4000")
    i =int(input("masukan pilihan anda : "))
    if i == 1:
        GOL = 2000
    elif i == 2:
        GOL = 3000
    elif i == 3:
        GOL = 4000
    n=input("Nomor Register : ")
    nm=input("Nama Pelanggan  : ")
    jl=30
    bayar = int(jl)*int(GOL)
    user[index1]['saldo'] =user[index1]['saldo'] - bayar
    print ("                  Daftar Bayar Air                ")
    print ("==============================================")
    print ("|| Nomor Register    :",n)
    print ("|| Nama Pelanggan    :",nm)
    print ("|| Total yang dibayar:",bayar)
    print ("|| Jumlah Pemakaian  :",jl)
    print ("|| Sisa Saldo anda   :Rp.",user[index1]['saldo'])
    print ("==============================================")
  
while pakai_atm == "y":
    while status_login == False:
        print("SELAMAT DATANG DI ATM BANK")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("selamat data "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")
     
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        print("SELAMAT DATANG DI ATM BANK")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Pembayaran Tagihan Listrik")
        print("5.Pembayaran Tagihan Air")
        print("6.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.",u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
             
            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                tranfer_uang(nominal,no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"                 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a== 4:
            Tagihan_listrik()
            loop = "n"
        elif a==5:
            Tagihan_air()
            loop = "n"
        elif a == 6:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True: 
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"