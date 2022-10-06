Tugas 5 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Heroku Tugas 5 - Mayfa Shadrina Siddi
[tugas5-mayfa-todolist](https://tugas2-mayfa.herokuapp.com/todolist/login/)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Internal CSS

Internal CSS adalah kode CSS yang ditulis dalam tag <style> pada masing - masing file HTML utnuk menciptakan tampilan yang unik pada setiap halaman website
* Kelebihan: 
- Perubahan yang dilakukan hanya berlaku pada halaman HTML itu saja
- Tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file yang sama
* Kekurangan:
- Tidak efisien jika ingin menggunakan CSS yang sama ke dalam beberapa file
- Membuat performa website menjadi lebih lambat karena setiap perpindahan halaman, website akan melakukan loading ulang akibat kode CSS yang berbeda-beda

2. External CSS

External CSS adalah kode CSS yang ditulis terpisah dari masing-masing file HTML-nya dan biasanya dibuat di sebuah file dengan extension .css. FIle ini biasanya diletakkan setelah bagian <head> pada sebuah halaman
* Kelebihan:
- Ukuran file HTML menjadi lebih kecil dan struktur HTML menjaid lebih rapi karena style-nya sudah ditetapkan pada file external
- Loading website menjadi lebih cepat
- File CSS dapat digunakan pada dua atau lebih halaman sekaligus
* Kekurangan:
- Tampilan halaman bisa menjadi berantakan akibat file CSS gagal terpanggil jika koneksi internet pengguna lambat

3. Inline CSS

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Inline CSS berfungsi hanya untuk mengubah satu elemen saja dan cara ini kurang efisien untuk digunakan.
* Kelebihan:
- Cocok digunakan apabila hanya ingin menguji perubahan pada suatau elemen saja
- Berguna untuk memperbaiki/meng-override tampilan dengan cepat
- Proses permintaan ke HTTP akan lebih kecil sehingga proses load menjadi lebih cepat
* Kekurangan:
- Tidak efisien untuk digunakan karena harus menuliskan kode-nya pada setiap elemen

## Jelaskan tag HTML5 yang kamu ketahui.
1. <script> Menampung sebuah script (seperti script Tailwind CSS CDN)
2. <div> Membuat bagian/section pada suatu halaman
3. <br> Membuat line break
4. <p> Membuat paragraf
5. <span> Menentukan warna atau background dari sebuah teks
6. <a href=""> Mengarahkan ke link halaman
7. <li> Membuat elemen list
8. <form> Membuat elemen-elemen pembuat form
9. <input> Membuat kolom input pada form
10. <button> Membuat button/tombol
11. <table> Membuat tabel
12. <th> Membuat baris header
13. <tr> Membuat baris pada tabel

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Universal Selectors
Pada Universal Selectors, semua element pada suatu halaman website akan memiliki style yang sama. Selector ini dapat digunakan dengan selector lain untuk dikombinasikan

```shell
   * {
    color: blue;
    font-size: 21px;
    } 
```

2. Element Selectors
Pada Element Selctor (atau yang bisa disebut juga dengan Type Selector), CSS akan mencoba untuk menyamakan tampilan pada tiap elemen dengan tipe yang sama. Contohnya semua elemen dengan tags <ul> akan memiliki style yang sama di suatau halaman website

```shell
   ul {
    border: solid 1px #ccc;
    } 
```

3. ID Selectors
Pada ID Selector, CSS akan menyamakan style/tampilan pada setiap elemen yang memiliki ID tertentu. ID Selector dibuat dengan penggunaan hash (#) sebelum ID yang diinginkan.

```shell
    #box {
      width: 90px;
      margin: 10px;  
    }
```

4. Class Selectors
Pada Class Selectors, CSS akan menyamakan style/tampilan pada setiap elemen yang berasal dari class yang sama. Selector ini dibuat dengan menggunakan dot (.) ditmabah dengan nama dari class yang diinginkan

```shell
    .square {
    margin: 20px;
    width: 20px;
    }
```

5. Attribute Selectors
Pada Attribute Selctors, CSS akan menyamakan style/tampilan pada setiap elemen yang memiliki attribute yang sama. Selector ini dapat dibuat dengan menuliskan atribut yang diinginkan ditambah dengan attribute value yang berad di dalam kurung siku

```shell
    input[type="text"] {
    background-color: #fff;
    width: 100px;
    }
```

# Poin 1: Kustomisasi template HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)
Pada Tugas 5 ini, saya menggunakan salah satu CSS Framework yaitu Tailwind dan memodifikasi tampilan pada aplikasi todolist yang telah dibuat sebelumnya

1. Mengimport script CDN Tailwind CSS ke base.html
```shell
    <script src="https://cdn.tailwindcss.com"></script>
```

2. Menambahkan Tailwind Configuration pada base.html yang berisikan screen, color, dan juga font type

3. Mengubah tampilan dengan arahan Tailwind Documentation dan melakukannya dengan style Inline CSS, yaitu dengan melakukan perubahan style pada masing-masing elemen

4. Membuat card dengan attribute-attribute seperti block, rounded, grid, shadow, dan lainnya

# Poin 2: Membuat keempat halaman yang dikustomisasi menjadi responsive

1. Melakukan settings pada masing-masing attribute agar tampilannya dapat berubah jika ukuran halaman diperkecil atau diperbesar dengan menggunakan configuration screen
COntoh:

```shell
<div class = "grid md:grid-cols-2 lg:grid-cols-3 w-full gap-5 mt-8 sm:mt-5 px-4 py-4">
```

Secara default card yang akan ditampilkan pada suatu halaman hanya akan memuat satu card pada satu baris. Tetapi ketika ukuran halaman mencapai md (900px), maka akan dimunculkan dua card pada satu baris. Selanjutnya, jika ukuran halaman telah mencapai lg (1280px), maka akan dimunculkan 3 card pada satu baris. Selain itu, saya juga menetapkan perbedaaan margin top (mt).

## Credits

Dokumen ini dijawab berdasarkan referensi-referensi yang saya baca dari 
1. [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy))
2. [Tailwind Documentation](https://tailwindcss.com/)
3. [Apa Perbedaan Inline CSS, Internal CSS, dan External CSS? - Niagahoster](https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/)
4. [Apa Itu HTML5? Simak Perbedaan HTML dan HTML5 di Sini! - Niagahoster](https://www.niagahoster.co.id/blog/html5-adalah/#Perbedaan_HTML_dan_HTML5)
5. [Types of CSS Selectors - EDUCBA](https://www.educba.com/types-of-css-selectors/)