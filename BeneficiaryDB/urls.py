from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('client/add', views.add_client, name="add-client"),
    path('client/update/<int:id>', views.update, name="update-client"),
]