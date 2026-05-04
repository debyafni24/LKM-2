from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi", 25000, 10)
p2 = Produk("Susu", 18000, 5)
p3 = Produk("Keyboard", 250000, 2)

print(p1.kode_produk)
print(p2.kode_produk)
print(p3.kode_produk)

keranjang = Keranjang(member=True)

keranjang.tambah_produk(p1, 2)
keranjang.tambah_produk(p2, 1)
keranjang.tambah_produk(p3, 1)

keranjang.cetak_struk()
keranjang.bayar(500000)