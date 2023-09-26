from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Ivan'},
            {'last_name': 'Ivanov', 'first_name': 'Petr'},
            {'last_name': 'Semenov', 'first_name': 'Aleksandr'},
            {'last_name': 'Aleksandrov', 'first_name': 'Semen'},
        ]

        # Для маленького количества студентов
        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        # Для ~4000 студентов
        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        # print(students_for_create)
        Student.objects.bulk_create(students_for_create)
