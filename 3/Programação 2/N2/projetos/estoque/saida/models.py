from django.db import models
from produto.models import Produtos


# Create your models here.
class Saidas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT,verbose_name='Produto')
    preco = models.DecimalField('Preço', decimal_places=2,max_digits=8, default=0)
    quantidade = models.IntegerField('Quantidade', default=0)