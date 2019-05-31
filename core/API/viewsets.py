from rest_framework.viewsets import ModelViewSet

from core.API.serializers import CadastroSerializer ,CoberturaSerializer
from core.models import Cadastro, Cobertura


class CoberturaViewSet(ModelViewSet):
    queryset = Cobertura.objects.all()
    serializer_class = CoberturaSerializer


class CadastroViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer

