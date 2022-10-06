from django.db import models


class Item(models.Model):
    new = 'Новая'
    process = 'В процессе'
    done = 'Сделано'
    CHOICES = [
        ('new', 'Новая'),
        ('process', 'В процессе'),
        ('done', 'Сделано')
    ]
    description = models.CharField(max_length=250, null=False, blank=False, verbose_name='Описание')
    description_details = models.CharField(max_length=500, null=True, blank=True, verbose_name='Подробное описание')
    state = models.CharField(max_length=50, null=False, blank=False, choices=CHOICES, default=new,
                             verbose_name='Статус')
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    date_to_do = models.TextField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f'Описание: {self.description}, Статус: {self.get_state_display()}, Дата выполнения: {self.date_to_do}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
