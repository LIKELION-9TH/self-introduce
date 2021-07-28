from django.shortcuts import render, get_object_or_404, redirect
from .models import Diary
from django.utils import timezone

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
    diarys = Diary.objects.all
    return render(request, 'diary.html', {'diarys' : diarys})

def detail(request, id):
    diary = get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary' : diary})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diary()
    new_diary.title = request.POST['title']
    new_diary.pub_date = timezone.now()
    new_diary.body = request.POST['body']
    new_diary.save()
    return redirect('detail', new_diary.id)