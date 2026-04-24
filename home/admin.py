from django.contrib import admin
from .models import Projeto, Receita, Despesa

admin.site.register(Projeto)
admin.site.register(Receita)
admin.site.register(Despesa)