from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    CONCLUSAO_CHOICES = [('TCC', 'TCC'), ('Estágio', 'Estágio'), ('TCC e estágio', 'TCC e estágio'), ('Não decidiu', 'Não decidiu')]
    nome = models.CharField(max_length=50, blank=False)
    matricula = models.CharField(blank=False, default='', max_length=11)
    email = models.EmailField(blank=False, default='')
    serie = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)
    curso = models.CharField(max_length=5, choices=[('INTIN', 'INTIN'), ('INTEL', 'INTEL'), ('INTED', 'INTED')], blank=False, default='INTIN')
    idade = models.IntegerField(blank=False, default=0)
    conclusao = models.CharField(max_length=13, choices=CONCLUSAO_CHOICES, default=CONCLUSAO_CHOICES[3])