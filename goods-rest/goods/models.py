from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    id = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        pass


class Item(Base):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_seller')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item_category')

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.IntegerField(blank=True)

    STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DENIED', 'Denied'),
        ('SOLD', 'Sold'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0])

    booked = models.BooleanField(default=True)
    course = models.CharField(max_length=10, blank=True, null=True)
    approved = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        pass


class Image(Base):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_image')

    name = models.CharField(max_length=400, blank=True, null=True)
    path = models.CharField(max_length=4096)
    thumbnail = models.CharField(max_length=4096, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        pass


class Location(Base):
    name = models.CharField(max_length=400)
    longitude = models.CharField(max_length=400, blank=True, null=True)
    latitude = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        pass


class Message(Base):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_recipient')
    about_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='message_item')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='message_location')

    content = models.CharField(max_length=2000, blank=False)
    sent = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return str(self.content)

    class Meta:
        pass


class WishList(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_user')
    item = models.ManyToManyField(Item, related_name='wishlist_item')

    def __str__(self):
        return str(self.user) + str(self.item)

    class Meta:
        pass

