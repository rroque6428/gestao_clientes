from django.contrib import admin
from .models import Person, Documento


# - - - PERSON :: MODELADMIN

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


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)

admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Bem vindo ao Gestão de Clientes'
