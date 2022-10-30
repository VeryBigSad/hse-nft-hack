from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from nftHackBackend.logic import get_generation_prompt


def get_dict_data(raw_data):
    lst = raw_data.split('\n')
    print(lst)
    name = lst[0].split('NAME:')[1]
    style = lst[1].split('STYLE:')[1]
    attributes_background = [i.strip() for i in lst[3].split('background:')[1].split(', ')]
    attributes_head = [i.strip() for i in lst[4].split('head:')[1].split(', ')]
    attributes_clothing = [i.strip() for i in lst[5].split('clothing:')[1].split(', ')]
    return {
        'name': name,
        'style': style,
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
        print(request.POST)
        raw_data = get_generation_prompt(request.POST['collection'])
        dict_data = get_dict_data(raw_data)
        return JsonResponse(dict_data)
