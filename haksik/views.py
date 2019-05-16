from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime

from . import haksik


# Create your views here.

say_hello = "안녕하세요! 오늘은 " + str(datetime.today().month) +"월 " + str(datetime.today().day) + "일입니다.\n어떤 날짜의 메뉴를 원하시나요?\n"

def keyboard(request):
    content = {
        'type':'buttons',
        'buttons':['오늘','내일','모레']
    }
    return JsonResponse(content)

@csrf_exempt
def message(request):
    data = json.loads(request.body)
    day = data['content']
    proper_day = ["내일","모레"]
    if day in proper_day:
        if day == "내일":
            day = 1
        else:
            day = 2
    else:
        day = 0
    menu = haksik.get_menu(day)

    response = {
        "message": {
            "text": menu
        },
        "keyboard": {
            'type':'buttons',
            'buttons':['오늘','내일','모레']
        }
    }
    return JsonResponse(response)