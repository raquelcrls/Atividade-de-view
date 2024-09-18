from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=200)
    data_de_nascimento = models.DateField()

def __str__(self):
    return self.nome
    


