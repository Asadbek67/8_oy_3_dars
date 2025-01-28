from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwner


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permisson_classes=[IsOwner] 


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_class = [IsOwner]
    