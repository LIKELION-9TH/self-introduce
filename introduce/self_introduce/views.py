from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request, 'main.html')

def hobby(request):
    return render(request, 'hobby.html')

def place(request):
    return render(request, 'place.html')

def music(request):
    return render(request, 'music.html')

def picture(request):
    return render(request, 'picture.html')

def diary(request):
    return render(request, 'diary.html')