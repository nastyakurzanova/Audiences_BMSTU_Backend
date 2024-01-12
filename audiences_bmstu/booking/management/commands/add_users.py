from django.core.management import BaseCommand

from booking.models import CustomUser


def add_users():
    CustomUser.objects.create_user("user1", "user1@user.com", "1234")
    CustomUser.objects.create_user("user2", "user2@user.com", "1234")
    CustomUser.objects.create_user("user3", "user3@user.com", "1234")
    CustomUser.objects.create_superuser("root", "root@root.com", "1234")
    CustomUser.objects.create_superuser("root2", "root2@root.com", "1234")
    CustomUser.objects.create_superuser("root3", "root3@root.com", "1234")

    print("Пользователи созданы")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        add_users()

