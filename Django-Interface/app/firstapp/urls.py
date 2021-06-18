from django.urls import path

from . import views

urlpatterns = [
    #path('',views.vista,name='vista'),
    path('car-api',views.carApi,name='carApi'),
    path('car-api/search-brand/<brandName>',views.carApiSearch,name='carApiSearch'),
    path('car-api/search-brand',views.searchBrand,name='carApiSearchBrand'),
    path('rate',views.rateCar,name='rateCar'),
    path('add',views.addCar,name='addCar'),
    path('delete-rating',views.deleteRating,name='deleteRating'),
    #path('ejemplo',views.ejemplo,name='ejemplo'),
    path('car-model/<int:carid>',views.seeCar,name='carModel'),
    path('edit-car-model/<int:carid>',views.editCar,name='editCarModel'),
    path('rate-car-model/<int:carid>',views.rateCarModel,name='rateCarModel'),
    path('edit/<int:carid>',views.editCarModel,name='editCarModel'),
    path('rate/<int:carid>',views.rateCar,name='editCarModel'),
    path('add-car-model',views.addCarModel,name='addCarModel'),
    path('delete-car/<int:carid>',views.deleteCar,name='deleteCar'),
    path('delete-rating/<int:carid>',views.deleteRating,name='deleteRating'),
    
    #path('prueba',views.prueba1,name='prueba'),
    #path('modal1',views.modal1,name='modal1'),
    #path('add-car',views.add,name='add'),
    #path('dogs',views.dogs,name='dogs'),
    #path('dog/add',views.dogsAdd,name='dogsAdd'),
    #path('dog/delete',views.dogsDelete,name='dogsdelete'),
    #path('dog/get',views.dogsGet,name='dogsGet'),
    #path('dog/get/<int:dogid>',views.dogsGetId,name='dogsGetId'),
    #path('dog/update/<int:dogid>',views.dogsUpdate,name='dogsUpdate'),
    #path('types',views.types,name='types'),
]