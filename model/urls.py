from django.urls import path
from .views import CommunityAPIView, CommunityDetail 

urlpatterns = [
    path('', CommunityAPIView.as_view(), name='community'),
    path('<int:pk>', CommunityDetail.as_view(), name='community_detail')
]