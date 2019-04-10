from django.urls import path

from .views import DashboardView, NovoPedido, VendaCreateView

urlpatterns = [
    path('novo-pedido/', NovoPedido.as_view(), name="url_novo_pedido"),
    path('nova-venda/', VendaCreateView.as_view(), name="url_nova_venda"),
    path('dashboard/', DashboardView.as_view(), name="url_dashboard"),
]