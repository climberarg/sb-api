from .models import BackScratcher
from .serializers import BackScratcherSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class BackScratcherViewSet(viewsets.ModelViewSet):
    queryset = BackScratcher.objects.all()
    serializer_class = BackScratcherSerializer