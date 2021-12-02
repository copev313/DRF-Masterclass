from django.urls import path
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, ReviewsList,
                                     StreamingPlatformAV, StreamingPlatformDetailsAV)

urlpatterns = [

    path('list/', WatchListAV.as_view(),
         name='watch-list'),

    path('<int:pk>/', WatchDetailsAV.as_view(),
         name='watch-details'),

    path('stream/', StreamingPlatformAV.as_view(),
         name='stream'),

    path('stream/<int:pk>/', StreamingPlatformDetailsAV.as_view(),
         name='stream-details'),

    path('reviews/', ReviewsList.as_view(),
         name='reviews-list'),
]
