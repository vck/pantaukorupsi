# pantaukorupsi

pemantau berita bersentimen korupsi yang terjadi di Indonesia, Riau khususnya. pantaukorupsi menggunakan `lxml parser` sebagai parser tag HTML `<a href=<path> ></a>` dari halaman website portal news, kemudian melakukan filtering sentiment `korupsi` terhadap URL yang telah ter-parser. ** untuk saat ini, karena terkendala masalah teknikal, hanya menggunakan 1 sumber**.

current hosts:

* [pekanbaru.tribunnews.com](http://pekanbaru.tribunnews.com/tag/korupsi)
* [pekanbaruexpress.com](http://www.pekanbaruexpress.com/korupsi.html)


# usage

```
vickydasta@lab ~/dev/git/pantaukorupsi/script $ ipython
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
Type "copyright", "credits" or "license" for more information.

IPython 1.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: run pantau.py


{11138: ['sidang korupsi batal karena pesawat jaksa kpk gagal mendarat.html'], 11015: ['diperiksa penyidik kpk perlihatkan absen anggota dprd.html'], 10760: ['annas maamun diboyong ke rutan suka miskin.html'], 10761: ['annas maamun sidang perdana di tipikor bandung.html'], 11155: ['kesaksian politisi pkb di pengadilan tipikor dibantah.html'], 10908: ['mantan kakan satpol pp kampar ditahan.html'], 10916: ['jaksa gagal eksekusi terpidana korupsi 72 miliar.html'], 10917: ['terjerat kasus korupsi kaban bpbpk pekanbaru nonaktif.html'], 10924: ['mabes polri tetapkan direktur rsud embung fatimah tersangka korupsi alkes.html'], 10925: ['mantan bupati pelalawan terancam masuk penjara lagi.html'], 10926: ['azmun heran dijadikan tersangka kasus pengadaan lahan bakti praja.html'], 10799: ['dugaan korupsi pengadaan buku 15 saksi diperiksa kejari.html'], 10929: ['annas maamun dilarikan ke rumah sakit.html'], 10802: ['menderita sakit maag akut annas maamun tak hadiri sidang.html'], 11060: ['politisi kih ngotot pangkas kewenangan kpk.html'], 10934: ['korupsi baju koko eks kepala bkd hanya divonis 1 tahun.html'], 10943: ['mantan menteri bumn dahlan iskan tersangka.html'], 10944: ['dahlan iskan dicegah ke luar negeri.html'], 10946: ['dahlan siap bertanggung jawab.html'], 10821: ['tim pidsus kajati riau geledah kantor bupati rohil.html'], 10823: ['annas maamun dimarahi hakim tipikor.html'], 10952: ['terdakwa tppu minyak dipenjara 4 tahun adiknya divonis bebas.html'], 10958: ['terima suap gubri nonaktif divonis 6 tahun.html'], 10962: ['terdakwa kasus k2i jalani sidang perdana.html'], 10851: ['asisten ii pemprov diperiksa penyidik kpk.html'], 10854: ['eks ketua dprd riau diperiksa penyidik kpk.html'], 10987: ['bareskrim tetapkan bupati bengkalis tersangka dugaan korupsi.html'], 10866: ['asisten ii riau tersangka korupsi jembatan.html'], 11027: ['kasus korupsi bansos berkas eks ketua dprd diserahkan ke kejati riau.html'], 10748: ['di kpk sekdaprov riau ditanyai soal apbd p 2014.html']}



sidang korupsi batal karena pesawat jaksa kpk gagal mendarat.html diperiksa penyidik kpk perlihatkan absen anggota dprd.html annas maamun diboyong ke rutan suka miskin.html annas maamun sidang perdana di tipikor bandung.html kesaksian politisi pkb di pengadilan tipikor dibantah.html mantan kakan satpol pp kampar ditahan.html jaksa gagal eksekusi terpidana korupsi 72 miliar.html terjerat kasus korupsi kaban bpbpk pekanbaru nonaktif.html mabes polri tetapkan direktur rsud embung fatimah tersangka korupsi alkes.html mantan bupati pelalawan terancam masuk penjara lagi.html azmun heran dijadikan tersangka kasus pengadaan lahan bakti praja.html dugaan korupsi pengadaan buku 15 saksi diperiksa kejari.html annas maamun dilarikan ke rumah sakit.html menderita sakit maag akut annas maamun tak hadiri sidang.html politisi kih ngotot pangkas kewenangan kpk.html korupsi baju koko eks kepala bkd hanya divonis 1 tahun.html mantan menteri bumn dahlan iskan tersangka.html dahlan iskan dicegah ke luar negeri.html dahlan siap bertanggung jawab.html tim pidsus kajati riau geledah kantor bupati rohil.html annas maamun dimarahi hakim tipikor.html terdakwa tppu minyak dipenjara 4 tahun adiknya divonis bebas.html terima suap gubri nonaktif divonis 6 tahun.html terdakwa kasus k2i jalani sidang perdana.html asisten ii pemprov diperiksa penyidik kpk.html eks ketua dprd riau diperiksa penyidik kpk.html bareskrim tetapkan bupati bengkalis tersangka dugaan korupsi.html asisten ii riau tersangka korupsi jembatan.html kasus korupsi bansos berkas eks ketua dprd diserahkan ke kejati riau.html di kpk sekdaprov riau ditanyai soal apbd p 2014.html



{'kantor': 1, 'adiknya': 1, 'buku': 1, 'mabes': 1, 'kpk.html': 3, 'tppu': 1, 'pkb': 1, 'dimarahi': 1, 'penjara': 1, 'geledah': 1, 'kejati': 1, 'rohil.html': 1, 'hakim': 1, '4': 1, 'minyak': 1, 'bebas.html': 1, 'saksi': 1, 'terima': 1, 'di': 3, 'jawab.html': 1, 'ketua': 2, 'eksekusi': 1, 'pangkas': 1, 'maag': 1, 'tipikor': 2, 'bengkalis': 1, 'gubri': 1, 'korupsi.html': 1, 'sakit': 1, 'apbd': 1, 'fatimah': 1, 'perlihatkan': 1, 'akut': 1, 'gagal': 2, 'kpk': 3, 'kewenangan': 1, 'jalani': 1, 'bumn': 1, 'tipikor.html': 1, 'pengadaan': 2, 'menteri': 1, 'nonaktif': 1, 'p': 1, 'dicegah': 1, 'rumah': 1, 'kakan': 1, 'perdana.html': 1, 'terancam': 1, 'direktur': 1, 'koko': 1, 'maamun': 5, 'hadiri': 1, 'pidsus': 1, 'ditanyai': 1, 'pengadilan': 1, 'korupsi': 8, 'miskin.html': 1, 'anggota': 1, 'rutan': 1, 'sidang.html': 1, '2014.html': 1, 'embung': 1, 'tahun.html': 2, 'dprd.html': 1, 'ngotot': 1, 'tahun': 1, 'annas': 5, 'kaban': 1, 'luar': 1, 'tersangka.html': 1, 'ditahan.html': 1, 'terpidana': 1, 'dprd': 2, 'rsud': 1, 'bertanggung': 1, 'sakit.html': 1, 'absen': 1, 'kepala': 1, 'berkas': 1, 'eks': 3, 'terjerat': 1, 'bandung.html': 1, 'masuk': 1, 'diboyong': 1, 'iskan': 2, 'nonaktif.html': 1, 'kampar': 1, 'divonis': 3, 'bareskrim': 1, 'bupati': 3, 'pp': 1, 'satpol': 1, 'siap': 1, 'jembatan.html': 1, 'polri': 1, 'dijadikan': 1, 'menderita': 1, 'lahan': 1, 'praja.html': 1, 'bakti': 1, '6': 1, 'baju': 1, 'dahlan': 3, 'jaksa': 2, 'tetapkan': 2, 'suap': 1, 'karena': 1, '15': 1, 'mendarat.html': 1, 'hanya': 1, 'k2i': 1, 'diperiksa': 4, 'pelalawan': 1, 'negeri.html': 1, 'penyidik': 3, 'azmun': 1, 'heran': 1, 'mantan': 3, 'pekanbaru': 1, 'dugaan': 2, 'ii': 2, 'kasus': 4, 'ke': 4, 'bpbpk': 1, 'tak': 1, 'soal': 1, 'riau': 4, 'suka': 1, 'sekdaprov': 1, 'terdakwa': 2, '1': 1, 'tim': 1, 'dipenjara': 1, 'kajati': 1, 'pemprov': 1, 'kejari.html': 1, 'bkd': 1, 'diserahkan': 1, 'perdana': 1, 'pesawat': 1, 'bansos': 1, 'alkes.html': 1, 'politisi': 2, '72': 1, 'riau.html': 1, 'dibantah.html': 1, 'tersangka': 4, 'miliar.html': 1, 'dilarikan': 1, 'lagi.html': 1, 'batal': 1, 'kih': 1, 'asisten': 2, 'sidang': 3, 'kesaksian': 1}

In [2]:

```
## License

[![License](https://img.shields.io/packagist/l/doctrine/orm.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)


```
The MIT License (MIT)

Copyright © 2015 Vicky Vernando Dasta

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

# Author

`vickydasta`
