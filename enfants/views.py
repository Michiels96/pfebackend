from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Enfants, Handicaps, HandicapEnfant
from .serializers import EnfantSerializer, HandicapSerializer, HandicapEnfantSerializer
from rest_framework.response import Response

class EnfantsView(viewsets.ModelViewSet):
    queryset = Enfants.objects.all()
    serializer_class = EnfantSerializer

class HandicapsView(viewsets.ModelViewSet):
    queryset = Handicaps.objects.all()
    serializer_class = HandicapSerializer

class HandicapsEnfantsView(viewsets.ModelViewSet):
    queryset = HandicapEnfant.objects.all()
    serializer_class = HandicapEnfantSerializer