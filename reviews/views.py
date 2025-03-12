from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Проверка длины заголовка
            if len(form.cleaned_data['title']) < 5:
                form.add_error('title', 'Заголовок должен содержать не менее 5 символов.')
            else:
                form.save()
                return redirect('add_book')  # Перенаправление после успешного сохранения
    else:
        form = BookForm()
    return render(request, 'reviews/add_book.html', {'form': form})

# Create your views here.
