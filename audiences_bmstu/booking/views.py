from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *


# def get_draft_booking_id():
#     discovery = Booking.objects.filter(status=1).first()

#     if discovery is None:
#         return None

#     return discovery.pk


# @api_view(["GET"])
# def search_audiences(request):
#     query = request.GET.get("query", "")

#     pioneers = Audiences.objects.filter(status=1).filter(name__icontains=query)

#     serializer = AudiencesSerializer(pioneers, many=True)

#     data = {
#         "audiences": serializer.data,
#         "draft_vacancy": get_draft_booking_id()
#     }

#     return Response(data)


# def get_draft_audiences():

#     # audiences = Audiences.objects.filter(status=1).first()
#     audiences = Audiences.objects.filter(status=1).first()
#     if audiences is None:
#         return None

#     return audiences

# @api_view(["GET"])
# def search_audiences(request):
#     name = request.GET.get('query', '')
    
#     audiences = Audiences.objects.filter(status=1).filter(name__contains=name)
    
#     serializer = AudiencesSerializer(audiences, many=True)
#     draft_audiences = get_draft_audiences()
#     # draft_audiences.pk
#     data = {
#         "info": serializer.data,
#         "draft_audiences": draft_audiences.pk if draft_audiences else None
#     }
#     print(data)
#     return Response(data)


def get_draft_audiences():
    # audiences = Audiences.objects.filter(status=1).first()
    audiences = Audiences.objects.filter(status=1).first()
    if audiences is None:
        return None

    return audiences


@api_view(["GET"])
def search_audiences(request):
    name = request.GET.get('query', '')
    
    audiences = Audiences.objects.filter(status=1).filter(name__contains=name)
    
    serializer = AudiencesSerializer(audiences, many=True)
    draft_audiences = get_draft_audiences()
    # draft_audiences.pk
    data = {
        "info": serializer.data,
        "draft_audiences": draft_audiences.pk if draft_audiences else None
    }
    print(data)
    return Response(data)

@api_view(["GET"])
def get_audiences_by_id(request, audiences_id):
    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    auditorium = Audiences.objects.get(pk=audiences_id)
    serializer = AudiencesSerializer(auditorium, many=False)

    return Response(serializer.data)


@api_view(["PUT"])
def update_audiences(request, audiences_id):
    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    auditorium = Audiences.objects.get(pk=audiences_id)
    serializer = AudiencesSerializer(auditorium, data=request.data, many=False, partial=True)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def create_audiences(request):
    serializer = AudiencesSerializer(data=request.data)
    serializer.initial_data["image"] = request.FILES['image']
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_audiences(request, audiences_id):
    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    auditorium = Audiences.objects.get(pk=audiences_id)
    auditorium.status = 2
    auditorium.save()

    audiencess = Audiences.objects.filter(status=1)
    serializer = AudiencesSerializer(audiencess, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def add_audiences_to_booking(request, audiences_id):
    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    audiences = Audiences.objects.get(pk=audiences_id)
    print(audiences)
    booking = Booking.objects.filter(status=1).last()
    print(booking)
    if booking is None:
        booking = Booking.objects.create()
    # audiencess = Audiences.objects.filter(status=1)
    booking.audincess.add(audiences)
    # booking.audiences.add(audiences)
    booking.save()

    serializer = AudiencesSerializer(booking.audincess, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_audiences_image(request, audiences_id):
    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    audiences = Audiences.objects.get(pk=audiences_id)

    return HttpResponse(audiences.image, content_type="image/png")


@api_view(["PUT"])
def update_audiences_image(request, audiences_id):
    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    pioneer = Audiences.objects.get(pk=audiences_id)
    serializer = AudiencesSerializer(pioneer, data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# @api_view(["GET"])
# def search_cosmetics(request):
#     cosmetics = Cosmetic.objects.all()

#     request_status = request.GET.get("status")
#     if request_status:
#         cosmetics = cosmetics.filter(status=request_status)

#     serializer = CosmeticSerializer(cosmetics, many=True)

#     return Response(serializer.data)

@api_view(["GET"])
def get_booking(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_booking_by_id(request, booking_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    discovery = Booking.objects.get(pk=booking_id)
    serializer = BookingSerializer(discovery, many=False)

    return Response(serializer.data)


@api_view(["PUT"])
def update_booking(request, booking_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    bookings = Booking.objects.get(pk=booking_id)
    serializer = BookingSerializer(bookings, data=request.data, many=False, partial=True)

    if serializer.is_valid():
        serializer.save()

    bookings.status = 1
    bookings.save()

    return Response(serializer.data)


@api_view(["PUT"])
def update_status_user(request, booking_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    request_status = request.data["status"]

    if request_status not in [1, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    bookings = Booking.objects.get(pk=booking_id)
    lesson_status = bookings.status

    if lesson_status == 5:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    bookings.status = request_status
    bookings.save()

    serializer = BookingSerializer(bookings, many=False)

    return Response(serializer.data)


@api_view(["PUT"])
def update_status_admin(request, booking_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    request_status = request.data["status"]

    if request_status in [1, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    bookings = Booking.objects.get(pk=booking_id)

    lesson_status = bookings.status

    if lesson_status in [3, 4, 5]:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    bookings.status = request_status
    bookings.save()

    serializer = BookingSerializer(bookings, many=False)

    return Response(serializer.data)


@api_view(["DELETE"])
def delete_booking(request, booking_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    bookings = Booking.objects.get(pk=booking_id)
    bookings.status = 5
    bookings.save()

    return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_audiences_from_booking(request, booking_id, audiences_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not Audiences.objects.filter(pk=audiences_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    bookings = Booking.objects.get(pk=booking_id)
    bookings.audincess.remove(Audiences.objects.get(pk=audiences_id))
    bookings.save()

    serializer = AudiencesSerializer(bookings.audincess, many=True)

    return Response(serializer.data)

ACCESS_TOKEN = "123456"

@api_view(["PUT"])
def update_free_audiences(request, booking_id):
    if not Booking.objects.filter(pk=booking_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(f'========== {request.data}')
    
    element_value = request.data.get('access_token', 0)
    if(element_value==ACCESS_TOKEN):
        booking = Booking.objects.get(pk=booking_id)
        serializer = BookingSerializer(booking, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
        booking.save()
        print(booking.free_audiences)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
















# ----------------------------------------!!!!!!!!!!!!!!!!!!!!_---------------------
# ----------------------
# def get_draft_discovery_id():
#     discovery = Discovery.objects.filter(status=1).first()

#     if discovery is None:
#         return None

#     return discovery.pk


# @api_view(["GET"])
# def search_pioneers(request):
#     query = request.GET.get("query", "")

#     pioneers = Pioneer.objects.filter(status=1).filter(name__icontains=query)

#     serializer = PioneerSerializer(pioneers, many=True)

#     data = {
#         "pioneers": serializer.data,
#         "draft_vacancy": get_draft_discovery_id()
#     }

#     return Response(data)


# @api_view(["GET"])
# def get_pioneer_by_id(request, pioneer_id):
#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     pioneer = Pioneer.objects.get(pk=pioneer_id)
#     serializer = PioneerSerializer(pioneer, many=False)

#     return Response(serializer.data)


# @api_view(["PUT"])
# def update_pioneer(request, pioneer_id):
#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     pioneer = Pioneer.objects.get(pk=pioneer_id)
#     serializer = PioneerSerializer(pioneer, data=request.data, many=False, partial=True)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(["POST"])
# def create_pioneer(request):
#     Pioneer.objects.create()

#     pioneers = Pioneer.objects.all()
#     serializer = PioneerSerializer(pioneers, many=True)

#     return Response(serializer.data)


# @api_view(["DELETE"])
# def delete_pioneer(request, pioneer_id):
#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     pioneer = Pioneer.objects.get(pk=pioneer_id)
#     pioneer.status = 2
#     pioneer.save()

#     pioneers = Pioneer.objects.filter(status=1)
#     serializer = PioneerSerializer(pioneers, many=True)

#     return Response(serializer.data)


# @api_view(["POST"])
# def add_pioneer_to_discovery(request, pioneer_id):
#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     pioneer = Pioneer.objects.get(pk=pioneer_id)

#     discovery = Discovery.objects.filter(status=1).last()

#     if discovery is None:
#         discovery = Discovery.objects.create()

#     discovery.pioneers.add(pioneer)
#     discovery.save()

#     serializer = PioneerSerializer(discovery.pioneers, many=True)

#     return Response(serializer.data)


# @api_view(["GET"])
# def get_pioneer_image(request, pioneer_id):
#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     pioneer = Pioneer.objects.get(pk=pioneer_id)

#     return HttpResponse(pioneer.image, content_type="image/png")


# @api_view(["PUT"])
# def update_pioneer_image(request, pioneer_id):
#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     pioneer = Pioneer.objects.get(pk=pioneer_id)
#     serializer = PioneerSerializer(pioneer, data=request.data, many=False, partial=True)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(["GET"])
# def get_discoveries(request):
#     discoveries = Discovery.objects.all()
#     serializer = DiscoverySerializer(discoveries, many=True)

#     return Response(serializer.data)


# @api_view(["GET"])
# def get_discovery_by_id(request, discovery_id):
#     if not Discovery.objects.filter(pk=discovery_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     discovery = Discovery.objects.get(pk=discovery_id)
#     serializer = DiscoverySerializer(discovery, many=False)

#     return Response(serializer.data)


# @api_view(["PUT"])
# def update_discovery(request, discovery_id):
#     if not Discovery.objects.filter(pk=discovery_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     discovery = Discovery.objects.get(pk=discovery_id)
#     serializer = DiscoverySerializer(discovery, data=request.data, many=False, partial=True)

#     if serializer.is_valid():
#         serializer.save()

#     discovery.status = 1
#     discovery.save()

#     return Response(serializer.data)


# @api_view(["PUT"])
# def update_status_user(request, discovery_id):
#     if not Discovery.objects.filter(pk=discovery_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     request_status = request.data["status"]

#     if request_status not in [1, 5]:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     discovery = Discovery.objects.get(pk=discovery_id)
#     lesson_status = discovery.status

#     if lesson_status == 5:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     discovery.status = request_status
#     discovery.save()

#     serializer = DiscoverySerializer(discovery, many=False)

#     return Response(serializer.data)


# @api_view(["PUT"])
# def update_status_admin(request, discovery_id):
#     if not Discovery.objects.filter(pk=discovery_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     request_status = request.data["status"]

#     if request_status in [1, 5]:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     discovery = Discovery.objects.get(pk=discovery_id)

#     lesson_status = discovery.status

#     if lesson_status in [3, 4, 5]:
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     discovery.status = request_status
#     discovery.save()

#     serializer = DiscoverySerializer(discovery, many=False)

#     return Response(serializer.data)


# @api_view(["DELETE"])
# def delete_discovery(request, discovery_id):
#     if not Discovery.objects.filter(pk=discovery_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     discovery = Discovery.objects.get(pk=discovery_id)
#     discovery.status = 5
#     discovery.save()

#     return Response(status=status.HTTP_200_OK)


# @api_view(["DELETE"])
# def delete_pioneer_from_discovery(request, discovery_id, pioneer_id):
#     if not Discovery.objects.filter(pk=discovery_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if not Pioneer.objects.filter(pk=pioneer_id).exists():
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     discovery = Discovery.objects.get(pk=discovery_id)
#     discovery.pioneers.remove(Pioneer.objects.get(pk=pioneer_id))
#     discovery.save()

#     serializer = PioneerSerializer(discovery.pioneers, many=True)

#     return Response(serializer.data)

