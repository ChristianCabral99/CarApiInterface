# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import redirect, render , HttpResponse
from django.http import JsonResponse
import json
import requests
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

apiKey = "cdb030999"

def ejemplo(request):
    return render(request,'table.html')

def vista(request):

    query = "batman"
    apiKey = "c809e516f37fa7407b060cc0dd57bce4"

    #API URL
    url = 'https://api.themoviedb.org/3/search/movie?query=' + query + '&api_key=' + apiKey;

    response = requests.get(url)
    result = response.json()
    cuantos = len(result['results']);

    #post_data = {'remote_api_file_field': self.file}
    #requests.post(REMOTE_API_URL, data=post_data)

    #url = 'https://www.googleapis.com/urlshortener/v1/url'
    #data = {'longUrl': 'http://www.google.com/'}
    #headers = {'Content-Type': 'application/json'}

    #response = requests.post(url, data=json.dumps(data), headers=headers)

    return render(request, 'clase.html', {'cuantos': cuantos , "movies": result })
    #return JsonResponse(result)

def prueba1(request):

    apiKey = "cdb030999"

    response = requests.get('http://host.docker.internal:8000/search/car_model?brand=subaru', headers={'api-key': apiKey})

    result = response.json()

    #cuantos = len(result['results']);
    #return render(request, 'clase.html', {'cuantos': cuantos , "movies": result })
    
    return JsonResponse(result)

def carApi(request):

    query = "subaru"
    apiKey = "cdb030999"

    #API URL
    url = 'http://localhost:8000/search/car_model?brand=' + query;

    #response = requests.get('http://host.docker.internal:8000/search/car_model?brand=subaru', headers={'api-key': apiKey})
    #response = requests.get('https://api.themoviedb.org/3/search/movie?query=batman&api_key=c809e516f37fa7407b060cc0dd57bce4')

    #response = requests.get('http://host.docker.internal:8080/prueba')


    try:
        #r = requests.get('http://host.docker.internal:8000/articulos',timeout=3)
        r = requests.get('http://host.docker.internal:8000/search/car_model?', headers={'api-key': apiKey})
        r.raise_for_status()
        result = r.json()
        cuantos = len(result['data'])
        #return JsonResponse(result)
        return render(request, 'table.html', {'cuantos': cuantos , "modelos": result })
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error ", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

    #try:
    #    response = requests.get('http://gateway.docker.internal:8000/articulos')
    #except requests.exceptions.HTTPError as err:
    #    raise SystemExit(err)


    #result = response.json()
    #cuantos = len(result['data']);

    #post_data = {'remote_api_file_field': self.file}
    #requests.post(REMOTE_API_URL, data=post_data)

    #url = 'https://www.googleapis.com/urlshortener/v1/url'
    #data = {'longUrl': 'http://www.google.com/'}
    #headers = {'Content-Type': 'application/json'}

    #response = requests.post(url, data=json.dumps(data), headers=headers)

    #return render(request, 'carapi.html', {'cuantos': cuantos , "modelos": result })

    #responseData = {}
    #responseData['success'] = 'true'
    #responseData['data'] = {}

    #return JsonResponse(result)

def carApiSearch(request, brandName):

    #query = "subaru"
    apiKey = "cdb030999"

    #API URL
    #url = 'http://localhost:8000/search/car_model?brand=' + query;

    #response = requests.get('http://host.docker.internal:8000/search/car_model?brand=subaru', headers={'api-key': apiKey})
    #response = requests.get('https://api.themoviedb.org/3/search/movie?query=batman&api_key=c809e516f37fa7407b060cc0dd57bce4')

    #response = requests.get('http://host.docker.internal:8080/prueba')


    try:
        #r = requests.get('http://host.docker.internal:8000/articulos',timeout=3)
        r = requests.get('http://host.docker.internal:8000/search/car_model?brand=' + brandName, headers={'api-key': apiKey})
        r.raise_for_status()
        result = r.json()
        cuantos = len(result['data'])
        #return JsonResponse(result)
        return render(request, 'table.html', {'cuantos': cuantos , "modelos": result })
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error ", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def rateCar(request):

    query = "subaru"
    apiKey = "cdb030999"

    #API URL
    #url = 'http://localhost:8000/search/car_model?brand=' + query;

    #response = requests.get('http://host.docker.internal:8000/search/car_model?brand=subaru', headers={'api-key': apiKey})
    #response = requests.get('https://api.themoviedb.org/3/search/movie?query=batman&api_key=c809e516f37fa7407b060cc0dd57bce4')

    #response = requests.get('http://host.docker.internal:8080/prueba')


    try:
        #r = requests.get('http://host.docker.internal:8000/articulos',timeout=3)
        r = requests.post('http://host.docker.internal:8000/car/10/rate', json = {'rating': '7'}, headers={'api-key': apiKey}, timeout=3)
        #r = requests.post('http://host.docker.internal:8000/car/10/rate')
        #r.raise_for_status()
        result = r.json()
        #cuantos = len(result['data'])
        return JsonResponse(result)
        #return render(request, 'carapi.html', {'cuantos': cuantos , "modelos": result })
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error ", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def deleteRating(request):

    query = "subaru"
    apiKey = "cdb030999"

    #API URL
    url = 'http://localhost:8000/search/car_model?brand=' + query;

    #response = requests.get('http://host.docker.internal:8000/search/car_model?brand=subaru', headers={'api-key': apiKey})
    #response = requests.get('https://api.themoviedb.org/3/search/movie?query=batman&api_key=c809e516f37fa7407b060cc0dd57bce4')

    #response = requests.get('http://host.docker.internal:8080/prueba')


    try:
        #r = requests.get('http://host.docker.internal:8000/articulos',timeout=3)
        r = requests.delete('http://host.docker.internal:8000/car/10/delete_rating', headers={'api-key': apiKey})
        r.raise_for_status()
        result = r.json()
        cuantos = len(result['data'])
        return JsonResponse(result)
        #return render(request, 'carapi.html', {'cuantos': cuantos , "modelos": result })
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error ", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def addCar(request):

    apiKey = "cdb030999"

    try:
        carToAdd = request.POST
        r = requests.put('http://host.docker.internal:8000/add/car_model', json = carToAdd, headers={'api-key': apiKey}, timeout=10)
        #r.raise_for_status()
        result = r.json()
        return redirect("/car-api")
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error 2", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def editCarModel(request, carid):

    apiKey = "cdb030999"

    try:
        newData = request.POST
        r = requests.post('http://host.docker.internal:8000/car/' + str(carid) + '/update', json = newData, headers={'api-key': apiKey}, timeout=10)
        r.raise_for_status()
        result = r.json()
        return redirect("/car-api")
        #return JsonResponse(newData)
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error 2", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def rateCar(request, carid):

    apiKey = "cdb030999"

    try:
        newData = request.POST
        r = requests.post('http://host.docker.internal:8000/car/' + str(carid) + '/rate', json = newData, headers={'api-key': apiKey}, timeout=10)
        r.raise_for_status()
        result = r.json()
        return redirect("/car-api")
        #return JsonResponse(newData)
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error 2", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def deleteRating(request, carid):

    apiKey = "cdb030999"

    try:
        newData = request.POST
        r = requests.delete('http://host.docker.internal:8000/car/' + str(carid) + '/delete_rating', headers={'api-key': apiKey}, timeout=10)
        r.raise_for_status()
        result = r.json()
        return redirect("/car-api")
        #return JsonResponse(newData)
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error 2", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def seeCar(request, carid):
    r = requests.get('http://host.docker.internal:8000/car/'+ str(carid))
    result = r.json()
    rat = requests.get('http://host.docker.internal:8000/car/' + str(carid) + '/obtain_rating', headers={'api-key': apiKey}, timeout=10)
    resultRat = rat.json()
    return render(request, 'model-table.html', {'ratings': resultRat , "modelos": result })

def editCar(request, carid):
    r = requests.get('http://host.docker.internal:8000/car/'+ str(carid))
    result = r.json()
    cuantos = len(result['data'])
    return render(request, 'edit-model.html', {'id_car_model': carid , "modelos": result })

def rateCarModel(request, carid):
    apiKey = "cdb030999"
    r = requests.get('http://host.docker.internal:8000/car/'+ str(carid))
    result = r.json()
    rat = requests.get('http://host.docker.internal:8000/car/' + str(carid) + '/obtain_rating', headers={'api-key': apiKey}, timeout=10)
    resultRat = rat.json()
    

    cuantos = len(result['data'])
    return render(request, 'rate-model.html', {'id_car_model': carid , "modelos": result, "ratings": resultRat })

def addCarModel(request):
    
    return render(request, 'add-model.html')

def deleteCar(request, carid):
    r = requests.get('http://host.docker.internal:8000/car/'+ str(carid) + '/delete')
    return redirect("/car-api")

def searchBrand(request):
    jsonData = request.POST
    strData = json.dumps(jsonData)
    data = json.loads(strData)
    #r = requests.get('http://host.docker.internal:8000/car/'+ str(carid))
    #result = r.json()
    #cuantos = len(result['data'])
    #return render(request, 'edit-model.html', {'id_car_model': carid , "modelos": result })
    #return HttpResponse(data['brand'])

    brandName = data['brand']

    try:
        #r = requests.get('http://host.docker.internal:8000/articulos',timeout=3)
        r = requests.get('http://host.docker.internal:8000/search/car_model?brand=' + brandName, headers={'api-key': apiKey})
        r.raise_for_status()
        result = r.json()
        cuantos = len(result['data'])
        #return JsonResponse(result)
        return render(request, 'search-table.html', {'cuantos': cuantos , "modelos": result, "marca": brandName })
    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        responseData = {}
        responseData['success'] = errh
        responseData['data'] = "hola"
        return HttpResponse(errh)
    except requests.exceptions.ConnectionError as errc:
        return HttpResponse("Error ", errc)
    except requests.exceptions.Timeout as errt:
        return HttpResponse("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        return HttpResponse("Oops: Something Else",err)

def add(request):  
    print(request.POST)
    #if request.method == "POST":  
    #    form = EmployeeForm(request.POST)  
    #    if form.is_valid():  
    #        try:  
    #            form.save()  
    #            return redirect('/show')  
    #        except:  
    #            pass  
    #else:  
    #    form = EmployeeForm()  
    #return render(request,'index.html',{'form':form})
    response = request
    return JsonResponse(request.POST)
    #return render(request, 'emp.html', {'res': response })

def modal1(request):
    
    return render(request, 'modal.html')



def dogs(request):

    if request.method == 'GET':

        apikey = request.headers.get('api_key')
        apikey = "33390d09esdioewu0qe0uqu0"
        if apikey is not None:

            if apikey != "33390d09esdioewu0qe0uqu0":
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'API KEY NOT VALID'
                return JsonResponse(responseData, status=400)

            responseData = {}
            responseData['success'] = 'true'
            responseData['key'] = apikey
            responseData['data'] = list(Dogs.objects.all().values())
            return JsonResponse(responseData, status=200)

        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'No api Key'
        return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newDog = Dogs(name=json_object['dog_name'], type_id=json_object['dog_type_id'], color=json_object['dog_color'], size= json_object['dog_size'])
            #INSERT INTO dogs (name, type_id,color,size) values ('Solovino',4,'black','big')
            newDog.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Dog inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            Dogs.objects.filter(id=json_object["dog_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The dog has been deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['name'] = one_entry.name
            responseData['data']['size'] = one_entry.size
            responseData['data']['color'] = one_entry.color
            responseData['data']['type_id'] = one_entry.type_id

            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsGetId(request, dogid):

    if request.method == 'GET':

        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['size'] = one_entry.size
        responseData['data']['color'] = one_entry.color
        responseData['data']['type_id'] = one_entry.type_id

        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsUpdate(request,dogid):

    if request.method == 'POST':
        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            #AQUI VA EL CODIGO DEL UPDATE
            try:
                value = json_object["dog_name"]
                Dogs.objects.filter(id=dogid).update(name=json_object["dog_name"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_size"]
                Dogs.objects.filter(id=dogid).update(size=json_object["dog_size"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_color"]
                Dogs.objects.filter(id=dogid).update(color=json_object["dog_color"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_type"]
                Dogs.objects.filter(id=dogid).update(type_id=json_object["dog_type"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['message'] = 'Datos actualizados'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def types(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Types.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)
