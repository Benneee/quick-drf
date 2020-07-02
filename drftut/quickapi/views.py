from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickapi.serializers import UserSerializer, GroupSerializer

# Create your views here.

# Using viewsets, we are able to avoid writing multiple views 
# Viewsets keeps the view logic nicely organized and concise
class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

