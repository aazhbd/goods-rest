from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from goods import views

from django.conf import settings
from django.conf.urls.static import  static

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'wishlist', views.WishListViewSet)
router.register(r'search', views.SearchViewSet, base_name='search-view')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^upload/', views.FileUploadView.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
