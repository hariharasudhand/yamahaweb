from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Departments, GroupPermission, Role_Permission, Module
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import InlineRadios

def get_modules():
    return (('User', 'User'), ('Dcn Creation', 'Dcn Creation'),
            ('Dcn Verification', 'Dcn Verification'), ('Dcn Approval', 'Dcn Approval'))

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
    department = forms.ModelChoiceField(queryset=Departments.objects.all(),
                                        required=True)
    phone = forms.CharField(max_length=10, required=False)
    # CHOICES = [('M', 'Male'), ('F', 'Female'), ('P', 'Prefer not to answer')]
    # gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ['phone', 'department', 'image']

class UserActivateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['group', 'status']
        widgets = {'status': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:  # Editing and existing instance
            self.fields['group'].queryset = GroupPermission.objects.filter(status__iexact='ACTIVE')


class DepartmentForm(forms.ModelForm):
    department_name = forms.CharField(max_length=100)

    class Meta:
        model = Departments
        fields = ['department_name']

class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['module_name']

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']


class RolePermissionForm(forms.ModelForm):
    module = forms.ModelChoiceField(queryset=Module.objects.all(), required=True)

    class Meta:
        model = Role_Permission
        fields = ['name', 'module', 'create', 'view', 'update', 'delete']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:  # Editing and existing instance
            self.fields['module'].queryset = Module.objects.filter(status__iexact='ACTIVE')

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('module', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('create', css_class='form-group col-md-3 mb-0'),
                Column('view', css_class='form-group col-md-3 mb-0'),
                Column('update', css_class='form-group col-md-3 mb-0'),
                Column('delete', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )


class GroupPermissionForm(forms.ModelForm):

    class Meta:
        model = GroupPermission
        fields = ['name', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:  # Editing and existing instance
            self.fields['role'].queryset = Role_Permission.objects.filter(status__iexact='ACTIVE')


        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('role', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )

