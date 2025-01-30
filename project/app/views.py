from rest_framework import serializers
from .models import Book
from .permissions import IsOwner, BasePermission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' 

class BookListCreateView(APIView):
    permission_classes = [IsOwnerPermission] 

    def get(self, request):
        books = Book.object.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    permission_classes = [IsOwnerPermission]  

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,  pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

































# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer
# from .permissions import IsOwner


# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permisson_classes=[IsOwner] 


# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):  
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permissions_class = [IsOwner]
    