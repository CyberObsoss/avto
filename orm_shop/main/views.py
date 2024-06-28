from django.http import Http404
from django.shortcuts import render

from main.models import Car


def cars_list_view(request):
    # context = Car.objects.all()
    cars = Car.objects.all()
    context = {'cars': cars}
    template_name = 'main/list.html'
    return render(request, template_name, context)


def car_details_view(request, car_id):
    try:
        context = {'car': Car.objects.get(id=car_id)}
        template_name = 'main/details.html'
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        car_ = Car.objects.get(id=car_id)
        try:
            context = {'sales': Sale.objects.filter(car=car_)}
            template_name = 'main/sales.html'
            return render(request, template_name, context)
        except Sale.DoesNotExist:
            raise Http404('Sales not found')
    except Car.DoesNotExist:
        raise Http404('Car not found')
