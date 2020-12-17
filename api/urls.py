from django.contrib import admin
from django.urls import path

from .views import PersonList, PersonDetail, BookingList, BookingDetail

import api.views as api_views

urlpatterns = [
    path('persons/', api_views.PersonList.as_view(), name="person_list"),
    path('person/<int:pk>', api_views.PersonDetail.as_view(), name="person_detail"),
    path('bookings/', api_views.BookingList.as_view(), name="bookings_list"),
    path('booking/<int:pk>', api_views.PersonDetail.as_view(), name="booking_detail"),
]
