from django.core.management.base import BaseCommand
from icfes.models import Subject, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Hola mundo')
        subjects = ["Geometria", "Estadistica", "Aritmetica", "Algebra"]

        category = Category.objects.filter(name="Matematicas").first()
        for subjec in subjects:
            print(f'Creando la materia {subjec}')
            sub = Subject(
                name = subjec,
                category = category
            )
            sub.save()
        print('Se han creado las materias exitosamente')