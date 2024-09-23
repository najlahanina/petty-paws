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
  - Tekan tombol logout untuk kembali ke halaman awal dan daftarkan lagi satu akun sesuai dengan langkah sebelumnya

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
          mood_entry = form.save(commit=False)
          mood_entry.user = request.user
          mood_entry.save()
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