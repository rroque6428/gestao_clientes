from django.contrib import admin
from django.http import Http404

from .models import Venda
from .models import ItemDoPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


# - - - ADMIN

# - - - VENDAS :: ACTIONS

def nfe_emitida(modeladmin, request, queryset):
    if not request.user.has_perm('vendas.setar_nfe'):
        raise Http404

    queryset.update(nfe_emitida=True)
nfe_emitida.short_description = "NFe Emitida"


def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)
nfe_nao_emitida.short_description = "NFe Não Emitida"


# - - - VENDAS :: MODELADMIN

class VendaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'pessoa', 'nfe_emitida')
    list_filter = ('pessoa__doc',)
    search_fields = ('id', 'pessoa__first_name', 'pessoa__last_name',
                     'pessoa__doc__num_doc')
    # raw_id_fields = ('pessoa',)  # Open a popup
    autocomplete_fields = ('pessoa',)
    readonly_fields = ('valor',)
    actions = [nfe_emitida, nfe_nao_emitida]  # exec batch funcs
    # filter_horizontal = ['produtos']  # 'produtos' must have a search_fields
    inlines = [ItemPedidoInline]


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)
