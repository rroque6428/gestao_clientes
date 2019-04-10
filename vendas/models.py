from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from django.db.models import F, Sum, FloatField

from clientes.models import Person
from produtos.models import Produto

from .managers import VendaManager


# - - - MODEL

# - - - VENDA

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    objects = VendaManager()

    # Necessita rodar 'makemigrations'
    class Meta:
        permissions = (
            ('setar_nfe', 'Usuário pode alterar param NFe'),
            ('ver_dashboard', 'Ver o Dasjboard'),
        )

    def __str__(self):
        return self.numero

    def calcular_total(self):
        tot = self.itemdopedido_set.aggregate(
            tot=Sum(F('quantidade')*F('produto__preco')-F('desconto'),
                    output_field=FloatField()))['tot'] or 0
        tot -= float(self.desconto + self.impostos)
        self.valor = tot
        Venda.objects.filter(pk=self.id).update(valor=tot)


# - - - ITENSDOPEDIDO

class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s - %s" % (self.venda.numero, self.produto.descricao)

    class Meta:
        verbose_name_plural = 'Itens do Pedido'


# - - - SIGNALS

# Atualiza o campo 'valor' automaticamente
@receiver(post_save, sender=ItemDoPedido)
def update_vendas_total(sender, instance, **kwargs):
    instance.venda.calcular_total()


@receiver(post_save, sender=Venda)
def update_vendas_total(sender, instance, **kwargs):
    instance.calcular_total()
