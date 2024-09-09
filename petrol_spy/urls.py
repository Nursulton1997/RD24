from django.urls import path
from petrol_spy.views import LastUserHundred

urlpatterns = [
    path('api/v1/petrol-spy/leaderboard/', LastUserHundred.as_view())
]