from django.db import models
from django.utils.text import slugify

# Create your models here.

SCALE_CHOICES = (
    ("1/43", "1/43"),
    ("1/24", "1/24"),
    ("1/18", "1/18"),
)


class OrderModelCars(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    size = models.CharField(choices=SCALE_CHOICES, max_length=20)
    slug = models.SlugField(unique=True, null=False, blank=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:  # slugify("My name") -> "My-name"
            self.slug = slugify(f"model-cars-{self.title}-{self.pk}")

        super().save(*args, **kwargs)
