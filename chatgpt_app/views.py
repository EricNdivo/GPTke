# chatgpt_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai
import json

@csrf_exempt
def chatgpt_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')

        if not message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        openai.api_key = settings.OPENAI_API_KEY

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=message,
                max_tokens=150
            )
            return JsonResponse(response.choices[0].text.strip(), safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
