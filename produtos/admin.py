from django.contrib import admin
from .models import Produto


# - - - PRODUTOS :: MODELADMIN

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco')


admin.site.register(Produto, ProdutoAdmin)
