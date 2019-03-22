from django.db import models
from django.db.models import Avg, Max, Min, Count, Sum


class VendaManager(models.Manager):

    def total_vendas(self):
        return self.aggregate(value=Sum('valor'))['value']

    def venda_minima(self):
        return self.aggregate(value=Min('valor'))['value']

    def venda_maxima(self):
        return self.aggregate(value=Max('valor'))['value']

    def media_descontos(self):
        return self.aggregate(value=Avg('desconto'))['value']

    def media(self):
        return self.aggregate(value=Avg('valor'))['value']

    def qtd_vendas(self):
        return self.aggregate(value=Count('id'))['value']

    def num_ped_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(value=Count('id'))['value']
