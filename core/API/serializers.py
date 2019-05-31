from rest_framework.serializers import ModelSerializer

from core.models import Cadastro, Cobertura

class CoberturaSerializer(ModelSerializer):
    class Meta:
        model = Cobertura
        fields = '__all__'


class CadastroSerializer(ModelSerializer):
    #cobertura = CoberturaSerializer(many=True)
    class Meta:
        model = Cadastro
        fields = ('nome', 'tipo', 'modelo')

