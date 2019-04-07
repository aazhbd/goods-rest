from django.contrib.auth.models import User, Group
from rest_framework import serializers

from goods.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'groups', 'last_login')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created', 'modified', 'enabled')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'item', 'name', 'path', 'thumbnail', 'created', 'modified', 'enabled')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'longitude', 'latitude', 'created', 'modified', 'enabled')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'seller', 'title', 'description', 'price', 'category', 'status', 'booked', 'course', 'approved', 'created', 'modified', 'enabled')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'sent', 'sender', 'recipient', 'about_item', 'location', 'created', 'modified', 'enabled')


class WishListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'user', 'item', 'created', 'modified', 'enabled')
