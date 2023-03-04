
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.show, name='show'),
    path('/<int:slug>',views.specific_book, name='specific_book'),
]
