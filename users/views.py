from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(
            request, "login.html"
        )  # login.html은 로그인 페이지의 템플릿 파일입니다.

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("메인 페이지 URL")
        else:
            return render(
                request,
                "login.html",
                {"error": "이메일 또는 비밀번호가 잘못되었습니다."},
            )


User = get_user_model()


@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        birth_date = request.POST.get("birth_date")
        nickname = request.POST.get("nickname")
        mbti = request.POST.get("mbti")

        if not (email and password and birth_date and nickname and mbti):
            return JsonResponse(
                {"message": "필수 정보를 모두 입력해주세요."}, status=400
            )

        User.objects.create_user(
            email=email,
            password=password,
            birth_date=birth_date,
            nickname=nickname,
            mbti=mbti,
        )
        return JsonResponse({"message": "회원가입 성공!"}, status=201)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "로그인 성공!"}, status=200)
        else:
            return JsonResponse(
                {"message": "로그인 실패. 이메일 또는 비밀번호를 확인해주세요."},
                status=401,
            )
