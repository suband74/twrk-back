from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

        ordering = ["title"]

    STATUS_CHOICES = (
        (1, "В наличии"),
        (2, "Под заказ"),
        (3, "Ожидается поступление"),
        (4, "Нет в наличии"),
        (5, "Не производится"),
    )

    title = models.CharField("Название", max_length=255)
    vendor_code = models.CharField("Артикул", max_length=255, unique=True)
    price = models.DecimalField("Цена", max_digits=11, decimal_places=2, blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        "Статус", choices=STATUS_CHOICES, default=1
    )
    img = ResizedImageField(force_format="WEBP", quality=75, upload_to="photos/%Y/%m/%d", verbose_name="Изображение")

    extension = models.CharField("Доступный формат", max_length=8, blank=True)

    def __str__(self):
        return self.title
