from django.shortcuts import render
from rest_framework.decorators import api_view
from books.serializers import bookserializer,userserilizer
from rest_framework.response import Response
from books.models import Book
from rest_framework import status


# @api_view(['GET',"POST"])
#
# def booklist(request):
#     if(request.method=="GET"):
#         book=Book.objects.all()
#         b=bookserializer(book,many=True)
#         return Response(b.data)
#     elif(request.method=="POST"):
#         b=bookserializer(data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#     return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def bookdetail(request,pk):
#     try:
#         book=Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         b =bookserializer(book)
#         return Response(b.data)
#     elif(request.method=="PUT"):
#         b = bookserializer(book,data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import mixins,generics



#
# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)



# class booklist(generics.ListCreateAPIView):
#     queryset = Book.objects.all()                   #non-primary key based
#     serializer_class = bookserializer
#
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()                 #primary key based
#     serializer_class = bookserializer


from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
class bookviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()  # non-primary key based and primary key based  urls change und
    serializer_class = bookserializer

class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserilizer