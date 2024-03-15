from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


class Station:
    def __init__(self, name, street, district):
        self.Name = name
        self.Street = street
        self.District = district


def index(request):
    return redirect(reverse('bus_stations'))


BUS_STATION = []
with open(BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        BUS_STATION.append(Station(row['Name'], row['Street'], row['District']))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(BUS_STATION, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'stations/index.html', context)
