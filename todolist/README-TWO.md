Tugas 6 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Heroku Tugas 6 - Mayfa Shadrina Siddi
[tugas5-mayfa-todolist](https://tugas2-mayfa.herokuapp.com/todolist/login/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
* Pada asynchronous programming, proses jalannya program dapat dilakukan secara bersamaan tanpa menunggu proses lain yang berjalan lebih dahulu untuk selesai. Asynchronous programming ini dapat ditemukan di hampir semua bahasa pemrograman, tetapi belum ditemukan di PHP. Untuk dapat melakukan asynchronous programming di PHP, kita dapat menggunakan AJAX (Asynchronous Javascript & XML). 
* Pada synchronous programming, proses jalannya program bersifat sequential, yaitu suatu proses harus berjalan sesuai dengan antrian eksekusi program. Dengan kata lain, dua program tidak dapat berjalan secara bersamaan. Synchronous programming ini dapat ditemukan di semua bahasa pemrograman, khususnya PHP.


## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
* Event-driven programming merupakan suatu paradigma dimana program akan berjalan sesuai dengan event yang dilakukan oleh user pada suatu halaman website/aplikasi, seperti ketika mouse click, mouse hover, mouse drag, press keyword, dan lain-lain. Setiap event yang sudah ditentukan oleh programmer, nantinya akan dihubungkan pada function yang akan berjalan ketika trigger event dilakukan.
* Pada tugas 6, saya mengimplementasikan paradigma ini pada fitur Tambah Tugas, yaitu ketika button dengan id "tambah" di-klik, maka akan memunculkan modal Tambah Tugas yang akan menyediakan form dengan text field Title dengan Description bagi pengguna untuk diisi.

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

1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON

```shell
    def show_json(request):
    data_task = Task.objects.filter(user = request.user) #sesuai sama user yang lagi login
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")
```

2. Menambah path /todolist/json yang mengarah ke view yang baru kamu buat.

```shell
    path('json/', show_json, name='show_json'),
```

# Poin 1.2: Melakukan pengambilan task menggunakan AJAX GET.

1. Mengimport library AJAX di bagian head dengan mengimport link:

```shell
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```

2. Menghapus elemen card pada HTML dan hanya menyisakan grid layouting-nya saja dengan id = "todolist"

```shell
    <div class = "grid md:grid-cols-2 lg:grid-cols-3 w-full gap-5 mt-8 sm:mt-5" id = "todolist">
```

3. Menambahkan script AJAX GET dengan memanfaatkan fungsi show_json yang telah dibuat sebelumnya lalu menambahkan tiap data (berupa card) ke dalam grid yang telah dibuat di struktur HTML dengan mengiterasi seluruh data yang ada

```shell
    $.get( "/todolist/json/", function( data ) {
        for (let i = 0; i < data.length; i++) {
          $('#todolist').append(
            `<div id = "${data[i].pk}--tugas" class = "rounded-lg pl-10 pr-6 py-5 bg-white shadow-md hover:shadow-xl">
              <div>
                <h1 class = "font-semibold text-grey text-sm">${data[i].fields.date}</h1>
                <h1 class = "text-lg font-bold">${data[i].fields.title}</h1>
                <p class="text-gray-700 text-base mb-4">
                  ${data[i].fields.description}
                </p>
              </div>
      
              <div class="flex justify-between">
                ${data[i].fields.is_finished ?
                  `<span class = "text-sm sm:text-md bg-green text-white py-2 px-3 sm: px-3 rounded-full">Selesai</span>` :
                  `<span class = "text-sm sm:text-md bg-red text-white py-2 px-3 sm: px-3 rounded-full">Belum Selesai</span>`}      
                <div>
                  ${data[i].fields.is_finished ?
                  `<td><button class = "text-sm sm:text-md bg-blue hover:bg-dark_blue text-white font-semibold hover:text-white py-2 px-3 border border-transparent hover:border-transparent rounded"><a href="/todolist/ubah/${data[i].pk}"><i class="bi bi-x-circle-fill"></i></a></button></td>` :
                  `<td><button class = "text-sm sm:text-md bg-blue hover:bg-dark_blue text-white font-semibold hover:text-white py-2 px-3 border border-transparent hover:border-transparent rounded"><a href="/todolist/ubah/${data[i].pk}"><i class="bi bi-check-circle-fill"></i></a></button></td>`}
                  <td><button class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded"><a href="/todolist/delete/${data[i].pk}"><i class="bi bi-trash-fill"></i></a></button></td>
                </div>
              </div>
            </div>`
          );
        }
    });
```

# Poin 2: Implementasi AJAX POST

# Poin 2.1: Membuat modal dan view baru untuk melakukan penambahan tugas secara asynchronous

1. Membuat modal yang berisikan dengan form dengan text field Title dan Description

```shell
    <div class="modal fade" id="modalTambah" tabindex="-1" role="dialog" aria-labelledby="createTaskModalLabel" aria-hidden="true">
    <div class="modal-dialog bg-white rounded-md" role="document">
      <div class="modal-content bg-white rounded-md">
        <div class="modal-header rounded-md">
          <h5 class="modal-title text-black" id="createTaskModalLabel">Add Task</h5>
        </div>
        <div class="modal-body">
          {% csrf_token %}
          <table>  
            <tr>
                <td>Title: </td>
                <td><input type="text" id="title" name="title" placeholder="Title" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"></td>
            </tr>
                    
            <tr>
                <td>Description: </td>
                <td><input type="text" id="description" name="description" placeholder="Description" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"></td>
            </tr>
          </table>
        </div>
        <div class="modal-footer">
          <button type="button" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" data-bs-dismiss="modal">Cancel</button>
          <button id="tambah" type="button" class = "text-sm sm:text-md bg-blue hover:bg-dark_blue text-white font-semibold hover:text-white py-2 px-4 border border-transparent hover:border-transparent rounded">Tambah</button>
        </div>
      </div>
    </div>
  </div>
```

2. Menghubungkan tombol Tambah Tugas agar dapat membuka modal yang sebelumnya telah dibuat dengan menambahkan kode ini setelah object class dengan menyesuaikannya dengan ID modal

```shell
    <button class = "....." data-bs-toggle="modal" data-bs-target="#modalTambah">
```

3. Membuat view baru untuk menambahkan task baru ke dalam database.

```shell
    @login_required(login_url='/todolist/login/')
    @csrf_exempt
    def create_task_ajax(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            if title != "" or description != "":
                task = Task.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user)
                context = {
                    'pk' : task.pk,
                    'fields' : {
                        'title' : task.title,
                        'description' : task.description,
                        'is_finished' : task.is_finished,
                        'date' : task.date
                    }
                }
                return JsonResponse(context)
```

4. Menambah path yang mengarah ke view yang baru dibuat.

```shell
    ...
    path('create-ajax/', create_task_ajax, name='create_task_ajax'),
    ...
```

# Poin 2.2: Menghubungkan form yang telah dibuat di dalam modal kamu ke path /todolist/add
1. Menambahkan script AJAX POST dengan memanfaatkan event-driven programming, yaitu ketika button dengan ID "tambah" di-klik, maka AJAX akan menambahkan data yang telah diinput ke database dan langsung membuat card Tugas

```shell
    $("#tambah").click(function(){
        $.post( "/todolist/create-ajax/", {title : $("#title").val(), description : $("#description").val()}, function(data, status) {
          if (status == "success") {
            $('#todolist').append(
            `<div id = "${data.pk}--tugas" class = "rounded-lg pl-10 pr-6 py-5 bg-white shadow-md hover:shadow-xl">
              <div>
                <h1 class = "font-semibold text-grey text-sm">${data.fields.date}</h1>
                <h1 class = "text-lg font-bold">${data.fields.title}</h1>
                <p class="text-gray-700 text-base mb-4">
                  ${data.fields.description}
                </p>
              </div>
      
              <div class="flex justify-between">
                ${data.fields.is_finished ?
                  `<span class = "text-sm sm:text-md bg-green text-white py-2 px-3 sm: px-3 rounded-full">Selesai</span>` :
                  `<span class = "text-sm sm:text-md bg-red text-white py-2 px-3 sm: px-3 rounded-full">Belum Selesai</span>`}      
                  <div>
                    ${data.fields.is_finished ?
                    `<td><button class = "text-sm sm:text-md bg-blue hover:bg-dark_blue text-white font-semibold hover:text-white py-2 px-3 border border-transparent hover:border-transparent rounded"><a href="/todolist/ubah/${data.pk}"><i class="bi bi-x-circle-fill"></i></a></button></td>` :
                    `<td><button class = "text-sm sm:text-md bg-blue hover:bg-dark_blue text-white font-semibold hover:text-white py-2 px-3 border border-transparent hover:border-transparent rounded"><a href="/todolist/ubah/${data.pk}"><i class="bi bi-check-circle-fill"></i></a></button></td>`}
                    <td><button class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded"><a href="/todolist/delete/${data.pk}"><i class="bi bi-trash-fill"></i></a></button></td>
                  </div>
              </div>
            </div>`
            )
            $('#title').val('')
            $('#description').val('')
          }
        })
    })
```

2. Menambahkan kode sebagai berikut setelah object class pada button Tambah sehingga modal bisa ditutup

```shell
    <button class = "..." data-bs-dismiss="modal">
```

## Credits

Dokumen ini dijawab berdasarkan referensi-referensi yang saya baca dari 
1. [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy))
2. [Tailwind Documentation](https://tailwindcss.com/)
3. [Apa Perbedaan Inline CSS, Internal CSS, dan External CSS? - Niagahoster](https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/)
4. [Apa Itu HTML5? Simak Perbedaan HTML dan HTML5 di Sini! - Niagahoster](https://www.niagahoster.co.id/blog/html5-adalah/#Perbedaan_HTML_dan_HTML5)
5. [Types of CSS Selectors - EDUCBA](https://www.educba.com/types-of-css-selectors/)