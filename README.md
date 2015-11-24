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

In [1]: from pantau import getdata

In [2]: d = getdata()

In [3]: d
Out[3]:
[{11060: 'politisi kih ngotot pangkas kewenangan kpk.html'},
 {11015: 'diperiksa penyidik kpk perlihatkan absen anggota dprd.html'},
 {10987: 'bareskrim tetapkan bupati bengkalis tersangka dugaan korupsi.html'},
 {10958: 'terima suap gubri nonaktif divonis 6 tahun.html'},
 {10952: 'terdakwa tppu minyak dipenjara 4 tahun adiknya divonis bebas.html'},
 {10943: 'mantan menteri bumn dahlan iskan tersangka.html'},
 {10929: 'annas maamun dilarikan ke rumah sakit.html'},
 {10925: 'mantan bupati pelalawan terancam masuk penjara lagi.html'},
 {10924: 'mabes polri tetapkan direktur rsud embung fatimah tersangka korupsi alkes.html'},
 {10916: 'jaksa gagal eksekusi terpidana korupsi 72 miliar.html'},
 {11155: 'kesaksian politisi pkb di pengadilan tipikor dibantah.html'},
 {11060: 'politisi kih ngotot pangkas kewenangan kpk.html'},
 {11015: 'diperiksa penyidik kpk perlihatkan absen anggota dprd.html'},
 {10987: 'bareskrim tetapkan bupati bengkalis tersangka dugaan korupsi.html'},
 {10958: 'terima suap gubri nonaktif divonis 6 tahun.html'},
 {10952: 'terdakwa tppu minyak dipenjara 4 tahun adiknya divonis bebas.html'},
 {10943: 'mantan menteri bumn dahlan iskan tersangka.html'},
 {10929: 'annas maamun dilarikan ke rumah sakit.html'},
 {10925: 'mantan bupati pelalawan terancam masuk penjara lagi.html'},
 {10924: 'mabes polri tetapkan direktur rsud embung fatimah tersangka korupsi alkes.html'},
 {10916: 'jaksa gagal eksekusi terpidana korupsi 72 miliar.html'},
 {10917: 'terjerat kasus korupsi kaban bpbpk pekanbaru nonaktif.html'},
 {11155: 'kesaksian politisi pkb di pengadilan tipikor dibantah.html'},
 {11138: 'sidang korupsi batal karena pesawat jaksa kpk gagal mendarat.html'},
 {11060: 'politisi kih ngotot pangkas kewenangan kpk.html'},
 {11027: 'kasus korupsi bansos berkas eks ketua dprd diserahkan ke kejati riau.html'},
 {11015: 'diperiksa penyidik kpk perlihatkan absen anggota dprd.html'},
 {10987: 'bareskrim tetapkan bupati bengkalis tersangka dugaan korupsi.html'},
 {10962: 'terdakwa kasus k2i jalani sidang perdana.html'},
 {10958: 'terima suap gubri nonaktif divonis 6 tahun.html'},
 {10952: 'terdakwa tppu minyak dipenjara 4 tahun adiknya divonis bebas.html'},
 {10946: 'dahlan siap bertanggung jawab.html'},
 {10944: 'dahlan iskan dicegah ke luar negeri.html'},
 {10943: 'mantan menteri bumn dahlan iskan tersangka.html'},
 {10934: 'korupsi baju koko eks kepala bkd hanya divonis 1 tahun.html'},
 {10929: 'annas maamun dilarikan ke rumah sakit.html'},
 {10926: 'azmun heran dijadikan tersangka kasus pengadaan lahan bakti praja.html'},
 {10925: 'mantan bupati pelalawan terancam masuk penjara lagi.html'},
 {10924: 'mabes polri tetapkan direktur rsud embung fatimah tersangka korupsi alkes.html'},
 {10916: 'jaksa gagal eksekusi terpidana korupsi 72 miliar.html'},
 {10917: 'terjerat kasus korupsi kaban bpbpk pekanbaru nonaktif.html'},
 {10908: 'mantan kakan satpol pp kampar ditahan.html'},
 {10866: 'asisten ii riau tersangka korupsi jembatan.html'},
 {10854: 'eks ketua dprd riau diperiksa penyidik kpk.html'},
 {10851: 'asisten ii pemprov diperiksa penyidik kpk.html'},
 {10823: 'annas maamun dimarahi hakim tipikor.html'},
 {10821: 'tim pidsus kajati riau geledah kantor bupati rohil.html'},
 {10802: 'menderita sakit maag akut annas maamun tak hadiri sidang.html'},
 {10799: 'dugaan korupsi pengadaan buku 15 saksi diperiksa kejari.html'},
 {10760: 'annas maamun diboyong ke rutan suka miskin.html'},
 {10761: 'annas maamun sidang perdana di tipikor bandung.html'},
 {10748: 'di kpk sekdaprov riau ditanyai soal apbd p 2014.html'},
 {11155: 'kesaksian politisi pkb di pengadilan tipikor dibantah.html'},
 {11155: 'kesaksian politisi pkb di pengadilan tipikor dibantah.html'},
 {11138: 'sidang korupsi batal karena pesawat jaksa kpk gagal mendarat.html'},
 {11060: 'politisi kih ngotot pangkas kewenangan kpk.html'},
 {11060: 'politisi kih ngotot pangkas kewenangan kpk.html'},
 {11027: 'kasus korupsi bansos berkas eks ketua dprd diserahkan ke kejati riau.html'}]

In [4]:


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
