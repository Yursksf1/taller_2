from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name


class Question(models.Model):
    CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]

    text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.text[:50]


class Exam(models.Model):
    student_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    questions = models.ManyToManyField(Question, related_name='exams')  # <-- AÑADIDO

    def __str__(self):
        return f"{self.student_name}'s Exam - {self.date.strftime('%Y-%m-%d')}"


class Answer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1, choices=Question.CHOICES)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"Answer to Q{self.question.id} by {self.exam.student_name}"
