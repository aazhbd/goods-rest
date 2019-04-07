from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters, generics
from goods.serializers import *
from goods.models import *

from django_filters import rest_framework as restfilters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView

from django.core.files.storage import default_storage
from django.conf import settings
import os
from PIL import Image as PImage


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    ordering_fields = ('username', 'email')


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (restfilters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('category', 'category__name')
    search_fields = ('title', 'description')


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = (restfilters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    __fields = ('item', 'item__id')
    filter_fields = __fields
    search_fields = __fields


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (restfilters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    __fields = ('sender', 'recipient', 'sender__id', 'recipient__id', 'about_item', 'about_item__id')
    filter_fields = __fields
    search_fields = __fields


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    filter_backends = (restfilters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    __fields = ('user', 'user__id', 'item', 'item__id')
    filter_fields = __fields
    search_fields = __fields


class SearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (restfilters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    __fields = ('title', 'description')
    filter_fields = '__all__'
    search_fields = __fields


class FileUploadView(APIView):
    parser_class = (MultiPartParser,)

    def post(self, request, format=None):
        if 'image' not in request.data:
            raise ParseError("Content not provided")

        item_id = request.POST.get('item_id', False)
        f = request.data['image']
        filename = "big__" + str(f)
        save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
        path = default_storage.save(save_path, f)
        thumb = "small__" + str(f)
        PImage.open(path).resize((80, 80)).save(os.path.join(settings.MEDIA_ROOT, 'uploads', thumb))

        im = Image(name=filename, path=filename, thumbnail=thumb, item=Item.objects.get(pk=item_id))
        im.save()

        return Response(status=status.HTTP_201_CREATED)


class DisableCSRFMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response


