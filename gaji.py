#==========================================================
#| Nama        :  Galih Gratia Arno
#| NPM         : -
#| STMIK DHARMA WACANA KOTA METRO LAMPUNG
#==========================================================


#inisialisasi input data dengan variabel nomor
def goto(label):
   global nomor
   nomor = label

#inisialisasi untuk pengulangan program
def ulang():
   ulang = input("apakah anda ingin mengulang program? [y/n]: ")
   if ulang == "y":
      goto(0)
   elif ulang == "n":
      exit()
   else:
      exit()

#inisialisasi untuk setiap perhitungan data input karyawan
def rumus():
   global bonus,gapok,tun_jab,tun_kel,tun_ank,gatot
   
   #menghitung tunjangan
   tun_jab = (gapok*tj)/100 #tunjangan jabatan adalah gapok di kali dengan variabel tun_jab sesuai presentase
   tun_kel = (gapok*tk)/100 #berlaku rumus yang sama dengan tunjangan jabatan
   tun_ank = jml_anak*ta #tunjangan anak adalah jumlah anak di kali dengan tunjungan anak sesuai dengan grade

   #menghitung bonus
   if bonus == "y":
      bonus = gapok*b #jika bonus tersedia maka bonus di kali dengan varibel bonus sesuai dengan grade
   elif bonus == "n":
      bonus = gapok*0 #jika tidak ada maka bonus akan di kali dengan 0
   else:
      goto(4)

   #menghitung total gaji
   gatot = bonus + gapok + tun_jab + tun_kel + tun_ank

#inisialisasi untuk output atau tampilan akhir dari data input
def tampil() :
   print("====================================================")
   print("|                 Program Penggajian               |")
   print("====================================================")

   print("| Nama Karyawan                : ", nama)
   print("| Bagian                       : ", bagian)
   print("| Grade                        : ", grade)
   print("| Jumlah Anak                  : ", jml_anak, "anak")
   print("| Bonus                        : Rp. ", bonus)
   print("| Gaji Pokok                   : Rp. ", gapok)
   print("| Tunjangan Jabatan            : Rp. ", tun_jab)
   print("| Tunjangan Keluarga           : Rp. ", tun_kel)
   print("| Tunjangan Anak               : Rp. ", tun_ank)
   print("| Total Gaji                   : Rp. ", gatot)
   print("====================================================")

#melakukan penomoran untuk input data
nomor = 0

#melakukan perulangan program input data
while True:
   
   #awal dari input data karyawan
   if nomor == 0:
      
      print("====================================")
      print("|       Form Data Karyawan         |")
      print("====================================")

      nama = input("Masukkan Nama : ")
      bagian = input("Masukan Bagian : ")
      goto(1)

   #proses penginputan data grade karyawan dan inisialisasi variabel
   elif nomor == 1 :
      grade = input("Masukkan Grade : ")
      #dalam proses ini, variabel ditentukan sesuai data yang terdapat pada tabel dengan penyesuaian grade
      if grade == "1" :
         gapok = 12000000
         tj = 25
         tk = 30
         b = 3
         ta = 300000
         goto(2)
      elif grade == "2" :
         gapok = 9000000
         tj = 15
         tk = 30
         b = 3
         ta = 300000
         goto(2)
      elif grade == "3" :
         gapok = 6000000
         tj = 10
         tk = 30
         b = 2
         ta = 200000
         goto(2)
      elif grade == "4" :
         gapok = 4000000
         tj = 0
         tk = 20
         b = 2
         ta = 200000
         goto(2)
      elif grade == "5" :
         gapok = 3000000
         tj = 0
         tk = 20
         b = 1
         ta = 100000
         goto(2)
      elif grade == "6" :
         gapok = 2000000
         tj = 0
         tk = 20
         b = 1
         ta = 100000
         goto(2)
      elif grade == "7" :
         gapok = 1500000
         tj = 0
         tk = 20
         b = 1
         ta = 100000
         goto(2)
      else :
         print("Tidak ada dalam pilihan grade. Input ulang grade anda.")
         goto(1)

   #proses input data status perkawinan karyawan
   elif nomor == 2 :
      kawin = input("apakah karyawan sudah menikah? (y/n): ")
      if kawin == "y":
         goto(3)
      elif kawin == "n":
         goto(3)
      else:
         print("data yang anda masukan salah, silahkan coba lagi!")
         goto(2)

   #proses input data jumlah anak jika program nomor 2 (status perkawinan) = TRUE or False
   elif nomor == 3 :
      jml_anak = int(input("masukan jumlah anak: "))
      if jml_anak >= 5:
         rumus()
         tampil()
         goto(4)
      else:
         goto(4)

   #proses input bonus jika tersedia
   elif nomor == 4:
      bonus = input("apakah bonus tersedia? [y/n]: ")
      if bonus == "y":
         rumus()
         tampil()
         goto(5)
      elif bonus == "n":
         rumus()
         tampil()
         goto(5)

   #proses perulangan program jika ingi mengulangi program penggajian
   elif nomor == 5 :
      ulang = input("Ulang perhitungan? (y/n) : ")
      if ulang == "y" :
         goto(0)
      elif ulang == "n" :
         exit()
      else :
         print("Tidak ada dalam pilihan")
         goto(5)
