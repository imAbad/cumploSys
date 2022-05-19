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
        result = getBanxico(serie, startDate, endDate)
        longitud = len(result['bmx']['series'][0]['datos'])
        dicc = result['bmx']['series'][0]['datos']
        listaValores = []
        print('LONGLONG', longitud)
        for i in range(longitud):
            listaValores.append(float(dicc[i]['dato']))
        print('LISTAAA',listaValores)
        nMayor = np.amax(listaValores)
        nMin = np.amin(listaValores)
        mean = np.mean(listaValores)
        
        try:
            context = {
                'banxico' : result['bmx']['series'][0]['datos'],
                'Mayor' : nMayor,
                'Min' : nMin,
                'Promedio' : mean
            
            }
            print('Context---->', context)
        except Exception as e:
            context = {
                'banxico' : 'Hey!',
                
            }
            
            
        #result = context['banxico']['bmx']['series'][0]['datos']
        #sprint('__________>Res', result)
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
        # context = context.update(statistical)
       


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
            print('Simonnnnn')
            return context
        else:
            print('Nelson')
            return ''



            