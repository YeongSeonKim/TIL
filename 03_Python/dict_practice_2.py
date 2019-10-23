# 문제: bit.do/yeoksam_python_2
# 강사님 코드 : bit.do/yeoksam_answer

'''
Python dictionary 심화 문제
'''
t4ir = {
    "location": ["역삼", "강남", "삼성", "왕십리"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "connected":  {
            "lecturer": "유창오",
            "manager": "유주희",
            "class president": "정세환",
            "groups": {
                "A": ["정세환", "오은애", "황민승", "소현우", "김한석"],
                "B": ["최재범", "서혁진", "감자", "이도현", "합기도"],
                "C": ["이수연", "남찬우", "이승희", "은승찬", "김건"],
                "D": ["박경희", "김영선", "이동열", "이건희", "최찬종"],
                "E": ["공선아", "최주현"]
            }
        },
        "bigdata": {
            "lecturer": "이민교",
            "manager": "매니저"
        }
    }
}


"""
난이도* 1. 지역(location)은 몇개 있나요? : list length
출력예시)
4
"""



"""
난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력예시)
False
"""


"""
난이도** 3. connected반의 반장의 이름을 출력하세요. : depth 있는 접근
출력예시)
정세환
"""


"""
난이도*** 4. t4ir에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web
"""



"""
난이도*** 5 t4ir bigdata반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
이민교
매니저
"""



"""
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""



"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 황민승
"""