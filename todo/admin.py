from django.contrib import admin
# todomodelがどこにあるか指定する
from .models import TodoModel
# Register your models here.

# todomodel
admin.site.register(TodoModel)
