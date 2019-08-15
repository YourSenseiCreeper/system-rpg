from django.urls import path
from django.contrib.auth.views import LoginView
import game.views as views

app_name = 'game'

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('editor/', views.editor, name="editor"),
    path('editor/<int:id>/', views.editor, name="editor_id"),
    path('user/<slug:user>/', views.user, name="user"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='memes/login.html', redirect_field_name='success'), name="login"),
]


