from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def get_info():
    info = []
    with open(settings.BUS_STATION_CSV, 'r', newline='') as file:
        obj = csv.DictReader(file, delimiter=',')
        for item in obj:
            info.append({"Name": item["Name"],
                         "Street": item["Street"],
                         "District": item["District"]})
        return info


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    info = get_info()
    paginator = Paginator(info, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
