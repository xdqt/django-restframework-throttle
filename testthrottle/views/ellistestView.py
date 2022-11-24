from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import throttle_classes
from rest_framework.response import Response
from rest_framework import status
from testthrottle.models import EllisTest
from testthrottle.serilizerModel.ellisTest import EllisTestSerilizer
from testthrottle.throttling import CustomScopeThrottle,CustomUserRateThrottle


class EllisTestView(GenericViewSet):
    serializer_class = EllisTestSerilizer
    queryset = EllisTest.objects.all()
    throttle_scope = "ll"
    # throttle_classes = [CustomUserRateThrottle]

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [CustomUserRateThrottle]
        else:
            # throttle_classes = []  # No throttle for other actions
            throttle_classes = [CustomScopeThrottle]  # No throttle for other actions
        return [throttle() for throttle in throttle_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # @throttle_classes([CustomUserRateThrottle])
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

