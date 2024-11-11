from rest_framework import serializers

from .models import CallRecord, Bill

class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = ['id', 'type', 'timestamp', 'call_id', 'source', 'destination']

    
class BillSerializer(serializers.ModelSerializer):
    call_records = CallRecordSerializer(many=True)

    class Meta:
        model = Bill
        fields = ['phone_number', 'period', 'total_cost', 'call_records']
        
    