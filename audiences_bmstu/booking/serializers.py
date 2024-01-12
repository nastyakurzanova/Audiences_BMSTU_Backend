from rest_framework import serializers

from .models import *


class AudiencesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Audiences
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    audiences = AudiencesSerializer(read_only=True, many=True)

    class Meta:
        model = Booking
        fields = "__all__"
# class PioneerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pioneer
#         fields = "__all__"


# class DiscoverySerializer(serializers.ModelSerializer):
#     pioneers = PioneerSerializer(read_only=True, many=True)

#     class Meta:
#         model = Discovery
#         fields = "__all__"

