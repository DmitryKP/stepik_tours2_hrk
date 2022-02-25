from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View
import random
from tours.data import tours


class main_view(View):
    def get(self, request):
        return render(request, 'index.html', context={'tours': dict(random.sample(tours.items(), 6))})


class departure_view(View):
    def get(self, request, departure):
        return render(request, 'departure.html', context={'tours': {k: v for k, v in tours.items() if v['departure'] == departure},
                                                          'num_tours': len([v for k, v in tours.items() if v['departure'] == departure]),
                                                          'min_price': min([v['price'] for k, v in tours.items() if v['departure'] == departure]),
                                                          'max_price': max([v['price'] for k, v in tours.items() if v['departure'] == departure]),
                                                          'min_nights': min([v['nights'] for k, v in tours.items() if v['departure'] == departure]),
                                                          'max_nights': max([v['nights'] for k, v in tours.items() if v['departure'] == departure]),
                                                          'dep_name': [v['departure_name'] for k, v in tours.items() if v['departure'] == departure][0],
                                                          })


class tour_view(View):
    def get(self, request, id):
        return render(request, 'tour.html', context=tours[id])


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
