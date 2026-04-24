from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def home(request):
    produtos = Produto.objects.all()

    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')  # evita duplicar envio

    return render(request, 'home.html', {
        'produtos': produtos,
        'form': form
    })