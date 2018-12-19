from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages

from .forms import BookForm
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def show(request, pk):
    #try:
    #    book = Book.objects.get(pk=pk)
    #except Exception:
    #    raise Http404

    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/show.html', {'book': book})

def add(request):

    #if request.method == 'POST':
        # print(request.POST)

        #name = request.POST.get('name')
        #price = request.POST.get('price')
        #introduction = request.POST.get('introduction')

        #if not name:
        #    return render(request, 'books/add.html', {'message': 'name can not be bull'})

        #if not price.isdigit():
        #    pass

        #price = int(price)

        #if price <= 0:
        #    pass

        #if not introduction:
        #    pass

        #Book.objects.create(
        #    name=name,
        #    price=price,
        #    introduction=introduction,
        #)
    # form = None
    # if request.method == 'POST':
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         Book.objects.create(**form.cleaned_data)
    #         #return render(request, 'books/add.html', {'message': 'create success'})
    #         #print(form.errors.get_json_data())
    #     #return render(request, 'books/add.html', {'message': form.errors.get_json_data()})
    # else:
    #     form = BookForm()
    # return render(request, 'books/add.html', {'form': form})

    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('books-index') #重新導向回XX頁

    return render(request, 'books/add.html', {'form': form})
