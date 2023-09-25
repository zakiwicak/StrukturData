class BangunRuang:
    def __init__(self):
        self._volume = None
        self._luas_permukaan = None

    def hitung_volume(self):
        pass

    def hitung_luas_permukaan(self):
        pass

    def set_volume(self, volume):
        self._volume = volume

    def get_volume(self):
        return self._volume

    def set_luas_permukaan(self, luas_permukaan):
        self._luas_permukaan = luas_permukaan

    def get_luas_permukaan(self):
        return self._luas_permukaan


class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__()
        self._sisi = sisi

    def hitung_volume(self):
        self.set_volume(self._sisi ** 3)
        return self.get_volume()

    def hitung_luas_permukaan(self):
        self.set_luas_permukaan(6 * self._sisi ** 2)
        return self.get_luas_permukaan()

    def set_sisi(self, sisi):
        self._sisi = sisi

    def get_sisi(self):
        return self._sisi


class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self._panjang = panjang
        self._lebar = lebar
        self._tinggi = tinggi

    def hitung_volume(self):
        self.set_volume(self._panjang * self._lebar * self._tinggi)
        return self.get_volume()

    def hitung_luas_permukaan(self):
        self.set_luas_permukaan(2 * ((self._panjang * self._lebar) +
                                (self._panjang * self._tinggi) + (self._lebar * self._tinggi)))
        return self.get_luas_permukaan()

    def set_panjang(self, panjang):
        self._panjang = panjang

    def get_panjang(self):
        return self._panjang

    def set_lebar(self, lebar):
        self._lebar = lebar

    def get_lebar(self):
        return self._lebar

    def set_tinggi(self, tinggi):
        self._tinggi = tinggi

    def get_tinggi(self):
        return self._tinggi


class Prismasegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_prisma):
        super().__init__()
        self._alas = alas
        self._tinggi_alas = tinggi_alas
        self._tinggi_prisma = tinggi_prisma

    def hitung_volume(self):
        self.set_volume((1/2) * self._alas *
                        self._tinggi_alas * self._tinggi_prisma)
        return self.get_volume()

    def hitung_luas_permukaan(self):
        self.set_luas_permukaan(
            (2 * self._alas * self._tinggi_alas) + (3 * self._tinggi_prisma * self._alas))

    def set_alas(self, alas):
        self._alas = alas

    def get_alas(self):
        return self._alas

    def set_tinggi_alas(self, tinggi_alas):
        self._tinggi_alas = tinggi_alas

    def get_tinggi_alas(self):
        return self._tinggi_alas

    def set_tinggi_prisma(self, tinggi_prisma):
        self._tinggi_prisma = tinggi_prisma

    def get_tinggi_prisma(self):
        return self._tinggi_prisma


def menu():
    while True:
        print("\nPilih bangun ruang untuk dihitung volumenya:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Prisma Segitiga")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            sisi = float(input("Masukkan panjang sisi kubus: "))
            kubus = Kubus(sisi)
            print("Volume kubus adalah:", kubus.hitung_volume())
            print("Luas permukaan kubus adalah", kubus.hitung_luas_permukaan())
        elif pilihan == '2':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            balok = Balok(panjang, lebar, tinggi)
            print("Volume balok adalah:", balok.hitung_volume())
            print("Luas permukaan balok adalah", balok.hitung_luas_permukaan())
        elif pilihan == '3':
            alas = float(input("Masukkan alas prisma segitiga: "))
            tinggi_alas = float(
                input("Masukkan tinggi alas prisma segitiga: "))
            tinggi_prisma = float(input("Masukkan tinggi prisma segitiga: "))
            prisma = Prismasegitiga(alas, tinggi_alas, tinggi_prisma)
            print("Volume prisma segitiga adalah:", prisma.hitung_volume())
            print("Luas permukaan prisma segitiga adalah",
                  prisma.hitung_luas_permukaan())
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


if __name__ == '__main__':
    menu()
