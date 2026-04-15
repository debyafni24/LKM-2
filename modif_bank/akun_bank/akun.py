class AkunBank:
    def __init__(self, nomor, pemilik, saldo_awal):
        self.nomor = nomor 
        self.pemilik = pemilik
        self.saldo = saldo_awal
        self.riwayat = []

    def cek_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
        elif jumlah <= self.saldo:
            self.saldo -= jumlah
            pesan = f"{self.pemilik} menarik Rp{jumlah}"
            print(pesan)
            self.riwayat.append(pesan)
        else:
            print("Saldo tidak cukup!")
  
    def transfer(self, tujuan, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
        elif self.saldo >= jumlah + 2500:
            self.saldo -= (jumlah + 2500)
            tujuan.saldo += jumlah
            pesan = f"Transfer Rp{jumlah} ke {tujuan.pemilik} (biaya admin Rp2500)"
            print(pesan)
            self.riwayat.append(pesan)
        else:
            print("Transfer gagal: saldo tidak cukup.")

    def tampilkan_riwayat(self):
        print(f"Riwayat transaksi {self.pemilik}:")
        for r in self.riwayat:
            print("-", r)