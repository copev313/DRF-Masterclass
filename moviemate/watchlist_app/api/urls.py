from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from moviemate.watchlist_app.api.views import ReviewList
from watchlist_app.api.views import (ReviewCreate, ReviewDetail, ReviewsList,
                                     StreamingPlatformAV, StreamPlatformVS,
                                     StreamingPlatformDetailsAV,
                                     WatchDetailsAV, WatchListAV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
     
    path('list/', WatchListAV.as_view(),
          name='watch-list'),

    path('<int:pk>/', WatchDetailsAV.as_view(),
          name='watch-details'),
    
    path('', include(router.urls)),

#     path('stream/', StreamingPlatformAV.as_view(),
#           name='stream'),

#     path('stream/<int:pk>/', StreamingPlatformDetailsAV.as_view(),
#           name='stream-details'),

#     path('reviews/', ReviewsList.as_view(),
#          name='reviews-list'),

#     path('reviews/<int:pk>/', ReviewDetail.as_view(),
#          name='review-detail'),

     path('stream/<int:pk>/review-create/', ReviewCreate.as_view(),
          name='reviews-create'),

     path('stream/<int:pk>/review/', ReviewsList.as_view(),
          name='reviews-list'),

     path('stream/review/<int:pk>/',  ReviewDetail.as_view(),
          name='review-detail'),
]
