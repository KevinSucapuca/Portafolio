from django.db import models

# Create your models here.
class Portafolio(models.Model):
    foto = models.ImageField(upload_to="portafolio", null=True)
    titulo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=100)
    tags = models.CharField(max_length=80)
    url= models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo
    
    
opciones_consulta = [
    [ 0, "Deseo asesoria" ],
    [1, "Deseo clases"],
    [2, "Ayuda en mi codigo"]
    
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50) 
    correo = models.EmailField(max_length=150)
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje= models.TextField()
    
    def __str__(self):
        return self.nombre
    