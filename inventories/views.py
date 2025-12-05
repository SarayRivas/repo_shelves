
from rest_framework import viewsets
from .models import  Shelve
from .serializers import ShelveSerializer

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

        


class ShelveViewSet(viewsets.ModelViewSet):
    queryset = Shelve.objects.all().order_by('id_shelve')
    serializer_class = ShelveSerializer




    
@require_http_methods(["GET", "HEAD"])
def health_check(request):

    res = JsonResponse({"status": "ok"})
    return _no_store(res)
