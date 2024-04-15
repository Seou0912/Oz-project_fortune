from django.shortcuts import render
from django.conf import settings
import openai
from users.models import User


# OpenAI API 키 설정
openai.api_key = settings.OPENAI_API_KEY


def Mbti(request):
    mbti = request.user.mbti

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": f"오늘 나의 {mbti}에 맞는 오늘의 운세는 어떻게 좋게 얘기 해줄 수 있어? 500자이내로 얘기해주세요?",
            }
        ],
        temperature=0.7,
        # max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # context = {"mbti": response.choices[0].text.strip()}
    quote = response["choices"][0]["message"]["content"].strip()
    return render(request, "mbti.html", {"quote": quote})
