from django.contrib import admin

# Register your models here.
from .models import Board
from .models import Reply
admin.site.register(Reply)
admin.site.register (Board)
