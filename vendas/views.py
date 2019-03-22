from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Venda


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Permissão Negada!')

        # return super(DashboardView, self).dispatch(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        dct_ = {}
        objs = Venda.objects

        dct_['media'] = objs.media()
        dct_['media_desconto'] = objs.media_descontos()
        dct_['venda_min'] = objs.venda_minima()
        dct_['venda_max'] = objs.venda_maxima()
        dct_['qtd_vendas'] = objs.qtd_vendas()
        dct_['total_vendas'] = objs.total_vendas()
        dct_['media'] = objs.media()
        dct_['num_ped_nfe'] = objs.num_ped_nfe()

        return render(request, 'vendas/dashboard.html', dct_)
