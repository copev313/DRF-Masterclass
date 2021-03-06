from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform


class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value



# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()

#         return instance

#     # Field Validation:
#     def validated_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
#         else:
#             return value

#     # Object Validation:
#     def validated(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 'Title and description must be different!'
#             )
#         else:
#             return data
