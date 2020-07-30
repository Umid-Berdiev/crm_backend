from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class InternationalFinancialInstitute(models.Model):
    name = models.CharField(max_length=60)
    legalAddress = models.TextField()
    responsiblePersonFullname = models.CharField(max_length=60, blank=True)
    responsiblePersonPosition = models.CharField(max_length=50, blank=True)
    responsiblePersonPhoneNumber = models.CharField(max_length=50, blank=True)
    responsiblePersonEmail = models.CharField(max_length=50, blank=True)
    additionalContactPersonFullname = models.CharField(max_length=60, blank=True)
    additionalContactPersonPosition = models.CharField(max_length=50, blank=True)
    additionalContactPersonPhoneNumber = models.CharField(max_length=50, blank=True)
    additionalContactPersonEmail = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name

# class ParticipatingFinancialInstitution(models.Model):
#     name = models.CharField(max_length=60)
#     level = models.IntegerChoices('level', 'HEAD_OFFICE BRANCH')
#     region = models.IntegerField()
#     district = models.IntegerField()
#     legalAddress = models.TextField()
#     contactPerson = models.IntegerField() # relation: this belongs to User model
#     financingVolume = models.IntegerField()
#     subsidiaryLoanConditions = models.IntegerField()

#     def __str__(self):
#         return self.name

# class Beneficiary(models.Model):
    # ownershipForm = 
    # name = models.CharField(max_length=60)
    # activitySector = 
    # region = models.IntegerField()
    # district = models.IntegerField()
    # legalAddress = models.TextField()
    # numberOfEmployees = 
    # landArea = 
    # contactPerson = models.IntegerField() # relation: this belongs to User model
    # financingVolume = models.IntegerField()
    # subsidiaryLoanConditions = models.IntegerField()

