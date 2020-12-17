import graphene
from graphene_django import DjangoObjectType
from graphene import ObjectType
import api.models as app_models

class PersonType(DjangoObjectType):
    class Meta:
        model = app_models.Person

class BookingType(DjangoObjectType):
    class Meta:
        model = app_models.Booking

class Query(graphene.AbstractType):
    all_people = graphene.List(PersonType)
    all_bookings = graphene.List(BookingType)

    def resolve_all_people(self, *args, **kwargs):
        return app_models.Person.objects.all()

    def resolve_all_bookings(self, *args, **kwargs):
        return app_models.Booking.objects.all()
