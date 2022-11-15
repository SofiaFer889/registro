from django.urls import path, re_path

from . import apiviews, views

app_name = 'login_app'

urlpatterns = [
    path('api/user/create', apiviews.UsersCreateAPIView.as_view(),),
    path('api/user/list', apiviews.UserListAPIView.as_view(),),
    path('api/user/destroy/<pk>', apiviews.UserDestroyAPIView.as_view(),),
    path('api/user/update/<pk>', apiviews.UserUpdateAPIView.as_view(),),
    path('api/user/update2/<pk>', apiviews.UserUpdate2APIView.as_view(),),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('create/user', views.UserCreateView.as_view(), name='create-user'),
    path('lista/user', views.UserListView.as_view(), name='lista-user'),
    path('eliminar/user/<pk>', views.UserDeleteView.as_view(), name='delate-user'),
    path('actualizar/user/<pk>', views.UserUpdateView.as_view(), name='update-user'),
    path('actualizar2/user/<pk>', views.User2UpdateView.as_view(), name='update2-user'),
    path('actualizar/password', views.PasswordUpdateView.as_view(), name='update-password'),
]