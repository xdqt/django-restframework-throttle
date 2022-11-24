from rest_framework import throttling
from rest_framework.throttling import UserRateThrottle

class CustomScopeThrottle(throttling.ScopedRateThrottle):
    # scope = 'anon'
    rate = '1/second'
    # scope = 'll'
    # THROTTLE_RATES = {"anon": "1/s"}

class CustomUserRateThrottle(UserRateThrottle):
    rate= '1/second'