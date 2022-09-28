Tugas 4 Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Heroku Tugas 3 - Mayfa Shadrina Siddi
[tugas4-mayfa-todolist](https://tugas2-mayfa.herokuapp.com/todolist/)

## Kegunaan {% csrf_token %}

Cross-Site Request Forgery (CSRF) adalah salah satu jenis serangan yang kerap ditemukan pada Web yang dilakukan oleh peretas dengan merekayasa HTTP request (berpura-pura sebagai Client) untuk mendapatkan data - data dan informasi (khususnya yang diinput oleh Client) sehingga dapat mengakibatkan kerugian ekonomi atau pengambilalihan akun. Untuk mencegah serangan tersebut, dibuatkan CSRF Token yang merupakan value unik dan rahasia yang dihasilkan oleh aplikasi untuk nantinya dikirimkan dan dibuat di client-server. Hal ini akan mencegah penyerangan akun karena peretas tidak dapat menebak value dari CSRF Token yang dibuat. Dengan adanya implementasi CSRF Token, maka aplikasi dapat melakukan validasi terhadap HTTP request yang dikirimkan oleh peretas dan menolaknya apabila CSRF Token-nya tidak tersedia atau tidak valid (tidak sesuai dengan yang dibuat pada Client-server sebelumnya). Potongan kode yang dibutuhkan untuk mengaktifkan CSRF Token adalah dengan menambahkan {% csrf_token %} pada elemen <form>.

Jika tidak terdapat potongan kode tersebut pada elemen <form>, maka data dan informasi Client yang terdapat pada aplikasi akan rawan diserang karena tidak terdapat ‘pembeda’ antara HTTP request yang dikirimkan oleh Client asli dan peretas. Selain itu, akan lebih baik bagi CSRF Token untuk disisipkan sedini mungkin pada dokumen HTML agar peretas tidak mudah memanipulasi dokumen dan mendapatkan data - data di dalamnya.


## Pembuatan Form Secara Manual
Selain menggunakan generator, kita dapat membuat elemen <form> secara manual, yaitu dengan menambahkan <form> pada start tag dan menambahkan </form> pada end tag yang menjadi container bagi jenis-jenis elemen input, seperti text field, checkbox, radio button, submit button, dll.

    ```shell
    <form>
        .
        form elements
        .
    </form>
    ```
Elemen-elemen yang dapat digunakan pada <form> berupa
1. <input>
    Elemen <input> dapat ditampilkan dengan bermacam-macam bentuk, tergantung dengan atribut-nya

    ```shell
    <input type="text">
    <input type="radio">
    <input type="checkbox">
    <input type="submit">
    <input type="button">
    ```

2. <label>
    ELemen <label> berfungsi untuk memberikan penamaan/text pada masing-masing <input> sehingga dapat mempermudah user untuk memahami <form>

Contoh:
    ```shell
    <form>
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname">
    </form>
    ```

## Proses Alur Data pada HTML Form, Penyimpanan Data ke Database, dan Menampilkan Data ke Template HTML
Pertama, pengguna akan mengeklik tombol "Tambah Tugas" yang telah dihubungkan pada halaman create_task.html sehingga akan muncul elemen <form> yang telah dirouting dengan filem forms.py dan akan meminta data Judul/Title serta Deskripsi/Description kepada pengguna. Setelah pengguna mengisi TextField dan mengeklik tombol "Tambah" maka data akan tersimpan ke database, lalu function show_todolist akan mengakses data - data yang telah dikumpulkan (sesuai dengan pengguna) melalui model Task, lalu di-render dengan todolist.html. Setelah proses render selesai, maka data dapat dimunculkan pada halaman HTML pengguna, dan atribut-nya akan ditampilkan pada tabel terkait

## Poin 1: Membuat Aplikasi “todolist”

1. Pertama, saya membuka command prompt, mengakses direktori Tugas 2 lalu mengaktifkan virtual environment dengan instruksi

   ```shell
   python -m venv env
   env\Scripts\activate.bat
   ```

2. Lalu, saya menjalankan instruksi untuk membuat aplikasi baru yang bernama “todolist”

   ```shell
   python manage.py startapp todolist
   ```

3. Kemudian saya menambahkan keyword ‘mywatchlist’ pada variabel INSTALLED_APPS pada file settings.py di folder project_django

    ```shell
    INSTALLED_APPS = [
    ...,
    'todolist',
    ]
    ```

## Poin 2: Menambahkan Path “todolist”


1. Untuk menambakan path “todolist”, saya menambahkan nama aplikasi ke variable urlpatterns pada file urls.py di folder project_django 

   ```shell
   ...
    path('mywatchlist/', include('mywatchlist.urls')),
    ...
   ```

## Poin 3: Membuat Model Task

1. Saya membuka file models.py yang ada pada folder todolist untuk membuat model yang nantinya akan mendistribusikan data-data dengan membuat kelas Task

   ```shell
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField()
        title = models.TextField()
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
   ```

2. Selanjutnya, saya melakukan perintah 

   ```shell
    python manage.py makemigrations 
    python manage.py migrate
   ```
   untuk menjalankan migrasi skema model ke dalam database Django lokal.

## Poin 4: Mengimplementasikan Form Registrasi, Log In, dan Log Out

## Poin 4.1: Registrasi
1. Pertama, saya menambahkan import redirect, UserCreationForm, dan messages pada baris paling atas berkas views.py

    ```shell
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```

2. Lalu saya menambahkan potongan kode untuk membuat fungsi register yang menerima parameter request agar dapat menghasilkan formulir pendaftaran secara otomatis dan mendaftarkan akun pengguna ketika sedang register (dengan informasi username & password)

    ```shell
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Akun telah berhasil dibuat!')
                return redirect('todolist:login')
        
        context = {'form':form}
        return render(request, 'register.html', context)
    ```

3. Setelah itu saya membuat berkas HTML bernama “register.html” pada folder todolist/templates untuk menampilkan formulir registrasi pada mesin pengguna. Saya juga menyertakan kode {% csrf_token %} untuk melindungi data dan informasi dari serangan Cross-Site Request Forgery

4. Lalu saya mengimport fungsi register ke urls.py

    ```shell
    from todolist.views import register
    ```

5. Terakhir, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi

    ```shell
    ...
    path('register/', register, name='register'),
    ...
    ```
    
## Poin 4.2: Log In
1. Pertama, saya menambahkan import authenticate dan login pada baris paling atas berkas views.py

    ```shell
    from django.contrib.auth import authenticate, login
    ```

2. Lalu saya menambahkan potongan kode untuk membuat fungsi login_user yang menerima parameter request agar dapat menghasilkan formulir autentikasi secara otomatis untuk emmvalidasi pengguna yang log in (dengan informasi username & password)

    ```shell
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todolist:show_todolist')
            else:
                messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)
    ```

3. Setelah itu saya membuat berkas HTML bernama "login.html" pada folder todolist/templates untuk menampilkan formulir log in pada mesin pengguna. Saya juga menyertakan kode {% csrf_token %} untuk melindungi data dan informasi dari serangan Cross-Site Request Forgery

4. Lalu saya mengimport fungsi login ke urls.py

    ```shell
    from todolist.views import login_user
    ```

5. Terakhir, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi

    ```shell
    ...
    path('login/', login_user, name='login'),
    ...
    ```

## Poin 4.3: Log Out
1. Pertama, saya menambahkan import logout pada baris paling atas berkas views.py

    ```shell
    from django.contrib.auth import logout
    ```

2. Lalu saya menambahkan potongan kode untuk membuat fungsi logout_user yang menerima parameter request agar mengimplementasikan mekanisme logout

    ```shell
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('todolist:login'))
        return response
    ```

3. Lalu saya mengimport fungsi logout ke urls.py

    ```shell
    from todolist.views import logout_user
    ```

4. Selanjutnya, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi

    ```shell
    ...
    path('logout/', logout_user, name='logout'),
    ...
    ```

5. Terakhir, saya membuat button Logout pada template todolist.html yang dapat diklik untuk menjalankan mekanisme logout

    ```shell
    ...
    <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
    ...
    ```

## Poin 5: Membuat Halaman Utama “todolist”

1. Pertama, saya membuat sebuah fungsi yang menerima parameter request pada file views.py di folder todolist untuk memanggil fungsi query ke model database (Task) dan menyimpan hasil query tersebut ke dalam sebuah variabel. Pada fungsi HTML saya juga menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat agar dapat memunculkan datanya pada halaman.

    ```shell
    def show_todolist(request):
        data_task = Task.objects.filter(user = request.user)
        context = {
        'list_task': data_task,
        }
        return render(request, 'todolist.html', context)

    ```

2. Selanjutnya saya membuat sebuah berkas bernama todolist.html pada folder templates untuk melakukan iterasi terhadap variabel list_task agar dapat mengambil data/atribut spesifik dari masing-masing objek yang terdapat dalam variabel tersebut.

3. Lalu saya mengimport fungsi logout ke urls.py

    ```shell
    from todolist.views import show_todolist
    ```

4. Terakhir, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi

    ```shell
    path('', show_todolist, name='show_todolist')
    ```

## Poin 6: Membuat Halaman Form Penambahan Task

1. Pertama, saya membuat berkas bernama “forms.py” pada folder todolist dan melakukan import forms dan mengimport model Task pada baris paling atas

    ```shell
    from django import forms
    from todolist.models import Task
    ```

2. Lalu, saya membuat class create_form yang berisikan parameter forms.Form pada forms.py lalu membuat CharField dan TextField yang dapat diisi oleh pengguna ketika menambahkan task baru

    ```shell
    class create_form(forms.Form):
        title = forms.CharField(label = "Title", max_length=255)
        description = forms.TextField(label = "Description")
    ```

3. Selanjutnya, saya membuat fungsi create_task yang akan menghasilkan formulir penambahan tugas

    ```shell
    def create_task(request):
    if request.method == 'POST':
        form = create_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Task.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user)
            return redirect('todolist:show_todolist')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = create_form()
    context = {
        'form': form,
        }
    return render(request, 'create_task.html', context)
    ```

4. Selanjutnya saya membuat berkas bernama “create_task.html” pada folder todolist/templates yang berisikan potongan kode untuk membuat tampilan formulir

5. Lalu saya mengimport fungsi create_task ke urls.py

    ```shell
    from todolist.views import create_task
    ```

6. Selanjutnya, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi

    ```shell
    path('create-task/', create_task, name='create_task'),
    ```

7. Terakhir, saya menambahkan button pada todolist.html yang menyambungkannya pada mekanisme penambahan task

    ```shell
    <button><a href="{% url 'todolist:create_task' %}">Tambah Tugas</a></button>
    ```

## Poin 7: Membuat Routing pada URL

1. Saya melakukan routing terhadap fungsi views yang telah dibuat pada file urls.py di todolist agar tiap halaman dapat dimunculkan pada browser

    ```shell
    from django.urls import path
    from todolist.views import show_todolist
    from todolist.views import register
    from todolist.views import login_user
    from todolist.views import logout_user
    from todolist.views import create_task

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('create-task/', create_task, name='create_task'),
    ]
    ```

## Poin 8: Melakukan Deployment ke Heroku

1. Terakhir saya melakukan deployment dengan instruksi

    ```shell
    git add .
    git commit -m “<pesan commit>”
    git push -u origin main
   ```
   dan GitHub akan secara otomatis melkaukan deployment ke Heroku yang saya miliki

2. Membuat akun pengguna dan data dummy pada aplikasi “todolist”

## Credits

Dokumen ini dijawab berdasarkan referensi-referensi yang saya baca dari 
1. [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy))
2. [Working with forms - Django](https://docs.djangoproject.com/en/4.1/topics/forms/)
3. [Making queries - Django](https://docs.djangoproject.com/en/4.1/topics/db/queries/#:~:text=Creating%20objects&text=To%20create%20an%20object%2C%20instantiate,save%20it%20to%20the%20database.&text=This%20performs%20an%20INSERT%20SQL,method%20has%20no%20return%20value.)
4. [Cross Site Request Forgery protection - DJango](https://docs.djangoproject.com/en/4.1/ref/csrf/)
5. [Django Delete Record - W3Schools](https://www.w3schools.com/django/django_delete_record.php)
6. [Apa itu pengertian CSRF? - Pemburu Kode](https://pemburukode.com/apa-itu-csrf-pengertian-csrf-dan-implemntasi-di-form-input-website/)