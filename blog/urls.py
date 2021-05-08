from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_post/', views.add_post, name='Add_Post'),
    path('update_post/<int:id>/', views.update_post, name='Update_Post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_Post'),
    path('comment/<int:id>', views.user_comment, name='comment')

]