from django.shortcuts import render
import random, requests

# view 함수 -> 중간관리자
# 사용자가 접속해서 볼 페이지를 작성. 즉 하나하나의 페이지를 view라고 부른다
# view 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다
def index(request): #첫번째 인자 반드시 request
    return render(request,'pages/index.html') #첫번째 인자 반드시 request

## GET
# 정보를 던져줄 페이지
def throw(request):
    return render(request,'pages/throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
def catch(request):
    print(request)
    print(request.GET)
    # => <QueryDict: {'message': ['ㅇㅇ']}>

    message = request.GET.get('message')
    context = {'message':message}
    return render(request,'pages/catch.html', context)

# 아스키 아티 ASCII ARTII
# 사용자로부터 텍스트를 입력받는 페이지
def art(request):
    return render(request, 'pages/art.html')

# 텍스트를 받아서 아스키 아트로 보여주는 페이지
def result(request):
    word = request.GET.get('word')
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    fonts = fonts.split('\n')
    font = random.choice(fonts)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context ={
        'result':result,
    }
    return render(request, 'pages/result.html', context)

## POST
# 회원가입 폼을 보여주는 페이지
def user_new(request):
    return render(request,'pages/user_new.html')

# 회원가입 요청을 처리하는 페이지(로직)
# 실제로는 이렇게 구현하지 않는다. 저 세상 코드~
# 사실 사용자 인증(회원가입,로그인)이 끝나면 메인페이지로 이동시켜줘야 함.
def user_create(request):
    user_id = request.POST.get('user_id')
    pwd = request.POST.get('pwd')
    context={
        'user_id':user_id,
        'pwd':pwd,
    }
    return render(request, 'pages/user_create.html', context)


# static
def static_sample(request):
    return render(request,'pages/static_sample.html')