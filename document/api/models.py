from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Company(models.Model):
    entities = [
        ('proprietorship', 'Proprietorship'),
        ('partnership', 'Partnership'),
        ('private_ltd', 'Private Ltd'),
        ('public_ltd', 'Public Ltd'),
        ('huf', 'HUF'),
        ('llp', 'LLP'),
        ('llc', 'LLC'),
        ('aop', 'AOP'),
        ('trust', 'Trust'),
    ]


    company = models.CharField(max_length=122)
    date_of_incorporation = models.DateField()
    contact_person = models.CharField(max_length=122)
    entity_type = models.CharField(max_length=100, choices=entities)
    # file_no = models.CharField(max_length=100, unique=True)


    # def save(self):
    #     if not self.file_no and self.pk is None:
    #         last_invoice = Company.objects.all().order_by("-pk").first()
    #         last_pk = 0
    #         if last_invoice:
    #             last_pk = last_invoice.pk
        
    #         self.file_no = "SA-" + str(last_pk+1).zfill(3)

    #     super(Company, self).save()


    def __str__(self):
        return self.company + "-" 
    
# + self.file_no


class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username