from django.shortcuts import render
from .models import Books
from django.urls import reverse
from .forms import Library


def Main_window(request):
    return render(request, 'librar/main.html')


def Show_book(request):
    All_books = Books.objects.all()
    url = reverse(viewname="home")
    return render(request, 'librar/all_book.html', context={"books": All_books,
                                                            "url": url})


def Info_book(request, id_book: int):
    info_book = Books.objects.get(id=id_book)
    return render(request, 'librar/info_book.html', context={'info': info_book})


def Add_book(request):
    if request.GET.get('name') or request.GET.get('Author'):
        form = Library(request.GET)
        if form.is_valid():
            Books(name=form.cleaned_data['name'], Author=form.cleaned_data['Author']).save()
            form = Library()
    else:
        form = Library()
    return render(request, 'librar/add_book.html', context={'form': form})
