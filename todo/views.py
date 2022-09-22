from django.shortcuts import render
# 
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from todo.models import TodoModel

#                   🔻リストviewを継承　どこにあるか分からないので上でimport
class TodoList(ListView):
     template_name = 'list.html'
    # 🔻modelsの中でたくさんテーブルを作っていくため、どのテーブルを使うか指示をする🔺でimport
     model = TodoModel
    
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # 🔻fieldsによってmodelsの中のどの項目を使用するか、指定する必要がある
    fields = ('title', 'memo', 'priority', 'duedate')
    #🔻データの作成が完了したときに、遷移させるURLを指定することができる
    success_url = reverse_lazy('list')
    # クラスの中で指定する場合、🔺reverse_lazyを指定する
    # 関数の場合、reverse 

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    
class TodoUpdate(UpdateView):
    template_name ='update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')#createviewと同様
    success_url = reverse_lazy('list')
    # 記載したらupdate.htmlの作成