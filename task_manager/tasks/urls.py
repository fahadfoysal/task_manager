from django.urls import path
from .views import (
    TaskList, 
    TaskDetail, 
    TaskCreate, 
    TaskUpdate,
    TaskDelete,
    TaskImageUpload,
    TaskImageDelete
)

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('<int:pk>/task/', TaskDetail.as_view(), name='task_detail'),
    path('task/create', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update', TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDelete.as_view(), name='task_delete'),
    path('task/<int:pk>/upload', TaskImageUpload.as_view(), name='task_image_upload'),
    path('task/<int:t_id>/<int:i_id>/delete', TaskImageDelete.as_view(), name='task_image_delete')

]