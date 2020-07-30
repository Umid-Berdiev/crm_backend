from rest_framework import serializers
from .models import InternationalFinancialInstitute

class IFISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InternationalFinancialInstitute
        fields = ('name', 'legalAddress', 'responsiblePersonFullname', 'responsiblePersonPosition', 'responsiblePersonPhoneNumber', 'responsiblePersonEmail', 'additionalContactPersonFullname', 'additionalContactPersonPosition', 'additionalContactPersonPhoneNumber', 'additionalContactPersonEmail',)
