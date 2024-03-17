from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ("Shirt", "Shirt"),
    ("Jacket", "Jacket"),
    ("Shorts", "Shorts"),
)

SIZE_CHOICES = (
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)


class OrderClothes(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    size = models.CharField(choices=SIZE_CHOICES, max_length=20)
    slug = models.SlugField(unique=True, null=False, blank=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         "detail_clothes",
    #         kwargs={"slug": self.slug}
    #     )
    #
    # def get_add_to_cart_url(self):
    #     return reverse(
    #         "add_to_cart",
    #         kwargs={"slug": self.slug}
    #     )
    #
    # def get_remove_from_cart_url(self):
    #     return reverse(
    #         "remove_from_cart",
    #         kwargs={"slug": self.slug}
    #     )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:  # slugify("My name") -> "My-name"
            self.slug = slugify(f"clothes-{self.title}-{self.pk}")

        super().save(*args, **kwargs)
