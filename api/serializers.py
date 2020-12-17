from rest_framework import serializers

from .models import(
    Person as PersonModel,
    Booking as BookingModel
)

class serializerBooking(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ('__all__')

class serializerPerson(serializers.ModelSerializer):
    bookings = serializerBooking(many=True, read_only=True)
    class Meta:
        model = PersonModel
        fields = ('__all__')
