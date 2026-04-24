from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import Projeto, Receita, Despesa
from .forms import ReceitaForm, DespesaForm

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista_projetos.html', {'projetos': projetos})

def projeto_detalhe(request, projeto_id):
    from django.db.models import Sum
    projeto = get_object_or_404(Projeto, id=projeto_id)

    receitas = projeto.receitas.all().order_by('-data_entrada')
    despesas_orcadas = projeto.despesas.filter(status='orcada').order_by('-data')
    despesas_realizadas = projeto.despesas.filter(status='realizada').order_by('-data')

    total_receitas = receitas.aggregate(total=Sum('valor'))['total'] or 0
    total_despesas_orcadas = despesas_orcadas.aggregate(total=Sum('valor'))['total'] or 0
    total_despesas_realizadas = despesas_realizadas.aggregate(total=Sum('valor'))['total'] or 0

    saldo_disponivel = projeto.orcamento_total + total_receitas - total_despesas_realizadas

    receita_form = ReceitaForm()
    despesa_form = DespesaForm()

    if request.method == 'POST':
        if 'salvar_receita' in request.POST:
            receita_form = ReceitaForm(request.POST)
            if receita_form.is_valid():
                receita = receita_form.save(commit=False)
                receita.projeto = projeto
                receita.save()
                return redirect('projeto_detalhe', projeto_id=projeto.id)

        if 'salvar_despesa' in request.POST:
            despesa_form = DespesaForm(request.POST)
            if despesa_form.is_valid():
                despesa = despesa_form.save(commit=False)
                despesa.projeto = projeto
                despesa.save()
                return redirect('projeto_detalhe', projeto_id=projeto.id)

    # AGRUPAR DESPESAS POR CATEGORIA
    despesas_categoria = (
    despesas_realizadas
    .values('categoria')
    .annotate(total=Sum('valor'))
)

    categorias = [item['categoria'] for item in despesas_categoria]
    valores = [float(item['total']) for item in despesas_categoria]

    
    return render(request, 'projeto_detalhe.html', {
        'projeto': projeto,
        'receitas': receitas,
        'despesas_orcadas': despesas_orcadas,
        'despesas_realizadas': despesas_realizadas,
        'total_receitas': total_receitas,
        'total_despesas_orcadas': total_despesas_orcadas,
        'total_despesas_realizadas': total_despesas_realizadas,
        'saldo_disponivel': saldo_disponivel,
        'receita_form': receita_form,
        'despesa_form': despesa_form,
        'categorias': categorias,
        'valores': valores,
    })