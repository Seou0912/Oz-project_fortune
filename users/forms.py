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
        max_length=50,
        label="Email",
        widget=forms.TextInput(
            attrs={"placeholder": "Email", "class": "no-border"},
        ),
    )

    nickname = forms.CharField(
        label="Nickname",
        widget=forms.TextInput(
            attrs={"placeholder": "Nickname", "class": "no-border"},
        ),
        max_length=10,
    )

    password1 = forms.CharField(
        label="password1",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "At least 4 letters and numbers",
                "class": "no-border",
            },
        ),
    )

    password2 = forms.CharField(
        label="password2",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password checkbox", "class": "no-border"},
        ),
    )

    birth_date = forms.DateField(
        label="Birth date",
        widget=forms.DateInput(
            attrs={"placeholder": "YYYY.MM.DD", "class": "no-border"}
        ),
        input_formats=["%Y.%m.%d"],
        required=True,
    )

    mbti = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(  # 여기에 widget을 추가하여 attrs를 설정합니다.
            attrs={"placeholder": "MBTI", "class": "no-border"},
        ),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                f"The email account{{email}} you entered is already in use."
            )
        return email

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error(
                "password2",
                "The values for the password and password checkbox are different.",
            )

    def save(self):
        email = self.cleaned_data["email"]
        password1 = self.cleaned_data["password1"]
        user = User.objects.create_user(
            email=email,
            password=password1,
        )
        return user
