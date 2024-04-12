from django import forms
from django.core.exceptions import ValidationError
from users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="이메일",
        widget=forms.TextInput(
            attrs={"placeholder": "이메일로 입력해주세요"},
        ),
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={"placeholder": "(영문+숫자 4자리 이상)"},
        ),
    )


class SignupForm(forms.Form):
    email = forms.EmailField(
        label="이메일",
        widget=forms.TextInput(
            attrs={"placeholder": "이메일로 입력해주세요"},
        ),
    )

    nickname = forms.CharField(
        label="닉네임",
        widget=forms.TextInput(attrs={"placeholder": "닉네임"}),
        max_length=10,
    )

    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={"placeholder": "영문+숫자 4자리 이상"},
        ),
    )

    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호 확인란"},
        ),
    )

    birth_date = forms.DateField(
        label="생년월일",
        widget=forms.DateInput(attrs={"placeholder": "YYYY.MM.DD"}),
        input_formats=["%Y.%m.%d"],
        required=True,
    )

    mbti = forms.CharField(max_length=10, required=True)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"입력한 이메일 계정{{email}}은 이미 사용 중입니다.")
        return email

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다.")

    def save(self):
        email = self.cleaned_data["email"]
        password1 = self.cleaned_data["password1"]
        user = User.objects.create_user(
            email=email,
            password=password1,
        )
        return user
