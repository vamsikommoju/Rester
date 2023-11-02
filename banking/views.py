from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Account
from .serializers import AccountSerializer
from rest_framework import status

# Create your views here.


# def json_resp(request):
#     account = {'id':1, 'name':'Vamsi', 'type':'savings', 'currency':'INR', 'balance':5000}
#     return JsonResponse({'account':[account]})

@api_view(['GET','POST'])
def AccountList(request):
        if request.method == "GET":
            account = Account.objects.all()
            serializer = AccountSerializer(account, many=True)
            return JsonResponse({'account':serializer.data}, safe=False)

        if request.method == "POST":
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
@api_view((['GET','PUT','DELETE']))
def AccountDetail(request, id):
        try:
            account = Account.objects.get(pk=id)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AccountSerializer(account,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE':
             account.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)


