from django.urls import path
from .views import hello_view,morning_view

urlpatterns = [
    path('', hello_view, name='home'),
    path('morning/', morning_view),
]
