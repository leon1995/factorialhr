import enum


class LocationType(enum.StrEnum):
    office = 'office'
    business_trip = 'business_trip'
    work_from_home = 'work_from_home'


class TimeUnit(enum.StrEnum):
    minute = 'minute'
    half_day = 'half_day'
    none = 'none'
