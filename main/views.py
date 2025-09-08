from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495653',
        'name': 'Muhammad Farrel Rajendra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)