import json
import random

from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from nftHackBackend.logic import get_generation_prompt

from backend.utils import download_file_from_colab


def get_dict_data(raw_data):
    lst = raw_data.split('\n')
    name = lst[0].split('NAME:')[1]
    style = lst[1].split('STYLE:')[1]
    attributes_background = [i.strip() for i in lst[3].split('background:')[1].split(', ')]
    attributes_head = [i.strip() for i in lst[4].split('head:')[1].split(', ')]
    attributes_clothing = [i.strip() for i in lst[5].split('clothing:')[1].split(', ')]
    return {
        'name': name.replace('"', ''),
        'style': style.replace('"', ''),
        'attributes':
            {
                'background': attributes_background,
                'head': attributes_head,
                'clothing': attributes_clothing
            }
    }


@csrf_exempt
def get_openai_data_view(request):
    if request.method == 'POST':
        raw_data = get_generation_prompt(request.POST['collection'])
        dict_data = get_dict_data(raw_data)
        return JsonResponse(dict_data)


@csrf_exempt
def download(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filename = f'clown{random.randint(1, 100000)}.png'
        download_file_from_colab(data, filename)
        return FileResponse(open(filename, 'rb'))
