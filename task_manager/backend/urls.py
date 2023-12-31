from django.urls import path 

from . import views

urlpatterns = [path("get-tasks/", views.GetTasks.as_view()),
               path("delete-task/<int:id>", views.DeleteTask.as_view()),
               path("add-task", views.AddTask.as_view()),
               path("finished-task/<int:id>", views.FinishedTask.as_view())]  