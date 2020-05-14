from django.db import models

# Create your models here.
class Certificate(models.Model):
    cf_name=models.CharField(max_length=100)
    cf_org=models.CharField(max_length=100)
    cf_link=models.CharField(max_length=250)
    def __str__(self):
        return self.cf_name[:30]


class Plateform(models.Model):
    org_name=models.CharField(max_length=70)
    org_link=models.CharField(max_length=250)
    org_image=models.CharField(max_length=265)
    def __str__(self):
        return self.org_name
    