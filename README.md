Tugas 2 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Heroku Tugas 2 - Mayfa Shadrina Siddi
[tugas2-mayfa](https://tugas2-mayfa.herokuapp.com/katalog/)

## Bagan Request Client ke Web Aplikasi Berbasis Django

![BaganDjango](https://user-images.githubusercontent.com/87022037/190303040-5cb0d383-3b36-4c06-ab00-ac84962b3c54.png)

Client dapat melakukan request pada web aplikasi berbasis Django melalui internet dengan mengakses urls.py. Selanjutnya, urls.py akan meneruskan request client ke file views.py yang akan memanggil data-data yang dibutuhkan dari database melalui models.py. Nantinya, models.py akan mengatur dan mengalokasikan data apa saja yang perlu dipenuhi sesuai dengan request yang diterima. Setelah mendapatkan data-nya dari models.py, views.py akan melakukan penggabungan data dengan tempate HTML (<filename>.html) agar tampilan yang dimunculkan di browser dapat disesuaikan dengan request yang dikirim oleh client. Setelah proses penggabungan (merging), HTTP response akan dikirimkan ke browser client dan browser akan menampilkan halaman yang diminta berdasarkan request client sebelumnya.

## Virtual Environment

Dalam melakukan pengembangan aplikasi, khususnya pada project yang berbasis Python, kita akan sering mendengar tools yang dinamakan virtual environment. Seperti namanya, virtual environment merupakan ruang lingkup virtual yang memperbolehkan programmer untuk mengisolasi suatu project dari dependencies utama. Virtual environment ini akan sangat berguna jika kita mengembangkan berbagai project yang mempunyai kebutuhan/dependent yang berbeda-beda dalam satu sistem operasi yang sama. Dengan adanya virtual environment, kita dapat memenuhi dan menyesuaikan kebutuhan project yang berbeda-beda, tanpa harus mengubah konfigurasi pada sistem operasi yang kita gunakan. Khususnya pada pengembangan aplikasi berbasis Python, programmer direkomendasikan untuk menggunakan virtual environment setiap kali mereka membuat project baru agar dapat memastikan bahwa library yang digunakan pada suatu project tidak akan berubah meskipun dilakukan pengubahan di project lainnya.

Programmer dapat memilih untuk tidak menggunakan virtual environment dalam melakukan pengembangan aplikasi. Namun, dalam pengembangan jangka panjangnya, hal ini akan menyulitkan programmer karena terdapat beberapa kekurangan/resiko yang bisa muncul, seperti:
1. Mengontaminasi atau tidak sengaja mengubah library project lain ketika melakukan pengubahan pada salah satu project
2. Memunculkan konflik pada versi Python atau packages jika ingin digunakan pada mesin lainnya
3. Direktori utama yang digunakan (tanpa virtual environment) akan berisikan package-package yang tidak diperlukan untuk kebutuhan program/aplikasi yang dikembangkan

## Poin 1: Menghubungkan Models dengan Views

1. Pertama, saya membuat sebuah fungsi yang menerima parameter request pada file views.py di folder katalog untuk memanggil fungsi query ke
   model database (CatalogItem) dan menyimpan hasil query tersebut ke dalam sebuah variabel.

   ```shell
   def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Mayfa Shadrina Siddi',
    'npm' : '2106634616'
    }
    return render(request, "katalog.html")
   ```

2. Setelah itu, saya menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat agar dapat  
   memunculkan data tersebut pada halaman HTML.

   ```shell
   return render(request, "katalog.html", context)
   ```

## Poin 2: Melakukan Routing untuk Mapping Fungsi

1. Saya melakukan routing terhadap fungsi views yang telah dibuat pada file urls.py di folder katalog agar halaman HTML dapat dimunculkan pada 
   browser

   ```shell
   from django.urls import path
   from katalog.views import show_katalog

   app_name = 'katalog'

   urlpatterns = [
      path('', show_katalog, name='show_katalog'),
   ]
   ```

2. Setelah itu, saya juga mendaftarkan aplikasi katalog ke dalam urls.py di folder project_django pada variabel urlpatterns.

   ```shell
   ...
   path('katalog/', include('katalog.urls')),
   ...
   ```

## Poin 3: Menghubungkan Models dengan Template

1. Pertama, saya mengubah Fill me! yang ada di dalam HTML tag <p> menjadi {{nama}} dan {{npm}} untuk memunculkan nama dan NPM saya di halaman 
   HTML berdasarkan variabel ‘nama’ dan ‘npm’ di file views.py. 

   ```shell
   ...
   <h5>Name: </h5>
   <p>{{nama}}</p>

   <h5>Student ID: </h5>
   <p>{{npm}}</p>
   ...
   ```

2. Setelah itu, saya melakukan iterasi terhadap variabel list_barang agar dapat mengambil data/atribut spesifik dari masing-masing objek yang 
   terdapat dalam variabel tersebut.

   ```shell
   ...
   {% comment %} Add the data below this line {% endcomment %}
      {% for barang in list_barang %}
         <tr>
            <th>{{barang.item_name}}</th>
            <th>{{barang.item_price}}</th>
            <th>{{barang.item_stock}}</th>
            <th>{{barang.rating}}</th>
            <th>{{barang.description}}</th>
            <th>{{barang.item_url}}</th>
         </tr>
      {% endfor %}
   ...
   ```

3. Untuk dapat melakukan pemetaan data CatalogItem ke file HTML, saya juga menjalankan perintah 

   ```shell
   python manage.py loaddata initial_catalog_data.json
   ```

   sehingga data yang terdapat pada file json dapat dimunculkan pada halaman HTML.

4. Terakhir, saya memeriksa tampilhan HTML dengan perintah 

   ```shell
   python manage.py runserver
   ```
   dan membuka http://localhost:8000/katalog/ di browser untuk memastikan bahwa halaman yang dimunculkan telah sesuai dengan ketentuan.

## Poin 4: Melakukan Deploy Aplikasi Django ke Heroku

1. Pertama, saya menyalin API Key dari akun Heroku yang saya miliki 

2. Selanjutnya, saya menambahkan dan menyimpan variabel repository secret baru untuk melakukan deployment dengan Name: Secret masing-masing  
   sebagai berikut:

    ```shell
   HEROKU_API_KEY: <VALUE_API_KEY>
   HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU>
   ```

3. Terakhir, saya menjalankan kembali workflow dari commit terakhir saya yang sebelumnya gagal.

## Credits

Dokumen ini dijawab berdasarkan referensi-referensi yang saya baca dari 
1. [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy))
2. [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage)
3. [Python Virtual Environment - Geeksforgeeks](https://www.geeksforgeeks.org/python-virtual-environment/#:~:text=A%20virtual%20environment%20is%20a,of%20the%20Python%20developers%20use.)
4. [What is Django? - IBM](https://www.ibm.com/cloud/learn/django-explained)
5. [Django introduction - mdn web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
