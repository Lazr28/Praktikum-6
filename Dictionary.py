dataMhs = {}

print("Program Input Nilai")
print("===================")
nim,nama
tugas,uts,uas,akhir
while True:
    menu = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if menu.capitalize() == "T":
        nim = input("Masukan NIM          : ")
        nama = input("Masukan Nama         : ")
        tugas = int(input("Masukan Nilai Tugas  : "))
        uts = int(input("Masukan Nilai UTS    : "))
        uas = int(input("Masukan Nilai UAS    : "))
        akhir = ((tugas / 100*30) + (uts/100*35) + (uas / 100*35))
        dataMhs[nim] = {"nama": nama, "tugas": tugas,
                        "uts": uts, "uas": uas, "akhir": akhir}
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
                    x, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
                x += 1
        print("====================================================================")

        continue
    if menu.capitalize() == "U":
        print("Mengubah data Mahasiswa")
        nim = input("Masukan NIM : ")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            nama = input("Masukan Nama         : ")
            if nama == None : nama = dataMhs[nim]['nama']
            tugas = input("Masukan Nilai Tugas  : ")
            if tugas == "" : tugas = dataMhs[nim]['tugas']
            tugas = int()
            uts = int(input("Masukan Nilai UTS    : "))
            if uts == None : uts = dataMhs[nim]['uts']
            uas = int(input("Masukan Nilai UAS    : "))
            if uas == None : uas = dataMhs[nim]['uas']
            akhir = ((tugas / 100*30) + (uts/100*35) + (uas / 100*35))
            dataMhs[nim] = {"nama": nama, "tugas": tugas,"uts": uts, "uas": uas, "akhir": akhir}
            print("Berhasil Mengubah Data")
        else:
            print("Data tidak ditemukan.\nPastikan anda memasukan NIM yang benar ")

    if menu.capitalize() == "H":
        print("Menghapus data Mahasiswa")
        nim = input("Masukan NIM : ")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            dataMhs.pop(nim)
            print("Berhasil menghapus data mahasiswa")
        else:
            print("Data tidak ditemukan.\nPastikan anda memasukan NIM yang benar ")

    if menu.capitalize() == "C":
        print("Mencari Nilai Mahasiswa")
        nim = input("Masukan Nim : ")
        print("====================================================================")
        print("| No |     NIM     |       NAMA        | TUGAS | UTS | UAS | AKHIR |")
        print("====================================================================")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            print('| {0:^3}| {1:11} | {2:<17} | {3:5} | {4:3} | {5:3} | {6:5.2f} |'.format(
                1, i, dataMhs[nim]["0"], dataMhs[nim][1], dataMhs[nim][2], dataMhs[nim][3], dataMhs[nim][4]))
        else:
            print("        DATA MAHASISWA DENGAN NO NIM",
                  nim, "KOSONG / TIDAK ADA")
        print("====================================================================")
    if menu.capitalize() == "K":
        print("Keluar dari program..")
        break
    elif menu.capitalize() not in ('L', 'T', 'U', 'H', 'C', 'K'):
        print("Mohon Pilih menu yang benar!")
