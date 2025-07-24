from django.urls import path
from .views import signin_view, login_view, index
from.import views
urlpatterns = [
    path('signin/', views.signin_view, name='signin'),
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path("prompt/", views.prompt_query, name="prompt_query"),  
]
