from django.db import models

# Create your models here.
class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()

    def __str__(self):
        return self.title


    def pub_date_clean(self):
        return self.pub_date.strftime('%b %e %Y')
