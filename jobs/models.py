from django.db import models

# Create your models here.
class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    
    sampleimage1=models.ImageField(upload_to='images/',blank=True)
    sampleimage2=models.ImageField(upload_to='images/',blank=True)
    sampleimage3=models.ImageField(upload_to='images/',blank=True)
    sampleimage4=models.ImageField(upload_to='images/',blank=True)
    sampleimage5=models.ImageField(upload_to='images/',blank=True)
    sampleimage6=models.ImageField(upload_to='images/',blank=True)
    sampleimage7=models.ImageField(upload_to='images/',blank=True)
    sampleimage8=models.ImageField(upload_to='images/',blank=True)
    sampleimage9=models.ImageField(upload_to='images/',blank=True)
    sampleimage10=models.ImageField(upload_to='images/',blank=True)

    url=models.URLField(blank=True)




    summary=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    body4=models.TextField(blank=True)
    body5=models.TextField(blank=True)
    body6=models.TextField(blank=True)
    body7=models.TextField(blank=True)
    body8=models.TextField(blank=True)
    body9=models.TextField(blank=True)
    body10=models.TextField(blank=True)





    def __str__(self):
        return self.title


    def pub_date_clean(self):
        return self.pub_date.strftime('%b %e %Y')
