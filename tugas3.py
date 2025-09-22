print ("\n--- String, Interger, Float, Boolean, List---")
nama = "Fajar F"
umur = 23
tinggi_badan = 166.5
mahasiswa_aktif= False
hobi = ["game", "menonton film", "menonton yt"]

print ("Nama:", nama)
print ("Umur:", umur)
print ("Tinggi Badan:", tinggi_badan)
print ("Mahasiswa Aktif:", mahasiswa_aktif)
print ("Hobi:" , hobi)

#//
print ("\n--- manipulasi string ---")
print ("Nama Lengkap:" + " " + nama + ".")
print ("panjang nama:" , len(nama) , "karakter.")
print ("Nama Huruf Besar:" + " " + nama.upper() + ".")
print ("Nama Huruf Kecil:" + " " + nama.lower() + ".")

#//
print ("\n--- Operasi Matematika Sederhana---")
a = 10
b = 3
print ("Penjumlahan", a + b)
print ("Penguruangan" , a - b)
print ("Perkalian" , a * b)
print ("pembagian", a / b)
print ("Pembagian Tanpa Sisa", a // b)
print ("Sisa Bagi", a % b)

#//
print ("\n--- List dan Akses Elemen--")
buah = ["Durian", "anggur", "apel", "mangga", "pisang"]
print ("daftar buah:", buah)
print ("buah kesukaan saya:", buah[0])
buah. append("semangka")
print ("setelah daftar ditambahkan:", buah)
buah.remove("pisang")
print ("setelah buah dihapus:", buah)

#//
print ("\n---  ---")
nama_user = input("masukan nama anda:")
umur_user = input("masukan umur anda:")
print ("halo  nama saya," + " " + nama_user + " " + "dan" +" " +"umur saya" + umur_user)