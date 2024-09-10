from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Nisa Najla Hanina Hasanah',
        'kelas' : 'PBP A',
        'name' : 'BOLT Salmon Cat Food 20 Kg',
        'image': 'https://petshopindonesia.com/wp-content/uploads/2022/12/i100282-bolt-salmon-cat-food-20-kg-makanan-kucing-1-1.jpg',
        'brands': 'Bolt Cat',
        'price': '450.000',
        'categories': 'Kucing, Makanan, Camilan Kucing',
        'description': 'Makanan kucing usia di atas 1 tahun. Bermanfaat untuk membuat kulit sehat, bulu berkilau, dan mengurangi risiko FLUTD. '
    }

    return render(request, "main.html", context)