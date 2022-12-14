dataMhs = {}

print("                         Program Input Nilai")
print("=========================================================================")
while True:
    menu = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if menu.capitalize() == "T":
        nim = input("Masukan NIM          : ")
        nama = input("Masukan Nama         : ")
        tugas = input("Masukan Nilai Tugas  : ")
        if tugas == "":
            tugas = 0
        uts = input("Masukan Nilai UTS    : ")
        if uts == "":
            uts = 0
        uas = input("Masukan Nilai UAS    : ")
        if uas == "":
            uas = 0

        akhir = ((int(tugas) / 100*30) +
                 (int(uts)/100*35) + (int(uas) / 100*35))
        dataMhs[nim] = {"nama": nama, "tugas": tugas,
                        "uts": uts, "uas": uas, "akhir": akhir}
        
    if menu.capitalize() == "L":
        print("Daftar Nilai")
        print("=========================================================================")
        print("| No |     NIM     |       NAMA        |  TUGAS  |  UTS | UAS |  AKHIR  |")
        print("=========================================================================")
        if len(dataMhs) == 0:
            print(
                "|                         TIDAK ADA DATA                                |")
        else:
            x = 1
            for i, j in dataMhs.items():
                print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:7.2f} |'.format(
                    x, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
                x += 1
        print("=========================================================================")

        continue
    if menu.capitalize() == "U":
        print("Mengubah data Mahasiswa")
        nim = input("Masukan NIM          : ")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            nama = input("Masukan Nama         : ")
            if nama == "":
                nama = dataMhs[nim]['nama']
            tugas = input("Masukan Nilai Tugas  : ")
            if tugas == "":
                tugas = dataMhs[nim]['tugas']
            uts = input("Masukan Nilai UTS    : ")
            if uts == "":
                uts = dataMhs[nim]['uts']
            uas = input("Masukan Nilai UAS    : ")
            if uas == "":
                uas = dataMhs[nim]['uas']
            akhir = ((int(tugas) / 100*30) +
                     (int(uts)/100*35) + (int(uas) / 100*35))
            dataMhs[nim] = {"nama": nama, "tugas": tugas,
                            "uts": uts, "uas": uas, "akhir": akhir}
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
        print("=========================================================================")
        print("| No |     NIM     |       NAMA        |  TUGAS  |  UTS | UAS |  AKHIR  |")
        print("=========================================================================")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:6.2f} |'.format(
                1, i, dataMhs[i]["nama"], dataMhs[i]["tugas"], dataMhs[i]["uts"], dataMhs[i]["uas"], dataMhs[i]["akhir"]))
        else:
            print("|                 DATA MAHASISWA DENGAN NO NIM ",
                  nim, "KOSONG / TIDAK ADA     |")
        print("=========================================================================")
    if menu.capitalize() == "K":
        print("Keluar dari program..")
        break
    elif menu.capitalize() not in ('L', 'T', 'U', 'H', 'C', 'K'):
        print("Mohon Pilih menu yang benar!")
