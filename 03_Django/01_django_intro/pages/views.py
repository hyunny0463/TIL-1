from django.shortcuts import render
from datetime import datetime
import random
import requests

#1. 기본 로직
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def image(request):
    return render(request, 'pages/image.html')


#2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name, 
        'age': age, 
        'pick': pick
    }
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def introduce2(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/introduce2.html', context)

#4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력 
def times(request, num1, num2):
    num3 = num1 * num2
    context = {
        'num3': num3,
        'num2': num2,
        'num1': num1,
    }
    return render(request, 'pages/times.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오.
def area(request, r):
    area = 3.14 * (r**2)
    context = {
        'area': area, 
        'r': r,
    }
    return render(request, 'pages/area.html', context)\

#5. DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus, 
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)

#6. 실습 
#6-1. isbirth
# Honey tip
# today.month -> 8 / today.day -> 6
# True/False를 담아 isbirth.html로 넘겨 DTL(템플릿 문법-조건문) 활용
def isbirth(request):
    today = datetime.now()
    if today.month == 9 and today.day == 28:
        result = True
    else:
        result = False

    context = {
        'result': result,
    }
    return render(request, 'pages/isbirth.html', context)

#6-2. 회문판별(palindrome)
# 회문이면(반대로 돌려도 같은 글자 -ex. racecar) '회문입니다'
# 회문이 아니면 '회문이 아닙니다' 
def ispal(request, word):
    result = False
    if word == word[::-1]:
        result = True

    context = {
        'word': word,
        'result': result,
    }
    return render(request, 'pages/ispal.html', context)

#6-3. 로또 번호 추첨
# lottos -> 1 ~ 45까지의 번호 중 6개를 랜덤으로 pick한 리스트 
# real_lottos -> [21, 24, 30, 32, 40, 42]
#1. lottos 번호를 하나씩 출력(DTL-for문)
#2. 컴시기가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)
def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = sorted(list(random.sample(range(1, 46), 6)))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }

    return render(request, 'pages/lotto.html', context)

#7. Form - GET
def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2, 
    }
    return render(request, 'pages/catch.html', context)

def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    ping = request.GET.get('ping')
    context = {
        'ping': ping,
    }
    return render(request, 'pages/pong.html', context)

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서
    # font라는 변수에 저장(str)
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시 
    # 요청을 보낸다. 그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result': result,
    }
    return render(request, 'pages/result.html', context)

#9. Form - POST
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd,
    }
    return render(request, 'pages/user_create.html', context)

#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')