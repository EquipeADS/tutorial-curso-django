from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    orcamento_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='receitas')
    tipo = models.CharField(max_length=100)
    origem = models.CharField(max_length=150)
    data_entrada = models.DateField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - {self.origem}"


class Despesa(models.Model):
    STATUS_CHOICES = [
        ('orcada', 'Orçada'),
        ('realizada', 'Realizada'),
    ]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='despesas')
    categoria = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='orcada')

    def __str__(self):
        return f"{self.descricao} - {self.valor}"
