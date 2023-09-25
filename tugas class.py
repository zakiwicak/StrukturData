class bangunruang(object):
    def __init__(self, rusuk, panjang, lebar, tinggi, l):
        self.rusuk = rusuk
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def set_rusuk(self, rusuk):
        self.rusuk = rusuk

    def set_panjang(self, panjang):
        self.panjang = panjang

    def set_lebar(self, lebar):
        self.lebar = lebar

    def set_tinggi(self, tinggi):
        self.tinggi = tinggi

    def get_rusuk(self):
        return self.rusuk

    def get_tinggi(self):
        return self.tinggi

    def get_lebar(self):
        return self.lebar

    def get_panjang(self):
        return self.panjang


class kubus(bangunruang):
    def __init__(self, rusuk, panjang, lebar, tinggi):
        bangunruang.__init__(self, rusuk, panjang, lebar, tinggi)

    def luas_permukaan(self):
        return bangunruang.get_rusuk(self) ** 2 * 2

    def volume(self):
        return bangunruang.get_rusuk(self) ** 3


class balok(bangunruang):
    def __init__(self, panjang, lebar, tinggi, rusuk):
        bangunruang.__init__(self, panjang, lebar, tinggi, rusuk)

    def luas_permukaan(self):
        return bangunruang.get_lebar(self) * bangunruang.get_panjang(self) * 2 + bangunruang.get_panjang(self) * bangunruang.get_rusuk(self) * 2 + bangunruang.get_rusuk(self) * bangunruang.get_tinggi(self) * 2

    def volume(self):
        return bangunruang.get_lebar(self) * bangunruang.get_panjang(self) * bangunruang.get_tinggi(self)


class prismasegitiga(bangunruang):

    def __init__(self, rusuk, panjang, lebar, tinggisegitigaalas, tinggi):
        self.tinggisegitigaalas = tinggisegitigaalas
        bangunruang.__init__(self, rusuk, panjang, lebar,
                             tinggisegitigaalas, tinggi)

    def set_tinggisegitigaalas(self, tinggisegitigaalas):
        self.tinggisegitigaalas = tinggisegitigaalas

    def get_tingisegitigaalas(self):
        return self.tinggisegitigaalas

    def luas_permukaan(self):
        return bangunruang.get_rusuk(self) * 3 * bangunruang.get_tinggi(self) + bangunruang.get_tinggi(self) * bangunruang.get_rusuk(self)

    def volume(self):
        return bangunruang.get_tinggi(self) * 1/2 * bangunruang.get_rusuk(self) * prismasegitiga.get_tingisegitigaalas(self)


def menu():
    print("bangun ruang")
    print("silahkan pilih menu :")
    print("1. kubus")
    print("2. balok")
    print("3. prisma segitiga")


def menukubus():
    print("masukan pilihan rumus:")
    print("1. luas permukaan")
    print("2. volume")


def menubalok():
    print("masukan pilihan menu")
    print("1. luas permukaan")
    print("2. volume")


def menuprisma():
    print("masukan pilihan menu")
    print("1. luas permukaan")
    print("2. volume")


while True:
    menu()
    pilihan = int(input("masukan pilihan anda:"))
    if pilihan == 1:
        menukubus()
        pilihan2 = int(input("masukan nomor:"))
        if pilihan2 == 1:
            if __name__ == "__main__":
                n = int(input("masukan angka:"))
                k = kubus(n, 0, 0, 0)
                print(k.luas_permukaan())

        elif pilihan2 == 2:
            if __name__ == "__main__":
                n = int(input("masukan nilai rusuk:"))
                k = kubus(n, 0, 0, 0)
                print(k.volume())

    elif pilihan == 2:
        menubalok()
        pilihan2 = int(input("masukan nomor:"))
        if pilihan2 == 1:
            if __name__ == "__main__":
                p = int(input("masukan panjang:"))
                l = int(input("masukan lebar:"))
                t = int(input("masukan tinggi:"))
                b = balok(p, l, t, 0)
                print(b.luas_permukaan())
        elif pilihan2 == 2:
            if __name__ == "__main__":
                p = int(input("masukan panjang:"))
                l = int(input("masukan lebar:"))
                t = int(input("masukan tinggi:"))
                b = balok(p, l, t, 0)
                print(b.volume())
    elif pilihan == 3:
        menuprisma()
        pilihan2 = int(input("masukan nomor:"))
        if pilihan2 == 1:
            if __name__ == "__main__":
                r = int(input("masukan rusuk:"))
                t = int(input("masukan tinggi:"))
                tsa = int(input("masukan tinggi segitiga alas:"))
                prs = prismasegitiga(r, 0, 0, tsa, t)
                print(prs.luas_permukaan())
        elif pilihan2 == 2:
            if __name__ == "__main__":
                r = int(input("masukan rusuk:"))
                t = int(input("masukan tinggi:"))
                tsa = int(input("masukan tinggi segitiga alas:"))
                prs = prismasegitiga(r, 0, 0, tsa, t)
                print(prs.volume())
    else:
        break
