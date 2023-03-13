from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="tasks_home"),
    path("", views.TaskListCreateView.as_view(), name="list_tasks"),
    path(
        "<int:pk>/",
        views.TaskRetrieveUpdateDeleteView.as_view(),
        name="task_detail",
    ),
    path("current_user/", views.get_posts_for_current_user, name="current_user"),
    path(
        "tasks_for/",
        views.ListTasksForAuthor.as_view(),
        name="tasks_for_current_user",
    ),
]
