from django.urls import path

from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name="task"),  # Changed to plural 'tasks' for the task list view
    path('tasks/', views.TaskList.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name="task-create"),  # Task creation
    path('login/', CustomLoginView.as_view(), name="login"),  # Login view
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),  # Logout view
    path('register/', RegisterPage.as_view(), name="register"),  # Register view
    path('task/<int:pk>/', TaskDetail.as_view(), name="task-detail"),  # Single task detail
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),  # Task update view
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete")  # Task delete view
]
