from rest_framework.generics import ListAPIView

from apps.user.api_endpoints.User.UserList.serializers import UserListSerializer
from apps.user.models import User


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


__all__ = ('UserListView',)
