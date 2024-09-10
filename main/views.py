from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Nisa Najla Hanina Hasanah',
        'npm' : '2306240055',
        'kelas' : 'PBP A'
    }

    return render(request, "main.html", context)