import datetime
import random
import datetime

import pandas as pd
from django.http import JsonResponse
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.utils import vars
from apps.utils.data import data_exel


class ExcelApiVIEW(APIView):

    def _type_exchange(self, value, type):
        if type == 'int':
            return int(value)
        elif type == 'float':
            return float(value)
        elif type == 'date':
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

        raise TypeError

    def _compare(self, value, op, op_value, type):
        if op == '>':
            return self._type_exchange(value, type) > self._type_exchange(value, type)
        elif op == '>=':
            return self._type_exchange(value, type) >= self._type_exchange(value, type)
        elif op == '<':
            return self._type_exchange(value, type) < self._type_exchange(op_value, type)
        elif op == '<=':
            return self._type_exchange(value, type) <= self._type_exchange(value, type)
        elif op == '==':
            return self._type_exchange(value, type) == self._type_exchange(value, type)
        elif op == '!=':
            return self._type_exchange(value, type) != self._type_exchange(value, type)
        return 'Input correct logical symbol (>, >=, <, <=, ==, !=)'

    def _get_type(self, name: str, value):
        if 'time' in name.lower():
            return 'date'
        elif '.' in value:
            return 'float'
        elif name.isalnum():
            return 'int'
        else:
            return 'bool'

    def _filter_obj(self, row, field, op, value):
        _type = self._get_type(field, value)
        if row.get(field):
            return self._compare(row.get(field), op, value, _type)

    @swagger_auto_schema(request_body=Schema(type=TYPE_OBJECT, properties=data_exel))
    def post(self, request, *args, **kwargs):
        offset = request.data.get('offset')
        file_path = 'apps/utils/exel/file.xlsx'
        response = {'result': 0,
                    'totalRecords': 0,
                    'version': '1.3',
                    'crossings': []}

        workbook = pd.read_excel(file_path)

        for _, row in workbook.iterrows():
            if request.data.get('filter'):
                for filter_row in request.data.get('filter'):
                    if not self._filter_obj(row, filter_row.get('Name'), filter_row.get('Op'), filter_row.get('Value')):
                        break
                else:
                    if offset:
                        offset -= 1
                        continue
                    response['crossings'].append(dict(row[1:]))
                    response['totalRecords'] += 1
            else:
                response['crossings'].append(dict(row[1:]))
                response['totalRecords'] += 1
        return JsonResponse(response, status=200)


class CreateFakeDataCreateAPIView(CreateAPIView):

    def random_datetime(self):
        start_date = datetime.datetime(2021, 1, 1, 0, 0, 0)
        end_date = datetime.datetime.now()

        days_diff = (end_date - start_date).days
        random_day = random.randint(0, days_diff)

        random_date = start_date + datetime.timedelta(days=random_day)

        random_time = datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

        random_datetime = datetime.datetime.combine(random_date, random_time)

        return random_datetime

    def axles_ids(self):
        path = 'apps/utils/exel/axles.xlsx'
        df = pd.read_excel(path, usecols=[1])
        return tuple(_ for _, row in df.iterrows())

    def fake_object(self):
        gw = random.randint(900, 2000)
        lw = gw - random.randint(0, gw)
        ax_ids = self.axles_ids()
        ac = random.randint(0, len(ax_ids))
        dt = self.random_datetime()
        return {
            'now': str(dt),
            'ut': int(dt.timestamp()),
            'lane_no': random.choice(list(vars.lane_name.keys())),
            'error': random.choice(list(vars.error_flags.keys())),
            'warning': random.choice(list(vars.warning_flags.keys())),
            'direction': random.choice(list(vars.direction.keys())),
            'move_status': random.choice(list(vars.move_status.keys())),
            'front_2_front': random.randint(10000, 100_000) * 0.01,
            'back_2_ront': random.randint(10000, 100_000) * 0.01,
            'duration': random.randint(100, 1000) * 0.01,
            'vehicle_length': random.randint(100, 1000) * 0.01,
            'gross_weight': gw,
            'left_weight': lw,
            'right_weight': gw - lw,
            'velocity': random.randint(500, 1000) * 0.1,
            'wheelbase': random.randint(100, 300) * 0.01,
            'front_overhang': 'front_overhang',
            'ntp_time_sync_status': 'ntp-nosync',
            'axles_count': ac,
            'axles': random.sample(self.axles_ids(), ac),
            'mass_unit': 'kg',
            'velocity_unit': 'km/h',
            'distance_unit': 'm',
            'marked': random.choice((True, False)),
            'marked_v': random.choice((True, False)),
        }

    @swagger_auto_schema(request_body=Schema(type=TYPE_OBJECT, properties={'amount': Schema(type=TYPE_INTEGER)}))
    def post(self, request, *args, **kwargs):
        n = request.data.get('amount')
        excel_headers = ['ID',
                         'MetrologicalID',
                         'LaneNo',
                         'LaneName',
                         'Error',
                         'ErrorFlag',
                         'Warning',
                         'WarningFlag',
                         'Scheme',
                         'Direction',
                         'MoveStatus',
                         'FrontToFront',
                         'BackToFront',
                         'Duration',
                         'VehicleLength',
                         'GrossWeight',
                         'LeftWeight',
                         'RightWeight',
                         'Velocity',
                         'WheelBase',
                         'FrontOverhang',
                         'NtpTimeSyncStatus',
                         'AxlesCount',
                         'Axles',
                         'MassUnit',
                         'VelocityUnit',
                         'DistanceUnit',
                         'Marked',
                         'MarkedViolations',
                         'VehicleID',
                         'StartTime',  # unix timestamp
                         'StartTimeStr',
                         'StartTimeFirstAxleFirstSensor',
                         'StartTimeFirstAxleFirstSensorStr',
                         'StartTimeFirstAxleLastSensor',
                         'StartTimeFirstAxleLastSensorStr',
                         'StartTimeFirstPresenceFall',
                         'StartTimeFirstPresenceFallStr',
                         'StartTimeFirstPresenceRise',
                         'StartTimeFirstPresenceRiseStr',
                         'StartTimeLastAxleFirstSensor',
                         'StartTimeLastAxleFirstSensorStr',
                         'StartTimeLastAxleLastSensor',
                         'StartTimeLastAxleLastSensorStr',
                         'StartTimeLastPresenceFall',
                         'StartTimeLastPresenceFallStr',
                         'StartTimeLastPresenceRise',
                         'StartTimeLastPresenceRiseStr',
                         'InternalBaseClassID',
                         'MappedClassCategoryID',
                         ]

        data = []

        for i in range(n):
            obj = self.fake_object()
            data.append([i,
                         'E4C87F3C',
                         obj.get('lane_no'),
                         vars.lane_name.get(obj.get('lane_no')),
                         vars.error_flags.get(obj.get('error')),
                         obj.get('error'),
                         vars.warning_flags.get(obj.get('warning')),
                         obj.get('warning'),
                         'Schema',
                         obj.get('direction'),
                         obj.get('move_status'),
                         obj.get('front_2_front'),
                         obj.get('back_2_front'),
                         obj.get('duration'),
                         obj.get('vehicle_length'),
                         obj.get('gross_weight'),
                         obj.get('left_weight'),
                         obj.get('right_weight'),
                         obj.get('velocity'),
                         obj.get('wheelbase'),
                         obj.get('front_overhang'),
                         obj.get('ntp_time_sync_status'),
                         obj.get('axles_count'),
                         obj.get('axles'),
                         obj.get('mass_unit'),
                         obj.get('velocity_unit'),
                         obj.get('distance_unit'),
                         obj.get('marked'),
                         obj.get('marked_v'),
                         None,
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         obj.get('ut'),
                         obj.get('now'),
                         1,
                         1,
                         ])
        df = pd.DataFrame(data, columns=excel_headers)
        writer = pd.ExcelWriter('apps/utils/exel/file.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='router_list')
        writer._save()

        return Response({f'Successfully {n} objects created!'}, status=status.HTTP_201_CREATED)
