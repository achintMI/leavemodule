from django import forms;
from . models import FacultyProfile;
from django.contrib.auth.models import User;
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
	class Meta:
		model =  User;
		fields = ('username', 'first_name', 'last_name', 'email');

class FacultyProfileForm(forms.ModelForm):
	class Meta:
		model = FacultyProfile;
		fields = ('facultyDepartment', 'facultyLeaveHead', 'facultyDesignation')  

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional');
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional');
	email = forms.EmailField(max_length=254, help_text='Required. Infromation');

	class Meta:
		model = User;
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2');