from django.shortcuts import render
from django.conf import settings
import openai

# OpenAI API 키 설정
openai.api_key = settings.OPENAI_API_KEY


def Mbti(request):
    user_profile = request.user.profile
    mbti = user_profile.mbti

    response = openai.Completion.create(
        engine="gpt-4-turbo",
        prompt=f"오늘의 {mbti} 운세는 어떤가요?",
        temperature=0.7,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    context = {"mbti": response.choices[0].text.strip()}
    return render(request, "mbti.html", context)
