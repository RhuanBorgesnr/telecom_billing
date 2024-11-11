from django.db import models
from django.utils import timezone

class CallRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('start', 'START'),
        ('end', 'END'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(choices=RECORD_TYPE_CHOICES, max_length=10)
    timestamp = models.DateTimeField()
    call_id = models.CharField(max_length=50)
    source = models.CharField(max_length=11, blank=True, null=True)
    destination = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"Call {self.call_id} ({self.type})"

    def get_duration(self, end_record):
        """
        Calculates call duration in seconds.
        """
        if self.type == 'start' and end_record.type == 'end' and self.call_id == end_record.call_id:
            return (end_record.timestamp - self.timestamp).total_seconds()
        return 0

    def calculate_call_price(self, price_per_minute=0.09):
        """
        Calculate call price based on duration, converting seconds to minutes.       
        """
        if self.type == 'start':
            end_record = CallRecord.objects.filter(call_id=self.call_id, type='end').first()
            if end_record:
                call_duration_minutes = self.get_duration(end_record) / 60
                return round(call_duration_minutes * price_per_minute, 2)
        return 0


class Bill(models.Model):
    phone_number = models.CharField(max_length=11)
    period = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    call_records = models.ManyToManyField(CallRecord, related_name='bills', blank=True)

    def __str__(self):
        return f"Bill for {self.phone_number} - {self.period.strftime('%Y-%m')}"