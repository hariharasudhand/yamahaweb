from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, UserUpdateForm, ProfileUpdateForm,
                    GroupPermissionForm, GroupForm, DepartmentForm)
from .models import Departments, GroupPermission

# # Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account is created, login with your credentials now!')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


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

# #handling user group starts here
def add_group(request):
    return grp_helper(request, 0)

def update_group(request, id):
    return grp_helper(request, id)

def grp_helper(request, id):
    model = Group.objects.all()
    if id > 0:
        group_obj = Group.objects.get(id=id)
        form = GroupForm(request.POST or None, instance=group_obj)
    else:
        form = GroupForm(request.POST or None)

    str_redirect = 'group'
    str_render = 'users/group.html'
    str_msg = 'Group'
    return helper(request, model, form, str_redirect, str_render, str_msg)
#handling user group ends here

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
        department_obj = Departments.objects.get(id=id)
        form = DepartmentForm(request.POST or None, instance=department_obj)
    else:
        form = DepartmentForm(request.POST or None)

    str_redirect = 'department'
    str_render = 'users/department.html'
    str_msg = 'Department'
    return helper(request, model, form, str_redirect, str_render, str_msg)

def group_permission(request):
    return grpPermission_helper(request, 0)

def update_group_permission(request, id):
    return grpPermission_helper(request, id)

def grpPermission_helper(request, id):
    model = GroupPermission.objects.all()
    if id > 0:
        group_obj = GroupPermission.objects.get(id=id)
        form = GroupPermissionForm(request.POST or None, instance=group_obj)
    else:
        form = GroupPermissionForm(request.POST or None)

    str_redirect = 'grouppermission'
    str_render = 'users/grouppermission.html'
    str_msg = 'Group Permission'
    return helper(request, model, form, str_redirect, str_render, str_msg)

def helper(request, model, form, str_redirect, str_render, str_msg):
    if form.is_valid():
        form.save()
        messages.success(request, f'{str_msg} data is updated')
        return redirect(str_redirect)

    context = {
        'form': form,
        'model': model
    }
    return render(request, str_render, context)
