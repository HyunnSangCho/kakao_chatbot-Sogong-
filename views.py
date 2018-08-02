from .uClass import *
from  django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from konlpy.tag import Mecab
from . import content, uFunction   #db나중에 추가
#from .weather_crawl import Weather


mecab = Mecab()



import json
#import cx_Oracle
import os

check = 0
users = {}
# GET ~/keyboard/ 요청에 반응
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['시작하기'],
    })

# csrf 토큰 에러 방지, POST 요청에 message response
@csrf_exempt
def message(request):
    #w = Weather()
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    answer_2 = received_json_data['content']
    userKey = received_json_data['user_key']
    answer = mecab.nouns(answer_2)
    global check
    global users
    if (userKey in users) == False:
        users[userKey] = User(userKey)
        print('make user!')
        check = 1
    else:
        check = 2
        print('not make')
    user = users[userKey]

    if '시작' in answer:
        user.flag = 1
        return JsonResponse({
            'message': {
                'text': content.sayhi
            },
            'keyboard' : {
                'type' : 'text'
            }
        })
    #날씨 테스트를 위한 구문
    elif '도움말' in answer_2:
        return JsonResponse({
            'message': {
                'text' : content.sayhelp
            },
            'keyboard' : {
                'type' : 'text'
            }
        })
    else:
        ans_msg = ''
        check_tag = uFunction.chooseTag(user, answer, answer_2)
        if check_tag != '':#태그리스트에서 질문매칭되면
            ans_msg = check_tag
        elif user.flag == 2:#수업시간
            ans_msg = uFunction.chooseClass(user, answer, answer_2)
        elif user.flag == 3:#시험시간
            ans_msg = uFunction.chooseClass(user, answer, answer_2)
        elif user.flag == 4:#졸업요건
            user.flag = 1
            ans_msg = content.chooseGradu(answer_2)
        elif user.flag == 5:#제본요청관리
            user.flag = 1
            ans_msg = '제본신청 완료되었습니다.'#db.setZebon(answer_2)
        else:#그외
            ans_msg = uFunction.chooseFunction(user, answer, answer_2)
        if user.flag == 6:
            user.flag = 1
            return JsonResponse({
            'message': {
                'text': str(ans_msg),
                'photo': {
                    'url': 'http://www.konkuk.ac.kr/img/Common/campus_map.jpg',
                    'width': 640,
                    'height': 480
                }
            },
            'keyboard' : {
                'type' : 'text'
            }
        })
        return JsonResponse({
            'message': {
                'text' : str(ans_msg)
            },
            'keyboard' : {
                'type' : 'text'
            }
        })

