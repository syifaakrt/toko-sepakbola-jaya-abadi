from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406417922',
        'name': 'Syifa Anabella',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
