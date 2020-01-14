from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_view

urlpatterns = [

    # user access permission related links
    path('register/', user_view.register, name='register'),
    path('profile/', user_view.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/index.html'), name='logout'),

    path('department/', user_view.departments, name='department'),
    path('update_department/<int:id>', user_view.update_dept, name='update_department'),
    path('group/', user_view.add_group, name='group'),
    path('group_update/<int:id>', user_view.update_group, name='update_group'),
    path('grouppermission/', user_view.group_permission, name='grouppermission'),
    path('grouppermission_update/<int:id>', user_view.update_group_permission, name='update_group_permission'),
]