from django.db import models

# Create your models here.


# - - - PRODUTO

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s - %d" % (self.descricao, self.preco)

