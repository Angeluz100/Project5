from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.CreatePractice.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdatePractice.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeletePractice.as_view(), name='delete'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]