from django.contrib.auth.models import User
from .models import Film, ExtraInfo, Ocena, Aktor
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Użytkownicy': reverse('ListaUzytkownikow', request=request, format=format),
        'Wszystkie filmy': reverse('ListaFilmow', request=request, format=format),
        'Informacje dodatkowe': reverse('InformacjeDodatkowe', request=request, format=format),
        'Wszystkie oceny': reverse('Recenzje', request=request, format=format),
        'Wszyscy aktorzy': reverse('Aktorzy', request=request, format=format),
    })

class FilmCreateList(generics.ListCreateAPIView):
    # queryset = Film.objects.all().order_by('-rok','tytul')
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Film.objects.all().order_by('-rok','tytul')
        tytul = self.request.query_params.get('tytul')
        id = self.request.query_params.get('id')
        if tytul is not None:
            queryset = queryset.filter(tytul__startswith=tytul)
        if id is not None:
            queryset = queryset.filter(id__exact=id)
        return queryset


class FilmRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ExtraInfoCreateList(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class ExtraInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class OcenaCreateList(generics.ListCreateAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class OcenaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class AktorCreateList(generics.ListCreateAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class AktorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

class UserSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        password = validated_data.get('password', None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort

