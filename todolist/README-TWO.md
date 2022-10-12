Tugas 5 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Heroku Tugas 5 - Mayfa Shadrina Siddi
[tugas5-mayfa-todolist](https://tugas2-mayfa.herokuapp.com/todolist/login/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
* Pada asynchronous programming, proses jalannya program dapat dilakukan secara bersamaan tanpa menunggu proses lain yang berjalan lebih dahulu untuk selesai. Asynchronous programming ini dapat ditemukan di hampir semua bahasa pemrograman, tetapi belum ditemukan di PHP. Untuk dapat melakukan asynchronous programming di PHP, kita dapat menggunakan AJAX (Asynchronous Javascript & XML). 
* Pada synchronous programming, proses jalannya program bersifat sequential, yaitu suatu proses harus berjalan sesuai dengan antrian eksekusi program. Dengan kata lain, dua program tidak dapat berjalan secara bersamaan. Synchronous programming ini dapat ditemukan di semua bahasa pemrograman, khususnya PHP.


## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
* Event-driven programming merupakan suatu paradigma dimana program akan berjalan sesuai dengan event yang dilakukan oleh user pada suatu halaman website/aplikasi, seperti ketika mouse click, mouse hover, mouse drag, press keyword, dan lain-lain. Setiap event yang sudah ditentukan oleh programmer, nantinya akan dihubungkan pada function yang akan berjalan ketika trigger event dilakukan.
* Pada tugas 6, saya mengimplementasikan paradigma ini pada xxx

## Jelaskan penerapan asynchronous programming pada AJAX
Kode yang kita tuliskan secara asynchronous dengan bantuan AJAX akan dieksekusi di belakang thread utama (main thread) sehingga tidak menghentikan proses runtime walaupun proses sebelumnya belum selesai dilakukan. Selagi menunggu proses sebelumnya selesai, compiler akan mengeksekusi perintah kode selanjutnya. Asynchronous programming memperbolehkan penukaran data dengan server di belakang main thread sehingga server dapat langsung mengubah/menambahkan komponen, elemen, atau data pada sebuah halaman website tanpa harus melakukan reloading halaman.

AJAX yang kita gunakan pada Tugas 6 ini biasa digunakan untuk meng-handle permintaan (request) dan tanggapan (response) dalam bentuk XML, Javascript, ataupun JSON.

Terdapat tiga metode AJAX request yang kerap digunakan oleh programmer:

1. XHR (XMLHTTPRequest)
* XHR merupakan metode AJAX paling tua dan tersedia pada Javascript secara native. Pada XHR kita perlu membuat sebuah fungsi AJAX secara manual sehingga langkah-langkah yang digunakan lebih kompleks dibandingkan metode lainnya

2. JQuery
* JQuery merupakan metode AJAX request yang menyediakan beberapa library sehingga kita tidak perlu membuat instance object dari XHR. Jquery memiliki beberapa requester khusus, seperti jQuery.get dan jQuery.post yang hanya dapat meng-handle HTTP Request GET dan POST. 
* Untuk menggunakan JQuery, kita bisa menambahkan script ini di akhir tag <body>
```shell
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous"></script>
```

3. Fetch API
* Fetch API merupakan gabungan antaar XHR dan JQuery, yaitu merupakan cara yang baru dalam melakukan network request. Untuk menggunakan fetch, kita dapat menggunakan keyword fetch() kemudian tuliskan URL yang akan dituju, seperti:

```shell
    fetch('<URL-to-the-resource-that-is-being-requested>');
```

# Poin 1: Implementasi AJAX GET

# Poin 1.1: Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON

1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON
```shell
    <script src="https://cdn.tailwindcss.com"></script>
```

2. Menambahkan Tailwind Configuration pada base.html yang berisikan screen, color, dan juga font type

3. Mengubah tampilan dengan arahan Tailwind Documentation dan melakukannya dengan style Inline CSS, yaitu dengan melakukan perubahan style pada masing-masing elemen

4. Membuat card dengan attribute-attribute seperti block, rounded, grid, shadow, dan lainnya

# Poin 1.2: Membuat path /todolist/json yang mengarah ke view yang baru kamu buat.

1. Melakukan settings pada masing-masing attribute agar tampilannya dapat berubah jika ukuran halaman diperkecil atau diperbesar dengan menggunakan configuration screen
COntoh:

```shell
<div class = "grid md:grid-cols-2 lg:grid-cols-3 w-full gap-5 mt-8 sm:mt-5 px-4 py-4">
```

Secara default card yang akan ditampilkan pada suatu halaman hanya akan memuat satu card pada satu baris. Tetapi ketika ukuran halaman mencapai md (900px), maka akan dimunculkan dua card pada satu baris. Selanjutnya, jika ukuran halaman telah mencapai lg (1280px), maka akan dimunculkan 3 card pada satu baris. Selain itu, saya juga menetapkan perbedaaan margin top (mt).

# Poin 1.3: Melakukan pengambilan task menggunakan AJAX GET.

1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON
```shell
    <script src="https://cdn.tailwindcss.com"></script>
```

2. Menambahkan Tailwind Configuration pada base.html yang berisikan screen, color, dan juga font type

3. Mengubah tampilan dengan arahan Tailwind Documentation dan melakukannya dengan style Inline CSS, yaitu dengan melakukan perubahan style pada masing-masing elemen

4. Membuat card dengan attribute-attribute seperti block, rounded, grid, shadow, dan lainnya

# Poin 2: Implementasi AJAX POST

# Poin 2.1: Membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
xxx

# Poin 2.2: Membuat view baru untuk menambahkan task baru ke dalam database.
xxx

# Poin 2.3: Membuat path /todolist/add yang mengarah ke view yang baru kamu buat.
xxx

# Poin 2.4: Menghubungkan form yang telah dibuat di dalam modal kamu ke path /todolist/add
xxx

# Poin 2.5: Menutup modal setelah penambahan task telah berhasil dilakukan.
xxx

# Poin 2.6: Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
xxx

## Credits

Dokumen ini dijawab berdasarkan referensi-referensi yang saya baca dari 
1. [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy))
2. [Tailwind Documentation](https://tailwindcss.com/)
3. [Apa Perbedaan Inline CSS, Internal CSS, dan External CSS? - Niagahoster](https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/)
4. [Apa Itu HTML5? Simak Perbedaan HTML dan HTML5 di Sini! - Niagahoster](https://www.niagahoster.co.id/blog/html5-adalah/#Perbedaan_HTML_dan_HTML5)
5. [Types of CSS Selectors - EDUCBA](https://www.educba.com/types-of-css-selectors/)