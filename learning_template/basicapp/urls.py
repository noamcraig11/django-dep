from django.urls import path, include
from . import views

# SET THE NAMESPACE!
app_name = 'basicapp'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
