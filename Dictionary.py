dataMhs = {}

print("Program Input Nilai")
print("===================")

while True:
    menu = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if menu.capitalize() == "T":
        nim = input("Masukan NIM          : ")
        nama = input("Masukan Nama         : ")
        tugas = int(input("Masukan Nilai Tugas  : "))
        uts = int(input("Masukan Nilai UTS    : "))
        uas = int(input("Masukan Nilai UAS    : "))
        akhir = ((tugas / 100*30) + (uts/100*35) + (uas / 100*35))
        dataMhs[nim] = nama, tugas, uts, uas, akhir
        continue
    if menu.capitalize() == "L":
        print("Daftar Nilai")
        print("====================================================================")
        print("| No |     NIM     |       NAMA        | TUGAS | UTS | UAS | AKHIR |")
        print("====================================================================")
        if len(dataMhs) == 0:
            print("|                         TIDAK ADA DATA                           |")
        else:
            x = 1
            for i, j in dataMhs.items():
                # print(dataMhs[i][1])
                print('| {0:^3}| {1:11} | {2:<17} | {3:5} | {4:3} | {5:3} | {6:5.2f} |'.format(
                    x, i, dataMhs[i][0], dataMhs[i][1], dataMhs[i][2], dataMhs[i][3], dataMhs[i][4]))
                x += 1
        print("====================================================================")

        continue
    if menu.capitalize() == "U":
        print("Mengubah data Mahasiswa")
        nim = input("Masukan NIM : ")
        

    if menu.capitalize() == "H":
        print("Menghapus Nilai Mahasiswa")
        found = True
        while found :
            nim = input("Masukan NIM : ")
            if nim in dataMhs :
                dataMhs.pop(nim)
                break
            else :
                print("Data tidak ditemukan.\nPastikan anda memasukan NIM yang benar")
                continue

    if menu.capitalize() == "C":
        print("Mencari Nilai Mahasiswa")
        nim = input("Masukan Nim : ")
        print("====================================================================")
        print("| No |     NIM     |       NAMA        | TUGAS | UTS | UAS | AKHIR |")
        print("====================================================================")
        print('| {0:^3}| {1:>9} | {2:<18} | {3:5} | {4:4} | {5:4} | {6:5.2f} |'.format(
            1, i, dataMhs[nim][0], dataMhs[nim][1], dataMhs[nim][2], dataMhs[nim][3], dataMhs[nim][4]))
        print("====================================================================")
    if menu.capitalize() == "K":
        print("Keluar dari program..")
        break
