from django.contrib import admin
from .models import blogpost,post,usercomm,userreply,userlike,userlist

# Register your models here.
admin.site.register(blogpost)
admin.site.register(post)
admin.site.register(usercomm)
admin.site.register(userreply)
admin.site.register(userlike)
admin.site.register(userlist)