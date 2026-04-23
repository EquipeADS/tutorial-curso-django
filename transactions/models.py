from django.db import models

class Transaction(models.Model):
    """Modelo que representa transação financeira"""
    name = models.CharField(max_length=255, verbose_name="Nome")
    value = models.FloatField(verbose_name="Valor")
    transaction_date = models.DateField(verbose_name="Data da transação")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de edição")

    def __str__(self):
        """Retorna: Str: O nome da transação"""
        return self.name
    
    class Meta:
        verbose_name = 'transação'
        verbose_name_plural = 'transações'
