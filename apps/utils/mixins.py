import datetime
import random

import pandas as pd

from apps.utils import vars


class FakeDataMixin:
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

    def fake_object_data(self):
        gw = random.randint(900, 2000)
        lw = gw - random.randint(0, gw)
        ax_ids = self.axles_ids()
        ac = random.randint(0, len(ax_ids))
        dt = self.random_datetime()
        return {
            'MetrologicalID': 'E4C87F3C',
            'Scheme': 'Scheme',
            'now': str(dt),
            'ut': int(dt.timestamp()),
            'LaneNo': random.choice(list(vars.lane_name.keys())),
            'Error': random.choice(list(vars.error_flags.keys())),
            'Warning': random.choice(list(vars.warning_flags.keys())),
            'Direction': random.choice(list(vars.direction.keys())),
            'MoveStatus': random.choice(list(vars.move_status.keys())),
            'FrontToFront': random.randint(10000, 100_000) * 0.01,
            'BackToFront': random.randint(10000, 100_000) * 0.01,
            'Duration': random.randint(100, 1000) * 0.01,
            'VehicleLength': random.randint(100, 1000) * 0.01,
            'GrossWeight': gw,
            'LeftWeight': lw,
            'RightWeight': gw - lw,
            'Velocity': random.randint(500, 1000) * 0.1,
            'WheelBase': random.randint(100, 300) * 0.01,
            'FrontOverhang': 'FrontOverhang',
            'NtpTimeSyncStatus': 'ntp-nosync',
            'AxlesCount': ac,
            'Axles': random.sample(self.axles_ids(), ac),
            'MassUnit': 'kg',
            'VelocityUnit': 'km/h',
            'DistanceUnit': 'm',
            'Marked': random.choice((True, False)),
            'MarkedViolations': random.choice((True, False)),
            'VehicleID': None,
        }

    def fake_object(self, id):
        obj = self.fake_object_data()
        return {'ID': id,
                'MetrologicalID': obj.get('MetrologicalID'),
                'LaneNo': obj.get('LaneNo'),
                'LaneName': vars.lane_name.get(obj.get('LaneNo')),
                'Error': vars.error_flags.get(obj.get('Error')),
                'ErrorFlag': obj.get('Error'),
                'Warning': vars.warning_flags.get(obj.get('Warning')),
                'WarningFlag': obj.get('Warning'),
                'Scheme': obj.get('Scheme'),
                'Direction': obj.get('Direction'),
                'MoveStatus': obj.get('MoveStatus'),
                'FrontToFront': obj.get('FrontToFront'),
                'BackToFront': obj.get('BackToFront'),
                'Duration': obj.get('Duration'),
                'VehicleLength': obj.get('VehicleLength'),
                'GrossWeight': obj.get('GrossWeight'),
                'LeftWeight': obj.get('LeftWeight'),
                'RightWeight': obj.get('RightWeight'),
                'Velocity': obj.get('Velocity'),
                'WheelBase': obj.get('WheelBase'),
                'FrontOverhang': obj.get('FrontOverhang'),
                'NtpTimeSyncStatus': obj.get('NtpTimeSyncStatus'),
                'AxlesCount': obj.get('AxlesCount'),
                'Axles': obj.get('Axles'),
                'MassUnit': obj.get('MassUnit'),
                'VelocityUnit': obj.get('VelocityUnit'),
                'DistanceUnit': obj.get('DistanceUnit'),
                'Marked': obj.get('Marked'),
                'MarkedViolations': obj.get('MarkedViolations'),
                'VehicleID': obj.get('VehicleID'),
                'StartTime': obj.get('ut'),
                'StartTimeStr': obj.get('now'),
                'StartTimeFirstAxleFirstSensor': obj.get('ut'),
                'StartTimeFirstAxleFirstSensorStr': obj.get('now'),
                'StartTimeFirstAxleLastSensor': obj.get('ut'),
                'StartTimeFirstAxleLastSensorStr': obj.get('now'),
                'StartTimeFirstPresenceFall': obj.get('ut'),
                'StartTimeFirstPresenceFallStr': obj.get('now'),
                'StartTimeFirstPresenceRise': obj.get('ut'),
                'StartTimeFirstPresenceRiseStr': obj.get('now'),
                'StartTimeLastAxleFirstSensor': obj.get('ut'),
                'StartTimeLastAxleFirstSensorStr': obj.get('now'),
                'StartTimeLastAxleLastSensor': obj.get('ut'),
                'StartTimeLastAxleLastSensorStr': obj.get('now'),
                'StartTimeLastPresenceFall': obj.get('ut'),
                'StartTimeLastPresenceFallStr': obj.get('now'),
                'StartTimeLastPresenceRise': obj.get('ut'),
                'StartTimeLastPresenceRiseStr': obj.get('now'),
                'InternalBaseClassID': 1,
                'MappedClassCategoryID': 1}

    def fake_data(self, n):
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
                         'StartTime',
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

        for i in range(1, n + 1):
            obj = self.fake_object(i)
            data.append(list(obj.values()))
        return excel_headers, data


class FilterMixin:
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
            return self._type_exchange(value, type) > self._type_exchange(op_value, type)
        elif op == '>=':
            return self._type_exchange(value, type) >= self._type_exchange(op_value, type)
        elif op == '<':
            return self._type_exchange(value, type) < self._type_exchange(op_value, type)
        elif op == '<=':
            return self._type_exchange(value, type) <= self._type_exchange(op_value, type)
        elif op == '==':
            return self._type_exchange(value, type) == self._type_exchange(op_value, type)
        elif op == '!=':
            return self._type_exchange(value, type) != self._type_exchange(op_value, type)
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
