from django.urls import path
from .views import esempio_if, esempio_ifelse, esempio_elif, esempio_for
app_name = 'app2'
urlpatterns = [
    path('if/', esempio_if, name='if'),
    path('ifelse/', esempio_ifelse, name='else'),
    path('ifelif/', esempio_elif, name='elif'),
    path('for/', esempio_for, name='for'),
]