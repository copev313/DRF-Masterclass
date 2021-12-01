from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.api.serializers import (StreamingPlatformSerializer,
                                           WatchListSerializer)
from watchlist_app.models import StreamingPlatform, WatchList


class StreamingPlatformAV(APIView):

    def get(self, request):
        platforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamingPlatformDetailsAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({ 'error': 'Streaming platform not found' },
                            status=status.HTTP_404_NOT_FOUND)

        serializer = serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailsAV(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({ 'error': 'Movie not found' },
                            status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------

# from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'error': 'Movie not found'},
#                         status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_205_RESET_CONTENT)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
