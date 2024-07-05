from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, ModifyUserForm
from .models import CustomUser
from django import forms


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            messages.success(request, 'Registro exitoso. Has iniciado sesión.')
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
    return render(request, 'login.html')

def registro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso!')
            return redirect('login')
        else:
            messages.error(request, 'El registro no fue exitoso. Por favor, verifica los datos.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido cambiada correctamente.')
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(request.user)

    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'profile.html', context)



def profile_update_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos de perfil han sido actualizados.')
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'profile_update.html', {'form': form})

def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Tu contraseña ha sido cambiada con éxito.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})

class ModifyUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']

@login_required
def modify_user_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Tus datos han sido modificados correctamente.')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'modify_user.html', {'form': form})

def chatbot_view(request):
    return render(request, 'chatbot.html')

def ciberseguridad_view(request):
    return render(request, 'ciberseguridad.html')

def servers_view(request):
    return render(request, 'servers.html')

def pagina4_view(request):
    return render(request, 'acerca_de_mi.html')
