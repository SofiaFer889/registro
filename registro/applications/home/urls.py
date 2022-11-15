from django.urls import path, re_path

from . import apiviews, views

app_name = 'home_app'

urlpatterns = [
    path('api/user/create', apiviews.ProyectoCreateAPIView.as_view(),),
    path('api/user/list', apiviews.ProyectoListAPIView.as_view(),),
    path('api/user/destroy/<pk>', apiviews.ProyectoDestroyAPIView.as_view(),),
    path('api/user/update/<pk>', apiviews.ProyectoUpdateAPIView.as_view(),),
    path('api/user/update2/<pk>', apiviews.ProyectoUpdate2APIView.as_view(),),
    path('api/proyecto-user/list', apiviews.ProyectoUserListAPIView.as_view(),),
    path('api/proyecto-user/create', apiviews.ProyectoUserCreateAPIView.as_view(),),
    path('api/proyecto-user/update/<pk>', apiviews.ProyectoUserUpdateAPIView.as_view(),),
    path('home', views.HomeView.as_view(), name='home'),
    path('proyecto-create', views.ProyectoCreateView.as_view(), name='create'),
    path('proyecto-lista', views.ProyectoListView.as_view(), name='lista'),
    path('eliminar-proyecto/<pk>', views.ProyectoDeleteView.as_view(), name='eliminar'),
    path('actualizar-proyecto/<pk>', views.ProyectoUpdateView.as_view(), name='actualizar'),
    path('actualizar-proyecto2/<pk>', views.Proyecto2UpdateView.as_view(), name='actualizar2'),
    path('lista-proyecto-user', views.ProyectoUserListView.as_view(), name='list-proyecto-user'),
    path('create-proyecto-user', views.ProyectoUserCreateView.as_view(), name='create-proyecto-user'),
    path('actualizar-proyecto-user/<pk>', views.ProyectoUserUpdateView.as_view(), name='actualizar_proyecto_user'),
]