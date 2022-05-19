from django.shortcuts import render
from django.views.generic import ListView
from .services import getBanxico
import json
import numpy as np

# Create your views here.
class getData(ListView):
    '''
    This class is for to display the data from API Banxico.
    It have methods to display the data in a template named udisList.
    '''
    template_name = 'API/udisList.html'
    

    def get_queryset(self):
        '''
        With this function, 
        the parameters can be received through the GET method of the template,
        this is done in order to make the request to the 
        endpoint that brings the required data.
        '''
        serie = self.request.GET.get('serie', '')
        startDate = self.request.GET.get('startDate', '')
        endDate = self.request.GET.get('endDate', '')
        result = getBanxico(serie, startDate, endDate)
        try: 
            longitud = len(result['bmx']['series'][0]['datos'])
            dicc = result['bmx']['series'][0]['datos']
            listaValores = []
            for i in range(longitud):
                listaValores.append(float(dicc[i]['dato']))
            nMayor = np.amax(listaValores)
            nMin = np.amin(listaValores)
            mean = np.mean(listaValores)
            print('------>', result)
        except Exception as e:
            print('No hay datos')
        
        try:
            context = {
                'banxico' : result['bmx']['series'][0]['datos'],
                'Mayor' : nMayor,
                'Min' : nMin,
                'Promedio' : mean,
                'Titulo' : result['bmx']['series'][0]['titulo'],
            
            }
        except Exception as e:
            print('No hay datos')
            
        
        if serie and startDate and endDate:
            return context
        else:
            return ''