from django.shortcuts import render
from django.conf import settings
import openai

# OpenAI API 키 설정
openai.api_key = settings.OPENAI_API_KEY


# 생년월일로부터 띠를 계산하는 함수
def get_zodiac_from_birthyear(birthyear):
    zodiacs = [
        "원숭이",
        "닭",
        "개",
        "돼지",
        "쥐",
        "소",
        "호랑이",
        "토끼",
        "용",
        "뱀",
        "말",
        "양",
    ]
    start_year = 1924  # 띠의 시작 연도
    zodiac_index = (birthyear - start_year) % 12  # 띠의 인덱스 계산
    return zodiacs[zodiac_index]  # 해당하는 띠 반환


# 사용자의 띠와 오늘의 운세를 보여주는 뷰
def daily_zodiac(request):
    user = request.user  # 현재 로그인한 사용자
    birthyear = user.birthdate.year  # 사용자 모델에서 생년월일 정보 가져오기

    user_zodiac = get_zodiac_from_birthyear(birthyear)  # 띠 계산

    # OpenAI를 사용하여 오늘의 운세 생성
    response = openai.ChatCompletion.create(
        engine="gpt-4-turbo", prompt=f"오늘의 {user_zodiac} 운세는?", max_tokens=100
    )
    today_fortune = response.choices[0].text.strip()

    # 결과를 템플릿에 전달
    return render(
        request, "zodiac.html", {"zodiac": user_zodiac, "fortune": today_fortune}
    )