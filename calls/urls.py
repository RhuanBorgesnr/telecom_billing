from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CallRecordViewSet,  BillViewSet

router = DefaultRouter()
router.register(r'call-records', CallRecordViewSet)
router.register(r'bills', BillViewSet, basename='bill')

urlpatterns = [
    path('', include(router.urls)),
]