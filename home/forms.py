from django import forms
from .models import Receita, Despesa
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio', 'data_termino', 'orcamento_total']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['tipo', 'origem', 'data_entrada', 'valor']


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['categoria', 'tipo', 'descricao', 'valor', 'data', 'status']