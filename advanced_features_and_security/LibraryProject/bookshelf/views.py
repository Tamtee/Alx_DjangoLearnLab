from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import ExampleForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Books.objects.all()
    form = ExampleForm()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = Exampl
