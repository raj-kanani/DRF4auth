from rest_framework.throttling import UserRateThrottle


class SetThrottle(UserRateThrottle):
    # use scope define in setting.py in 'newset':'3/hour'
    scope = 'newset'
