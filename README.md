# PRAKTIKUM 6 
## DICTIONARY
### PROGRAM MENAMPILKAN DATA NILAI MAHASIWA
--------
>- Program dibuat dengan menggunakan **Dictionary**
>- Tampilkan menu pilihan : (Tambah Data, Ubah Data, Hapus Data, Tampilkan Data, Cari Data)
>- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas : 30%, UTS : 35%, UAS : 35%)\
>- Buat Flowchart dan penjelasan programmnya pada README.md
>- Commit dan push repository ke github



 **Penjelasan**\
Berbeda dengan Varabel ber tipe `String`, `Int`, `Float`.\
Variabel `Tuple`, `List`, `Dictionary` perlu di deklarasikan atau dibuat terlebih dahulu.\
\
Buat Dictionary dengan sintaks berikut :
```python
dataMhs = {}
```
Setelah itu kita tampilkan untuk Header Judul \ Nama Program.
```python
print("                         Program Input Nilai")
print("=========================================================================")
```
Gunakan `while` looping agar dapat terus menampilkan menu setelah selesai memilih.
```python
while true :
```

\
Buat Inputan Menu dengan variabel `menu` ( Lihat, Tambah, Ubah, Hapus, Cari, Keluar ).
```python
menu = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
```
Setelah itu kita buat Kondisi dari inputan user / Pilihan menu user dengan menggunakan sintaks IF\
Kita buat Menu menjadi Kapital agar inputan user menjadi kapital dan kondisi nya lebih sedikit,
gunakan `.capitalize()` pada variabel menu.\
gunakan inisial menu untuk kondisi nya.\
\
Pada Kondisi `T` atau Tambah Data, kita gunakan kode berikut :
```python
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
```


> 1. Buat Inputan Nama
> 2. Buat Inputa Tugas, UTS, UAS Lakukan Kondisi jika user tidak memasukan nilai (kosong / null).\
 jika Benar maka tugas / UTS / UAS akan mendapatkan nilai 0 secara default.\
> 3. Lalu untuk <ins>**Nilai Akhir**</ins> kita buatkan rumus, tugas 30%, UTS 35%, UAS 35%
> 4. Setelah itu kita tambahkan Data data di atas kedalam Dictionary dengan Key NIM,\
didalamnya kita gunakan 2 dimensi dictionary untuk memudahkan membaca sintaks dan data.

\
Pada kondisi `L` atau Lihat Data, Kita gunakan kode berikut : 
```python
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
```
> Menu ini untuk menampilkan data yang tersimpan pada dictionary\
> 1. Buat tampilan Tabel bagian atas ( judul Tabel untuk menampilkan data)
> 2. Gunakan iF, untuk mengecek apakah sudah ada data tersimpan atau tidak.\
jika ya, akan menampilkan " **TIDAK ADA DATA** " di dalam tabel tersebut.\
jika tidak, akan menampilkan semua data nilai yang tersimpan dengan menggunakan for looping.


\
\
Pada kondisi `U` atau Ubah Data, Kita gunakan kode berikut : 
```python
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
```
> Menu ini untuk mengubah data yang ada pada dictionary
> 1. buat tampilan "Mengubah data Mahasiswa
> 2. Buat Inputan pada variabel `nim` untuk menampung inputan NIM oleh user.
> 3. Gunakan iF, untuk mengecek apakah ada data untuk NIM yang telah di inputkan.\
jika **Ya**, akan meminta user untuk memasukan nama, nilai Tugas, UTS, UAS. jika user tidak memasukan nilai \ null maka value nya tidak akan di ubah.\
setelah itu Jumlahkan kembali Nilai Akhir dengan value nilai tugas \ uts \ uas yang sudah di ubah.\
lalu update value dictionary dengan key `nim` sebelumnya.\
lalu menampilkan teks " <ins>Berhasil mengubah data</ins>\
jika **Tidak**, akan menampilkan tulisan " <ins>Data tidak ditemukan, pastikan anda memasukan NIM yang benar</ins> ".

\
Pada kondisi `H` atau Hapus Data, Kita gunakan kode berikut : 
```python
if menu.capitalize() == "H":
        print("Menghapus data Mahasiswa")
        nim = input("Masukan NIM : ")
        if (dataMhs.get(nim, "kosong") != "kosong"):
            dataMhs.pop(nim)
            print("Berhasil menghapus data mahasiswa")
        else:
            print("Data tidak ditemukan.\nPastikan anda memasukan NIM yang benar ")
```
> Menu ini untuk menghapus data yang ada pada dictionary
> 1. Tampilkan teks " <ins>Menghapus data Mahasiswa</ins> "
> 2. Buat Inputan pada variabel `nim` untuk menampung inputan NIM oleh user.
> 3. Gunakan iF, untuk mengecek apakah ada data untuk NIM yang telah di inputkan.\
jika **Ya**, hapus data menggunakan sintaks `.pop(key)` setelah nama dictionary. ( `dataMhs.pop(nim)`\
jika **Tidak**, akan menampilkan tulisan " <ins>Data tidak ditemukan, pastikan anda memasukan NIM yang benar</ins> ".

\
\
Pada kondisi `C` atau Cari Data, Kita gunakan kode berikut : 
```python
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
```
> Menu ini untuk mengcari data yang ada pada dictionary
> 1. Tampilkan teks " <ins>Mencari Nilai Mahasiswa</ins> "
> 2. Buat Inputan pada variabel `nim` untuk menampung inputan NIM oleh user.
> 3. Buat Tampilan Header Tabel.
> 3. Gunakan iF, untuk mengecek apakah ada data untuk NIM yang telah di inputkan.\
jika **Ya**, Tampilkan data menggunakan sintaks `print` dan gunakan formating\
jika **Tidak**, akan menampilkan tulisan " <ins>DATA MAHASISWA DENGAN NO NIM *'Nomor nim yang di input'* KOSONG / TIDAK ADA</ins> ".

\
\
Pada kondisi `K` atau Keluar dari program, Kita gunakan kode berikut : 
```python
if menu.capitalize() == "K":
        print("Keluar dari program..")
        break
```
> Menu ini untuk keluar dari program.
> dengan sintaks `break` untuk menghentikan while looping


Pada kondisi terakhir, kita gunakan kode berikut untuk menampung jika user memilih \ menginput huruf\
selain yang tertera pada menu. lalu menampilkan teks " <ins>Mohon Pilih menu yang benar!</ins>
```python
    elif menu.capitalize() not in ('L', 'T', 'U', 'H', 'C', 'K'):
        print("Mohon Pilih menu yang benar!")
```


\
\
Kode lengkap : \
[File Praktikum](Dictionary.py)\
Atau :
```python
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
```
---
## Screenshot Output :



1. Tampilan awal.\
![SS-1](/Screenshot/SS-01.png)

2. Menu Menampilkan Data ( kosong )\
![SS-2](/Screenshot/SS-02.png)

3. Menu menambahkan Data nilai\
!![SS-3](/Screenshot/SS-03.png)

4. Menu Menampilkan Data ( Sudah ada data )\
![SS-4](/Screenshot/SS-04.png)

5. Menu Ubah ( Salah memasukan NIM / NIM yang ingin di ubah tidak ada dalam dictionary)\
![SS-5](/Screenshot/SS-05.png)

6. Menu Ubah & Lihat Data\
![SS-6](/Screenshot/SS-06.png)

7. Menu Cari data ( Salah memasukan NIM / NIM yang ingin di ubah tidak ada dalam dictionary)\
![SS-7](/Screenshot/SS-07.png)

8. Menu Cari data\
![SS-8](/Screenshot/SS-08.png)

9. Hapus data ( Salah memasukan NIM / NIM yang ingin di ubah tidak ada dalam dictionary)\
![SS-9](/Screenshot/SS-09.png)

10. Hapus Data\
![SS-10](/Screenshot/SS-10.png)

11. Memilih / memasukan huruf yang tidak ada dalam menu.\
![SS-11](/Screenshot/SS-11.png)

12. Menu Keluar dari program / While Looping\
![SS-12](/Screenshot/SS-12.png)

