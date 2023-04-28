from django.urls import path

from apps.views import FakeDataApiVIEW, CreateFakeDataCreateAPIView, PictureListAPIView, ExcelApiVIEW

urlpatterns = [
    path('api/fake', FakeDataApiVIEW.as_view(), name='excel_api'),
    path('api/read-excel', ExcelApiVIEW.as_view(), name='excel_api'),
    path('api/create-fake-data', CreateFakeDataCreateAPIView.as_view(), name='create_fake_api'),
    path('api/picture', PictureListAPIView.as_view(), name='create_fake_api'),
]
