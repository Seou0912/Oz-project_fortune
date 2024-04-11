from datetime import datetime
from django.conf import settings
import openai

# OpenAI API 키 설정
openai.api_key = settings.OPENAI_API_KEY


# 사용자의 생년월일로부터 별자리 결정하는 함수
def get_zodiac_sign(month, day):
    # 별자리 날짜 범위
    zodiac_dates = [
        (120, "염소자리"),
        (218, "물병자리"),
        (320, "물고기자리"),
        (420, "양자리"),
        (521, "황소자리"),
        (621, "쌍둥이자리"),
        (722, "게자리"),
        (823, "사자자리"),
        (923, "처녀자리"),
        (1023, "천칭자리"),
        (1122, "전갈자리"),
        (1222, "사수자리"),
        (1231, "염소자리"),
    ]
    zodiac_sign = next(
        zodiac for zodiac, sign in zodiac_dates if month * 100 + day <= zodiac
    )
    return zodiac_sign


# GPT-4-Turbo를 사용하여 별자리 운세 요청하는 함수
def get_horoscope(zodiac_sign):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "별자리 운세를 알려주세요."},
            {"role": "user", "content": f"{zodiac_sign} 운세는 어떤가요?"},
        ],
    )
    return response.choices[0].message["content"]


# 사용자의 생년월일 예시
user_birthday = datetime(1990, 6, 24)
zodiac_sign = get_zodiac_sign(user_birthday.month, user_birthday.day)

# 별자리 운세 요청 및 결과 출력
horoscope = get_horoscope(zodiac_sign)
print(f"{zodiac_sign}의 운세: {horoscope}")
