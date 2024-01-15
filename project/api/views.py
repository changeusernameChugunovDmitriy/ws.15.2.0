from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

class MealGet(APIView):
    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializers(meals, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializers = MealSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        return Response({'data': serializers.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            meal = Meal.objects.get(pk=pk)
        except:
            return Response('Meal is not Exist')
        serializers = MealSerializers(data=request.data, instance=meal)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        return Response({'data': serializers.data})

class MealGetList(ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class MealOne(RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers
    # permission_classes = [IsAdminUser]