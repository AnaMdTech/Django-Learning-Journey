from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(on_delete=models.CASCADE, related_name='jobs', to=Category)

    class Meta:
        verbose_name_plural = 'Job'

    def __str__(self):
        return self.title