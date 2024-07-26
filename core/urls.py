from django.urls import path

from .views import (
    CustomLoginView,
    DeleteView,
    RegisterPage,
    TaskCreate,
    TaskDetail,
    TaskList,
    TaskUpdate,
    logout,
    TaskReorder
)

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("logout/", logout, name="logout"),
    path("task/update/<int:pk>/", TaskUpdate.as_view(), name="update"),
    path("task/delete/<int:pk>/", DeleteView.as_view(), name="delete"),
    path("task/create/", TaskCreate.as_view(), name="create"),
    path('reorder/', TaskReorder.as_view(), name='reorder'),
]
