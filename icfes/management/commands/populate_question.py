from django.core.management.base import BaseCommand
from icfes.models import Subject, Question

class Command(BaseCommand):
    help = "Popula la base de datos con preguntas de ejemplo para cada materia"

    def handle(self, *args, **options):
        questions_data = {
            "Geometria": [
                {
                    "text": "¿Cuántos lados tiene un hexágono?",
                    "option_a": "Cuatro",
                    "option_b": "Cinco",
                    "option_c": "Seis",
                    "option_d": "Siete",
                    "correct_answer": "C"
                },
                {
                    "text": "¿Cuál es la suma de los ángulos internos de un triángulo?",
                    "option_a": "180 grados",
                    "option_b": "360 grados",
                    "option_c": "90 grados",
                    "option_d": "270 grados",
                    "correct_answer": "A"
                }
            ],
            "Estadistica": [
                {
                    "text": "¿Cuál es la media de los números 2, 4 y 6?",
                    "option_a": "4",
                    "option_b": "5",
                    "option_c": "6",
                    "option_d": "3",
                    "correct_answer": "A"
                }
            ],
            "Aritmetica": [
                {
                    "text": "¿Cuánto es 7 + 5?",
                    "option_a": "10",
                    "option_b": "12",
                    "option_c": "13",
                    "option_d": "11",
                    "correct_answer": "B"
                }
            ],
            "Algebra": [
                {
                    "text": "¿Cuál es el valor de x en la ecuación 2x = 10?",
                    "option_a": "2",
                    "option_b": "5",
                    "option_c": "10",
                    "option_d": "20",
                    "correct_answer": "B"
                }
            ],
            "Comprension Lectora": [
                {
                    "text": "¿Qué significa inferir en un texto?",
                    "option_a": "Copiar el texto",
                    "option_b": "Leer en voz alta",
                    "option_c": "Sacar conclusiones",
                    "option_d": "Buscar palabras difíciles",
                    "correct_answer": "C"
                }
            ],
            "Gramática": [
                {
                    "text": "¿Cuál es el verbo en la oración: 'El perro corre rápido'?",
                    "option_a": "perro",
                    "option_b": "corre",
                    "option_c": "rápido",
                    "option_d": "El",
                    "correct_answer": "B"
                }
            ],
            "Vocabulario": [
                {
                    "text": "¿Cuál es el sinónimo de 'feliz'?",
                    "option_a": "Triste",
                    "option_b": "Contento",
                    "option_c": "Enojado",
                    "option_d": "Cansado",
                    "correct_answer": "B"
                }
            ],
            "Análisis Literario": [
                {
                    "text": "¿Qué es una metáfora?",
                    "option_a": "Una comparación directa",
                    "option_b": "Una exageración",
                    "option_c": "Una pregunta retórica",
                    "option_d": "Una repetición",
                    "correct_answer": "A"
                }
            ],
            "Historia de la Literatura": [
                {
                    "text": "¿Quién escribió 'Cien años de soledad'?",
                    "option_a": "Pablo Neruda",
                    "option_b": "Gabriel García Márquez",
                    "option_c": "Mario Vargas Llosa",
                    "option_d": "Jorge Luis Borges",
                    "correct_answer": "B"
                }
            ],
            "Historia": [
                {
                    "text": "¿En qué año llegó Colón a América?",
                    "option_a": "1492",
                    "option_b": "1500",
                    "option_c": "1453",
                    "option_d": "1519",
                    "correct_answer": "A"
                }
            ],
            "Geografía": [
                {
                    "text": "¿Cuál es el río más largo del mundo?",
                    "option_a": "Nilo",
                    "option_b": "Amazonas",
                    "option_c": "Yangtsé",
                    "option_d": "Misisipi",
                    "correct_answer": "B"
                }
            ],
            "Cívica": [
                {
                    "text": "¿Qué es la democracia?",
                    "option_a": "Un sistema económico",
                    "option_b": "Un sistema político donde el pueblo elige",
                    "option_c": "Una religión",
                    "option_d": "Una ley",
                    "correct_answer": "B"
                }
            ],
            "Botánica": [
                {
                    "text": "¿Qué estudia la botánica?",
                    "option_a": "Los animales",
                    "option_b": "Las plantas",
                    "option_c": "Los minerales",
                    "option_d": "Los planetas",
                    "correct_answer": "B"
                }
            ],
            "Zoología": [
                {
                    "text": "¿Qué animal es un mamífero?",
                    "option_a": "Tiburón",
                    "option_b": "Gallina",
                    "option_c": "Ballena",
                    "option_d": "Cocodrilo",
                    "correct_answer": "C"
                }
            ],
            "Genética": [
                {
                    "text": "¿Qué molécula contiene la información genética?",
                    "option_a": "ADN",
                    "option_b": "ARN",
                    "option_c": "Proteína",
                    "option_d": "Lípido",
                    "correct_answer": "A"
                }
            ]
        }

        created = 0
        for subject_name, questions in questions_data.items():
            subject = Subject.objects.filter(name=subject_name).first()
            if not subject:
                self.stdout.write(self.style.WARNING(f"Materia '{subject_name}' no encontrada."))
                continue

            for q in questions:
                if not Question.objects.filter(text=q["text"], subject=subject).exists():
                    Question.objects.create(
                        text=q["text"],
                        subject=subject,
                        option_a=q["option_a"],
                        option_b=q["option_b"],
                        option_c=q["option_c"],
                        option_d=q["option_d"],
                        correct_answer=q["correct_answer"]
                    )
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"Pregunta creada para {subject_name}: {q['text'][:40]}..."))

        self.stdout.write(self.style.SUCCESS(f"Total de preguntas creadas: {created}"))