from rest_framework import viewsets
from .serializers import PatientRecordSerializer
from .models import PatientRecord


class PatientRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view patient records
    """
    queryset = PatientRecord.objects.all().order_by('-created')
    serializer_class = PatientRecordSerializer