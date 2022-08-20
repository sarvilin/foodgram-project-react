# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from users.models import User
#
# # from .permissions import (AdminOnly)
# from .serializers import (UserSerializer)
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """Вьюсет для пользователей."""
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = (IsAuthenticated, AdminOnly,)
#     lookup_field = 'username'
#     filter_backends = (SearchFilter,)
#     search_fields = ('username',)
#
#     @action(
#         methods=['get', 'patch'],
#         detail=False,
#         permission_classes=(IsAuthenticated,),
#         url_path='me',
#         url_name='me'
#     )
#     def me(self, request):
#         user_me = self.request.user
#         serializer = self.get_serializer(user_me)
#         if self.request.method == 'PATCH':
#             serializer = self.get_serializer(
#                 user_me,
#                 data=request.data,
#                 partial=True
#             )
#             serializer.is_valid(raise_exception=True)
#             serializer.save(
#                 email=user_me.email,
#                 role=user_me.role
#             )
#         return Response(serializer.data)
