from enum import Enum



GEAR_RATIO_1:float = 5.034042
GEAR_RATIO_2:float = 3.199118
GEAR_RATIO_3:float = 2.357342
GEAR_RATIO_4:float = 1.92907
GEAR_RATIO_5:float = 1.678014
FINAL_DRIVE_RATIO:float = 3.875
DYNAMIC_ROLLING_RADIUS:float = 0.267 # in [m]
NUMBER_OF_PULSES_PER_ROTATION_VSS:int = 10
MPS_TO_KPH_RATIO:float = 3.6

class GearRatio(Enum):
    GEAR_1 = (1, 5.034042)
    GEAR_2 = (2, 3.199118)
    GEAR_3 = (3, 2.357342)
    GEAR_4 = (4, 1.92907)
    GEAR_5 = (5, 1.678014)

    def __new__(cls, gear_step: int, ratio: float):
        obj = object.__new__(cls)
        obj._value_ = gear_step
        obj.ratio = ratio
        return obj

class GearShiftSimulator:

    def calculate_vehicle_speed(in_rpm:int , in_gear_ratio:float)->int:
        vehicle_speed: int = 0
        angular_wheel_speed:float = (in_rpm * 2.0 * pi * 60.0) / (in_gear_ratio * FINAL_DRIVE_RATIO)  # converted to rad/s
        vehicle_speed = int(angular_wheel_speed * DYNAMIC_ROLLING_RADIUS / 1000.0)

        return vehicle_speed

    def calculate_gearshift_rpm_drop(in_current_rpm:int, in_current_gear:int)->tuple[int, int]:
        if in_current_gear < GearRatio.GEAR_1.value or in_current_gear >= GearRatio.GEAR_5.value:
            raise ValueError("RPM drop can only be calculated for upshifts from gear 1 to gear 4.")

        current_ratio:float = GearRatio(in_current_gear).ratio
        next_ratio:float = GearRatio(in_current_gear + 1).ratio
        rpm_after_shift:int = int(round(in_current_rpm * next_ratio / current_ratio))
        rpm_drop:int = in_current_rpm - rpm_after_shift

        return rpm_after_shift, rpm_drop

    def calculate_downshift_rpm_rise(in_current_rpm:int, in_current_gear:int)->tuple[int, int]:
        if in_current_gear <= GearRatio.GEAR_1.value or in_current_gear > GearRatio.GEAR_5.value:
            raise ValueError("RPM rise can only be calculated for downshifts from gear 2 to gear 5.")

        current_ratio:float = GearRatio(in_current_gear).ratio
        previous_ratio:float = GearRatio(in_current_gear - 1).ratio
        rpm_after_shift:int = int(round(in_current_rpm * previous_ratio / current_ratio))
        rpm_rise:int = rpm_after_shift - in_current_rpm

        return rpm_after_shift, rpm_rise

    def convert_vehicle_speed_to_signal(in_vehicle_speed:int)->int:
        wheel_circumference_m:float = 2.0 * pi * DYNAMIC_ROLLING_RADIUS
        sig_gen_frequency:int = int(
            in_vehicle_speed
            * NUMBER_OF_PULSES_PER_ROTATION_VSS
            / (wheel_circumference_m * MPS_TO_KPH_RATIO)
        )

        return sig_gen_frequency