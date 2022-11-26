from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from .models import Account

class AccountView(APIView):
    def get(self, request: Request, account_id: int) -> Response:
        try:
            account_user = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response({'msg': 'User not found'}, status.HTTP_404_NOT_FOUND)

        return Response(model_to_dict(account_user), status.HTTP_200_OK)

class AccountCreateView(APIView):
    def post(self, request: Request) -> Response:
        return Response(model_to_dict(Account.objects.create(**request.data)), status.HTTP_201_CREATED)

