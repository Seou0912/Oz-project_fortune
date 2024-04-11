import openai
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render


def daily_quote(request):
    openai.api_key = settings.OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",  # 사용할 GPT 모델 선택
        messages=[{"role": "system", "content": "오늘의 명언을 생성해주세요."}],
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    quote = response.choices[0].message["content"].strip()  # 생성된 텍스트 추출

    return render(request, "daily.html", {"quote": quote})
