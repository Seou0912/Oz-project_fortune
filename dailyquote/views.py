from datetime import datetime
from django.shortcuts import render
from .models import DailyQuote
import openai
from django.conf import settings


def daily_quote(request):
    openai.api_key = settings.OPENAI_API_KEY
    today = datetime.today().date()  # 오늘 날짜

    # 오늘 날짜에 대한 명언이 이미 있는지 확인
    quote_obj, created = DailyQuote.objects.get_or_create(date=today)

    if not created:
        # 이미 존재하는 경우, 새 명언으로 업데이트
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "오늘의 새로운 좋은 글귀 한마디를  100자이내로 생성해주세요. 5개로 만들고 리턴은 JSON으로 해줘",
                }
            ],
            temperature=0.7,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        quote = response.choices[0].message["content"].strip()
        quote_obj.quote = quote  # 새 명언으로 업데이트
        quote_obj.save()
    else:
        # 새로 생성된 경우, 이미 response에서 명언을 생성했음
        quote = quote_obj.quote

    return render(request, "daily.html", {"quote": quote})
