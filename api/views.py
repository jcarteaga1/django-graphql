from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import serializerBooking, serializerPerson
from .models import(
    Person as PersonModel,
    Booking as BookingModel
)

class PersonList(ListAPIView, CreateAPIView):
    queryset = PersonModel.objects.all()
    serializer_class = serializerPerson

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PersonDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = PersonModel.objects.all()
    serializer_class = serializerPerson

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class BookingList(ListAPIView, CreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = serializerBooking

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookingDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = serializerBooking

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
