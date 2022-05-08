from rest_framework import generics
from .serializers import CarDetailSerializer, CarsListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


#create an object
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


#check all objects
class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )

#change or delete an object
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )