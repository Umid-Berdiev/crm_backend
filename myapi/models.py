from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class InternationalFinancialInstitute(models.Model):
    name = models.CharField(max_length=60)
    legalAddress = models.TextField()
    responsiblePerson = models.IntegerField()
    additionalContactPerson = models.IntegerField()

    def __str__(self):
        return self.name

class ParticipatingFinancialInstitution(models.Model):
    name = models.CharField(max_length=60)
    level = models.IntegerChoices('level', 'HEAD_OFFICE BRANCH')
    region = models.IntegerField()
    district = models.IntegerField()
    legalAddress = models.TextField()
    contactPerson = models.IntegerField() # relation: this belongs to User model
    financingVolume = models.IntegerField()
    subsidiaryLoanConditions = models.IntegerField()

class Beneficiary(models.Model):
    pass
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

