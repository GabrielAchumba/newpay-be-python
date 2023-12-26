# from django.conf.urls import url 
from django.urls import include, re_path
from users import views 

urlpatterns = [  
    re_path('user/users_list', views.users_list),
    re_path('user/register', views.RegisterUser),
    re_path('user/delete_users', views.delete_users),
    re_path('user/:id', views.GetUser),
    re_path('user/update_user', views.update_user),
    re_path('user/delete_user', views.delete_user)
]