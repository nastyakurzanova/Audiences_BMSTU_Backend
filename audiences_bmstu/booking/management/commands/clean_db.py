from django.core.management.base import BaseCommand
from booking.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Audiences.objects.all().delete()
        Booking.objects.all().delete()
        # CustomUser.objects.all().delete()