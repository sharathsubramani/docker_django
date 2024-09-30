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
from datetime import datetime
import json
import base64


from django.contrib.auth import get_user_model

# Create your views here.


class UserProfileViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_logged_in_user(request):
        User = get_user_model()
        user = request.user
        return print(user)

    def post(self, request):

        request_headers = request.headers
        data = request.data
        user = User.objects.filter(email=data['email'])
        print(data)
        print('data', )
        # decoded =  base64.b64decode(data['passport_pic'])
        # print('decoded',decoded)

        # for x in user:
        #     user_id = x.id
        # if (request_headers['Content-Type'] != 'application/json'):
        #     return Response(data={"We are sorry, we cannot understand your requirement"}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     if user:
        # print(data)

        file = data['file'].file
        byte_file = file.read()

        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            current_year = datetime.now().year
            s3_obj_folder_key = 'CUST_' + \
                str(current_year)+'_'+str(serializer.data['id'])
            # print()
            s3service = s3uploadservice.upload_file_to_s3_bucket(
                s3_obj_folder_key, str(data['file']), byte_file)
            print(s3service.headers)
            user.update(user_profile_id=serializer.data['id'])

            elanResponse = s3uploadservice.elanrequest()
            print(elanResponse,'elanResponse')
            return Response(data={"data": serializer.data, "s3response": json.loads(s3service.content),
                                  "s3_status_code": s3service.status_code}, status=status.HTTP_201_CREATED)

    # def get(self, request):
    #     queryset = BlogPost.objects.all()
    #     # print(queryset)
    #     serializer_class = BlogPostSerializer(data=queryset, many=True)
    #     print(serializer_class)
    #     if serializer_class.is_valid():
    #         return Response(data=serializer_class.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(data={"data": "there is no blogs"}, status=status.HTTP_404_NOT_FOUND)


class UserActivationSet(APIView):

    def post(self, request):
        print(request)
        print("hello user")
        data = "hello world"
        return render(request, "sample.html", data)

    # def get(self,request):
    #     return None
