from sistem_kasir import Produk, Keranjang

p1 = Produk("kopi", 25000, 10)
p2 = Produk("susu", 18000, 5)
p3 = Produk("keyboard", 250000, 2)

keranjang = Keranjang(member=True)

keranjang.tambah_produk(p1, 2)
keranjang.tambah_produk(p2, 1)
keranjang.tambah_produk(p3, 1)

keranjang.bayar(500000)