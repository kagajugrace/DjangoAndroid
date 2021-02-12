from django.shortcuts import render
from django. http import HttpResponse
from .models import*
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def welcome(request):
    return HttpResponse('get home')


# def posts(request):
#     if request.method =='GET':
#         getdata = Posts.object.all().orderby('-id')[:15]
#         serializer =PostSerializers(getdata, many=True)
#         return JsonResponse({'message': 'success', 'data':serializers.data}, safe=False)
#     elif request.method=='POST':
#         data =JSONParser().parser(request)
#         serializer=PostSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'success', 'data':serializers.data})

# Create your views here.

@csrf_exempt
def pharmacy (request):
    if request.method=='GET':
        reg=Pharmacy.objects.all()
        serializer=PharmacySerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=PharmacySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def medicine (request):
    if request.method=='GET':
        reg=Medicine.objects.all()
        serializer=MedicineSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=MedicineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def kipharma (request):
    if request.method=='GET':
        reg=Kipharma.objects.all()
        serializer=KipharmaSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=KipharmaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

def posts(request):
    if request.method =='GET':
        getdata = Postnews.objects.all().order_by('-id')[:40]
        serializer =PostSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})