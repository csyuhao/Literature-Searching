from django.db import models

# Create your models here.


class LiteratureItem(models.Model):
    title = models.CharField(max_length=256)
    literature_id = models.SlugField(max_length=128)
    category = models.CharField(max_length=64)
    report_number = models.CharField(max_length=128)
    author = models.CharField(max_length=256)
    details_link = models.CharField(max_length=256)
    pub_date = models.DateField('date published');
    abstract = models.TextField()
    journal_ref = models.TextField()

    def __str__(self):
        return self.title


