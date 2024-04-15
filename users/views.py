from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/dailyquote/today")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]

            user = authenticate(email=email, password=password1)

            if user:
                login(request, user)
                return redirect("/dailyquote/today/")
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        context = {"form": form}
        return render(request, "login.html", context)

    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)


def logout_view(request):
    logout(request)

    return redirect("/")


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            user = form.save()
            user.birth_date = form.cleaned_data["birth_date"]
            user.mbti = form.cleaned_data["mbti"]
            user.nickname = form.cleaned_data["nickname"]
            user.save()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return redirect("/dailyquote/today/")

    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "signup.html", context)
