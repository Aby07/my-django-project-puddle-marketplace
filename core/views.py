from django.shortcuts import render, redirect

from items.models import Category, Items

from . forms import SignUpForm

def index(request):
    items = Items.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
       'categories' : categories,
        'items' : items,
    })

def contacts(request):
    return render(request, 'core/contacts.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })