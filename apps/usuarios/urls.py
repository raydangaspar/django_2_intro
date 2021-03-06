from django.urls import path

from . import views

# primeiro parâmetro é a rota. Segundo parâmetro é o view.
# Terceiro parâmetro namespace do aplicativo para a entrada url
urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')
]