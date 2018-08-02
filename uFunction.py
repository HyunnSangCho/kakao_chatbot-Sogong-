from . import content  #,db 나중에 추가
from .uClass import *
#import cx_Oracle
import os


def chooseTag(user, answer, answer_2):
    TagList = {}
    TagList['univ'] = 'False'
    TagList['loca'] = 'False'
    TagList['test'] = 'False'
    TagList['clas'] = 'False'
    TagList['festi'] = 'False'
    TagList['weather'] = 'False'
    TagList['build'] = 'False'
    TagList['when'] = 'False'
    TagList['month'] = 'False'
    TagList['profe'] = 'False'
    TagList['number'] = 'False'
    TagList['email'] = 'False'
    TagList['lab'] = 'False'
    if '건대' in answer_2 or '건국대' in answer_2 or '건국대학교' in answer_2 or '우리학교' in answer_2 or '학교' in answer_2:
        TagList['univ'] = 'True'
    for s in content.Loca_List:
        if s in answer_2:
            TagList['loca'] = 'True'
    for s in content.profe_name:
        if s in answer_2:
            TagList['profe'] = 'True'
    for s in content.ques_lab:
        if s in answer_2:
            TagList['lab'] = 'True'
    for s in content.ques_email:
        if s in answer_2:
            TagList['email'] = 'True'
    for s in content.ques_number:
        if s in answer_2:
            TagList['number'] = 'True'
    if '시험' in answer_2 or '셤' in answer_2:
        TagList['test'] = 'True'
    for s in content.Class_List:
        if s in answer_2:
            TagList['clas'] = 'True'
    if '행사' in answer_2:
        TagList['festi'] = 'True'
    if '날씨' in answer_2:
        TagList['weather'] = 'True'
    for s in content.Build_List:
        if s in answer_2:
            TagList['build'] = 'True'
    if '언제' in answer_2:
        TagList['when'] = 'True'
    for s in content.Month_List:
        if s in answer_2:
            TagList['month'] = 'True'
    #태그 체크
    if TagList['loca'] == 'True' and TagList['weather'] == 'True':
        #해당 위치의 날씨 검색
        msg = '해당 위치의 날씨 검색'
        return msg
    elif TagList['profe'] == 'True' and TagList['lab'] == 'True':
        msg = content.findlab(answer_2)
        return msg
    elif TagList['profe'] == 'True' and TagList['email'] == 'True':
        msg = content.findemail(answer_2)
        return msg
    elif TagList['profe'] == 'True' and TagList['number'] == 'True':
        msg = content.findnumber(answer_2)
        return msg
    elif TagList['build'] == 'True' and TagList['loca'] == 'True':
        user.flag = 6
        msg = 'http://www.konkuk.ac.kr/img/Common/campus_map.jpg\n 해당 url을 클릭하면 학교 지도를 크게 볼 수 있어. 건물별 자세한 지도는 추후에 업데이트 하도록 할게^^'
        return msg
    elif TagList['build'] == 'True':
        #해당 건물 위치 전송
        user.flag = 6
        msg = 'http://www.konkuk.ac.kr/img/Common/campus_map.jpg\n 해당 url을 클릭하면 학교 지도를 크게 볼 수 있어. 건물별 자세한 지도는 추후에 업데이트 하도록 할게^^'
        return msg
    elif TagList['clas'] == 'True' and TagList['test'] == 'True':
        #해당 수업의 시험시간 전송
        msg = content.examClass(answer_2)
        return msg
    elif TagList['clas'] == 'True' and (TagList['loca'] == 'True' or TagList['when'] == 'True'):
        #해당 수업 시간 전송
        msg = content.findClass(answer_2)
        return msg
    elif TagList['month'] == 'True' and TagList['festi'] == 'True':
        #해당 월의 행사
        msg = content.findFestival(answer_2)
        #msg = '준비중'
        return msg
    else:
        msg = ''
        return msg


def chooseFunction(user, answer, answer_2):
    if '행사' in answer:
        msg = content.festi
        return msg
    elif '수업' in answer:
        user.flag = 2
        msg = '어떤 수업의 강의실 위치를 찾으세요?'
        return msg
    elif '제본' in answer:
        user.flag = 5
        msg = content.currentZebon
        return msg
    elif '시험' in answer:
        user.flag = 3
        msg = '어떤 수업의 시험 강의실과 시간을 알고싶으세요?'
        return msg
    elif '동아리' in answer:
        msg = '현재 우리 학과에 있는 동아리 목록 입니다.\n\n동아리 이름 : 비빔밥\n동아리 소개 : 학술동아리\n가입기간 : 3월 10일~4월 10일\n가입문의 : 010-3394-0029\n\n\n동아리 이름 : Edge\n동아리 소개 : 게임개발동아리\n가입기간 : 3월 15일~4월 15일\n가입문의 : 010-2249-3077'
        return msg
    elif '졸업' in answer:
        user.flag = 4
        msg = '학번과 단일전공(1), 다전공(2), 부전공(3) 여부를 아래와 같은 형식으로 입력해주세요.\n\n Ex) 11,1  (다전공이나 부전공은 다전공과 부전공을 시작한 년도를 입력하셔야 합니다. 예를 들어 12년도에 다전공을 시작했다면 12,2 를 입력해주세요.)'
        return msg
    elif '날씨' in answer:
        msg = '날씨기능은 현재  준비중입니다.'
        return msg
    elif '과방' in answer_2:
        msg = '과방은 새천년관 지하 2층에 있어. ^^ 좋은 친구들을 만나길 바래~'
        return msg
    elif '과사' in answer_2 or '학과사무실' in answer_2 or '학과 사무실' in answer_2 or '과사무실' in answer_2 or '과 사무실' in answer_2:
        msg = '학과 사무실은 공대 A동 1105호로  옮겼어!\n전화번호는 02-450-4071이야!'
        return msg
    elif '홈피' in answer_2 or '홈페이지' in answer_2:
        msg = '학과 홈페이지 주소는 http://sw.konkuk.ac.kr/ 이야~'
        return msg
    else:
        user.flag = 1
        msg = '죄송합니다.\n'+ '['+answer_2+']' + '에 대한 대답은 아직 준비되지 않았습니다. 보내주신 메세지는 저희 데이터베이스에 저장하여 향후 업데이트에 활용하도록 하겠습니다. 감사합니다.'
        return msg

def chooseClass(user, answer, answer_2):
    if user.flag == 2:
        user.flag = 1
        msg = content.findClass(answer_2)
        return msg
    elif user.flag == 3:
        user.flag = 1
        msg = content.examClass(answer_2)
        return msg
    
