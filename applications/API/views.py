from django.shortcuts import render
from django.views.generic import ListView
from .services import getBanxico
import json
import numpy as np

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
        # result = context['banxico']['bmx']['series'][0]['datos']
        # longitud = len(result)
        # listaValores = []
        # for i in range(longitud):
        #      listaValores.append(float(result[i]['dato']))
        # print('_________>>>>>>>>>>Lista', listaValores)
        # nMayor = np.amax(listaValores)
        # nMin = np.amin(listaValores)
        # mean = np.mean(listaValores)
        # print('MinMAxMean_________>>>>>>>>',nMayor,nMin,mean)
        # statistical = {
        #      'Mayor' : nMayor,
        #      'Menor' : nMin,
        #      'Promedio' : mean 
        # }
        # context.update('Datos',statistical)


        # print('=========================', context['Mayor']['Menor']['Promedio'])

        # result = context['banxico']['bmx']['series'][0]['datos']
        # print(result)
        # longitud = len(result)
        # listaValores = []
        # for i in range(longitud):
        #     listaValores.append(float(result[i]['dato']))
        # nMayor = np.amax(listaValores)
        # nMin = np.amin(listaValores)
        # mean = np.mean(listaValores)
        
        # statistical = {
        #     'Mayor' : nMayor,
        #     'Menor' : nMin,
        #     'Promedio' : mean 
        # }
        # result = result.update(statistical)

        #print('Resultado_____>',result)
        
        if serie and startDate and endDate:
            return context['banxico']['bmx']['series'][0]['datos']
        else:
            return ''


            