class FitnessTracker:
    def __init__(self, nama, langkah, target):
        self.nama = nama
        self.langkah = langkah
        self.target = target
        self.kalori = 0

    def tambah_langkah(self, jumlah):
        if jumlah > 0:
            self.langkah += jumlah
            print(f"{self.nama} nambah {jumlah} langkah")
        else:
            print("jumlah harus lebih dari 0")

    def hitung_kalori(self):
        self.kalori = self.langkah * 0.04
        return self.kalori

    def cek_target(self):
        if self.langkah >= self.target:
            print(f"{self.nama} udah mencapai target")
        else:
            kurang = self.target - self.langkah
            print(f"{self.nama} kurang {kurang} langkah lagi")

    def info(self):
        print(f"{self.nama} | langkah: {self.langkah} | kalori: {self.kalori} | target: {self.target}")


orang1 = FitnessTracker("Deby", 3000, 8000)
orang2 = FitnessTracker("Rofiq", 9000, 8000)

orang1.tambah_langkah(2000)
orang2.tambah_langkah(1000)

orang1.hitung_kalori()
orang2.hitung_kalori()

orang1.cek_target()
orang2.cek_target()

orang1.info()
orang2.info()