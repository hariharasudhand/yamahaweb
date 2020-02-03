from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, UserUpdateForm, ProfileUpdateForm,
                    GroupPermissionForm, DepartmentForm, UserActivateForm,
                    RolePermissionForm, ModuleForm)
from .models import Departments, GroupPermission, Role_Permission, Module

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account is created, login with your credentials now!')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def activate_user(request):
    return activate_helper(request, 0)

def activate_user_update(request, id):
    return activate_helper(request, id)

def activate_helper(request, id):
    model = User.objects.all()
    if id > 0:
        obj = User.objects.get(id=id)
        form = UserActivateForm(request.POST or None, instance=obj)
        is_update = True
    else:
        form = UserActivateForm(request.POST or None)
        obj = None
        is_update = False

    str_redirect = 'activate_user'
    str_render = 'users/activate.html'
    str_msg = 'User Activation'
    return helper(request, model, form, str_redirect, str_render, str_msg, is_update, obj)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile is updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

# #handling user modules starts here
def add_module(request):
    return module_helper(request, 0)

def update_module(request, id):
    return module_helper(request, id)

def cancel_module(request, id):
    model = Module.objects.get(status='ACTIVE')
    obj = Module.objects.get(id=id)
    if request.method == 'POST':
        form = ModuleForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('module-delete')
    else:
        form = ModuleForm(request.POST or None)
    context = {
        'model':model,
        'form': form
    }
    return render(request, "users/module.html", context)


def module_helper(request, id):
    model = Module.objects.all()
    if id > 0:
        obj = Module.objects.get(id=id)
        form = ModuleForm(request.POST or None, instance=obj)
        is_update = True
    else:
        form = ModuleForm(request.POST or None)
        is_update = False
        obj = None

    str_redirect = 'module'
    str_render = 'users/module.html'
    str_msg = 'Module'
    return helper(request, model, form, str_redirect, str_render, str_msg, is_update, obj)

# this is to create new department
def departments(request):
    return dept_helper(request, 0)

# this is to update department
def update_dept(request, id):
    return dept_helper(request, id)

# this helper function helps to handle department
def dept_helper(request, id):
    model = Departments.objects.all()
    if id > 0:
        obj = Departments.objects.get(id=id)
        form = DepartmentForm(request.POST or None, instance=obj)
        is_update = True
    else:
        form = DepartmentForm(request.POST or None)
        is_update = False
        obj = None

    str_redirect = 'department'
    str_render = 'users/department.html'
    str_msg = 'Department'
    return helper(request, model, form, str_redirect, str_render, str_msg, is_update, obj)

def role_permission(request):
    return role_permission_helper(request, 0)

def update_role_permission(request, id):
    return role_permission_helper(request, id)

def role_permission_helper(request, id):
    model = Role_Permission.objects.all()

    if id > 0:
        obj = Role_Permission.objects.get(id=id)
        form = RolePermissionForm(request.POST or None, instance=obj)
        is_update = True
    else:
        form = RolePermissionForm(request.POST or None)
        is_update = False
        obj = None

    str_redirect = 'rolepermission'
    str_render = 'users/rolepermission.html'
    str_msg = 'Role Permission'
    return helper(request, model, form, str_redirect, str_render, str_msg, is_update, obj)

def group_permission(request):
    return grpPermission_helper(request, 0)

def update_group_permission(request, id):
    return grpPermission_helper(request, id)

def grpPermission_helper(request, id):
    model = GroupPermission.objects.all()

    if id > 0:
        obj = GroupPermission.objects.get(id=id)
        form = GroupPermissionForm(request.POST or None, instance=obj)
        is_update = True
    else:
        form = GroupPermissionForm(request.POST or None)
        is_update = False
        obj = None

    str_redirect = 'grouppermission'
    str_render = 'users/grouppermission.html'
    str_msg = 'Group Permission'
    return helper(request, model, form, str_redirect, str_render, str_msg, is_update, obj)

def helper(request, model, form, str_redirect, str_render, str_msg, is_update, obj):
    if form.is_valid():
        form.save()
        messages.success(request, f'{str_msg} data is updated')
        return redirect(str_redirect)

    context = {
        'form': form,
        'model': model,
        'is_update': is_update,
        'obj': obj
    }
    return render(request, str_render, context)
