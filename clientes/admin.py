from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    # Agrupando fields
    # fields = (('first_name', 'last_name'), 'age', 'salary', 'doc', 'bio',
    #           'photo')
    # Usando o recurso de fieldsets para agrupamento
    fieldsets = (
        ('Dados Pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Complemento', {
            # 'classes': ('collapse',),
            'fields': ('age', 'salary', 'bio', 'photo')}
         )
    )
    # Listando mais campos na lista
    list_display = ('nome_completo', 'age', 'salary', 'doc', 'has_photo')
    # Criando Filtros para pesquisa
    list_filter = ('age', 'salary')
    search_fields = ('id', 'first_name', 'last_name')

    def has_photo(self, obj):
        if obj.photo:
            return "Sim"
        return "Não"
    has_photo.short_description = "Has Picture"

    def nome_completo(self, obj):
        return "%s, %s" % (obj.last_name, obj.first_name)


# Admin Actions for Vendas
def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)
nfe_emitida.short_description = "NFe Emitida"


def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)
nfe_nao_emitida.short_description = "NFe Não Emitida"


class VendaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'pessoa', 'total_vendas', 'nfe_emitida')
    list_filter = ('pessoa__doc',)
    search_fields = ('id', 'pessoa__first_name', 'pessoa__last_name',
                     'pessoa__doc__num_doc')
    # raw_id_fields = ('pessoa',)  # Open a popup
    autocomplete_fields = ('pessoa',)
    readonly_fields = ('valor',)
    actions = [nfe_emitida, nfe_nao_emitida]  # exec batch funcs
    filter_horizontal = ['produtos']  # 'produtos' must have a search_fields


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)

admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Bem vindo ao Gestão de Clientes'
