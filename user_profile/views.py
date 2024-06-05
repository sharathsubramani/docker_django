from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from authuser.models import User
from utils import s3uploadservice
from pathlib import Path


# Create your views here.
class UserProfileViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request_headers = request.headers
        data = request.data
        user = User.objects.filter(email=data['email'])
        print(data)
        print(data['passport_pic'])

        folder_path = data['first_name']+data['last_name']
        s3service = s3uploadservice.upload_fileto_s3(
            data['passport_pic'], folder_path)
        for x in user:
            user_id = x.id
        if (request_headers['Content-Type'] != 'application/json'):
            return Response(data={"We are sorry, we cannot understand your requirement"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if user:
                # print(data)
                serializer = UserProfileSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    user.update(user_profile_id=serializer.data['id'])
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    # def get(self, request):
    #     queryset = BlogPost.objects.all()
    #     # print(queryset)
    #     serializer_class = BlogPostSerializer(data=queryset, many=True)
    #     print(serializer_class)
    #     if serializer_class.is_valid():
    #         return Response(data=serializer_class.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(data={"data": "there is no blogs"}, status=status.HTTP_404_NOT_FOUND)
