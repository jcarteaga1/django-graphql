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

class CreatePerson(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        person = app_models.Person(name=name)
        person.save()
        return CreatePerson(
            name=person.name
        )

class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
