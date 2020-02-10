from django.db import models

class Car(models.Model):
    T_CHOICES = (
        ('m', 'механика'),
        ('a', 'автомат'),
        ('r', 'робот'),
    )
    
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    model = models.CharField(max_length=255, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    transmission = models.CharField(max_length=1, choices=T_CHOICES, default='a', verbose_name='Коробка передач')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f"{self.manufacturer} - {self.model}"
