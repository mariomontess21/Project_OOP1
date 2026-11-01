from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import UserSerializer

user = {
    "username": "marioms",
    "name": "Mario",
    "email": "mariomontess2106@gmail.com",
    "password": "456",
    "birth_day": "1998/06/21",
    "phone": "6981046214"
}

@api_view(["GET"])
def get_user(request):
    data = UserSerializer(user).data
    birth = data['birth_day']
    return Response(data)



@api_view(["POST"])
def create_user(request):
    serialized_data = UserSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

from users.models import User

@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)

@api_view(["GET", "PATCH", "DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


    






   








