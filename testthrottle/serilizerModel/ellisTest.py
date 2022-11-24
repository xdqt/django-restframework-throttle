from rest_framework import serializers
from testthrottle.models import EllisTest

class EllisTestSerilizer(serializers.ModelSerializer):
    class Meta:
        model = EllisTest
        fields='__all__'
