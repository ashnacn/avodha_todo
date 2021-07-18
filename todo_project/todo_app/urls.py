
from django . urls import path
from . import views
urlpatterns=[


    path('',views.task_view,name='task_view'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvtask/',views.tasklistview.as_view(),name='cbvtask'),
    path('detail/<int:pk>/', views.taskdetailview.as_view(),name='detail'),
    path('edit/<int:pk>/', views.taskupdate.as_view(),name='edit'),
    path('delete/<int:pk>/', views.taskdelete.as_view(),name='delete'),

]