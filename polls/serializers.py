from rest_framework import serializers

from polls.models import Delivary, Message, Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'phone', 'code_phone', 'teg', 'time_zone']

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'date_time_send', 'status']

class DelivarySerializer(serializers.ModelSerializer):
    clients = ClientSerializer(read_only=True, many=True)
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = Delivary
        fields = ['id', 'text', 'filter_code', 'filter_teg', 'count_send_yes', 'count_send_no']



