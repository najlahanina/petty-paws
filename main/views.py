from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Nisa Najla Hanina Hasanah',
        'kelas' : 'PBP A'
    }

    return render(request, "main.html", context)