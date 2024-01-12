from rest_framework import serializers

from .models import *


# class SpareSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Audiences
#         fields = "__all__"

class AudiencesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Audiences
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'is_moderator')

class BookingSerializer(serializers.ModelSerializer):
    audiences = AudiencesSerializer(read_only=True, many=True)
    owner = UserSerializer(read_only=True, many=False)
    moderator = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Booking
        fields = "__all__"

# class OrderSerializer(serializers.ModelSerializer):
#     spares = SpareSerializer(read_only=True, many=True)
#     owner = UserSerializer(read_only=True, many=False)
#     moderator = UserSerializer(read_only=True, many=False)

#     class Meta:
#         model = Booking
#         fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

class BookingAudiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingAudiences
        fields = "__all__"