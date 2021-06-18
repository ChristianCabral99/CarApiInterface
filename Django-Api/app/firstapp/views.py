# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Articulos, Paciente, Car, RatingM, User

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def get_queryset(self):
    brand = self.request.query_params.get('brand')
    model= self.request.query_params.get('model')
    year = self.request.query_params.get('year')
    version = self.request.query_params.get('version')

    queryset = Car.objects.filter(location__distance_lte=(location, D(m=distance))).distance(location).order_by('distance')

    return queryset

def vista(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'clase.html', {'title': "Bumblebee" })

def searchCarModel(request):

    if request.method == 'GET':
        responseData = {}
        responseData['success'] = 'true'

        try:
            #apikey = request.headers.get('api-key')
            #requestedApiKey = request.GET['api_key']
            requestedApiKey = request.headers.get('api-key')
            user_entry = User.objects.get(api_key=requestedApiKey)
        except:
            
            if requestedApiKey is None:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'No Api Key'
                return JsonResponse(responseData, status=422)

            else:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Invalid Api Key'
                return JsonResponse(responseData, status=422)

        rBrand = False
        rModel = False
        rYear = False
        rVersion = False

        if 'brand' in request.GET:
            requestedBrand = request.GET['brand']
            rBrand = True

        if 'model' in request.GET:
            requestedModel = request.GET['model']
            rModel = True

        if 'year' in request.GET:
            requestedYear = request.GET['year']
            rYear = True

        if 'version' in request.GET:
            requestedVersion = request.GET['version']
            rVersion = True

        if rBrand:
            if rModel:
                if rYear:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, model=requestedModel, year = requestedYear, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, model=requestedModel, year = requestedYear).values())
                else:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, model=requestedModel, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, model=requestedModel).values())
            else:
                if rYear:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, year = requestedYear, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, year = requestedYear).values())
                else:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(brand=requestedBrand).values())
        else:
            if rModel:
                if rYear:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(model=requestedModel, year = requestedYear, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(model=requestedModel, year = requestedYear).values())
                else:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(model=requestedModel, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(model=requestedModel).values())
            else:
                if rYear:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(year = requestedYear, version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.filter(year = requestedYear).values())
                else:
                    if rVersion:
                        responseData['data'] = list(Car.objects.filter(version = requestedVersion).values())
                    else:
                        responseData['data'] = list(Car.objects.all().values())

        #if requestedModel is not None:
        #    responseData['data'] = list(Car.objects.filter(brand=requestedBrand).values())
        #else:
        #    responseData['data'] = list(Car.objects.filter(brand=requestedBrand, model=requestedModel).values())
        return JsonResponse(responseData, status=200)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=422)

def addCarModel(request):

    if request.method == 'PUT':
        try:
            #user_entry = User.objects.get(api_key=user_api_key)
            requestedApiKey = request.headers.get('api-key')
            user_entry = User.objects.get(api_key=requestedApiKey)
        except:
            if requestedApiKey is None:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'No Api Key'
                return JsonResponse(responseData, status=422)

            else:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Invalid Api Key'
                return JsonResponse(responseData, status=422)

        try:
            json_object = json.loads(request.body)
            b = Car(
            id=None, 
            brand=json_object['brand'], 
            model=json_object['model'],
            year=json_object['year'],
            version=json_object['version'],
            country_of_origin=json_object['country'],
            body_style=json_object['body'],
            engine_location=json_object['engine_location'],
            engine_cylinders=json_object['cylinders'],
            engine_hp=json_object['hp'],
            engine_nm=json_object['nm'],
            drive=json_object['drive'],
            transmission=json_object['transmission'],
            doors=json_object['doors'],
            weight=json_object['weight'],
            rating=json_object['rating'])
            b.save()
            inserted_car = Car.objects.order_by('id').last()
            responseData = {}
            responseData['id'] = inserted_car.id
            responseData['success'] = 'true'
            responseData['message'] = 'Data inserted'
            return JsonResponse(responseData, status=200)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Error: data was not inserted'
            return JsonResponse(responseData, status=422)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=422)

def updateCarModel(request, car_model_id):
    
    if request.method == 'POST':

        try:
            #user_entry = User.objects.get(api_key=user_api_key)
            requestedApiKey = request.headers.get('api-key')
            user_entry = User.objects.get(api_key=requestedApiKey)
        except:
            if requestedApiKey is None:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'No Api Key'
                return JsonResponse(responseData, status=422)

            else:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Invalid Api Key'
                return JsonResponse(responseData, status=422)

        try: 
            one_entry = Car.objects.get(id=car_model_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The Car ID its not valid'
            return JsonResponse(responseData, status=422)
        try:
            json_object = json.loads(request.body)
            contador = 0
            try:
                value = json_object["brand"]
                Car.objects.filter(id=car_model_id).update(brand=json_object["brand"])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["model"]
                Car.objects.filter(id=car_model_id).update(model=json_object['model'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["year"]
                Car.objects.filter(id=car_model_id).update(year=json_object['year'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["version"]
                Car.objects.filter(id=car_model_id).update(version=json_object['version'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["country"]
                Car.objects.filter(id=car_model_id).update(country_of_origin=json_object['country'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["body"]
                Car.objects.filter(id=car_model_id).update(body_style=json_object['body'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["engine_location"]
                Car.objects.filter(id=car_model_id).update(engine_location=json_object['engine_location'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["cylinders"]
                Car.objects.filter(id=car_model_id).update(engine_cylinders=json_object['cylinders'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["hp"]
                Car.objects.filter(id=car_model_id).update(engine_hp=json_object['hp'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["nm"]
                Car.objects.filter(id=car_model_id).update(engine_nm=json_object['nm'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["drive"]
                Car.objects.filter(id=car_model_id).update(drive=json_object['drive'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["transmission"]
                Car.objects.filter(id=car_model_id).update(transmission=json_object['transmission'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["doors"]
                Car.objects.filter(id=car_model_id).update(doors=json_object['doors'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["weight"]
                Car.objects.filter(id=car_model_id).update(weight=json_object['weight'])
                contador = contador +1
            except KeyError:
                responseData={}

            try:
                value = json_object["rating"]
                Car.objects.filter(id=car_model_id).update(rating=json_object['rating'])
                contador = contador +1
            except KeyError:
                responseData={}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['data'] = 'Nothing to update'
                return JsonResponse(responseData, status=422)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['data'] = 'Updated data'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong method'
        return JsonResponse(responseData, status=404)

def rateCarModel(request, car_model_id):

    if request.method == 'POST':

        try:
            #user_entry = User.objects.get(api_key=user_api_key)
            requestedApiKey = request.headers.get('api-key')
            user_entry = User.objects.get(api_key=requestedApiKey)
        except:
            if requestedApiKey is None:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'No Api Key'
                return JsonResponse(responseData, status=422)

            else:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Invalid Api Key'
                return JsonResponse(responseData, status=422)

        try:
            car_entry = Car.objects.get(id=car_model_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The Car ID its not valid'
            return JsonResponse(responseData, status=422)
        try:
            json_object = json.loads(request.body)

            try:
                RatingM.objects.filter(car=car_entry, user=user_entry).delete()
                b = RatingM(
                        car= car_entry,
                        rating=json_object['rating'],
                        user=user_entry
                )

                b.save()
                responseData = {}
                responseData['success'] = 'true'
                responseData['message'] = 'Rating inserted'
                return JsonResponse(responseData, status=200)
            except ValueError as e:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = json_object['rating']
                return JsonResponse(responseData, status=422)
        
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'Wrong method 2'
            return JsonResponse(responseData, status=404)
            
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong method'
        return JsonResponse(responseData, status=422)

def deleteRatingCarModel(request, car_model_id):

    if request.method == 'DELETE':
        try:
            #user_entry = User.objects.get(api_key=user_api_key)
            requestedApiKey = request.headers.get('api-key')
            user_entry = User.objects.get(api_key=requestedApiKey)
        except:
            if requestedApiKey is None:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'No Api Key'
                return JsonResponse(responseData, status=422)

            else:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Invalid Api Key'
                return JsonResponse(responseData, status=422)

        try:
            car_entry = Car.objects.get(id=car_model_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The Car ID its not valid'
            return JsonResponse(responseData, status=422)

        try:
            #json_object = json.loads(request.body)
            
            RatingM.objects.filter(car=car_entry, user=user_entry).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Deleted rating'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = "Rating was not deleted"
            return JsonResponse(responseData, status=422)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=422)

def obtainRatingCarModel(request, car_model_id):

    if request.method == 'GET':
        try:
            #user_entry = User.objects.get(api_key=user_api_key)
            requestedApiKey = request.headers.get('api-key')
            user_entry = User.objects.get(api_key=requestedApiKey)
        except:
            if requestedApiKey is None:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'No Api Key'
                return JsonResponse(responseData, status=422)

            else:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Invalid Api Key'
                return JsonResponse(responseData, status=422)

        try:
            car_entry = Car.objects.get(id=car_model_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The Car ID its not valid'
            return JsonResponse(responseData, status=422)

        try:
            #json_object = json.loads(request.body)
            
            #resp = RatingM.objects.filter(car=car_entry, user=user_entry).values()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = list(RatingM.objects.filter(car=car_entry, user=user_entry).values())
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = "Rating was not deleted"
            return JsonResponse(responseData, status=422)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=422)

def car(request, car_model_id):

    if request.method == 'GET':
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Car.objects.filter(id=car_model_id).values())
        return JsonResponse(responseData, status=200)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Error'
        return JsonResponse(responseData, status=422)

def deleteCar(request, car_model_id):

    if request.method == 'GET':
        Car.objects.filter(id=car_model_id).delete()
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = "Deleted car model"
        return JsonResponse(responseData, status=200)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Error'
        return JsonResponse(responseData, status=422)


def articulos(request):

    if request.method == 'GET':
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Articulos.objects.all().values())
        return JsonResponse(responseData, status=200)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=422)
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    #return render(request, 'dos.html', {'title': "Bumblebee" })  

def articulosAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            b = Articulos(id_articulo=json_object['id'], 
            nombre_articulo=json_object['name'], 
            precio=json_object['price'])
            b.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Data inserted'
            return JsonResponse(responseData, status=200)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Wrong Method'
            return JsonResponse(responseData, status=422)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=422)

def articulosUpdate(request, product_id):

    if request.method == 'POST':
        try:
            one_entry = Articulos.objects.get(id_articulo=product_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The product_id its not valid'
            return JsonResponse(responseData, status=422)
        try:
            json_object = json.loads(request.body)

            try:
                value = json_object["name"]
                Articulos.objects.filter(id=product_id).update(nombre_articulo=json_object["name"])
            except KeyError:
                responseData = {}
                responseData['success'] = 'false'
                return JsonResponse(responseData, status=422)

            try:
                value = json_object["price"]
                Articulos.objects.filter(id=product_id).update(precio=json_object["price"])
            except KeyError:
                responseData = {}
                responseData['success'] = 'false'
                return JsonResponse(responseData, status=422)
        
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'Product not found'
            return JsonResponse(responseData, status=422)
            
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong method'
        return JsonResponse(responseData, status=422)

def articulosDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Articulos.objects.get(id_articulo=json_object['id'])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'ID not valid'
                return JsonResponse(responseData, status=400)
            Articulos.objects.filter(id_articulo=json_object['id']).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def articulosGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Articulos.objects.get(id_articulo=json_object['id'])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'ID not valid'
                return JsonResponse(responseData, status=400)

            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['nombre_articulo'] = one_entry.nombre_articulo
            responseData['data']['precio'] = one_entry.precio
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Methodo'
        return JsonResponse(responseData, status=400)

def articulosGetId(request, product_id):

    if request.method == 'GET':
        try: 
            one_entry = Articulos.objects.get(id_articulo=product_id)
        except:
            responseData ={}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)
           
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['nombre_articulo'] = one_entry.nombre_articulo
        responseData['data']['precio'] = one_entry.precio
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong method'
        return JsonResponse(responseData, status=400)



def paciente(request):
    if request.method == 'GET':

        apikey = request.headers.get('api-key')

        if apikey is not None:

            if apikey != "12345":
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'API Key not valid'
                return JsonResponse(responseData, status=404)

            responseData = {}
            responseData['success'] = 'true'
            responseData['key'] = apikey
            responseData['data'] = list(Paciente.objects.all().values())
            return JsonResponse(responseData, status=200)

        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'No API Key'
        return JsonResponse(responseData, status=404)

    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=404)

def pacienteAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Valid Json'
            return JsonResponse(responseData, status=200)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Wrong Method'
            return JsonResponse(responseData, status=404)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=404)

def pacienteEdit(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Valid Json'
            return JsonResponse(responseData, status=200)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Wrong Method'
            return JsonResponse(responseData, status=404)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=404)

def pacienteDelete(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Valid Json'
            return JsonResponse(responseData, status=200)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Wrong Method'
            return JsonResponse(responseData, status=404)
    else:
        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'Wrong Method'
        return JsonResponse(responseData, status=404)


def vistaIndex(request):
    return render(request, 'index.html')

def vistaCotizador(request):
    return render(request, 'cotizador.html')