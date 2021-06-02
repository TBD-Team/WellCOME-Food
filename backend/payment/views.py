import io
from datetime import date, datetime as dt

from wsgiref.util import FileWrapper
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pyGRU.core import GRUPDF

from .models import Account, GRU, Credit, Purchase
from .serializers import PurchaseSerializer


class PurchaseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get(self, request):
        purchases = Purchase.objects.all().order_by('-created_at')

    def post(self, request):
        account = request.user.account
        try:
            purchase = account.make_purchase()
        except Exception as e:
            return Response(e.args[0], 405)
        else:
            return Response(PurchaseSerializer(purchase).data, 201)


class CreditAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        account = request.user.account
        value = str(request.data["value"]).replace('.', ',')
        pdf = GRUPDF(
            codigo_favorecido=settings.GRU["codigo_favorecido"],
            gestao=settings.GRU["gestao"],
            codigo_correlacao=settings.GRU["codigo_correlacao"],
            nome_favorecido=settings.GRU["nome_favorecido"],
            codigo_recolhimento=settings.GRU["codigo_recolhimento"],
            nome_recolhimento=settings.GRU["nome_recolhimento"],
            referencia=settings.GRU["referencia"],
            vencimento=request.data["expiration_time"],
            cnpj_cpf=request.user.cpf,
            nome_contribuinte=request.user.first_name,
            valorPrincipal=value,
            valorTotal=value
        )
        credit = Credit.create(
            account=account,
            value=request.data["value"],
            code=pdf.get_barcode(),
            expiration_time=dt.strptime(
                request.data["expiration_time"],
                "%d/%m/%Y"
            )
        )
        return HttpResponse(FileWrapper(io.BytesIO(pdf.get_pdf_obj())), 201)
