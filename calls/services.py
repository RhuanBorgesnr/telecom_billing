from datetime import datetime, timedelta
from django.utils import timezone
from .models import CallRecord, Bill


class BillingService:

    @staticmethod
    def get_billing_period(period: str = None):
        """
        Returns the start and end dates of the billing period.
        If the period is not specified, uses the previous month.
        """
        if period:
            try:
                start_date = datetime.strptime(period, "%Y-%m").date()
                end_date = (
                    start_date.replace(day=1) + timedelta(days=31)
                ).replace(day=1) - timedelta(days=1)
            except ValueError:
                raise ValueError("Invalid period format. Use 'YYYY-MM'.")
        else:
            now = timezone.now()
            first_day_of_current_month = now.replace(
                day=1, hour=0, minute=0, second=0, microsecond=0
            )
            end_date = first_day_of_current_month - timedelta(days=1)
            start_date = end_date.replace(day=1)

        return start_date, end_date

    @staticmethod
    def calculate_total_cost(phone_number: str, start_date: datetime, end_date: datetime) -> float:
        """
        Calculates the total cost of calls made within the specified period.
        """
        calls = CallRecord.objects.filter(
            source=phone_number,
            timestamp__date__range=[start_date, end_date]
        ).order_by('timestamp')

        total_cost = sum(call.calculate_call_price() for call in calls)
        
        return round(total_cost, 2)

    @staticmethod
    def get_or_create_bill(phone_number: str, period: str = None):
        """
        Retrieves or creates a bill (`Bill`) for the specified phone number and period.
        """
        start_date, end_date = BillingService.get_billing_period(period)

        bill = Bill.objects.filter(
            phone_number=phone_number,
            period=start_date,
            start_date=start_date,
            end_date=end_date
        ).first()

        if not bill:
            total_cost = BillingService.calculate_total_cost(phone_number, start_date, end_date)
            bill = Bill.objects.create(
                phone_number=phone_number,
                period=start_date,
                start_date=start_date,
                end_date=end_date,
                total_cost=total_cost
            )
            calls = CallRecord.objects.filter(
                source=phone_number,
                timestamp__date__range=[start_date, end_date]
            )
            bill.call_records.set(calls)

        return bill
