from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer


@api_view(['GET'])
def me(request):
    print("gg")
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data=request.data
    message='success'
    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    }) 

    if form.is_valid():
        form.save()
        print(message)

        #send verification email later!
    else:
        message='error'
        print(form.errors)

    return JsonResponse({'message':message})

@api_view(['POST'])
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)
    print('send_friendship_request', pk)

    friendship_request = FriendshipRequest(created_for=user, created_by=request.user)

    return JsonResponse({'message':'friendship request created'})