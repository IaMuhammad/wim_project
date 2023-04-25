from django.urls import path

from apps.views import ExcelApiVIEW, CreateFakeDataCreateAPIView

urlpatterns = [
    path('api/excel/', ExcelApiVIEW.as_view(), name='excel_api'),
    path('api/create-fake-data/', CreateFakeDataCreateAPIView.as_view(), name='create_fake_api'),
]
