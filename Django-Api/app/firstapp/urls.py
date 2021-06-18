from django.urls import path, re_path

from . import views

urlpatterns = [
    path('',views.vistaIndex, name='index'),
    path('cotizador', views.vistaCotizador, name='cotizador'),
    path('articulos', views.articulos, name='articulos'),
    path('articulos/add', views.articulosAdd, name='articulos/add'),
    path('articulos/update/<int:product_id>', views.articulosUpdate, name='articulos/update'),
    path('articulos/delete', views.articulosDelete, name='articulos/delete'),
    path('articulos/get', views.articulosGet, name='articulos/get'),
    path('articulos/get/<int:product_id>', views.articulosGetId, name='articulos/getid'),
    path('paciente', views.paciente, name='paciente'),
    path('paciente/add', views.pacienteAdd, name='paciente/add'),
    path('paciente/edit', views.pacienteEdit, name='paciente/edit'),
    path('paciente/delete', views.pacienteDelete, name='paciente/delete'),
    path('car/<int:car_model_id>', views.car, name='car'),
    path('car/<int:car_model_id>/delete', views.deleteCar, name='car'),
    re_path(r'^search/car_model/$', views.searchCarModel, name='search/car_model'),
    #path('add/car_model/<user_api_key>', views.addCarModel, name='add/car_model'),
    path('add/car_model', views.addCarModel, name='add/car_model'),
    path('car/<int:car_model_id>/update', views.updateCarModel, name='update/car_model'),
    #re_path(r'^add/car_model/$', views.addCarModel, name='add/car_model'),
    path('car/<int:car_model_id>/rate', views.rateCarModel, name='rate/car_model'),
    path('car/<int:car_model_id>/delete_rating', views.deleteRatingCarModel, name='deleteRating/car_model'),
    path('car/<int:car_model_id>/obtain_rating', views.obtainRatingCarModel, name='obtainRating/car_model'),





    #path('uno',views.vista,name='vista'),
    #path('dos',views.vista2,name='vista2'),
]
