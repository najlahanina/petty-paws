## TUGAS 2
## 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.Membuat sebuah proyek Django baru.
      
  - Buat direktori baru untuk dijadikan lokal direktori dan repository github   bernama petty-paws.
     
  - Buka direktori tersebut pada vscode dan jalankan git init, git config user.name, dan git config user.email pada terminal untuk kebutuhan repository github.
    
  - Buat repository baru pada github bernama petty-paws.
      
  - Jalankan perintah git branch -M main, git remote add origin https://github.com/najlahanina/petty-paws.git, dan git push -u origin main untuk membuat  branch dengan nama main, menghubungkan lokal direktori dengan repository github, dan uodate semua perubahan ke github.

  - Jalankan perintah python3 -m venv env dan source env/bin/activate untuk membuat dan mengaktifkan virtual environment untuk directory yang akan digunakan untuk pengembangan proyek Django
      
  - Buat file bernama requirements.txt yang kemudian diisi dengan dependencies yang ingin diinstall, lalu jalankan pip install -r requirements.txt untuk menginstallnya
  
  - Jalankan django-admin startproject petty_paws . untuk membuat proyek baru

  - Menambahkan local host pada ALLOWED_HOSTS di settings.py sebagai host yang diizinkan untuk akses app web

  - Buat file bernama .gitignore untuk memberikan informasi mengenai berkas yang perubahannya tidak perlu ditrack git

  - Lakukan add, commit, dan push dari direktori repositori lokal.

2.Membuat aplikasi dengan nama main pada proyek tersebut.

  - Jalankan perintah python3 manage.py startapp main untuk membuat app baru bernama main pada terminal yang sama.

  - Buka file settings.py dan tambahkan 'main' pada variable INSTALLED_APPS.

  - Dalam direktori main, buat direktori baru bernama templates untuk menyimpan file html yang akan digunakan.

  - Pada direktori templates, buat file bernama main.html yang diisi dengan format 2nama aplikasi, nama, npm, dan kelas.

3.Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
      
  - Buka file urls.py pada direktori petty_paws

  - Tambahkan import "from django.urls import path, include" dan pada variable urlpatters tambahkan path('', include('main.urls')).
  - Jalankan proyek dengan perintah python3 manage.py runserver dan buka http://localhost:8000/ utnuk melihat web yang sudah dibuat.

4.Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
      
  - Buka file models.py dan isi dengan atribut yang diperlukan. Saya menggunakan 6 atribut yaitu name (CharField), image (ImageField), brands (CharField),  price (IntegerField), categories (TextField), dan description (TextField)

  - Membangun dan menerapkan migrasi model ke database lokal untuk melacak perubahan yang terjadi pada model database.

5.Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

  - Buka file views.py dan buat fungsi show_main yang berisi nama, npm, dan kelas untuk menghubungkan views dan templates

  - Ubah file main.html menjadi template variable seperti {{ nama }} untuk menampilkan value variable yang sudah didefinisikan dalam context.
 
6.Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

  - Buat file urls.py di direktori main dan isi urlpatterns dengan path('', show_main, name='show_main')

  - '' berguna saat mengakses .../main/ akan memanggil show_main dari views.py

7.Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    
  - Pada terminal yang sama, update repository github dengan menjalankan perintah git add ., git commit -m "komentar", dan git push -u origin main

  - Akses PWS kemudian login dan create new project

  - Pada file settings.py tambahkan URL deployment PWS "nisa-najla-pettypaws.pbp.cs.ui.ac.id" pada ALLOWED_HOSTS.

  - Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS.

  - Jika ada perubahan kembali pada proyek, cukup jalankan perintah git push pws main:master

## 2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/najlahanina/petty-paws/blob/main/BaganTugas2PBP.jpeg)
Permintaan dari client dikirim melalui Internet, lalu diteruskan ke Python/Django dan diarahkan ke urls.py. Setelah itu, proses berlanjut ke views.py untuk memproses URL yang diminta. Dalam tahap ini, sistem membaca atau menulis data dari/ke models.py dan database. Data kemudian diinput atau ditampilkan melalui templates. File HTML yang sudah digabung dengan berbagai value yang dibutuhkan akan dikembalikan melalui Internet dan akhirnya ditampilkan di perangkat client.

## 3.  Jelaskan fungsi git dalam pengembangan perangkat lunak!

- Membantu mengorganisir project karena memungkinkan para programmer untuk memiliki salinan lengkap dari seluruh repository, termasuk riwayat perubahan, commit, dan branch. Hal itu karena fitur Distributed Version Control System (DVCS) yang dimiliki git sehingga pengelolaan proyek menjadi lebih terorganisir dan konsisten.

- Memberikan fleksibilitas karena git bersifat open source dan  cross platform sehingga dapat diinstall dan digunakan tanpa masalah di berbagai sistem operasi, seperti Windows, macOS, dan Linux. 

- Memudahkan kolaborasi antar developer melalui fitur merging dan branching karena dapat membuat cabang baru untuk mengembangkan fitur atau memperbaiki bug tanpa mempengaruhi cabang utama lalu menggabungkannya kembali dengan perintah merge. Fitur push dan pull juga mempermudah berbagi dan mengintegrasikan perubahan.

## 4.  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan untuk pembelajaran pengembangan perangkat lunak karena framework ini menggunakan bahasa Python sebagai basisnya. Seperti yang kita ketahui, Python merupakan bahasa pemrograman yang termasuk mudah untuk dipelajari untuk pemula karena sintaksnya yang sederhana dan bahasa yang digunakan masih mendekati bahasa “manusia”. Dengan struktur kode yang jelas tentunya akan memudahkan para developer untuk membaca dan memahaminya sehingga akan mempermudah mereka dalam pengembangan perangkat lunak. 

Selain itu, Django juga merupakan framework yang bersifat open source. Hal itu membuat dokumentasinya dapat diakses untuk dipelajari secara bebas dan terperinci. Django juga memiliki banyak fitur yang akan membantu developer dalam pengembangan perangkat lunak.

## 5.  Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut dengan ORM (Object-Relational Mapping) karena model ini berfungsi untuk memetakan data dari database relasional dengan objek dalam kode pemrograman yaitu Python. Model ini juga memungkinkan developer untuk berinteraksi dengan data menggunakan operasi objek Python tanpa harus menulis query SQL secara langsung. Dengan Django ORM merepresentasikan tabel di database dan setiap atribut model adalah kolom dari tabel tersebut. ORM otomatis menangani hubungan antara tabel, membuat operasi data menjadi lebih mudah dan abstrak.


## TUGAS 3
## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Berguna untuk konektivitas antar komponen karena platform terdiri dari berbagai komponen seperti database, server aplikasi, dan front-end. Dengan data delivery maka data dapat dipindahkan di antara komponen-komponen tersebut dengan cara yang efisien sehingga dapat bekerja dengan baik.

- Menjaga keamanan data karena semakin tingginya ancaman keamanan siber. Data delivery dapat melindungi data tersebut  agar tetap rahasia selama transmisi dengan menerapkan enkripsi dan otentikasi. Enkripsi adalah mengubah data menjadi bentuk yang tidak terbaca sedangkan otentikasi untuk memastikan bahwa yang terlibat dalam pertukaran data adalah pihak yang sah. 

- Dapat mengelola trafik dan kinerja. Dalam platform yang berskala besar, jumlah data yang dikirim biasanya juga akan besar dan kompleks. Dengan data delivery, platform dapat mengelola trafik yang tinggi dengan menggunakan teknik load balancing dan caching. 

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
XML dan JSON keduanya memiliki tujuan yang sama yaitu untuk menyimpan dan mengirimkan data. Namun, ada beberapa perbedaan antara keduanya yang membuat JSON lebih populer dibandingkan XML.

- Syntax yang digunakan dalam JSON cenderung lebih sederhana dan ringkas dibandingkan XML. Data di JSON diwakili oleh objek dan array yang mudah dibaca dan ditulis, sedangkan XML memerlukan tag pembuka dan penutup yang membuatnya lebih rumit dan panjang.

- JSON terintegrasi dengan JavaScript sehingga mempermudah pengembangan aplikasi web. Data dalam format JSON bisa langsung digunakan dalam kode JavaScript tanpa memerlukan parsing yang rumit, berbeda dengan XML yang membutuhkan parsing tambahan.

- JSON juga didukung oleh berbagai API sehingga memudahkan developer dalam pengembangan web/aplikasi 

Dari kelebihan-kelebihan yang terdapat pada JSON, maka menurut saya lebih baik JSON dibandingkan dengan XML baik secara struktur, syntax, dan beberapa faktor lainnya.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dikirim melalui form memenuhi syarat validasi yang telah didefinisikan. Method ini juga memastikan bahwa input dari pengguna sudah benar sebelum diproses lebih lanjut. Method ini akan memeriksa validitas data dengan melihat apakah semua field dalam form sesuai dengan aturan validasi. Jika semua data valid, method ini mengembalikan nilai True dan mengisi atribut cleaned_data yaitu sebuah dictionary berisi data yang sudah divalidasi dan siap digunakan. Jika data tidak valid, Django menambahkan pesan kesalahan ke form dan mengembalikan False dan memungkinkan penanganan error yang tepat.

Method ini diperlukan karena berperan penting dalam menjamin integritas data dengan memastikan bahwa hanya data valid yang diproses, sesuai dengan aturan yang ditentukan, sehingga mencegah potensi kesalahan atau inkonsistensi dalam aplikasi. Selain itu, method ini memudahkan pengelolaan error karena Django secara otomatis menangani validasi dan kesalahan, sehingga developer dapat dengan mudah menampilkan pesan error yang tepat kepada pengguna. Dengan is_valid(), proses validasi juga disederhanakan, karena validasi dapat dilakukan hanya dengan satu panggilan method, membuat kode lebih bersih dan efisien.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token dibutuhkan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang mengelabui pengguna yang sudah terautentikasi di sebuah situs web untuk melakukan tindakan yang tidak diinginkan, seperti mentransfer dana atau mengubah email. Django menyediakan token CSRF unik untuk setiap sesi pengguna, yang disertakan dalam form dan diperiksa oleh server untuk memastikan bahwa permintaan tersebut berasal dari pengguna sah dan bukan dari sumber berbahaya.

Jika csrf_token tidak ditambahkan, aplikasi rentan terhadap serangan CSRF. Penyerang dapat mengirimkan tautan berbahaya melalui SMS, email, atau pesan obrolan yang, jika diakses oleh pengguna yang sedang login, dapat memicu permintaan berbahaya ke server. Contoh dampaknya bisa berupa perubahan email, transfer dana, atau bahkan akses penuh ke akun pengguna.

Hal tersebut bisa dimanfaatkan penyerang dengan mengarahkan pengguna untuk mengklik tautan berbahaya yang diam-diam mengirimkan permintaan yang tampak sah ke server menggunakan kredensial pengguna. Jika tidak ada token CSRF yang memverifikasi permintaan, server akan mengeksekusi tindakan tersebut, memberi penyerang kendali atas akun atau data pengguna.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat input form untuk menambahkan objek model pada app sebelumnya.

- Pada direktori utama, buat subdirektori bernama templates dan buat file baru bernama base.html. Kemudian isi file tersebut dengan kerangka umum untuk halaman pada proyek nantinya seperti berikut:
```html 
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
    </head>

    <body>
      {% block content %} {% endblock content %}
    </body>
  </html>
```
- Buka file settings.py lalu tambahkan kode 'DIRS': [BASE_DIR / 'templates'] pada variabel TEMPLATES agar base.html terdeteksi sebagai template.

- Ubah file main.html untuk menggunakan base.html sebagai template utama dengan menambahkan kode berikut pada bagian atas dan bawah
```html
{% extends 'base.html' %}
{% block content %}
…
{% endblock content %}
```
- Buka file models.py dan tambahkan import uuid

- Jalankan perintah berikut untuk migrasi model:
  python3 manage.py makemigrations
  python3 manage.py migrate

- Buat file baru bernama forms.py pada direktori main dan mengisinya dengan struktur form yang dapat menerima data produk baru seperti berikut
```python
  from django.forms import ModelForm
  from main.models import Product

  class  ProductForm(ModelForm):
      class Meta:
          model = Product
          fields = ["name", "image", "brands", "price", "categories", "description"]
```
"model = Product" menandakan bahwa isian form akan disimpan sebagai objek Product. "fields" menandakan objek Product memiliki 6 atribut yang dapat diisi melalui form.

- Tambah beberapa import sebagai berikut pada file views.py untuk menyediakan akses ke form dan model yang dibutuhkan dalam menampilkan form, memvalidasi input, menyimpan data ke database, serta mengarahkan pengguna ke halaman lain setelah form diproses.
  from django.shortcuts import render, redirect
  from main.forms import ProductForm
  from main.models import Product

- Setelah itu, buat fungsi baru bernama create_product pd views.py yang menerima parameter request untuk menghasilkan form yang berguna menerima input user untuk tambah data produk ketika data tersebut disubmit pada form, seperti berikut:
```python
def create_product(request):
    form = ProductForm(request.POST or None) 

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
- Ubah fungsi show_main pada views.py menjadi sebagai berikut:
```python
def show_main(request):
    products = Product.objects.all()
    context = {
        'nama' : 'Nisa Najla Hanina Hasanah',
        'kelas' : 'PBP A',
        'products': products
    }

    return render(request, "main.html", context)
```
"products = Product.objects.all()" dan "'products': products". products akan menyimpan seluruh produk yang ada pada proyek saat ini.

- Pada file urls.py di direktori main, import fungsi create_product dan tambahkan path URLnya ke dalam variable urlpatterns.

- Buat file baru pada direktori main/templates bernama create_product.html dan isi dengan kode berikut:
```html
  {% extends 'base.html' %} 

  {% block content %}
  <h1>Add New Product</h1>

  <form method="POST">
      {% csrf_token %}
      <table>
          {{ form.as_table }}
          <tr>
              <td></td>
              <td>
                  <input type="submit" value="Add Product"/>
              </td>
          </tr>
      </table>
  </form>

  {% endblock %}
```
- Pada file main.html, tambahkan kode berikut ke dalam {% block content %}  untuk representasi data produk ke dalam bentuk tabel dan menambahkan tombol Add New Product Entry yang akan redirect ke form page
```html
{% if not products %}
<p>Belum ada data produk pada Petty Paws.</p>
{% else %}
<table>
    <tr>
        <th>Name</th>
        <th>Image</th>
        <th>Brands</th>
        <th>Price</th>
        <th>Categories</th>
        <th>Description</th>
    </tr>
        
    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini 
    {% endcomment %}
    {% for product in products %}
    <tr>
        <td>{{product.name}}</td>
        <td><img src="{{product.image}}" alt="{{product.name}}" style="width: 200px; height: 200px;"></td>
        <td>{{product.brands}}</td>
        <td>{{product.price}}</td>
        <td>{{product.categories}}</td>
        <td>{{product.description}}</td>
    </tr>
    {% endfor %}
</table>
{% endif %}
        
<br />
        
<a href="{% url 'main:create_product' %}">
    <button>Add New Product</button>
</a>
```
- Jalankan server dengan perintah python3 manage.py runserver dan masuk ke http://localhost:8000/ untuk menambahkan produk.

2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

- Pada file views.py, tambahkan import HttpResponse dan Serializer pada bagian paling atas.

- Pada file views.py, tambahkan 4 fungsi berikut yang menerima parameter request:

  - fungsi "show_xml" yang berfungsi untuk menampilkan representasi semua produk dalam format XML dan dapat diakses pada (url)/xml
  ```python
  def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  ```
  - fungsi "show_json" yang berfungsi untuk menampilkan representasi semua produk dalam format JSON dan dapat diakses pada (url)/json
  ```python
  def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
  - fungsi "show_xml_by_id" yang berfungsi untuk menampilakn representasi produk sesuai id yang diinginkan dalam format XML dan dapat diakses pada (url)/xml/(desired_id)
  ```python
  def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  ```
  - fungsi "show_json_by_id" yang berfungsi untuk menampilakn representasi produk sesuai id yang diinginkan dalam format JSON dan dapat diakses pada (url)/json/(desired_id)
  ```python
  def show_json_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```

3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

- Buka file urls.py pada direktori main lalu tambahkan import fungsi-fungsi yang sudah dicantumkan pada file views.py dan masukkan urlnya pada variable urlpattern, seperti berikut:
```python
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
- Jalankan server dengan perintah python3 manage.py runserver dan masuk ke:

  - http://localhost:8000/xml/: Untuk menampilkan representasi seluruh products dalam format XML

  - http://localhost:8000/json/: Untuk menampilkan representasi seluruh products dalam format JSON

  - http://localhost:8000/xml/[id]/: Untuk menampilkan representasi product dengan id yang diinginkan dalam format XML

  - http://localhost:8000/json/[id]/: Untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON

## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
- Jalankan proyek dengan perintah python3 manage.py runserver

- Buka Postman lalu buat request baru dengan method GET dan masukkan url http://localhost:8000/xml/ atau http://localhost:8000/json/ lalu klik button send.

- Selain itu juga bisa memasukkan url http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] untuk pengambilan data berdasarkan ID.

Screenshot hasil akses URL pada Postman
1. XML
![](https://github.com/najlahanina/petty-paws/blob/main/SS%20XML.png)

2. JSON
![](https://github.com/najlahanina/petty-paws/blob/main/SS%20JSON.png)

3. XML by ID
![](https://github.com/najlahanina/petty-paws/blob/main/SS%20XML%20by%20ID.png)

4. JSON by ID
![](https://github.com/najlahanina/petty-paws/blob/main/SS%20JSON%20by%20ID.png)

## Tugas 4
## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
1. HttpResponseRedirect():

   - Ini adalah objek HTTP response bawaan Django yang secara eksplisit digunakan untuk melakukan pengalihan ke URL tertentu.
   
   - Memerlukan URL yang akan dialihkan sebagai argumen.

   - Perlu mengonversi URL secara manual menggunakan fungsi seperti reverse() atau menuliskan URL lengkap secara langsung.

2. redirect():

   - Merupakan shortcut function yang lebih fleksibel dari Django.

   - Bisa menerima URL, nama view, atau objek model sebagai argumen dan redirect() akan mengurus sisanya.

   - Jika diberikan nama view atau model, Django secara otomatis akan mengonversinya menjadi URL menggunakan reverse().
## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan Product dengan User, pertama, di models.py, tambahkan ForeignKey ke model Product untuk mengaitkan setiap produk dengan pengguna tertentu. Hal ini memungkinkan setiap produk memiliki referensi ke pengguna yang membuatnya.

Kemudian, di views.py, pada fungsi create_product, saat pengguna mengirim formulir untuk membuat produk baru, data produk divalidasi dan sebelum disimpan ke basis data, produk tersebut ditandai dengan pengguna yang sedang login menggunakan request.user. Ini memastikan produk yang dibuat terhubung dengan akun pembuatnya.

Selanjutnya, di fungsi show_main, hanya produk yang dimiliki oleh pengguna yang sedang login ditampilkan, dengan memfilter produk berdasarkan request.user. Hal ini memastikan setiap pengguna hanya melihat produk yang mereka buat sendiri.
## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Perbedaan antara autentikasi dan otorisasi saat pengguna login:

1. Autentikasi

- Autentikasi adalah proses verifikasi identitas pengguna yang ingin mengakses web page.

- Proses ini bertujuan untuk mengonfirmasi identitas pengguna sehingga dapat dipastikan pengguna tersebut benar-benar terdaftar dalam sistem.

- Pada saat login, autentikasi adalah tahap saat pengguna diminta untuk memasukkan username dan password mereka dan sistem akan memveririkasi apakah kredensial tersebut cocok dengan pengguna yang ada di database. Jika cocok, pengguna diizinkan mengakses web page tersebut.

2. Otorisasi

- Otorisasi adalah proses yang terjadi setelah autentikasi. Otorisasi merupakan mekanisme yang menentukan apakah pengguna yang telah diautentikasi memiliki izin untuk mengakses resorece atau fitur tertentu dalam sistem.

- Proses ini bertujuan untuk mengontrol apa saja yang bisa atau tidak bisa dilakukan oleh pengguna setelah mereka berhasil login.

- Otorisasi bekerja setelah proses login jadi setelah pengguna berhasil login, Django akan memeriksa hak akses yang dimiliki pengguna tersebut. Misal, pengguna dengan status admin bisa mengakses halaman yang hanya diperuntukkan bagi admin, sementara pengguna biasa tidak bisa.

Bagaimana Django mengimplementasikan kedua konsep tersebut:

Untuk autentikasi, Django menyediakan beberapa fungsi. Pertama, authenticate() digunakan untuk memverifikasi kredensial pengguna. Jika valid, fungsi ini mengembalikan objek pengguna, dan jika tidak valid, mengembalikan None. Setelah autentikasi berhasil, login() digunakan untuk login pengguna dan membuat sesi, memungkinkan pengguna tetap terhubung ke sistem. Sebaliknya, logout() digunakan untuk mengakhiri sesi pengguna dan mengeluarkannya dari sistem. Django juga menyediakan dekorator @login_required yang memastikan bahwa hanya pengguna yang telah login dapat mengakses view tertentu.

Untuk otorisasi, Django menggunakan sistem izin dan grup. Setiap model di Django memiliki izin bawaan seperti "add", "change", "delete", dan "view", dan izin ini dapat diperiksa menggunakan metode user.has_perm(). Selain itu, Django menyediakan fitur grup, di mana setiap grup dapat memiliki izin tertentu, dan anggota grup tersebut akan mewarisi izin tersebut. Django juga menyediakan dekorator @permission_required yang memastikan pengguna memiliki izin tertentu sebelum bisa mengakses suatu view. Dengan kombinasi autentikasi dan otorisasi ini, Django memungkinkan kontrol akses yang fleksibel dan aman untuk aplikasi web.

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan sesi dan cookies. Ketika pengguna login, Django membuat sesi yang menyimpan informasi pengguna di server dan menciptakan cookie sesi (biasanya sessionid) di sisi klien. Cookie ini dikirim bersama setiap permintaan untuk mengidentifikasi pengguna yang sedang login. Cookies memiliki beberapa kegunaan lain selain autentikasi. Salah satunya adalah menyimpan preferensi pengguna, seperti pilihan tema tampilan atau bahasa yang dipilih, sehingga pengalaman pengguna menjadi lebih personal. Selain itu, cookies juga digunakan untuk melacak aktivitas pengguna di situs web dengan mencatat halaman yang dikunjungi dan interaksi yang dilakukan, yang membantu pengembang memahami pola penggunaan.

Penggunaan cookies dapat menjadi tidak aman karena data yang disimpan di dalamnya berisiko diakses oleh pihak yang tidak berwenang jika tidak dikelola dengan baik. Potensi risiko meliputi pencurian informasi pengguna, peretasan sesi, dan penyadapan data sensitif. Untuk mengurangi risiko ini, developer perlu mengikuti praktik keamanan yang baik, seperti mengenkripsi data dalam cookies, menggunakan atribut keamanan seperti HttpOnly dan Secure untuk mencegah akses melalui JavaScript dan memastikan penggunaan HTTPS, serta menyimpan informasi sesi pengguna yang sensitif di server bukan di cookies.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

  REGISTRASI

  - Aktifkan virtual environtment pada terminal

  - Buka file views.py, tambahkan beberapa import dan fungsi register sebagai berikut:
  ```python
  from django.shortcuts import redirect
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib import messages  

  def register(request):
      form = UserCreationForm()

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)
  ```
  form.is_valid() berguna untuk memvalidasi isi form dan form.save() berguna untuk membuat dan menyimpan data.

  - Buat file baru bernama register.html pada direktori main/templates dan isi dengan kod eberikut:
  ```html
  {% extends 'base.html' %}

  {% block meta %}
      <title>Register</title>
  {% endblock meta %}

  {% block content %}  

  <div class = "login">
      
      <h1>Register</h1>  

          <form method="POST" >  
              {% csrf_token %}  
              <table>  
                  {{ form.as_table }}  
                  <tr>  
                      <td></td>
                      <td><input type="submit" name="submit" value="Daftar"/></td>  
                  </tr>  
              </table>  
          </form>

      {% if messages %}  
          <ul>   
              {% for message in messages %}  
                  <li>{{ message }}</li>  
                  {% endfor %}  
          </ul>   
      {% endif %}

  </div>  
  {% endblock content %}
  ```
  - Buka urls.py pada direktori main, import fungsi register dan tambahkan path url ke dalam variable urlpatterns seperti berikut:
  ```python
  from main.views import register
  urlpatterns =[
    path('register/', register, name='register'),]
  ```
  LOGIN

  - Buka file views.py, tambahkan beberapa import untuk melakukan autentikasi dan login pengguna, lalu buat fungsi login_user untuk membuat formulir regis dan menghasilkan akun pengguna
  ```python
  from django.contrib.auth import authenticate, login
  def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
  ```
  - Buat file baru bernama login.html pada direktori main/templates dan mengisinya dengan kode berikut:
  ```html
  {% extends 'base.html' %}

  {% block meta %}
      <title>Login</title>
  {% endblock meta %}

  {% block content %}

  <div class = "login">

      <h1>Login</h1>

      <form method="POST" action="">
          {% csrf_token %}
          <table>
              <tr>
                  <td>Username: </td>
                  <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
              </tr>
                      
              <tr>
                  <td>Password: </td>
                  <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
              </tr>

              <tr>
                  <td></td>
                  <td><input class="btn login_btn" type="submit" value="Login"></td>
              </tr>
          </table>
      </form>

      {% if messages %}
          <ul>
              {% for message in messages %}
                  <li>{{ message }}</li>
              {% endfor %}
          </ul>
      {% endif %}     
          
      Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

  </div>
  {% endblock content %}
  ```
  - Buka urls.py pada direktori main, import fungsi login_user dan tambahkan path url ke dalam variable urlpatterns seperti berikut:
  ```python
  from main.views import login_user
  urlpatterns =[
    path('login/', login_user, name='login'),]
  ```
  LOGOUT

  - Buka file views.py, tambahkan import logout dan buat fungsi login_user seperti berikut:
  ```python
  from django.contrib.auth import logout
  def logout_user(request):
      logout(request)
      return redirect('main:login')
  ```
  redirect berguna untuk mengembalikan pengguna ke halaman awal.

  - Buka file main.html dan isi dengan kode berikut untuk menambahkan button logout
  ```html
  <a href="{% url 'main:logout' %}">
      <button>
          Logout
      </button>
  </a>
  ```
  - Buka file urls.py pada direktori main, import fungsi logout_user dan tambahkan path url ke dalam variable urlpatterns seperti berikut:
  ```python
  from main.views import logou_user
  urlpatterns =[
    path('logout/', logout_user, name='logout'),]
  ```
  Merestriksi akses halaman main

  - Buka file views.py, tambahkan import login_required
  ```python
  from django.contrib.auth.decorators import login_required 
  ```
  - Tambahkan @login_required(login_url='/login') di atas fungsi show_main agar halaman main hanya bisa diakses pengguna yang telah diautentikasi.

2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
  - Jalankan proyek Django dengan perintah python3 manage.py runserver, pastikan jg virtual environment sudah menyala.
  - Buka http://localhost:8000/ di browser dan tekan tombol register now
  - Daftarkan diri untuk membuat akun
  - Setelah membuat akun, halaman web akan kembali ke awal dan lakukan login sesuai dengan username dan password yang didaftarkan.
  - Tekan tombol add product untuk menambahkan produk dan lakukan tiga kali untuk menambahkan tiga produk.
  - Tekan tombol logout untuk kembali ke halaman awal dan daftarkan lagi satu akun  dan tambah tiga produk lagi sesuai dengan langkah-langkah sebelumnya

3. Menghubungkan model Product dengan User.

  - Buka file models.py, import user dan tambahkan kode ini pada class product untuk menghubungkan product dengan user
  ```python
  from django.contrib.auth.models import User
  class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
  ```
  - Buka file views.py dan ubah fungsi create_product menjadi seperti ini:
  ```python
  def create_product(request):
      form = ProductForm(request.POST or None) 

      if form.is_valid() and request.method == "POST":
          product = form.save(commit=False)
          product.user = request.user
          product.save()
          return redirect('main:show_main')

      context = {'form': form}
      return render(request, "create_product.html", context)
  ```
  - Ubah fungsi show_main menjadi seperti berikut:
  ```python
  def show_main(request):
      products = Product.objects.filter(user=request.user)

      context = {
          'name': request.user.username,
      ...
      }
  ...
  ```
  - Simpan semua perubahan dengan melakukan migrasi

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

  Untuk menampilkan detail informasi pengguna dan data last login yang menerapkan cookies dapat menggunakan kode berikut pada file main.html
    ```html
    <p>Name: {{name}}</p> 
    <p>Class: {{class}}</p>
    <p>Sesi terakhir login: {{ last_login }}</p>
    ```
  Berikut step untuk mengimplementasikan cookiesnya:

  - Buka file views.py dan tambahkan beberapa import berikut:
  ```python
  import datetime
  from django.http import HttpResponseRedirect
  from django.urls import reverse
  ```
  - Mengganti fungsi login_user untuk menambahkan cookie yang akan digunakan untuk meilhat kapan pengguna terakhir login dengan mengganti kode pada blok if form.is_valid() menjadi:
  ```python
  if form.is_valid():
      user = form.get_user()
      login(request, user)
      response = HttpResponseRedirect(reverse("main:show_main"))
      response.set_cookie('last_login', str(datetime.datetime.now()))
      return response
  ```
  - Pada fungsi show_main tambahkan kode berikut ke dalam variable context
  ```python
  context = {
      'last_login': request.COOKIES['last_login'],
  }
  ```
  - Ubah fungsi logout_user menjadi seperti ini
  ```python
  def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
  ```
## TUGAS 5
## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector dari yang tertinggi hingga terendah:
1. Inline Styles yaitu gaya yang diterapkan langsung pada elemen HTML menggunakan atribut style, contohnya: <div style="color: red;">Hello</div>

2. ID Selector yaitu selector yang menggunakan ID elemen dengan tanda #, contohnya: #myElement {...}

3. Class, Attribute, dan Pseudo-class Selectors yaitu selector yang menggunakan kelas (dengan tanda .), atribut, atau pseudo-class, contohnya: .myClass {...}

4. Element (Type) Selectors yaitu selector yang menggunakan nama elemen HTML, contohnya: div {...}

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design sangat penting dalam pengembangan aplikasi web karena membantu menciptakan pengalaman pengguna yang nyaman di berbagai ukuran layar. Ini tidak hanya membuat konten lebih mudah diakses, tetapi juga berkontribusi pada peringkat SEO yang lebih baik. Dengan responsive design, pengembang bisa menghemat waktu dan biaya karena mereka tidak perlu membuat versi terpisah untuk setiap perangkat. 

Contoh aplikasi yang sudah menerapkan responsive design dengan baik adalah Twitter dan Amazon, yang menawarkan pengalaman yang memuaskan, baik di smartphone maupun desktop. Di sisi lain, beberapa situs berita dan aplikasi pemerintah masih belum responsif, sehingga pengguna kesulitan saat mengakses informasi di perangkat mobile. 
## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. Margin:

- Ruang di luar elemen, untuk memberi jarak antar elemen.

- Terletak di luar batas elemen.

- Tidak mempengaruhi ukuran elemen, hanya jarak di luar elemen.

- Implementasi:
```css
.element {
    margin: 10px;
}
```
2. Border:

- Garis yang mengelilingi elemen, sebagai batas visual.

- Terletak di antara margin dan padding, mengelilingi elemen.

- Mempengaruhi ukuran total elemen.

- Implementasi:
```css
.element{
  border: 2px solid black;
}
```
3. Padding:

- Ruang di dalam elemen, untuk mengatur jarak antara isi elemen dan batasnya.

- Terletak di dalam elemen, antara konten dan border.

- Tidak mempengaruhi ukuran elemen

- Implementasi:
```css
.element{
  padding: 15px;
}
```
## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
1. Flex box (Flexible Box Layout)

Flexbox adalah model tata letak satu dimensi yang dirancang untuk mengatur ruang di antara elemen dalam satu arah, baik secara horizontal maupun vertikal. Kegunaannya yaitu:

- Mengatur elemen dalam satu baris atau kolom.

- Memudahkan distribusi ruang di antara elemen dan penanganan alignment.

- Memungkinkan elemen untuk tumbuh atau menyusut sesuai dengan ruang yang tersedia.

2. Grid Layout

Grid Layout adalah model tata letak dua dimensi yang memungkinkan pengembang untuk mengatur elemen dalam baris dan kolom. Kegunaannya yaitu:

- Mengatur elemen dalam dua dimensi, memudahkan pembuatan layout yang lebih kompleks.

- Memungkinkan pengaturan ukuran kolom dan baris yang fleksibel.

- Membantu dalam menciptakan grid yang responsif dan teratur, cocok untuk desain web modern.
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Implementasikan fungsi untuk menghapus dan mengedit product.
FUNGSI EDIT
- Buka file base.html, tambahkan script cdn tailwind pada bagian head untuk menghubungkan template Django dengan tailwind, seperti berikut:
```html
<script src="https://cdn.tailwindcss.com">
</script>
```
- Buka views.py lalu buat fungsi baru bernama edit_product, seperti berikut:
```python
  def edit_product(request, id):
      product = Product.objects.get(pk = id)
      form = ProductForm(request.POST or None, instance=product)
      if form.is_valid() and request.method == "POST":
          form.save()
          return HttpResponseRedirect(reverse('main:show_main'))
      context = {'form': form}
      return render(request, "edit_product.html", context)
```
- Tambahkan juga import berikut
```python
from django.shortcuts import reverse
```
- Buat file baru bernama edit_product pada direktori main/templates dan isi dengan kode berikut:
```html
{% extends 'base.html' %}
{% load static %}
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nerko+One&display=swap');
</style>
{% block content %}
{% include 'navbar.html' %}
<div class="container mx-auto mt-10 p-6 bg-white rounded-lg shadow-lg">
    <h1 class="text-4xl font-extrabold mb-6 text-center text-[#52599D]" style="font-family: 'Nerko One', sans-serif;">Edit Product</h1>
    <form method="POST">
        {% csrf_token %}
        <div class="flex flex-col space-y-7">
            {{ form.as_p }}  
            <div class="flex justify-center">
                <input type="submit" value="Save Changes" class="bg-[#f49abb] text-white py-2 px-4 rounded-lg hover:bg-pink-500 transition duration-300"/>
            </div>
        </div>
    </form>
</div>
{% endblock %}
```
- Buka file urls.py pada direktori main, import fungsi edit_product dan tambahkan path url ke dalam variable urlpatterns seperti berikut:
  ```python
  from main.views import edit_product
  urlpatterns =[
    path('edit-product/<uuid:id>', edit_product, name='edit_product')]
  ```
- Buka file main.html lalu tambahkan kode berikut sejajar dengan elemen <td> untuk menampilkan tombol edit pada tiap baris tabel
```html
<td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
```
- Jalankan server lalu lihat hasilnya di http://localhost:8000 pada browser 

EDIT PRODUCT

- Buka file views.py dan buat fungsi baru bernama delete_product yang berisi kode berikut:
```python
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Buka file urls.py pada direktori main, import fungsi delete_product dan tambahkan path url ke dalam variable urlpatterns seperti berikut:
  ```python
  from main.views import delete_product
  urlpatterns =[
    path('delete/<uuid:id>', delete_product, name='delete_product')]
  ```
- Buka file main.html lalu tambahkan kode berikut dibawah kode button edit untuk menampilkan tombol delet pada tiap baris tabel
```html
<td>
        <a href="{% url 'main:delete_product' product.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
```
- Jalankan server lalu lihat hasilnya di http://localhost:8000 pada browser 

2. Kustomisasi halaman login, register, dan tambah product semenarik mungkin.

LOGIN

- Membuat suatu card di tengah web page dengan form yang telah dibuat sebelumnya

- Mengubah style input untuk isian username dan password

- Menambahkan massage jika login berhasil maupun gagal
```html
{% extends 'base.html' %}
{% block meta %}
<title>Login</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nerko+One&display=swap');
</style>
{% endblock meta %}
{% block content %}
<div class="min-h-screen flex items-center justify-center bg-[#9fbefc] py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full bg-[#fef9f8] rounded-xl shadow-lg p-8 space-y-6">
    <!-- Judul dan Deskripsi -->
    <div class="text-center">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-[#52599D]" style="font-family: 'Nerko One', sans-serif;">
        Welcome to Petty Paws🐾
      </h2>
      <p class="mt-2 text-sm text-gray-600">
        Log in to your account to continue
      </p>
    </div>
    <!-- Formulir Login -->
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div class="mb-4">
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required 
            class="appearance-none rounded-md relative block w-full px-4 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-[#f49abb] focus:z-10 sm:text-sm"
            placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required 
            class="appearance-none rounded-md relative block w-full px-4 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-[#f49abb] focus:z-10 sm:text-sm"
            placeholder="Password">
        </div>
      </div>
      <!-- Tombol Login -->
      <div>
        <button type="submit" 
          class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#f49abb] hover:bg-pink-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-200">
          Sign In
        </button>
      </div>
    </form>
    <!-- Pesan Error atau Sukses -->
    {% if messages %}
    <div class="mt-4 space-y-2">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}
    <!-- Link Registrasi -->
    <div class="text-center mt-4">
      <p class="text-sm text-gray-600">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-[#52599D] hover:text-indigo-500">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
REGISTER

- Membuat suatu card di tengah web page dengan form yang telah dibuat sebelumnya

- Mengubah style input untuk isian username, password, dan password confirmation

- Menambahkan massage jika register gagal
```html
{% extends 'base.html' %}
{% block meta %}
<title>Register</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nerko+One&display=swap');
</style>
{% endblock meta %}
{% block content %}
<div class="min-h-screen flex items-center justify-center bg-[#9fbefc] py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 bg-[#fef9f8] p-10 rounded-lg shadow-md">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-4xl font-extrabold text-[#52599D]" style="font-family: 'Nerko One', sans-serif;">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-[#9b5372]">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>
      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#f49abb] hover:bg-pink-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>
    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}
    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-[#52599D] hover:text-indigo-500">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```
ADD PRODUCT

- Membuat suatu card di tengah web page dengan form yang telah dibuat sebelumnya

- Mengubah style warna button dan juga warna text
```html
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Create Product</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nerko+One&display=swap');
</style>
{% endblock meta %}
{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-[#edf2fb]">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-5xl font-extrabold text-center mb-8 text-[#52599D]" style="font-family: 'Nerko One', sans-serif;">Create Product</h1>
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-[#9b5372]">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-[#f49abb] text-white text-lg font-bold px-8 py-4 rounded-lg hover:bg-[#f49abb] transition-transform transform hover:scale-105 duration-300 ease-in-out w-full shadow-md">
            Create Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```
3. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.

- Download image yang berformat png dan simpan dengan nama sedih-banget.png lalu masukkan ke direktori static/image.

- Menambahkan kode berikut pada main.html agar image tersebut muncul jika tidak ada produk yang disimpan
```html
{% if not products %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">Belum ada data product pada petty paws.</p>
    </div>
```
4. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card

CARD INFO untuk menampilkan informasi nama dan kelas
```html
<div class="bg-[#52599D] rounded-xl overflow-hidden border-2 border-[#52599D]">
    <div class="p-4 animate-shine">
      <h5 class="text-lg font-semibold text-white">{{ title }}</h5>
      <p class="text-white">{{ value }}</p>
    </div>
</div>
```
CARD PRODUCT untuk menampilkan daftar produk yang sudah tersimpan dan juga button edit dan delete pada tiap produknya
```html
<!-- Kontainer Utama -->
<div class="flex flex-wrap justify-center gap-5">
    <div class="relative w-100 max-w-full mx-auto flex flex-col">
        <!-- Gambar Produk -->
        <div class="relative bg-white shadow-lg rounded-lg overflow-hidden mb-6">
            <img src="{{ product.image }}" alt="{{ product.name }}" class="w-full h-50 object-cover">
            <!-- Nama Produk dan Brand -->
            <div class="p-4">
                <h3 class="font-bold text-xl text-[#9b5372] mb-2">{{ product.name }}</h3>
                <p class="text-sm text-gray-600 mb-4">Brand: {{ product.brands }}</p>
                <!-- Harga Produk -->
                <div class="text-lg font-semibold text-[#f49abb] mb-2">
                  Rp {{ product.price|floatformat:"0" }}
                </div>
                <!-- Kategori Produk -->
                <div class="text-sm text-gray-500 mb-4">
                  Category: {{ product.categories }}
                </div>
                <!-- Deskripsi Produk -->
                <p class="text-gray-700 leading-snug mb-4">{{ product.description|truncatewords:20 }}</p>
            </div>
            <!-- kotak button -->
            <div class="bg-[#f49abb] p-8 text-center">
            </div>
            <!-- Tombol Edit dan Delete -->
            <div class="absolute bottom-2 right-3 flex space-x-1">
                <a href="{% url 'main:edit_product' product.pk %}" class="bg-[#b6ccfe] hover:bg-[#9fbefc] text-white rounded-full p-2 transition duration-300 shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
                </a>
                <a href="{% url 'main:delete_product' product.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                </a>
            </div>
        </div>
    </div>
    <!-- Tambahkan produk berikutnya di dalam grid -->
</div>
```

5.  Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
```html
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nerko+One&display=swap');
</style>
<nav class="bg-[#bf7896] shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <!-- Brand -->
        <div class="flex items-center">
          <h1 class="text-3xl font-extrabold text-center text-[#fef9f8]" style="font-family: 'Nerko One', sans-serif;">Petty Paws🐾</h1>
        </div>
  
        <!-- Menu Items for Desktop -->
        <div class="hidden md:flex items-center space-x-8">
          <a href="#" class="text-[#fef9f8] hover:text-gray-300">Home</a>
          <a href="#" class="text-[#fef9f8] hover:text-gray-300">Products</a>
          <a href="#" class="text-[#fef9f8] hover:text-gray-300">Categories</a>
  
          {% if user.is_authenticated %}
            <span class="text-[#fef9f8] mr-4">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
        </div>
        <!-- Hamburger Icon for Mobile -->
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden px-4 w-full">
      <div class="pt-4 pb-4 space-y-4 text-center">
        <a href="#" class="block text-[#fef9f8] hover:text-gray-300">Home</a>
        <a href="#" class="block text-[#fef9f8] hover:text-gray-300">Products</a>
        <a href="#" class="block text-[#fef9f8] hover:text-gray-300">Categories</a>
        {% if user.is_authenticated %}
          <span class="block text-[#fef9f8]">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    <script>
      // Toggle mobile menu visibility
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```
Navbar diatas akan menghasilkan link navigasi untuk ke home, products, categories, dan tulisan Welcome,"username" serta tombol logout di kanan atas. Selain itu juga menampilkan nama toko saya yaitu Petty Paws di kiri atas. 

## TUGAS 6
## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- JavaScript dapat mendukung pembuatan elemen yang interaktif pada halaman web, contohnya seperti dropdown menus, animasi, dan lainnya sehingga memberikan pengalaman pengguna yang lebih dinamis.

- Dengan JavaScript, aplikasi web dapat merespons tindakan pengguna secara real-time. Contohnya, menggunakan AJAX untuk mengambil data dari server tanpa harus refresh halaman sehingga interaksi menjadi cepat dan efisien.

- JavaScript menyediakan banyak framework seperti React, Angular, dan Vue.js yang mempermudah pengembangan aplikasi web dengan menyediakan struktur dan alat untuk membangun aplikasi yang modular dan mudah dikelola.

- Aplikasi yang dibuat dengan JavaScript dapat diakses di berbagai perangkat dan sistem operasi karena JavaScript didukung oleh berbagai sistem operasi.

## 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi await saat digunakan bersama fetch() adalah untuk menunggu hasil dari operasi asinkron yang dijalankan oleh fetch(), sehingga kode tidak dilanjutkan sampai permintaan HTTP selesai. Karena fetch() mengembalikan Promise, await memastikan bahwa program menunggu hingga Promise tersebut terselesaikan, baik berhasil maupun gagal, sebelum melanjutkan ke kode berikutnya. 

Jika kita tidak menggunakan await, JavaScript akan melanjutkan eksekusi tanpa menunggu hasil dari fetch(), yang berarti variabel yang seharusnya berisi data dari respons HTTP hanya akan berisi Promise yang masih pending. Hal ini dapat menyebabkan program tidak berfungsi dengan benar karena mencoba mengakses data yang belum tersedia.
## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST karena Django secara default menerapkan CSRF protection pada semua permintaan POST untuk mencegah serangan CSRF. CSRF protection ini memverifikasi bahwa setiap permintaan POST berasal dari sumber yang valid dengan menggunakan token CSRF.

Namun, dalam beberapa kasus, seperti saat menggunakan AJAX POST requests, token CSRF mungkin tidak dikelola dengan baik. Hal itu menyebabkan permintaan POST dari AJAX ditolak oleh Django. Untuk menghindari hal ini, dapat menggunakan csrf_exempt untuk menonaktifkan validasi CSRF pada view tertentu sehingga permintaan AJAX POST dapat diproses tanpa harus memeriksa token CSRF.
## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
- Frontend dapat dengan mudah dimanipulasi oleh pengguna. Pembersihan di backend memastikan validasi yang konsisten dan aman.

- Meskipun frontend melakukan validasi, backend harus selalu memverifikasi ulang untuk keamanan maksimal.

- Pembersihan di backend memastikan semua data, termasuk yang mungkin tidak melalui frontend (misalnya, API calls) tetap bersih dan valid.

- Beberapa validasi mungkin memerlukan akses ke database atau logika kompleks yang lebih tepat dilakukan di backend.

- Backend memastikan data yang masuk valid dan aman, menghindari data kotor di sistem.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
AJAX GET

1. Ubahlah kode cards data product agar dapat mendukung AJAX GET.

- Buka file views.py, hapus kode bagian berikut pada fungsi show_main karena nantinya kita akna mendapatkan objek product dari endpoint /json
```python
products = Product.objects.filter(user=request.user)
'products': products,
```
- Masih di file views.py, ubah baris pertama dari fungsi show_json dan show_xml menjadi seperti ini
```python
data = Product.objects.filter(user=request.user)
```
- Buka file main.html dan hapus bagian block conditional untuk menampilkan card product ketika kosong atau tidak. Setelah itu tambahkan kode berikut di tempat yang sama
```html
<div id="product_cards"></div>
```
2. Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.

- Buka file main.html, tambahkan block <script> di bawah sebelum {% endblock content %} lalu buat fungsi baru bernama getProduct seperti berikut yang berfungsi untuk mengambil data melalui fetch() API ke data JSON secara asynchronous dan data akan diubah menjadi objek JavaScript. 
```javaScript
async function getProducts(){
    return fetch("{% url 'main:show_json' %}").then((res) => res.json())
}
```
AJAX POST

1. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.

- Buka file main.html, tambahkan kode berikut untuk mengatur tampilan form untuk menambahkan item melalui AJAX.
```JavaScript
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
          <!-- Modal header -->
          <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-[#52599D]" style="font-family: 'Nerko One', sans-serif";>
              Add New Product
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
              <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="px-6 py-4 space-y-6 form-style">
            <form id="productForm">
              <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input type="text" id="name" name="name" class="mt-1 block w-full border border-[#f49abb] rounded-md p-2 hover:border-[#f49abb]" placeholder="Enter name" required>
              </div>
              <div class="mb-4">
                <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
                <input type="url" id="image" name="image" class="mt-1 block w-full border border-[#f49abb] rounded-md p-2 hover:border-[#f49abb]" placeholder="Enter name" required>
              </div>
              <div class="mb-4">
                <label for="brands" class="block text-sm font-medium text-gray-700">Brands</label>
                <input type="text" id="brands" name="brands" class="mt-1 block w-full border border-[#f49abb] rounded-md p-2 hover:border-[#f49abb]" placeholder="Enter name" required>
              </div>
              <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                <input type="number" id="price" name="price" class="mt-1 block w-full border border-[#f49abb] rounded-md p-2 hover:border-[#f49abb]" required>
              </div>
              <div class="mb-4">
                <label for="categories" class="block text-sm font-medium text-gray-700">Categories</label>
                <input type="text" id="categories" name="categories" class="mt-1 block w-full border border-[#f49abb] rounded-md p-2 hover:border-[#f49abb]" placeholder="Enter name" required>
              </div>
              <div class="mb-4">
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-[#f49abb] rounded-md p-2 hover:border-[#f49abb]" placeholder="Describe your feelings" required></textarea>
              </div>
            </form>
          </div>
          <!-- Modal footer -->
          <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-[#d3b4d8] hover:bg-[#52599D] text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitProduct" form="productForm" class="bg-[#f49abb] hover:bg-pink-500 text-white font-bold py-2 px-4 rounded-lg">Save</button>
          </div>
        </div>
      </div>
```
- Tambahkan fungsi-fungsi JavaScript berikut agar modal dapat berfungsi pada tag ```<script>```
```JavaScript
const modal = document.getElementById('crudModal');
const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
```
- Tambahkan juga button baru bernama Add New Product by AJAX untuk melakukan penambahan produk dengan AJAX 

2. Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.

- Buka file views.py lalu tambahkan beberapa import berikut
```python
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
```
Pada file views.py, tambahkan fungsi berikut untuk menambahkan product by ajax
```python
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    image = strip_tags(request.POST.get("image"))
    brands = strip_tags(request.POST.get("brands"))
    price = request.POST.get("price")
    categories = strip_tags(request.POST.get("categories"))
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_product = Product(
        name=name, image=image,
        brands=brands, price=price,
        categories=categories, description=description,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
3. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

Buka file urls.py pada direktori main, import fungsi add_product_ajax dan tambahkan path url ke dalam variable urlpatterns seperti berikut:
  ```python
  from main.views import add_product_ajax
  urlpatterns =[
        path('create-product-ajax', add_product_ajax, name='add_product_ajax'),]
  ```
4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.

Buka file main.html lalu buat fungsi addProduct() di dalam ```<script>``` seperti kode berikut untuk menerapkan asynchronous dan event-handler pada button add product
```JavaScript
function addProduct() {
    fetch("{% url 'main:add_product_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productForm')),
    })
    .then(response => refreshProducts())

    document.getElementById("productForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }
```
5. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan.

Buka file main.html lalu buat fungsi addProduct() di dalam ```<script>``` seperti kode berikut yang akan me-refresh data item secara asynchronous.
```JavaScript
async function refreshProducts() {
    document.getElementById("product_cards").innerHTML = "";
    document.getElementById("product_cards").className = "";
    const products = await getProducts();
    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data product pada petty paws.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        products.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const image = DOMPurify.sanitize(item.fields.image);
            const brands = DOMPurify.sanitize(item.fields.brands);
            const price = DOMPurify.sanitize(item.fields.price);
            const categories = DOMPurify.sanitize(item.fields.categories);
            const description = DOMPurify.sanitize(item.fields.description);
            htmlString += `
            <!-- Kontainer Utama -->
            <div class="flex flex-wrap justify-center gap-5">
                <div class="relative w-100 max-w-full mx-auto flex flex-col">
                    <!-- Gambar Produk -->
                    <div class="relative bg-white shadow-lg rounded-lg overflow-hidden mb-6">
                        <img src="${image}" alt="${name}" class="w-full h-50 object-cover">
                    
                        <!-- Nama Produk dan Brand -->
                        <div class="p-4">
                            <h3 class="font-bold text-xl text-[#9b5372] mb-2">${name}</h3>
                            <p class="text-sm text-gray-600 mb-4">Brand: ${brands}</p>
                            
                            <!-- Harga Produk -->
                            <div class="text-lg font-semibold text-[#f49abb] mb-2">
                            Rp ${price.toLocaleString()}
                            </div>
                            
                            <!-- Kategori Produk -->
                            <div class="text-sm text-gray-500 mb-4">
                            Category: ${categories}
                            </div>
                            
                            <!-- Deskripsi Produk -->
                            <p class="text-gray-700 leading-snug mb-4">${description}</p>
                        </div>
                        
                        <!-- kotak button -->
                        <div class="bg-[#f49abb] p-8 text-center">
                        </div>
                    
                        <!-- Tombol Edit dan Delete -->
                        <div class="absolute bottom-2 right-3 flex space-x-1">
                            <a href="/edit-product/${item.pk}" class="bg-[#b6ccfe] hover:bg-[#9fbefc] text-white rounded-full p-2 transition duration-300 shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                                </svg>
                            </a>
                            <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
                <!-- Tambahkan produk berikutnya di dalam grid -->
            </div>

            `;
        });
    }
    document.getElementById("product_cards").className = classNameString;
    document.getElementById("product_cards").innerHTML = htmlString;
}
refreshProducts();
```
