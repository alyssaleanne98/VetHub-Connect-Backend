from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Community
from .serializers import CommunitySerializer

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

    def get(self, request):
        print(request) 
        #Show Request

    def put(self, request):
        print(request) 
        #Update Request

    def delete(self, request):
        #Delete Request
        print(request)



