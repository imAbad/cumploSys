from django.shortcuts import render
from django.views.generic import ListView
from .services import getBanxico


# Create your views here.
class getData(ListView):
    template_name = 'API/udisList.html'

    def get_queryset(self):
        serie = self.request.GET.get('serie', '')
        startDate = self.request.GET.get('startDate', '')
        endDate = self.request.GET.get('endDate', '')
        context = {
            'banxico' : getBanxico(serie, startDate, endDate),
        }
        print(context)
        if serie and startDate and endDate:
            return context.keys()
        else:
            return ''