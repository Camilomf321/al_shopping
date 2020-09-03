from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if username == '' or first_name == '' or last_name == '' or email == '' or password == '' or password2 == '':
            messages.error(request, 'Los campos no pueden estar vacíos')
            return redirect('account:register_user')
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya esta en uso')
                return redirect('account:register_user')

            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'El usuario ya esta en uso')
                    return redirect('account:register_user')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                    email=email, password=password)
                    user.save()
                    messages.success(request, 'Registro exitoso!! ahora puedes Iniciar Sesion')
                    return redirect('account:login_user')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('account:register_user')
    return render(request, 'account/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.error(request, 'Los campos no pueden estar vacíos')
            return redirect('account:login_user')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('account:login_user')

    return render(request, 'account/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Has cerrado sesion exitosamente')
    return redirect('home:home')
