lane_name = {
    1: 'rightmost',
    2: 'leftmost'
}

error_flags = {
    0: 'Out of Spec',
    1: 'Irregular Driving',
    2: 'Irregular Manoeuvring'
}

warning_flags = {
    0: 'Velocity above max',
    1: 'Velocity below min',
    2: 'Strong acceleration max',
    3: 'Strong deceleration min',
    4: 'High imbalance',
    5: 'Sensor missing',
    6: 'ADC overload',
    7: 'High vehicle dynamics',
    8: 'Acceleration change',
    9: 'Driving between two lanes',
    10: 'Single-track vehicle',
    11: 'Force record missing',
    12: 'Single axle vehicle',
    13: 'Stop and go',
    14: 'GVW above max',
    15: 'GVW below min',
    16: 'Axle load above max',
    17: 'Axle load below min',
    18: 'Wheel load below min',
    19: 'Stopping on sensor',
    20: 'Vehicle manoeuvring'
}

direction = {
    0: 'Normal driving direction',
    1: 'Inverse driving direction of the vehicle'
}

move_status = {
    0: 'constant speed',
    1: 'acceleration',
    -1: 'deceleration'
}
