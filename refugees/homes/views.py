from django.views.generic.edit import CreateView
from .models import Home


class HomeCreate(CreateView):
    model = Home
    success = "/thx.html"
    fields = (
        'name', 'dispo_from', 'dispo_to',
        'places', 'address', 'phone', 'email')
