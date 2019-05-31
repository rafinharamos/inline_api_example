from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=20)

    #def __str__(self):
        #return self.nome, self.tipo, self.modelo



class Cobertura(models.Model):
    peso = models.IntegerField(max_length=20)
    altura = models.IntegerField(max_length=20)
    cadastro = models.ForeignKey(Cadastro, null=False, blank=False, on_delete=models.DO_NOTHING)

    #def __str__(self):
        #return self.peso, self.altura, self.cadastro