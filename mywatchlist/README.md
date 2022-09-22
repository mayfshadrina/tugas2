Tugas 3 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Heroku Tugas 3 - Mayfa Shadrina Siddi
[tugas3-mayfa-html](https://tugas2-mayfa.herokuapp.com/mywatchlist/html/)
[tugas3-mayfa-xml](https://tugas2-mayfa.herokuapp.com/mywatchlist/xml/)
[tugas3-mayfa-json](https://tugas2-mayfa.herokuapp.com/mywatchlist/json/)

## Perbedaan antara JSON, XML, dan HTML

1. JSON
    * JavaScript Object Notation atau yang lebih kerap dikenal dengan JSON merupakan sebuah format yang digunakan untuk menyimpan, membaca, dan menukar dara-data dari web server sehingga dapat dibaca oleh para pengguna
    * JSON terdiri dari dua struktur, yaitu yang pertama merupakan kumpulan value yang saling berpasangan (seperti object) dan kumpulan value yang berurutan (seperti array)
    * JSON dapat digunakan oleh bahasa-bahasa pemrograman, seperti PHP, Python, C++, dan Ruby.
    * Jika dibandingkan dengan file lain, isi file JSON relatif lebih mudah untuk dibaca dibandingkan XML

2. XML
    * Extensible Markup Language atau yang lebih kerap dikenal dengan XML merupakan markup language yang mendefinisikan aturan-aturan untuk melakukan encoding pada data dalam format yang dapat dipahami oleh manusia dan juga mesin
    * Format XML ini dibuat untuk membawa data, bukan untuk menampilkan data, sehingga fokus yang diutamakan pada penggunaan format ini adalah kesederhanaan, keumuman, dan kemudahan dalam penggunaannya di Internet
    * Berbeda dengan format JSON, XML tidak dapat menampilkan data dalam bentuk array, tetapi penyimpanan datanya lebih aman dibandingkan penyimpanan data di file JSON

3. HTML
    * Hypertext Markup Language atau yang lebih kerap disebut dengan HTML merupakan sebuah markup language yang digunakan untuk menyusun struktur suatu website dan menampilkan data-data yang dibutuhkan kepada pengguna.
    * HTML merupakan kombinasi antara teks dan simbol dimana pengguna dapat menyusun heading, paragraf, gambar, dan link sehingga pengguna dapat mengakses data-data tersebut melalui halaman website
    * Pada fle HTML, programmer dapat dengan mudah menandai tulisan atau bagian-bagian pada website dengan kalimat cetak tebal, miring, atau format lainnya dengan bantuan tag di HTML, seperti <bold>, <italic>


## Data Delivery dalam Pengimplementasian Platform

![BaganDjango](https://user-images.githubusercontent.com/87022037/191642480-2887fe8c-054a-4e58-be8e-e1e115c790f4.png)

Ketika kita mengimplementasikan platform yang akan berinteraksi dengan pengguna untuk mendapatkan HTTP Request dan mengirimkan HTTP Response terkait dengan data, maka data delivery sangat dibutuhkan agar mempermudah pengaturan dan pendistribusian data dari database ke halaman pengguna. Nantinya, data delivery akan sangat berguna untuk menentukan dokumen apa saja yang akan di-return sesuai dengan kebutuhan ekstensi file-nya (bisa merupakan HTML, CSS, JPG, JS, XML, JSON, dan lain-lain).

## Poin 1: Membuat Aplikasi “mywatchlist”

1. Pertama, saya membuka command prompt, mengakses direktori Tugas 2 lalu mengaktifkan virtual environment dengan instruksi

   ```shell
   python -m venv env
   env\Scripts\activate.bat
   ```

2. Lalu, saya menjalankan instruksi untuk membuat aplikasi baru yang bernama “mywatchlist”

   ```shell
   python manage.py startapp mywatchlist
   ```

3. Kemudian saya menambahkan keyword ‘mywatchlist’ pada variabel INSTALLED_APPS pada file settings.py di folder project_django

    ```shell
    INSTALLED_APPS = [
    ...,
    'wishlist',
    ]
    ```

## Poin 2: Menambahkan Path “mywatchlist”


1. Untuk menambakan path “mywatchlist”, saya menambahkan nama aplikasi ke variable urlpatterns pada file urls.py di folder project_django 

   ```shell
   ...
    path('mywatchlist/', include('mywatchlist.urls')),
    ...
   ```

2. Setelah itu, saya juga mendaftarkan aplikasi katalog ke dalam urls.py di folder project_django pada variabel urlpatterns.

   ```shell
   ...
   path('katalog/', include('katalog.urls')),
   ...
   ```

## Poin 3: Membuat Model MyWatchList

1. Saya membuka file models.py yang ada pada folder mywatchlist untuk membuat model yang nantinya akan mendistribusikan data-data dengan membuat kelas MyWatchlist

   ```shell
    from django.db import models

    class MyWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
   ```

2. Selanjutnya, saya melakukan perintah 

   ```shell
    python manage.py makemigrations 
    python manage.py migrate
   ```
   untuk menjalankan migrasi skema model ke dalam database Django lokal.

## Poin 4: Menambahkan Data untuk Objek MyWatchList

1. Untuk menambahkan data dalam objek MyWatchList, saya membuat sebuah folder bernama fixtures di dalam folder aplikasi mywatchlist dan membuat sebuah berkas yang bernama initial_watchlist_data.json yang berisikan kode yang menampilkan data-data film yang terdiri dari watched, title, rating, release_date, dan review

    ```shell
    ...
    {
        "model":"mywatchlist.MyWatchlist",
        "pk":1,
        "fields":{
            "watched": "True",
            "title":"Elvis",
            "rating": "4",
            "release_date":"2022-06-24",
            "review": "austin butler played that role like his whole life depends on it."
        }
    },
    ...
   ```

2. Selanjutnya, saya melanjalankan instruksi loaddata untuk memasukkan data ke database django lokal  

    ```shell
    python manage.py loaddata initial_wishlist_data.json
    ```

3. Untuk dapat mengaksesnya ketika sudah di-deploy nanti, loaddata juga harus dilakukan di Procfile dengan menambahkan instruksi sebagai berikut:

    ```shell
    '… && python manage.py loaddata initial_watchlist_data.json'
    ```

## Poin 5: Menyajikan Data dalam Tiga Format (HTML, XML, JSON)

1. Pertama, saya membuat sebuah fungsi yang menerima parameter request pada file views.py di folder katalog untuk memanggil fungsi query ke model database (MyWatchlist) dan menyimpan hasil query tersebut ke dalam sebuah variabel. Pada fungsi HTML saya juga menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat agar dapat memunculkan datanya pada halaman.
    * HTML

    ```shell
    def show_watchlist(request):
        data_mywatchlist = MyWatchlist.objects.all()
        context = {
        'list_watchlist': data_mywatchlist,
        'nama': 'Mayfa Shadrina Siddi',
        'npm' : '2106634616',
        }
        return render(request, "mywatchlist.html", context)
   ```

   * XML

   ```shell
    def show_xml(request):
        data_mywatchlist = MyWatchlist.objects.all()
            return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")
   ```

   * JSON

    ```shell
    def show_json(request):
        data_mywatchlist = MyWatchlist.objects.all()
            return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
   ```

2. Lalu, saya menambahkan kode yang akan menampilkan pesan jika banyaknya film yang ditonton lebih sedikit dibandingkan banyaknya film yang belum ditonton dan sebaliknya pada file views.py. Kode yang saya tambahankan adalah sebagai berikut:

    ```shell
    data_true = MyWatchlist.objects.filter(watched = True)
    data_false = MyWatchlist.objects.filter(watched = False)
    
    lebih_banyak = 'Selamat, kamu sudah banyak menonton!'
    lebih_dikit = 'Wah, kamu masih sedikit menonton!'
    
    if len(data_true) > len(data_false):
        ucapan = lebih_banyak
    else:
        ucapan = lebih_dikit
        
    context = {
    …
    'watch_tf' : ucapan
    }
    ```

3. Selanjutnya saya membuat sebuah folder bernama templates di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama mywatchlist.html untuk melakukan iterasi terhadap variabel list_barang agar dapat mengambil data/atribut spesifik dari masing-masing objek yang terdapat dalam variabel tersebut. Isi dari mywatchlist.html saya isi dengan kode di bawah ini:

    ```shell
    {% extends 'base.html' %}

    {% block content %}

        <h1>3rd Assignment PBP/PBD</h1>

        <h5>Name: </h5>
        <p>{{nama}}</p>

        <h5>Student ID: </h5>
        <p>{{npm}}</p>

        <h5>Status: </h5>
        <p>{{watch_tf}}</p>

        <table>
            <table border="1">
            <tr>
            <th>Watched</th>
            <th>Title</th>
            <th>Rating</th>
            <th>Release Date</th>
            <th>Review</th>
            </tr>
            {% comment %} Add the data below this line {% endcomment %}
            {% for watchlist in list_watchlist %}
            <tr>
                <th>{{watchlist.watched}}</th>
                <th>{{watchlist.title}}</th>
                <th>{{watchlist.rating}}</th>
                <th>{{watchlist.release_date}}</th>
                <th>{{watchlist.review}}</th>
            </tr>
            {% endfor %}
        </table>

    {% endblock content %}

    ```

## Poin 6: Membuat Routing pada URL

1. Saya melakukan routing terhadap fungsi views yang telah dibuat pada file urls.py di folder katalog agar halaman HTML, XML, dan JSON dapat dimunculkan pada browser

    ```shell
    from django.urls import path
    from mywatchlist.views import show_watchlist
    from mywatchlist.views import show_xml
    from mywatchlist.views import show_json

    app_name = 'mywatchlist'

    urlpatterns = [
        path('html/', show_watchlist, name='show_watchlist'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
    ]
   ```

## Poin 7: Melakukan Deployment ke Heroku

1. Terakhir saya melakukan deployment dengan instruksi

    ```shell
    git add .
    git commit -m “<pesan commit>”
    git push -u origin main
   ```
   dan GitHub akan secara otomatis melkaukan deployment ke Heroku yang saya miliki


## Credits

Dokumen ini dijawab berdasarkan referensi-referensi yang saya baca dari 
1. [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy))
2. [Apa itu HTML? Berikut Fungsi dan Cara Kerjanya! - Niagahoster](https://www.niagahoster.co.id/blog/html-adalah/)
3. [Django Testing Tutorial - The Dumbfounds](https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3)
4. [Apa itu JSON? - Dicoding](https://www.dicoding.com/blog/apa-itu-json/)
5. [Difference between JSON and XML - Geeksforgeeks](https://www.geeksforgeeks.org/difference-between-json-and-xml/)