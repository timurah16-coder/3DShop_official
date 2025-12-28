from django.db import models

class Model3D(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена, ₽", max_digits=10, decimal_places=2)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фото", upload_to="models/", blank=True)

    def __str__(self):
        return f"{self.name} — {self.price}₽"

class Order(models.Model):
    email = models.EmailField("Email")
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    model = models.ForeignKey(Model3D, on_delete=models.CASCADE, verbose_name="Модель")
    color = models.CharField("Цвет", max_length=30)
    pickup_date = models.CharField("Дата забора", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} — {self.model.name}"