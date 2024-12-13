from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from rest_framework.decorators import api_view
from uuid import uuid4
from django.utils.dateparse import parse_date

@api_view(["GET"])
def list_credit_cards(request):
    credit_cards = models.CreditCard.objects.all()
    serializer = serializers.CreditCardSerializer(credit_cards, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_credit_card(request):
    serializer = serializers.CreditCardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def retrieve_credit_card(request, card_id):
    try:
        credit_card = models.CreditCard.objects.get(id=card_id)
        serializer = serializers.CreditCardSerializer(credit_card)
        return Response(serializer.data)
    except models.CreditCard.DoesNotExist:
        return Response({"error": "Cartão de crédito não encontrado"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_credit_card(request, card_id):
    try:
        credit_card = models.CreditCard.objects.get(id=card_id)
        serializer = serializers.CreditCardSerializer(credit_card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except models.CreditCard.DoesNotExist:
        return Response({"error": "Cartão de crédito não encontrado"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_credit_card(request, card_id):
    try:
        credit_card = models.CreditCard.objects.get(id=card_id)
        credit_card.delete()
        return Response({"message": "Cartão de crédito deletado com sucesso"}, status=status.HTTP_204_NO_CONTENT)
    except models.CreditCard.DoesNotExist:
        return Response({"error": "Cartão de crédito não encontrado"}, status=status.HTTP_404_NOT_FOUND)