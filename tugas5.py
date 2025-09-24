print ("\n--- Function ---")
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


print ("\n--- Class ---")
class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self):
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


print ("\n--- Demo ---")

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))

    print("\n--- CLASS STUDENT ---")
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(90)
    mhs1.tambah_nilai(80)

    mhs2 = Student("Sari", "A456")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(65)

    print(mhs1)
    print(f"Rata-rata: {mhs1.rata_nilai()}, Status: {mhs1.status()}")

    print(mhs2)
    print(f"Rata-rata: {mhs2.rata_nilai()}, Status: {mhs2.status()}")
