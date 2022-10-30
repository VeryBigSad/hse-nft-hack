import json
import random

from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from nftHackBackend.logic import get_generation_prompt

from backend.utils import download_file_from_colab


def get_dict_data(raw_data):
    lst = raw_data.split('\n')
    print(lst)
    name = lst[0].replace('NAME:', '').strip()
    style = lst[1].replace('STYLE:', '').strip()
    attributes_background = [i.strip() for i in lst[3].replace('background:', '').split(', ')]
    attributes_head = [i.strip() for i in lst[4].replace('head:', '').split(', ')]
    attributes_clothing = [i.strip() for i in lst[5].replace('clothing:', '').split(', ')]
    return {
        'collection': name.replace('"', ''),
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
        raw_data = get_generation_prompt(json.loads(request.body)['collection'])
        dict_data = get_dict_data(raw_data)
        print(dict_data)
        return JsonResponse(dict_data)
    return HttpResponse('hi')


@csrf_exempt
def download(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        filename = f'clown{random.randint(1, 100000)}.png'
        download_file_from_colab(data, filename)
        return FileResponse(open(filename, 'rb'))
    return HttpResponse('hi')