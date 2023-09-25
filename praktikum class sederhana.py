class BangunRuang:
    def hitung_volume(self):
        pass


class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3


class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi


class Prismasegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_prisma):
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_prisma = tinggi_prisma

    def hitung_volume(self):
        return (1/2) * self.alas * self.tinggi_alas * self.tinggi_prisma


def menu():
    while True:
        print("\nPilih bangun ruang untuk dihitung volumenya:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Prisma Segitiga")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan (0/1/2/3): ")

        if pilihan == '1':
            sisi = float(input("Masukkan panjang sisi kubus: "))
            kubus = Kubus(sisi)
            print("Volume kubus adalah:", kubus.hitung_volume())
        elif pilihan == '2':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            balok = Balok(panjang, lebar, tinggi)
            print("Volume balok adalah:", balok.hitung_volume())
        elif pilihan == '3':
            alas = float(input("Masukkan alas prisma segitiga: "))
            tinggi_alas = float(
                input("Masukkan tinggi alas prisma segitiga: "))
            tinggi_prisma = float(input("Masukkan tinggi prisma segitiga: "))
            prisma = Prismasegitiga(alas, tinggi_alas, tinggi_prisma)
            print("Volume prisma segitiga adalah:", prisma.hitung_volume())
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


if __name__ == '__main__':
    menu()
