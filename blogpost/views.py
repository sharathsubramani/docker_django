from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BlogPostViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = BlogPost.objects.all()
        # print(queryset)
        serializer_class = BlogPostSerializer(data=queryset, many=True)
        print(serializer_class)
        if serializer_class.is_valid():
            return Response(data=serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"data": "there is no blogs"}, status=status.HTTP_404_NOT_FOUND)
