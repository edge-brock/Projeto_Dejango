from django.contrib import admin

from app.models import Produto, Categoria, FormaDePagamento, Venda

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'categoria', 'custo', 'valor')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class FormaDePagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'taxa')

class VendaAdmin(admin.ModelAdmin):
    list_display = ('horario', 'total', 'formaDePagamento')

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(FormaDePagamento, FormaDePagamentoAdmin)
admin.site.register(Venda, VendaAdmin)
