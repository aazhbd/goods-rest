from django.contrib import admin

from goods.models import *


class CategoryAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass

class WishListAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)

admin.site.register(Item, ItemAdmin)

admin.site.register(Image, ImageAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(Message, MessageAdmin)

admin.site.register(WishList, WishListAdmin)
