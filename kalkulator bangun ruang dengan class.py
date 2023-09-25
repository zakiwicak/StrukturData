class BangunRuang:
    def _init_(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setNama(self, nama):
        self.nama = nama

    def LuasPermukaan(self):
        pass

    def Volume(self):
        pass


class Kubus(BangunRuang):
    def _init_(self, nama, sisi):
        super()._init_(nama)
        self.sisi = sisi

    def getSisi(self):
        return self.sisi

    def setSisi(self, sisi):
        self.sisi = sisi

    def LuasPermukaan(self):
        return 6 * self.sisi * self.sisi

    def Volume(self):
        return self.sisi * self.sisi * self.sisi


class Balok(BangunRuang):
    def _init_(self, nama, panjang, lebar, tinggi):
        super()._init_(nama)
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def getPanjang(self):
        return self.panjang

    def setPanjang(self, panjang):
        self.panjang = panjang

    def getLebar(self):
        return self.lebar

    def setLebar(self, lebar):
        self.lebar = lebar

    def getTinggi(self):
        return self.tinggi

    def setTinggi(self, tinggi):
        self.tinggi = tinggi

    def LuasPermukaan(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def Volume(self):
        return self.panjang * self.lebar * self.tinggi


class PrismaSegitiga(BangunRuang):
    def _init_(self, nama, rusuk1, rusuk2, rusuk3,  tinggi):
        super()._init_(nama)
        self.rusuk1 = rusuk1
        self.rusuk2 = rusuk2
        self.rusuk3 = rusuk3
        self.tinggi = tinggi

    def getrusuk(self):
        return self.rusuk1

    def setrusuk(self, rusuk1):
        self.rusuk1 = rusuk1

    def getrusuk(self):
        return self.rusuk2

    def setrusuk(self, rusuk2):
        self.rusuk2 = rusuk2

    def getrusuk(self):
        return self.rusuk3

    def setrusuk(self, rusuk3):
        self.rusuk3 = rusuk3

    def gettinggi(self):
        return self.tinggi

    def settinggi(self, tinggi):
        self.tinggi = tinggi

    def LuasPermukaan(self):
        return (2*(0.5 * self.rusuk1 * self.rusuk2)) + ((self.rusuk1 + self.rusuk2 + self.rusuk3) * self.tinggi)

    def Volume(self):
        return (0.5 * self.rusuk1 * self.rusuk2) * self.tinggi


# Fungsi Menu
def Menu():
    while True:
        print("=============================")
        print("=== PROGRAM BANGUN RUANG ====")
        print("=============================")
        print("1. Kubus")
        print("2. Balok")
        print("3. PrismaSegitiga")
        print("4. Keluar")

        pilihan = int(input("Masukkan pilihan anda: "))

        if pilihan == 1:
            sisi = int(input("Masukkan sisi kubus: "))
            kubus = Kubus("Kubus", sisi)
            print(f"Luas Permukaan {kubus.getNama()}: {kubus.LuasPermukaan()}")
            print(f"Volume {kubus.getNama()}: {kubus.Volume()}")
        elif pilihan == 2:
            panjang = int(input("Masukkan panjang balok: "))
            lebar = int(input("Masukkan lebar balok: "))
            tinggi = int(input("Masukkan tinggi balok: "))
            balok = Balok("Balok", panjang, lebar, tinggi)
            print(f"Luas Permukaan {balok.getNama()}: {balok.LuasPermukaan()}")
            print(f"Volume {balok.getNama()}: {balok.Volume()}")
        elif pilihan == 3:
            rusuk1 = int(input("Masukkan rusuk1 prisma segitiga: "))
            rusuk2 = int(input("Masukkan rusuk2 prisma segitiga: "))
            rusuk3 = int(input("Masukkan rusuk3 prisma segitiga: "))
            tinggi = int(input("Masukkan tinggi prisma segitiga: "))
            prisma = PrismaSegitiga(
                "Prisma Segitiga", rusuk1, rusuk2, rusuk3, tinggi)
            print(
                f"Luas Permukaan {prisma.getNama()}: {prisma.LuasPermukaan()}")
            print(f"Volume {prisma.getNama()}: {prisma.Volume()}")
        elif pilihan == 4:
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan 1-4.")


Menu()  # memanggil fungsi Menu()
