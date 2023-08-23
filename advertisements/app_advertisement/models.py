from django.db import models


class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)


    #Описание товара/информация о товаре
    #Большое текстовое поле
    description = models.TextField('Описание')

    #Цена
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    action = models.BooleanField('торг', help_text='Отметьте, уместен ли торг')

    #Дата публикации
    #Поле записывается при создании объявления
    created_at = models.DateTimeField(auto_now_add=True)

    #Дата изменения/обновления
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'




