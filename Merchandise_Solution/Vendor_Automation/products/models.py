from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProductCategory(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductCategory_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(default="")
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField()
    unit_price = models.IntegerField()
    product_counter = models.IntegerField()  # how much product is left

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


# productId, categoryId, product_name, buy_price, description, availability
