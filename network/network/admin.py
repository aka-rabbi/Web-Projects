from django.contrib import admin
from .models import Post, User, UserFollowing, PostLike
# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(UserFollowing)
admin.site.register(PostLike)