from django.shortcuts import render
from django.conf import settings
import openai

# OpenAI API 키 설정
openai.api_key = settings.OPENAI_API_KEY


#  띠와 오늘의 운세를 보여주는 뷰
def daily_allzodiac(request):

    # OpenAI를 사용하여 오늘의 운세 생성
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": f"오늘 개띠에 맞는 로또번호 1부터 45번 중에 6자리추천해줄래?? ",
            }
        ],
        temperature=0.7,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    all_fortune = response["choices"][0]["message"]["content"].strip()

    # 결과를 템플릿에 전달
    return render(request, "allzodiac.html", {"all_fortune": all_fortune})
