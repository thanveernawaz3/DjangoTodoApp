from django.urls import path

from . import views

urlpatterns=[
    path('list/',views.list_todo ,name='list_todo'),
    path('insert_todo/',views.insert_todo,name='insert_todo'),
    path('delete_todo/<int:todo_id>',views.delete_todo,name='delete_todo')
]