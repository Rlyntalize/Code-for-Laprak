Nama = input ("masukkan nama mahasiswa:")
nilai = int(input("masukkan nilainya:"))

if(nilai >=90):
    print (f"grade {Nama} adalah A")
elif (nilai >= 80):
    print (f"grade {Nama} adalah B")
elif (nilai >=70):
    print (f"grade {Nama} adalah C")
elif (nilai >=60):
    print (f"grade {Nama} adalah D-")
elif (nilai <=60):
    print (f"grade {Nama} adalah E")
    