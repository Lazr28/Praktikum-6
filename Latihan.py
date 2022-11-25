import os
print("Latihan Dictionary kontak person")
def warn(txt) : print("\033[91m{}\033[00m" .format(txt)) 
def success(txt) : print("\033[92m {}\033[00m" .format(txt)) 
def cls() : os.system('cls')
kontak = {}
menu = ""
cls()
while True:
    #if len(kontak) > 0:
    #    print(kontak)
    menu = input("Menu : \n(1) Tambah Kontak.\n(2) Ubah data.\n(3) Menyegarkan data.\n(4) Tampilkan Nama.\n(5) Tampilkan Nomor.\n(6) Tampilkan daftar nama dan nomor.\n(del) Hapus data.\n(x) Exit\nPilih menu : ")
    if menu == "1":
        nama = input("Masukan Nama : ")
        nomor = input("Masukan Nomor : ")
        kontak[nama] = nomor
        cls()
        success("Berhasil menambahkan Kontak.")
        continue
    elif menu == "2":
        if len(kontak) != 0 :
            i = input("Masukan Nama yang akan di ubah nomornya : ")
            print(i, "dengan nomor : ", kontak[i], "akan di ubah.")
            kontak[i] = input("Ubah nomor menjadi : ")
            cls()
            success("Berhasil mengubah nomor ")
        else :
            cls()
            warn("\nDictionary masih kosong\n")
        continue
    elif menu == "3":
        continue
    elif menu == "4":
        cls()
        print(*kontak)
        print("")
        continue
    elif menu == "5":
        cls()
        for i in kontak :
            print(kontak[i])
        continue
    elif menu == "6":
        cls()
        success(kontak)
        continue
    elif menu == "del":
        cls()
        success(kontak)
        continue
    elif menu == "x":
        success("Exiting Program..")
        break