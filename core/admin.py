from django.contrib import admin
from .models import Cadastro, Cobertura

class CoberturaInline(admin.TabularInline):
    model = Cobertura
    fields = ('peso', 'altura', )
    extra = 0


@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_filter = ('nome','tipo', 'modelo')
    list_display = ('nome', 'tipo', 'modelo')
    fields = ('nome', 'tipo', 'modelo')
    inlines = [CoberturaInline]

