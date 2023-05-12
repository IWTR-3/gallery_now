from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def login(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # 로그인 후 이동할 페이지 지정
            else:
                messages.error(request, '유효하지 않은 이메일 또는 비밀번호입니다.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다. 이제 로그인해주세요.')
            return redirect('login')  # 회원가입 후 로그인 페이지로 이동
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def delete(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('index')  # 회원탈퇴 후 이동할 페이지 지정
    return render(request, 'accounts/delete.html')


def logout(request):
    # if request.user.is_authenticated:
    logout(request)
    return redirect('index')  # 로그아웃 후 이동할 페이지 지정