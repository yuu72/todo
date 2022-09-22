
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #urlがadminでなければ以下を呼び出す
    path('', include('todo.urls')),
]
