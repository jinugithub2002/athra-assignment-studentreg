from django.urls import path
from .import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('insert/',views.insert,name="insert"),
    path('', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('userlog/',views.userlog,name='userlog'),
    path('view/',views.view,name='view'),
    path('detail_view/<str:pk>',views.detail_view,name='detail_view'),
    path('update/<str:pk>',views.update,name='update'), 
    path('delete/<str:pk>',views.delete,name='delete') 
]

