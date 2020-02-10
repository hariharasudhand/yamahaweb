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
    path('department/<int:id>/delete/', user_view.cancel_dept, name='dept-delete'),

    path('module/', user_view.add_module, name='module'),
    path('module_update/<int:id>', user_view.update_module, name='update_module'),
    path('module/<int:id>/delete/', user_view.cancel_module, name='module-delete'),

    path('grouppermission/', user_view.group_permission, name='grouppermission'),
    path('grouppermission_update/<int:id>', user_view.update_group_permission, name='update_group_permission'),
    path('grouppermission/<int:id>/delete/', user_view.cancel_grp_perm, name='grouppermission-delete'),

    path('rolepermission/', user_view.role_permission, name='rolepermission'),
    path('rolepermission_update/<int:id>', user_view.update_role_permission, name='update_role_permission'),
    path('rolepermission/<int:id>/delete/', user_view.cancel_role_perm, name='rolepermission-delete'),

    path('activate_user/', user_view.activate_user, name='activate_user'),
    path('activate_user_update/<int:id>', user_view.activate_user_update, name='activate_user_update'),
]