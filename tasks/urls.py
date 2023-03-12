from django.urls import path
from tasks.views import TodoList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete

urlpatterns = [
    path('', TodoList.as_view()),
    path('create-todo/', TodoCreate.as_view()),
    path('detail-todo/<int:id>/', TodoDetail.as_view()),
    path('update-todo/<int:id>/', TodoUpdate.as_view()),
    path('delete-todo/<int:id>/', TodoDelete.as_view()),
    
]