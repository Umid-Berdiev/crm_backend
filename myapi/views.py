from rest_framework import viewsets

from .serializers import IFISerializer
from .models import InternationalFinancialInstitute


class IFIViewSet(viewsets.ModelViewSet):
    queryset = InternationalFinancialInstitute.objects.all().order_by('name')
    serializer_class = IFISerializer
