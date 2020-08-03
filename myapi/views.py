from rest_framework import status, viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import IFISerializer, GetFullUserSerializer, UserSerializerWithToken
from .permissions import isOwnerOrReadOnly, isSuperUserOrReadOnly
from .models import InternationalFinancialInstitute
from django.http import Http404
from pprint import pprint

class IFIList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """
    List all ifis, or create a new ifi.
    """
    def get(self, request, format=None):
        ifis = InternationalFinancialInstitute.objects.all()
        serializer = IFISerializer(ifis, many=True)
        pprint(dir(serializer))
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IFISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class IFIDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    
    """
    Retrieve, update or delete a ifi instance.
    """
    def get_object(self, pk):
        try:
            return InternationalFinancialInstitute.objects.get(pk=pk)
        except InternationalFinancialInstitute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ifi = self.get_object(pk)
        serializer = IFISerializer(ifi)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ifi = self.get_object(pk)
        serializer = IFISerializer(ifi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ifi = self.get_object(pk)
        ifi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetAllUsers(generics.ListAPIView):
    permission_classes = [isSuperUserOrReadOnly]
    queryset = User.objects.all()
    serializer_class = GetFullUserSerializer

class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        user = request.data.get('user')
        
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = UserSerializerWithToken(data = user)
        
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        
        return Response({"response" : "success", "message" : "user created succesfully"})

@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)
