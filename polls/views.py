from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from polls.models import Message
from polls.serializers import MessageSerializer


class MeasurementAddView(CreateAPIView):#RetrieveUpdateAPIView):5 /2
    queryset = Message.objects.all()
    serializer_class = MessageSerializer