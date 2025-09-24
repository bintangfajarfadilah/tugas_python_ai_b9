print ("\n--- list Akses & Manupulasi---")
#//List 
data = ["Apel", "Durian", "Pisang", 7, 2, "Semangka"]
print ("element pertama:", data[0])
print ("element terakhir:", data[5])
print ("slicing [1:6:2]", data[1:6:2])
#// Append
data.append("Srikaya")
print ("setelah append 'Srikaya':", data)
#// insert
print ("sebelum insert ('anggur. 1'):", data)
data.insert (1, "anggur")
print ("setelah insert (1, 'anggur'):", data)
#// extend
data.extend (["melon", 3])
print ("setelah extend (['melon', 3]:", data)
#// pop (menghapus element terakhir)
hapus_pop = data.pop ()
print ("element terakhir terhapus:", hapus_pop)
print ("list sekarang", data)
#// remove\
print ("data sebelum 'Srikaya terhapus':", data)
data.remove ("Srikaya")
print ("list data setelah 'Srikaya' terhapus:", data)

print ("\n--- Tuple immutability & unpaking---")
data_tupel = ("durian", "2", "semangka", "rambutan", "7")
print ("Tupel:", data_tupel)
print ("panjang tupel (len()):", len(data_tupel))
print ("elemen pertama :", data_tupel[0])
print ("element ketiga/tengah :", data_tupel [2])
print ("element terakhir :", data_tupel[-1])

#// unpacking
buah_ke1, angka_ke1, buah_ke2, *rest = data_tupel
print ("unpacking:")
print ("Buah Pertama:", buah_ke1) 
print ("Angka Pertama:", angka_ke1)
print ("Buah Kedua:", buah_ke2)
print("*rest:", *rest)

print ("\n--- SET KEUNIKAN & OPERASI HIMPUNAN ---")
set_a = {1,2,3,4,5,3,2}
set_b = {4,6,8,2,4}
print ("Set A:", set_a)
print ("Set B:", set_b)

print ("---UNION---")
print ("Union A | B ", set_a | set_b)
print ("Intersection A & B:", set_a & set_b)
print (" Difference A - B  Yang berberda :;", set_a - set_b)
print ("Symetric Difference A ^ B :", set_a ^ set_b)

print("\n=== DICTIONARY: Key/Value Dasar ===")
mahasiswa = {
    'nama': 'Andi',
    'nim': 'A11.2022.12345',
    'angkatan': 2022,
    'kota': 'Semarang'
}

# Tambah, ubah, hapus
mahasiswa['jurusan'] = 'Informatika'
mahasiswa['kota'] = 'Yogyakarta'
del mahasiswa['nim']

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Iterasi dictionary:")
for k, v in mahasiswa.items():
    print(f"{k}: {v}")

print("\n--- NESTED STRUCTURES ---")
buku = [
    {'judul': 'Python Dasar', 'penulis': 'A. Nugroho', 'tahun': 2020},
    {'judul': 'AI Modern', 'penulis': 'B. Putra', 'tahun': 2023},
    {'judul': 'Data Science', 'penulis': 'C. Sari', 'tahun': 2019},
    {'judul': 'Machine Learning', 'penulis': 'D. Hadi', 'tahun': 2025}
]

print("Daftar judul buku:")
for b in buku:
    print("-", b['judul'])

tahun_min = 2020
buku_terbaru = [b for b in buku if b['tahun'] >= tahun_min]
print(f"\nBuku terbit sejak {tahun_min}:")
for b in buku_terbaru:
    print(f"{b['judul']} ({b['tahun']})")

print("\n--- COMPREHENSION & UTILITAS ---")
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("List genap 1–20:", genap)
print("List kuadrat 1–20:", kuadrat)

paritas = {x: ('genap' if x % 2 == 0 else 'ganjil') for x in range(1, 11)}
print("Paritas 1–10:", paritas)

kalimat = "Belajar Python Itu Menyenangkan"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)

print("\n--- KEANGGOTAAN & PENCARIAN ---")
buah = ['apel', 'jeruk', 'mangga']
cek = 'jeruk' in buah
print("Apakah 'jeruk' ada di list buah?:", cek)

if 'mangga' in buah:
    print("'mangga' ditemukan di indeks:", buah.index('mangga'))

angka_set = {10, 20, 30}
print("Apakah 20 ada di set?:", 20 in angka_set)


