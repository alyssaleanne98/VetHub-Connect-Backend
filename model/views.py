from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Community
from .serializers import CommunitySerializer
from django.shortcuts import get_object_or_404

# Create your views here.
# def index(request):
#     community = Community.objects.all()
#     data = list(community.values())
#     return JsonResponse(data, safe=False)

class CommunityAPIView(APIView):

    def get(self, request): 
        #Index Request
        print(request)
        community = Community.objects.all()
        #Use serializer to format table data to json
        data = CommunitySerializer(community, many=True).data
        return Response(data)
    
    def post(self, request): 
        #Post Request
        print(request.data)
        community = CommunitySerializer(data=request.data)
        if community.is_valid():
            community.save()
            return Response(community.data, status=status.HTTP_201_CREATED)
        else:
            return Response(community.errors, status=status.HTTP_400_BAD_REQUEST)
        




class CommunityDetail(APIView):

    def get(self, request, pk):
        print(request) 
        #Show Request 
        community = get_object_or_404(Community, pk=pk)
        data = CommunitySerializer(community).data
        return Response(data)

    def put(self, request, pk):
        print(request) 
        #Update Request

    def delete(self, request, pk):
        #Delete Request
        print(request)



