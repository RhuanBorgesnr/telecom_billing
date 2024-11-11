from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CallRecord, Bill
from .services import BillingService
from django.utils import timezone
from datetime import datetime, timedelta

class CallRecordTest(TestCase):
    def setUp(self):
        self.call_start = CallRecord.objects.create(
            type='start',
            timestamp=timezone.now(),
            call_id='123',
            source='123456789',
            destination='987654321'
        )
        self.call_end = CallRecord.objects.create(
            type='end',
            timestamp=timezone.now() + timedelta(minutes=5),
            call_id='123',
            source='123456789',
            destination='987654321'
        )

    def test_get_duration(self):
        duration = self.call_start.get_duration(self.call_end)
        self.assertAlmostEqual(duration, 300, places=2)


    def test_calculate_call_price(self):
        price = self.call_start.calculate_call_price(price_per_minute=0.1)
        self.assertEqual(price, 0.5)

class BillingServiceTest(TestCase):
    def setUp(self):
        self.call_start = CallRecord.objects.create(
            type='start',
            timestamp=timezone.now(),
            call_id='123',
            source='123456789',
            destination='987654321'
        )
        self.call_end = CallRecord.objects.create(
            type='end',
            timestamp=timezone.now() + timedelta(minutes=5),
            call_id='123',
            source='123456789',
            destination='987654321'
        )

    def test_get_billing_period_with_period(self):
        period = "2024-10"
        start_date, end_date = BillingService.get_billing_period(period)
        self.assertEqual(start_date, datetime(2024, 10, 1).date())
        self.assertEqual(end_date, datetime(2024, 10, 31).date())

    def test_get_billing_period_without_period(self):
        start_date, end_date = BillingService.get_billing_period()
        today = timezone.now().date()
        self.assertEqual(start_date.month, today.month - 1)
        self.assertEqual(end_date.month, today.month - 1)

    def test_calculate_total_cost(self):
        start_date = timezone.now().date() - timedelta(days=1)
        end_date = timezone.now().date()
        total_cost = BillingService.calculate_total_cost('123456789', start_date, end_date)
        self.assertAlmostEqual(total_cost, 0.5, places=1)



    def test_get_or_create_bill(self):
        bill = BillingService.get_or_create_bill('123456789', period="2024-10")
        self.assertIsNotNone(bill)
        self.assertEqual(bill.phone_number, '123456789')

class CallRecordViewSetTest(APITestCase):
    def setUp(self):
        self.call_start = CallRecord.objects.create(
            type='start',
            timestamp=timezone.now(),
            call_id='123',
            source='123456789',
            destination='987654321'
        )
        self.call_end = CallRecord.objects.create(
            type='end',
            timestamp=timezone.now() + timedelta(minutes=5),
            call_id='123',
            source='123456789',
            destination='987654321'
        )

    def test_get_bill(self):
        url = '/api/call-records/bill/?phone_number=123456789&period=2018-05'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_cost', response.data)
        