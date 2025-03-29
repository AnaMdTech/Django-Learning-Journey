from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  author = models.CharField(null=True, max_length=100)
  is_bestselling = models.BooleanField(default=False)
  slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)

  def get_absolute_url(self):
      return reverse("book-detail-page", args=[self.slug])

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)  

  def __str__(self):
    return f"{self.title} ({self.rating})"