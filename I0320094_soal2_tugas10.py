print("=======Program Biodata=======")
print("")

Nama = input("Nama: ")
Usia = input("Usia: ")
Asal = input("Asal Daerah: ")
Prodi = input("Program Studi: ")
Angkatan = input("Angkatan: ")

teks = "Nama : {}\nUsia : {}\nAsal : {}\nProdi : {}\nAngkatan : {}"\
    .format(Nama,Usia,Asal,Prodi,Angkatan)

file_biodata = open("biodata.txt","w")

file_biodata.write(teks)

file_biodata.close()
