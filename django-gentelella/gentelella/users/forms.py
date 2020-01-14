from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Departments, GroupPermission

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(max_length=10, required=False)
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    department = forms.ModelChoiceField(queryset=Departments.objects.all(),
                                   required=True)
    # CHOICES = [('M', 'Male'), ('F', 'Female'), ('P', 'Prefer not to answer')]
    # gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ['phone', 'group', 'department', 'image']


class DepartmentForm(forms.ModelForm):
    department_name = forms.CharField(max_length=100)

    class Meta:
        model = Departments
        fields = ['department_name']


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']

class GroupPermissionForm(forms.ModelForm):
    choice = {('User', 'User'), ('Dcn Creation', 'Dcn Creation'),
              ('Dcn Verification', 'Dcn Verification'), ('Dcn Approval', 'Dcn Approval')}
    module = forms.ChoiceField(choices=choice, required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    create = forms.CheckboxInput(check_test=None)
    view = forms.CheckboxInput(check_test=None)
    update = forms.CheckboxInput(check_test=None)
    delete = forms.CheckboxInput(check_test=None)

    class Meta:
        model = GroupPermission
        fields = ['module', 'group', 'create', 'view', 'update', 'delete']