from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path
from app.views import Server_List, web_shell, Login, Sign_Out, Add_Server, Change_Password, Account, Users, Create_User, Delete_User

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),

    path(r'serverlist/', Server_List.as_view(), name='server_list'),
    path(r'addserver/', Add_Server.as_view(), name='add_server'),
    path(r'webshell/', web_shell, name='web_shell'),

 	path(r'login/', Login.as_view(), name='login'),
 	path(r'logout/', Sign_Out.as_view(), name='sign_out'),
 	path(r'changepassword/', Change_Password.as_view(), name='change_password'),
 	path(r'account/', Account.as_view(), name='account'),
 	path(r'users/', Users.as_view(), name='users'),
 	path(r'createuser/', Create_User.as_view(), name='create_user'),
    path(r'deleteuser/', Delete_User.as_view(), name='delete_user'),

 	path(r'index/', Server_List.as_view(), name='default'),
]
