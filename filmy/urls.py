from django.urls import path
from filmy.views import wszystkie, szczegoly, nowy, edycja, usun


urlpatterns = [
    path('wszystkie/',wszystkie),
    path('wszystkie/<int:film_id>/',szczegoly),
    path('nowy/', nowy),
    path('edycja/<int:film_id>/', edycja),
    path('usun/<int:film_id>/', usun)
]