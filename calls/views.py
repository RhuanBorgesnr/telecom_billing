from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CallRecord, Bill
from .serializers import CallRecordSerializer, BillSerializer
from .services import BillingService


class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer

    @action(detail=False, methods=['get'], url_path='bill')
    def get_bill(self, request):
        phone_number = request.query_params.get('phone_number')
        period = request.query_params.get('period', None)

        if not phone_number:
            return Response(
                {"error": "Phone number is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            bill = BillingService.get_or_create_bill(phone_number, period)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BillSerializer(bill)
        return Response(serializer.data)


class BillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
