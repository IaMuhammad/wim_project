import datetime

import django_filters
import pandas as pd
from django.http import JsonResponse, HttpResponse
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from apps.models import Picture
from apps.serializers import PictureSerializer
from apps.utils.data import data_exel
from apps.utils.mixins import FakeDataMixin, FilterMixin


class FakeDataApiVIEW(FakeDataMixin, FilterMixin, APIView):

    @swagger_auto_schema(request_body=Schema(type=TYPE_OBJECT, properties=data_exel))
    def post(self, request, *args, **kwargs):
        offset = request.data.get('offset')
        file_path = 'apps/utils/exel/file.xlsx'
        response = {'result': 0,
                    'totalRecords': 0,
                    'version': '1.3',
                    'crossings': []}

        for i in range(1, 201):
            obj = self.fake_object(i)
            if request.data.get('filter'):
                for filter_row in request.data.get('filter'):
                    if not self._filter_obj(obj, filter_row.get('Name'), filter_row.get('Op'), filter_row.get('Value')):
                        break
                else:
                    if offset:
                        offset -= 1
                        continue
                    else:
                        break
                    response['crossings'].append(obj)
                    response['totalRecords'] += 1
            else:
                response['crossings'].append(obj)
                response['totalRecords'] += 1
        return JsonResponse(response, status=200)


class ExcelApiVIEW(FakeDataMixin, FilterMixin, APIView):
    @swagger_auto_schema(request_body=Schema(type=TYPE_OBJECT, properties=data_exel))
    def post(self, request, *args, **kwargs):
        offset = request.data.get('offset')
        file_path = 'apps/utils/exel/file.xlsx'
        response = {'result': 0,
                    'totalRecords': 0,
                    'version': '1.3',
                    'crossings': []}

        for i in range(1, 201):
            obj = self.fake_object(i)
            if request.data.get('filter'):
                for filter_row in request.data.get('filter'):
                    if not self._filter_obj(obj, filter_row.get('Name'), filter_row.get('Op'), filter_row.get('Value')):
                        break
                else:
                    if offset:
                        offset -= 1
                        continue
                    else:
                        break
                    response['crossings'].append(obj)
                    response['totalRecords'] += 1
            else:
                response['crossings'].append(obj)
                response['totalRecords'] += 1
        return JsonResponse(response, status=200)


class CreateFakeDataCreateAPIView(FakeDataMixin, CreateAPIView):
    @swagger_auto_schema(request_body=Schema(type=TYPE_OBJECT, properties={'amount': Schema(type=TYPE_INTEGER)}))
    def post(self, request, *args, **kwargs):
        n = request.data.get('amount')
        columns, data = self.fake_data(n)
        df = pd.DataFrame(data, columns=columns)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=fake_data.xlsx'

        df.to_excel(response, index=False)

        return response


class PictureListAPIView(ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id',)
