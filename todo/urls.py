from django.urls import path
 # クラスがどこに入っていくのかviewsへ入るというのを指定する
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    # urlが呼び出させるとどのクラスを呼び出すか viewsでクラスを作る
    # 🔻 なんでも良い       🔻クラスの場合as
    path('list/',TodoList.as_view(), name='list'),#reverseによってURLを指定するにはname属性
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/',TodoCreate.as_view(), name='create'),
    # detailと同様にpkを指定　指定しなければdjangoは理解することができない
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    
]